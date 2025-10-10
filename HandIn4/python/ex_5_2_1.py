#!/usr/bin/env python
# coding: utf-8
# %%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
from collab_functions import CreateAgent, AgentFormation


# It is necessary to plot in an external windows for the animations to work.
# Run the ipython-command below to activate plotting in external windows.
#
# If you have no default Matplotlib backend, you might have to write
#
%matplotlib tk
#
# to explicitly state which backend to use (tk is a good choice that should work on all platforms)


# %% Model, controllers, and agent formation
# 4 agents with double integrator dynamics and PD controller


def double_integrator(t, x, u, mdlpar):
    """
    Double integrator system-model function
    
    State vector x = [p_x, p_y, v_x, v_y] where:
    - p_x, p_y are positions
    - v_x, v_y are velocities
    
    Dynamics: ppp = u (acceleration = control input)
    
    Input arguments:
    t - time
    x - state vector [position_x, position_y, velocity_x, velocity_y]
    u - control input (acceleration command)
    mdlpar - dictionary with model parameters (wind force)
    
    Output:
    dxdt - state derivative [v_x, v_y, u_x, u_y]
    """
    # Extract wind force from model parameters
    wind_force = mdlpar.get("wind", np.array([0.0, 0.0]))
    
    # State: [p_x, p_y, v_x, v_y]
    # Derivative: [v_x, v_y, a_x, a_y]
    dxdt = np.zeros(4)
    dxdt[0] = x[2]  # dp_x/dt = v_x
    dxdt[1] = x[3]  # dp_y/dt = v_y
    dxdt[2] = u[0] + wind_force[0]  # dv_x/dt = u_x + wind_x
    dxdt[3] = u[1] + wind_force[1]  # dv_y/dt = u_y + wind_y
    
    return dxdt


def g_absolute_pd(y, xref, ctrlpar):
    """
    PD control function for double integrator
    
    Control law: u = k_v * (v* - v) + k_p * (p* - p)
    
    Input arguments:
    y - measurement [p_x, p_y, v_x, v_y] (position and velocity)
    xref - reference [p_x*, p_y*, v_x*, v_y*] (desired position and velocity)
    ctrlpar - dictionary with controller gains k_p and k_v
    
    Output:
    u - control signal (acceleration command)
    """
    k_p = ctrlpar["k_p"]  # Position gain
    k_v = ctrlpar["k_v"]  # Velocity gain
    
    # Split measurement and reference into position and velocity
    p = y[0:2]      # Current position [p_x, p_y]
    v = y[2:4]      # Current velocity [v_x, v_y]
    p_ref = xref[0:2]  # Reference position
    v_ref = xref[2:4]  # Reference velocity

    u = k_p * (p_ref - p) + k_v * (v_ref - v)
    
    return u

def g_relative_pd(y, xref, ctrlpar):
    k_p = ctrlpar["k_p"]
    k_v = ctrlpar["k_v"]

    # error = desired - measured
    errors_p = -(xref[0:2] - y[:,0:2])   # position error
    errors_v = -(xref[2:4] - y[:,2:4])   # velocity error

    # control = average over neighbors
    u = k_p * np.mean(errors_p, axis=0) + k_v * np.mean(errors_v, axis=0)
    return u

# Formation graph - all agents measure their own absolute position and velocity
# For double integrator, each measurement includes both position and velocity
n = 4  # number of states per agent: [p_x, p_y, v_x, v_y]

G = [(0,)]  # Agent 0 measures itself
for i in range(1, 8):
    G.append((i-1, i))
    
# G.append((6,7))  # Agent 7 measures relative to agent 6
# Formation references - now include both position and velocity references
# For a trajectory p(t), the velocity reference is dp/dt
# Reference setup
formation_references = [
    lambda t: [0, 4, 0, 0],  # agent 0 absolute reference
]
for _ in range(1, 8):
    formation_references.append(lambda t: [0, 1, 0, 0])  # relative reference



# Create agents with double integrator model and PD controller
# Model parameters with and without wind
modelparam_no_wind = {"wind": np.array([0.0, 0.0])}
modelparam_with_wind = {"wind": np.array([0.0, 0.0])}  # Wind force in x-direction

# Controller parameters - tune these for good performance
ctrl_params_1 = {"k_p": 2.0, "k_v": 2.0}   # Lower gains
#ctrl_params_2 = {"k_p": 5.0, "k_v": 5.0}   # Higher gains

