#!/usr/bin/env python

#%% all 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collab_functions import CreateAgent, AgentFormation

%matplotlib tk


def g_distance(y, xref, ctrlpar):
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
    Kp = ctrlpar["k"]
    p_i = y
    p_star = xref
    return Kp * (p_star - p_i)

n = 2
G = [
    (0,),
    (0, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (0, 2),
    (1, 2),
    (3, 2),
    (4, 2),
    (1, 3),
    (2, 3),
    (4, 3),
    (5, 3),
    (6, 3),
    (1, 4),
    (2, 4),
    (3, 4),
    (5, 4),
    (6, 4),
    (3, 5),
    (4, 5),
    (6, 5),
    (7, 5),
    (3, 6),
    (4, 6),
    (5, 6),
    (7, 6),
    (7,),
]


rotation_frequency = 0.3
formation_references = [
    lambda t: [2 * np.cos(rotation_frequency * t), 2 * np.sin(rotation_frequency * t)],
    lambda t: [1, 0, 2, 3, 4],
    lambda t: [2, 0, 1, 3, 4],
    lambda t: [3, 1, 2, 4, 5, 6],
    lambda t: [4, 1, 2, 3, 5, 6],
    lambda t: [5, 3, 4, 6, 7],
    lambda t: [6, 3, 4, 5, 7],
    lambda t: [2 * np.cos(rotation_frequency * t), 2 * np.sin(rotation_frequency * t) - 6],
]


modelparam = {"m": 1}
ctrl_params = {"k": 1}

agents = [
    CreateAgent(single_integrator, modelparam, g_absolute, ctrl_params),
    CreateAgent(single_integrator, modelparam, g_distance, ctrl_params),
    CreateAgent(single_integrator, modelparam, g_distance, ctrl_params),
    CreateAgent(single_integrator, modelparam, g_distance, ctrl_params),
    CreateAgent(single_integrator, modelparam, g_distance, ctrl_params),
    CreateAgent(single_integrator, modelparam, g_distance, ctrl_params),
    CreateAgent(single_integrator, modelparam, g_distance, ctrl_params),
    CreateAgent(single_integrator, modelparam, g_absolute, ctrl_params),
]

formation = AgentFormation(agents, G, formation_references, n)


# Simulate and animate

x0 = np.array([1, 0, 2, 2, 3, -1, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0])

t = np.arange(0, 50, 0.05)
x = odeint(formation.ode, x0, t)


# Animate the results

fig, ax = plt.subplots()
ax.axis([-5, 7, -9, 3])
ax.set_aspect(1)
ax.set_xlabel("x")
ax.set_ylabel("y")

m = [ax.plot(np.nan, np.nan, "bo")[0] for k in range(len(agents))]
text = ax.text(-1.5, 7, "")

edges = [e for e in G if len(e) > 1]
paths = [ax.plot([], [], "-", label=f"Agent {i}")[0] for i in range(len(agents))]
ax.legend()


def animate(i):
    for idx, mi in enumerate(m):
        mi.set_xdata([x[i, n * idx]])
        mi.set_ydata([x[i, n * idx + 1]])
        paths[idx].set_xdata(x[: i + 1, n * idx])
        paths[idx].set_ydata(x[: i + 1, n * idx + 1])

    # for line, (a, b) in zip(edge_lines, edges):
    #     line.set_xdata([x[i, n * a], x[i, n * b]])
    #     line.set_ydata([x[i, n * a + 1], x[i, n * b + 1]])

    text.set_text(f"t = {t[i]:.1f}")

    # return m + edge_lines + [text]
    return m + paths + [text]


if 0:
    ani = animation.FuncAnimation(
        fig, animate, interval=5, frames=x.shape[0], blit=True, repeat=False
    )
else:
    animate(x.shape[0] - 1)  # skip to end

plt.show()

# %%
