#!/usr/bin/env python
# coding: utf-8

# %% TSFS12 Hand-in exercise 1: Discrete planning in structured road networks

# Do initial imports of packages needed

import numpy as np
import matplotlib.pyplot as plt
from misc import Timer, latlong_distance
from queues import FIFO, LIFO, PriorityQueue
from osm import load_osm_map


# Run if you want plots in external windows (needed for manual mission definition)
%matplotlib qt



# Run the ipython magic below to activate automated import of modules. Useful if you write code in external .py files.
# %load_ext autoreload
# %autoreload 2


# %% Load map

osm_file = "linkoping.osm"
fig_file = "linkoping.png"
osm_map = load_osm_map(osm_file, fig_file)  # Defaults loads files from ../Maps

num_nodes = len(osm_map.nodes)  # Number of nodes in the map


# Define function to compute possible next nodes from node x and the corresponding distances distances.


def f_next(x):
    """Compute, neighbours for a node

    Returns: neighbor_nodes, control [not used here], distance
    """
    cx = osm_map.distancematrix[x, :].tocoo()
    return cx.col, np.full(cx.col.shape, np.nan), cx.data


# % Display basic information about map

# Print some basic map information

osm_map.info()


# Plot the map

_, ax = plt.subplots(num=10, clear=True)
osm_map.plotmap()
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
_ = ax.set_title("Linköping")


# Which nodes are neighbors to node with index 110?

n, _, d = f_next(110)
print(f"Neighbours: {n}")
print(f"Distances: {d}")


# Look up the distance (in meters) between the nodes 110 and 3400 in the distance matrix?

print(osm_map.distancematrix[110, 3400])


# Latitude and longitude of node 110

p = osm_map.nodeposition[110]
print(f"Longitude = {p[0]:.3f}, Latitude = {p[1]:.3f}")


# Plot the distance matrix and illustrate sparseness

_, ax = plt.subplots(num=20, clear=True)
ax.spy(osm_map.distancematrix > 0, markersize=0.5)
ax.set_xlabel("Node index")
ax.set_ylabel("Node index")
density = np.sum(osm_map.distancematrix > 0) / num_nodes**2
_ = ax.set_title(f"Density {density*100:.2f}%")


# %% Define planning mission

# Some pre-defined missions to experiment with. To use the first pre-defined mission, call the planner with
# ```planner(num_nodes, pre_mission[0], f_next, cost_to_go)```.

pre_mission = [
    {"start": {"id": 10906}, "goal": {"id": 1024}},
    {"start": {"id": 3987}, "goal": {"id": 4724}},
    {"start": {"id": 423}, "goal": {"id": 5119}},
]

mission = pre_mission[0]  # Use this line if you want to use the predefined missions


# To define a new mission, run the code below. In the map, click on start and goal positions to define a mission. Try different missions, ranging from easy to more complex.
# An easy mission is a mission in the city centre; while a more difficult could be from Vallastaden to Tannefors. Use this to find interesting plans when experimenting.
#
# For this to work you need to activate an interactive Matplotlib backend (`%matplotlib`).
#%%
_, ax = plt.subplots(num=30, clear=True)
osm_map.plotmap()
ax.set_title('Linköping - click in map to define mission')
mission = {}

mission['start'] = osm_map.getmapposition()
ax.plot(mission['start']['pos'][0], mission['start']['pos'][1], 'bx')
mission['goal'] = osm_map.getmapposition()
ax.plot(mission['goal']['pos'][0], mission['goal']['pos'][1], 'bx')

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

print('Mission: Go from node %d ' % (mission['start']['id']), end='')
if mission['start']['name'] != '':
    print('(' + mission['start']['name'] + ')', end='')
print(' to node %d ' % (mission['goal']['id']), end='')
if mission['goal']['name'] != '':
    print('(' + mission['goal']['name'] + ')', end='')
print('')

pre_mission.append(mission)  # Add to list of predefined missions


# Show mission details

mission


# %% Implement planners


def depth_first(num_nodes, mission, f_next, heuristic=None, num_controls=0):
    """Depth first planner."""
    t = Timer()
    t.tic()

    unvis_node = -1
    previous = np.full(num_nodes, dtype=int, fill_value=unvis_node)
    cost_to_come = np.zeros(num_nodes)
    control_to_come = np.zeros((num_nodes, num_controls), dtype=int)
    expanded_nodes = []

    startNode = mission["start"]["id"]
    goalNode = mission["goal"]["id"]

    q = LIFO()
    q.insert(startNode)
    foundPlan = False

    while not q.IsEmpty():
        x = q.pop()
        expanded_nodes.append(x)
        if x == goalNode:
            foundPlan = True
            break
        neighbours, u, d = f_next(x)
        for xi, ui, di in zip(neighbours, u, d):
            if previous[xi] == unvis_node:
                previous[xi] = x
                q.insert(xi)
                cost_to_come[xi] = cost_to_come[x] + di
                if num_controls > 0:
                    control_to_come[xi] = ui

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

        return {
            "plan": plan,
            "length": length,
            "num_expanded_nodes": len(expanded_nodes),
            "name": "DepthFirst",
            "time": t.toc(),
            "control": control,
            "expanded_nodes": expanded_nodes,
        }