# Choose whether to simulate with or without wind
USE_WIND = False  # Set to True to include wind force
modelparam = modelparam_with_wind if USE_WIND else modelparam_no_wind

agents = [
    CreateAgent(double_integrator, modelparam, g_absolute_pd, ctrl_params_1),  # Agent 0
]
for _ in range(1, 8):
    agents.append(CreateAgent(double_integrator, modelparam, g_relative_pd, ctrl_params_1))

print(len(agents),len(G), len(formation_references) )
formation = AgentFormation(agents, G, formation_references, n)

# %% Simulate and animate
# Initial state: [p_x0, p_y0, v_x0, v_y0] for each agent

x0 = np.array([
    0, 0, 0, 0,  # Agent 0: position (0,0), velocity (0,0)
    1, 0, 0, 0,  # Agent 1: position (1,0), velocity (0,0)
    2, 0, 0, 0,  # Agent 2: position (2,0), velocity (0,0)
    3, 0, 0, 0,  # Agent 3: position (3,0), velocity (0,0)
    4, 0, 0, 0,  # Agent 4: position (4,0), velocity (0,0)
    5, 0, 0, 0,  # Agent 5: position (5,0), velocity (0,0)
    6, 0, 0, 0,  # Agent 6: position (6,0), velocity (0,0)
    7, 0, 0, 0   # Agent 7: position (7,0), velocity (0,0)
])

# Simulate the formation
t = np.arange(0, 15, 0.05)  # Time vector

x = odeint(formation.ode, x0, t)

# %% Plot trajectories
fig_traj, ax_traj = plt.subplots(num=21, clear=True, figsize=(10, 8))
ax_traj.set_xlabel("x [m]")
ax_traj.set_ylabel("y [m]")
wind_status = "with wind" if USE_WIND else "without wind"
ax_traj.set_title(f"Agent Trajectories ({wind_status})")
ax_traj.grid(True, alpha=0.3)

colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
for idx in range(len(agents)):
    # Extract x and y positions for each agent
    x_pos = x[:, 0 + n * idx]
    y_pos = x[:, 1 + n * idx]
    ax_traj.plot(x_pos, y_pos, color=colors[idx], label=f'Agent {idx}', linewidth=2)
    # Mark start and end positions
    ax_traj.plot(x_pos[0], y_pos[0], 'o', color=colors[idx], markersize=8)
    ax_traj.plot(x_pos[-1], y_pos[-1], 's', color=colors[idx], markersize=8)

ax_traj.legend()
ax_traj.axis('equal')

# plot the other graph 
plt.figure()
for i in range(len(agents)):
    plt.plot(t, x[:, 1 + i * n], label=f"Agent {i}")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("y-position [m]")
plt.title(f"y-positions of agents")

# %% Animate the results
fig, ax = plt.subplots(num=20, clear=True)
ax.axis([-2, 6, -5, 6])
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title(f"Double Integrator Formation Control ({wind_status})")
ax.grid(True, alpha=0.3)

m = tuple([ax.plot(np.nan, np.nan, 'o', markersize=5, color=colors[k])[0] 
           for k in range(len(agents))])
text = ax.text(-1.5, 5.5, "")

# Add velocity vectors
velocity_arrows = [ax.quiver(0, 0, 0, 0, color=colors[k], scale=10, width=0.005) 
                   for k in range(len(agents))]


def animate(i):
    for idx, mi in enumerate(m):
        # Update position markers
        mi.set_xdata([x[i, 0 + n * idx]])
        mi.set_ydata([x[i, 1 + n * idx]])
        
        # Update velocity arrows
        pos_x = x[i, 0 + n * idx]
        pos_y = x[i, 1 + n * idx]
        vel_x = x[i, 2 + n * idx]
        vel_y = x[i, 3 + n * idx]
        # velocity_arrows[idx].set_offsets([[pos_x, pos_y]])
        # velocity_arrows[idx].set_UVC(vel_x, vel_y)
    
    text.set_text(f"t = {t[i]:.1f} s")
    return m + (text,)

#tuple(velocity_arrows) +
ani = animation.FuncAnimation(fig, animate, interval=5, frames=x.shape[0], 
                            blit=True, repeat=False)


plt.show()
# %%