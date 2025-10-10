#!/usr/bin/env python

#%% all
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collab_functions import CreateAgent, AgentFormation

%matplotlib tk


def g_distance(y, xref, ctrlpar):
    """
    Control function
    Compute the control signal, in this case it is a P-controller which gives a control signal proportional to the vector between the current position and the reference position.

      Input arguments:
      y - measurement y,
      xref - the reference vector xref (in this case the desired position of the agent)
      ctrlpar - dictionary which contains parameters used by the controller (in this case the proportional gain k).

     Output argument:
     Control signal"""
    Kp = ctrlpar["k"]

    u = 0
    p_i = np.array(absolute_positions[xref[0]])
    for i in range(y.shape[0]):

        p_j = np.array(absolute_positions[xref[i + 1]])

        displacement = y[i]

        p_diff = np.linalg.norm(displacement)

        pstar_diff = np.linalg.norm(p_j - p_i)

        gamma = p_diff**2 - pstar_diff**2

        u += gamma * (displacement / p_diff)

    return Kp * u

def single_integrator(t, x, u, mdlpar):
    """
    System-model functions

     Input arguments are:
     t - time
     x - state vector of the agent (position)
     u - the control input u,
     mdlpar - structure with parameters of the model

    Output:
    dxdt - state-derivative"""

    return u


absolute_positions = [
    [0, 0],    [1, 1],    [-1, 1],    [1, 3],
    [-1, 3],    [1, 5],    [-1, 5],    [0, 6],
]


def g_absolute(y, xref, ctrlpar):
    """
    Control function
    Compute the control signal, in this case it is a P-controller which gives a control signal proportional to the vector between the current position and the reference position.

      Input arguments:
      y - measurement y,
      xref - the reference vector xref (in this case the desired position of the agent)
      ctrlpar - dictionary which contains parameters used by the controller (in this case the proportional gain k).

     Output argument:
     Control signal"""

    Kp = ctrlpar["k"]
    p_i = y
    p_star = xref
    return Kp * (p_star - p_i)

n = 2
G = [
    (0,),
    (0, 1),
    (2, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (2, 4),
    (3, 5),
    (4, 5),
    (5, 6),
    (4, 6),
    (6, 7),
    (5, 7),
]


formation_references = [
    lambda t: [2 * np.cos(t), 2 * np.sin(t)],
    lambda t: [1, 0, 2],
    lambda t: [2, 0, 1],
    lambda t: [3, 1, 2],
    lambda t: [4, 3, 2],
    lambda t: [5, 3, 4],
    lambda t: [6, 5, 4],
    lambda t: [7, 6, 5],
]


modelparam = {"m": 1}
kp = 5

agents = [
    CreateAgent(single_integrator, modelparam, g_absolute, {"k": kp}),
    CreateAgent(single_integrator, modelparam, g_distance, {"k": kp}),
    CreateAgent(single_integrator, modelparam, g_distance, {"k": kp}),
    CreateAgent(single_integrator, modelparam, g_distance, {"k": kp}),
    CreateAgent(single_integrator, modelparam, g_distance, {"k": kp}),
    CreateAgent(single_integrator, modelparam, g_distance, {"k": kp}),
    CreateAgent(single_integrator, modelparam, g_distance, {"k": kp}),
    CreateAgent(single_integrator, modelparam, g_distance, {"k": kp}),
]

formation = AgentFormation(agents, G, formation_references, n)


# Simulate and animate
x0 = np.array([1, 0, 2, 2, 3, -1, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0])

t = np.arange(0, 50, 0.05)
x = odeint(formation.ode, x0, t)


# Animate the results

fig, ax = plt.subplots()
ax.axis([-2, 6, -3, 6])
ax.set_xlabel("x")
ax.set_ylabel("y")

m = tuple([ax.plot(np.nan, np.nan, "bo")[0] for k in range(len(agents))])
text = ax.text(-1.5, 4, "")


def animate(i):
    for idx, mi in enumerate(m):
        mi.set_xdata([x[i, 0 + n * idx]])
        mi.set_ydata([x[i, 1 + n * idx]])
    text.set_text(f"t = {t[i]:.1f}")
    return m + (text,)


ani = animation.FuncAnimation(
    fig, animate, interval=5, frames=x.shape[0], blit=True, repeat=False
)

plt.figure()
plt.plot(t, np.linalg.norm(x[:, 0:2] - x[:, 2:4], axis=1))
plt.xlabel("Time [s]")
plt.ylabel("Distance [m]")
plt.title(rf"Distance between agent 0 and agent 1, $k_p = {kp}$")
plt.show()
# %%