def plot_plan(plan,label, title):
    print(
    f"{plan['length']:.1f} m, {plan['num_expanded_nodes']} expanded nodes, planning time {plan['time'] * 1e3:.1f} msek"
    )
    # Plot the resulting plan

    _, ax = plt.subplots()
    osm_map.plotmap()
    osm_map.plotplan(plan["plan"], "b", label=label)
    ax.set_title("Linköping")
    _ = ax.legend()

    # Plot nodes visited during search

    _, ax = plt.subplots()
    osm_map.plotmap()
    osm_map.plotplan(plan["expanded_nodes"], "b.")
    ax.set_ylabel("Latitude")
    ax.set_xlabel("Longitude")
    _ = ax.set_title(f"Nodes visited during {title} search")

    # Names of roads along the plan ...

    plan_way_names = osm_map.getplanwaynames(plan["plan"])
    print("Start: ", end="")
    for w in plan_way_names[:-1]:
        print(w + " -- ", end="")
    print("Goal: " + plan_way_names[-1])

# %%# Planning example using the DepthFirst planner

# Make a plan using the ```DepthFirst``` planner

df_plan = depth_first(num_nodes, mission, f_next)
plot_plan(df_plan,f"Depth first ({df_plan['length']:.1f} m)", "DepthFirst")



# %% Define planners

# Here, write your code for your planners. Start with the template code for the depth first search and extend.

# %% run BreadthFirst planner
def breadth_first(num_nodes, mission, f_next, heuristic=None, num_controls=0):
    """Breadth first planner."""
    t = Timer()
    t.tic()

    unvis_node = -1
    previous = np.full(num_nodes, dtype=int, fill_value=unvis_node)
    cost_to_come = np.zeros(num_nodes)
    control_to_come = np.zeros((num_nodes, num_controls), dtype=int)
    expanded_nodes = []
    # expanded = visited

    startNode = mission["start"]["id"]
    goalNode = mission["goal"]["id"]

    q = FIFO()
    q.insert(startNode)
    foundPlan = False

    while not q.IsEmpty():
        x = q.pop()
        expanded_nodes.append(x)
        if x == goalNode:
            foundPlan = True
            break
        neighbours, u, d = f_next(x)
        for xi, ui, di in zip(neighbours, u, d):
            if previous[xi] == unvis_node:
                previous[xi] = x
                q.insert(xi)
                cost_to_come[xi] = cost_to_come[x] + di
                if num_controls > 0:
                    control_to_come[xi] = ui

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

        return {
            "plan": plan,
            "length": length,
            "num_expanded_nodes": len(expanded_nodes),
            "name": "BreadthFirst",
            "time": t.toc(),
            "control": control,
            "expanded_nodes": expanded_nodes,
        }

# Make a plan using the ```Breadthfirst``` planner
bf_plan = breadth_first(num_nodes, mission, f_next)
plot_plan(bf_plan,f"Breadth first ({bf_plan['length']:.1f} m)", "BreadthFirst")

# %% run Dijkstra planner

def dijkstra(num_nodes, mission, f_next, heuristic=None, num_controls=0):
    # I think dijkstra is just breadth first with a priority queue
    """Dijkstra planner."""
    t = Timer()
    t.tic()

    unvis_node = -1
    previous = np.full(num_nodes, dtype=int, fill_value=unvis_node)
    cost_to_come = np.zeros(num_nodes)
    control_to_come = np.zeros((num_nodes, num_controls), dtype=int)
    expanded_nodes = []
    # expanded = visited

    startNode = mission["start"]["id"]
    goalNode = mission["goal"]["id"]

    q = PriorityQueue()
    q.insert(startNode, 0)
    foundPlan = False

    while not q.IsEmpty():
        x = q.pop()[0]
        expanded_nodes.append(x)
        if x == goalNode:
            foundPlan = True
            break
        neighbours, u, d = f_next(x)
        for xi, ui, di in zip(neighbours, u, d):
            if previous[xi] == unvis_node or cost_to_come[x] + di < cost_to_come[xi]:
                previous[xi] = x
                q.insert(xi, di + cost_to_come[x])
                cost_to_come[xi] = cost_to_come[x] + di
                if num_controls > 0:
                    control_to_come[xi] = ui

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

        return {
            "plan": plan,
            "length": length,
            "num_expanded_nodes": len(expanded_nodes),
            "name": "Dijkstra",
            "time": t.toc(),
            "control": control,
            "expanded_nodes": expanded_nodes,
        }

