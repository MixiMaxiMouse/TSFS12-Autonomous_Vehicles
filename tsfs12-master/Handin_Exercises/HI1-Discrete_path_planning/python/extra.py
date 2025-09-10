#!/usr/bin/env python
# coding: utf-8

# %% TSFS12 Hand-in exercise 1, extra assignment: Discrete planning in structured road networks

# Do initial imports of packages needed

import matplotlib.pyplot as plt
from misc import Timer, latlong_distance
from osm import load_osm_map
from utils import plot_plan
from queues import PriorityQueue
import numpy as np


# Run if you want plots in external windows
# %matplotlib


# Run the ipython magic below to activate automated import of modules. Useful if you write code in external .py files.
# %load_ext autoreload
# %autoreload 2


# %% Load map, define state transition function, and heuristic for Astar

osm_file = "linkoping.osm"
fig_file = "linkoping.png"
osm_map = load_osm_map(osm_file, fig_file)  # Defaults loads files from ../Maps

num_nodes = len(osm_map.nodes)  # Number of nodes in the map

missions = [
    {"start": {"id": 10906}, "goal": {"id": 1024}},
    {"start": {"id": 3987}, "goal": {"id": 1024}},
    {"start": {"id": 423}, "goal": {"id": 1024}},
]

mission = missions[0]  # Pick one of the predefined missions
# Define function to compute possible next nodes from node x and the corresponding distances distances.


def f_next(x):
    """Compute, neighbours for a node"""
    cx = osm_map.distancematrix[x, :].tocoo()
    return cx.col, np.full(cx.col.shape, np.nan), cx.data


def heuristic(x, xg):
    # YOUR CODE HERE
    p_x = osm_map.nodeposition[x]
    p_g = osm_map.nodeposition[xg]
    return latlong_distance(p_x, p_g)


# %% Define planning missions with same goal node
# %% define AnytimeAstar planner
def anytime_astar(num_nodes, mission, f_next, heuristic=None, num_controls=0):
    """Anytime Astar planner."""
    allowed_time = 50.0 # seconds
    c_factor = 3.0 # initial inflation factor
    c_values = []
    c_decay = 0.5 # inflation factor decay per iteration
    t = Timer()
    Ti = Timer()
    t.tic()
    out = []

    while c_factor > 1.0 and t.toc() < allowed_time:
        iter_time = Ti.tic()
        c_factor -= c_decay
        unvis_node = -1
        previous = np.full(num_nodes, dtype=int, fill_value=unvis_node)
        cost_to_come = np.zeros(num_nodes)
        control_to_come = np.zeros((num_nodes, num_controls), dtype=int)
        expanded_nodes = []
        # expanded = visited

        startNode = mission["start"]["id"]
        goalNode = mission["goal"]["id"]

        q = PriorityQueue()
        q.insert(startNode, c_factor * heuristic(startNode, goalNode)) 
        foundPlan = False

        while not q.IsEmpty() and t.toc() < allowed_time:
            x = q.pop()[0]
            expanded_nodes.append(x)
            if x == goalNode:
                foundPlan = True
                duration = Ti.toc()
                break
            neighbours, u, d = f_next(x)
            for xi, ui, di in zip(neighbours, u, d):
                if previous[xi] == unvis_node or cost_to_come[x] + di < cost_to_come[xi] :
                    previous[xi] = x
                    cost_to_come[xi] = cost_to_come[x] + di
                    q.insert(xi,cost_to_come[xi] + c_factor * heuristic(xi, goalNode))
                    if num_controls > 0:
                        control_to_come[xi] = ui
        c_values.append(c_factor)
        # Recreate the plan by traversing previous from goal node
        if not foundPlan:
            return []
        else:
            plan = [goalNode]
            length = cost_to_come[goalNode]
            control = []
            while plan[0] != startNode:
                if num_controls > 0:
                    control.insert(0, control_to_come[plan[0]])
                plan.insert(0, previous[plan[0]])
            plan_to_plot = {
                "plan": plan,
                "length": length,
                "num_expanded_nodes": len(expanded_nodes),
                "name": "AnytimeAstar",
                "time": duration,
                "control": control,
                "expanded_nodes": expanded_nodes,
            }
            out.append(plan_to_plot)
            #plot_plan(plan_to_plot, f"Anytime Astar ({plan_to_plot['length']:.1f} m)", "AnytimeAstar")
    return out, c_values

# %% run AnytimeAstar planner
anytime_astar_plans = anytime_astar(num_nodes, mission, f_next, heuristic)[0]
for plan in anytime_astar_plans:
    plot_plan(plan,osm_map, f"Anytime Astar ({plan['length']:.1f} m)", "AnytimeAstar")

# Predefined planning missions with the same goal node that you can use. You are welcome to experiment with other missions.




# %% Exercises

# %% run anytime astar plot
def plot_c_anytime_astar(out):
    out, c_values = out
    plt.figure()
    for i, plan in enumerate(out):
        plt.plot(c_values[i], plan['length'],
                 'o-',
                 label=c_values[i],
                 linewidth=1.)

    plt.xlabel('c')
    plt.ylabel('plan length [m]')
    plt.title('Anytime Astar: Plan length for different inflation factors')
    
    plt.grid(True)
    plt.show()
out = anytime_astar(num_nodes, mission, f_next, heuristic)
plot_c_anytime_astar(out)
# %%
plt.show()
