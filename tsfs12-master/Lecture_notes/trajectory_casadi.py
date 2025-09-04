# %% Optimize a trajectory
import casadi
import matplotlib.pyplot as plt
import numpy as np
from seaborn import despine
# %matplotlib

# %% Vehicle parameters and constraints
L = 1.5  # Wheel base (m)
v = 15   # Constant velocity (m/s)
u_max = np.pi / 4  # Maximum steering angle (rad)

state_i = [0, 0, 0]
state_f = [3, 1, 0]

# Parameters for collocation
N = 75  # Number of elements
nx = 3  # Degree of state vector
Nc = 3  # Degree of interpolation polynomials

# Define optimization variables and motion equations
x = casadi.MX.sym('x', nx)
u = casadi.MX.sym('u')

F = casadi.Function('f', [x, u],
                    [v * casadi.cos(x[2]), v * casadi.sin(x[2]), v * casadi.tan(u) / L])

# Create optimizaer object
opti = casadi.Opti()

X = opti.variable(nx, N + 1)
pos_x = X[0, :]
pos_y = X[1, :]
ang_th = X[2, :]

U = opti.variable(N, 1)
T = opti.variable(1)
dt = T / N

# Set initial guess values of variables
opti.set_initial(T, 0.1)
opti.set_initial(U, 0.0 * np.ones(N))
opti.set_initial(pos_x, np.linspace(state_i[0], state_f[0], N + 1))
opti.set_initial(pos_y, np.linspace(state_i[1], state_f[1], N + 1))

# Define collocation parameters
tau = casadi.collocation_points(Nc, 'radau')
C = casadi.collocation_interpolators(tau)
if type(C) is tuple:  # Handle different versions of casadi
    C = C[0]

# Formulate collocation constraints
for k in range(N):  # Loop over elements
    Xc = opti.variable(nx, Nc)
    X_kc = casadi.horzcat(X[:, k], Xc)
    for j in range(Nc):
        # Make sure that the motion equations are satisfied at all collocation points
        fo = F(Xc[:, j], U[k])
        opti.subject_to(X_kc @ C[j + 1] == dt * casadi.vertcat(fo[0], fo[1], fo[2]))

    # Continuity constraints for states between elements
    opti.subject_to(X_kc[:, Nc] == X[:, k + 1])

# Input constraints
for k in range(N):
    opti.subject_to(U[k] <= u_max)
    opti.subject_to(-u_max <= U[k])

# Initial and terminal constraints
opti.subject_to(T >= 0.001)
opti.subject_to(X[:, 0] == state_i)
opti.subject_to(X[:, -1] == state_f)

# Formulate the cost function
alpha = 1e-2
opti.minimize(T + alpha * casadi.sumsqr(U))

# Choose solver ipopt and solve the problem
opti.solver('ipopt', {'expand': True},
            {'tol': 10**-8, 'print_level': 3})
sol = opti.solve()

x_opt = sol.value(pos_x)
y_opt = sol.value(pos_y)
th_opt = sol.value(ang_th)
u_opt = sol.value(U)
T_opt = sol.value(T)

tt = np.linspace(0, T_opt, N)

# %%
fig, ax = plt.subplots(1, 2, num=10, clear=True, figsize=(12, 6))
ax[0].plot(x_opt, y_opt)
ax[0].set_xlabel("x [m]")
ax[0].set_ylabel("y [m]")
despine(ax=ax[0])

ax[1].plot(tt, u_opt * 180 / np.pi)
ax[1].plot(tt, tt * 0 + u_max * 180 / np.pi, 'k--')
ax[1].plot(tt, tt * 0 - u_max * 180 / np.pi, 'k--')
ax[1].set_xlabel("t [s]")
ax[1].set_ylabel("u")
despine(ax=ax[1])

fig.suptitle((f"Optimal trajectory (T = {T_opt:.2f}) from " +
             f"({state_i[0]}, {state_i[1]}, {state_i[2]}) -- ({state_f[0]}, {state_f[1]}, {state_f[2]})"))
# %%
plt.show()