dijkstra_plan = dijkstra(num_nodes, mission, f_next)
plot_plan(dijkstra_plan,f"Dijkstra ({dijkstra_plan['length']:.1f} m)", "Dijkstra")

# %% run Astar planner
def astar(num_nodes, mission, f_next, heuristic=None, num_controls=0):
    """astar planner."""
    t = Timer()
    t.tic()

    unvis_node = -1
    previous = np.full(num_nodes, dtype=int, fill_value=unvis_node)
    cost_to_come = np.zeros(num_nodes)
    control_to_come = np.zeros((num_nodes, num_controls), dtype=int)
    expanded_nodes = []
    # expanded = visited

    startNode = mission["start"]["id"]
    goalNode = mission["goal"]["id"]

    q = PriorityQueue()
    q.insert(startNode, heuristic(startNode, goalNode))
    foundPlan = False

    while not q.IsEmpty():
        x = q.pop()[0]
        expanded_nodes.append(x)
        if x == goalNode:
            foundPlan = True
            break
        neighbours, u, d = f_next(x)
        for xi, ui, di in zip(neighbours, u, d):
            if previous[xi] == unvis_node or cost_to_come[x] + di < cost_to_come[xi] :
                previous[xi] = x
                cost_to_come[xi] = cost_to_come[x] + di
                q.insert(xi,cost_to_come[xi] + heuristic(xi, goalNode))
                if num_controls > 0:
                    control_to_come[xi] = ui

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

        return {
            "plan": plan,
            "length": length,
            "num_expanded_nodes": len(expanded_nodes),
            "name": "Astar",
            "time": t.toc(),
            "control": control,
            "expanded_nodes": expanded_nodes,
        }
    


# %% Define heuristic for Astar and BestFirst planners

# Define the heuristic for Astar and BestFirst. The ```latlong_distance``` function will be useful.

def cost_to_go(x, xg):
    p_x = osm_map.nodeposition[x]
    p_g = osm_map.nodeposition[xg]
    return latlong_distance(p_x, p_g)


astar_plan = astar(num_nodes, mission, f_next, cost_to_go)
plot_plan(astar_plan,f"Astar({astar_plan['length']:.1f} m)", "Astar")

def best_first(num_nodes, mission, f_next, heuristic=None, num_controls=0):
    """best first planner."""
    t = Timer()
    t.tic()

    unvis_node = -1
    previous = np.full(num_nodes, dtype=int, fill_value=unvis_node)
    cost_to_come = np.zeros(num_nodes)
    control_to_come = np.zeros((num_nodes, num_controls), dtype=int)
    expanded_nodes = []
    # expanded = visited

    startNode = mission["start"]["id"]
    goalNode = mission["goal"]["id"]

    q = PriorityQueue()
    q.insert(startNode, heuristic(startNode, goalNode))
    foundPlan = False

    while not q.IsEmpty():
        x = q.pop()[0]
        expanded_nodes.append(x)
        if x == goalNode:
            foundPlan = True
            break
        neighbours, u, d = f_next(x)
        for xi, ui, di in zip(neighbours, u, d):
            if previous[xi] == unvis_node or cost_to_come[x] + di < cost_to_come[xi] :
                previous[xi] = x
                cost_to_come[xi] = cost_to_come[x] + di
                q.insert(xi,heuristic(xi, goalNode))
                if num_controls > 0:
                    control_to_come[xi] = ui

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

        return {
            "plan": plan,
            "length": length,
            "num_expanded_nodes": len(expanded_nodes),
            "name": "bestFirst",
            "time": t.toc(),
            "control": control,
            "expanded_nodes": expanded_nodes,
        }

# %% run BestFirst planner

best_first_plan = best_first(num_nodes, mission, f_next, cost_to_go)
plot_plan(best_first_plan,f"Best first ({best_first_plan['length']:.1f} m)", "BestFirst")

# %% run AnytimeAstar planner
def anytime_astar(num_nodes, mission, f_next, heuristic=None, num_controls=0):
    """Anytime Astar planner."""
    allowed_time = 50.0 # seconds
    c_factor = 3.0 # initial inflation factor
    c_values = []
    c_decay = 0.05 # inflation factor decay per iteration
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
    return out #, c_values

anytime_astar_plan = anytime_astar(num_nodes, mission, f_next, cost_to_go)
# %% Assertions

