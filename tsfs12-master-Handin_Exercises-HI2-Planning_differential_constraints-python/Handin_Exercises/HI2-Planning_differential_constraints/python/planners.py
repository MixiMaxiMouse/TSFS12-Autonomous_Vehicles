#!/usr/bin/env python
# coding: utf-8

# %% TSFS12 Hand-in exercise 1: Discrete planning in structured road networks

# Do initial imports of packages needed

import numpy as np
import matplotlib.pyplot as plt
from misc import Timer
from queues import FIFO, LIFO, PriorityQueue

#  %% Implement planners

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