# Below are a few of tests on your implementations. Note, just because your implementation passes the tests doesn't mean that your implementations are fully correct. Do not submit a solution if you fail any of these tests!

res_dijkstra = dijkstra(num_nodes, pre_mission[0], f_next)
res_astar = astar(num_nodes, pre_mission[0], f_next, cost_to_go)

assert res_dijkstra["length"] == res_astar["length"]
assert abs(res_astar["length"] - 5085.5957) < 1e-2


res_dijkstra = dijkstra(num_nodes, pre_mission[1], f_next)
res_astar = astar(num_nodes, pre_mission[1], f_next, cost_to_go)

assert res_dijkstra["length"] == res_astar["length"]
assert abs(res_astar["length"] - 2646.2140) < 1e-2


res_dijkstra = dijkstra(num_nodes, pre_mission[2], f_next)
res_astar = astar(num_nodes, pre_mission[2], f_next, cost_to_go)

assert res_dijkstra["length"] == res_astar["length"]
assert abs(res_astar["length"] - 1860.7143) < 1e-2


# %% Investigations using all planners

def get_length_vs_time(planner, num_nodes, f_next, heuristic=None):
    out = []  # (length, time)
    for mission in pre_mission:
        plan = planner(num_nodes, mission, f_next, heuristic)
        print(
            f"{planner.__name__:12s}: {plan['length']:8.1f} m, {plan['num_expanded_nodes']:5d} expanded nodes, planning time {plan['time']*1e3:8.1f} msek"
        )
        out.append((plan["length"], plan["time"]))
    return out

def get_time_vs_expanded(planner, num_nodes, f_next, heuristic=None):
    out = []  # (time, expanded)
    for mission in pre_mission:
        plan = planner(num_nodes, mission, f_next, heuristic)
        if not plan or not isinstance(plan, dict):  # skip if plan is empty or not a dict
            continue
        print(
            f"{planner.__name__:12s}: {plan['length']:8.1f} m, {plan['num_expanded_nodes']:5d} expanded nodes, planning time {plan['time']*1e3:8.1f} msek"
        )
        out.append((plan["time"], plan["num_expanded_nodes"]))
    return out

def plot_length_vs_time(data, title):
    plt.figure()
    for i, (planner_name, planner_data) in enumerate(data.items()):
       
        planner_data_sorted = sorted(planner_data, key=lambda x: x[0])
        lengths, times = zip(*planner_data_sorted)

       
        plt.plot(lengths, times,
                 label=planner_name,
                 linewidth=1.)

    plt.xlabel('Plan length [m]')
    plt.ylabel('Planning time [s]')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_time_vs_expanded(data, title):
    plt.figure()
    for i, (planner_name, planner_data) in enumerate(data.items()):
       
        planner_data_sorted = sorted(planner_data, key=lambda x: x[0])
        if not planner_data_sorted:
            continue
        lengths, times = zip(*planner_data_sorted)

       
        plt.plot(lengths, times,
                 label=planner_name,
                 linewidth=1.)

    plt.xlabel('Planning time [ms]')
    plt.ylabel('Expanded nodes[#]')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def cycle_len_time():
    planners = {
        'DepthFirst': (depth_first, None),
        'BreadthFirst': (breadth_first, None),
        'Dijkstra': (dijkstra, None),
        'BestFirst': (best_first, cost_to_go),
        'Astar': (astar, cost_to_go),
        'AnytimeAstar': (anytime_astar, cost_to_go)
    }
    data = {}
    for planner_name, (planner_func, heuristic) in planners.items():
        print(f'Running planner: {planner_name}')
        data[planner_name] = get_length_vs_time(planner_func, num_nodes, f_next, heuristic)
    plot_length_vs_time(data, 'Plan length vs Planning time for different planners')

# %% run len time
cycle_len_time()

#%% run time vs expanded
def cycle_time_expanded():
    planners = {
        'DepthFirst': (depth_first, None),
        'BreadthFirst': (breadth_first, None),
        'Dijkstra': (dijkstra, None),
        'BestFirst': (best_first, cost_to_go),
        'Astar': (astar, cost_to_go),
        'AnytimeAstar': (anytime_astar, cost_to_go)
    }
    data = {}
    for planner_name, (planner_func, heuristic) in planners.items():
        print(f'Running planner: {planner_name}')
        data[planner_name] = get_time_vs_expanded(planner_func, num_nodes, f_next, heuristic)
    plot_time_vs_expanded(data, 'Planing time vs expanded nodes for different planners')
cycle_time_expanded()

# %% run anytime astar plot
def plot_anytime_astar(out):
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
out = anytime_astar(num_nodes, mission, f_next, cost_to_go)
plot_anytime_astar(out)
# %%
plt.show()

# %%
