#!/usr/bin/env python
# coding: utf-8

# %% TSFS12 Hand-in Exercise 2: Planning for Vehicles with Differential Motion Constraints --- Motion Planning Using a State Lattice

import numpy as np
import matplotlib.pyplot as plt

# Assumes that you have all your planners in the file planners.py
from planners import breadth_first, depth_first, dijkstra, astar, best_first
from world import BoxWorld
from motionprimitives import MotionPrimitives
import os
from seaborn import despine


# %% Run instead if you want plots in external windows
%matplotlib qt


# Run the ipython magic below to activate automated import of modules. Useful if you write code in external .py files.
# %load_ext autoreload
# %autoreload 2


# %% Motion Primitives

# Run CasADi to pre-compute all motion primitives and save results in a pickle file for later re-use

file_name = "mprims.pickle"
if os.path.exists(file_name):
    mp = MotionPrimitives(file_name)
    print(f"Read motion primitives from file {file_name}")
else:
    # Define the initial states and desired goal states for the motion
    # primitives
    theta_init = np.array(
        [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, -3 * np.pi / 4, -np.pi / 2, -np.pi / 4]
    )

    x_vec = np.array([3, 2, 3, 3, 3, 1, 3, 3, 3, 2, 3])
    y_vec = np.array([2, 2, 2, 1, 1, 0, -1, -1, -2, -2, -2])
    th_vec = np.array(
        [0, np.pi / 4, np.pi / 2, 0, np.pi / 4, 0, -np.pi / 4, 0, -np.pi / 2, -np.pi / 4, 0]
    )
    state_0 = np.column_stack((x_vec, y_vec, th_vec))

    # Vehicle parameters and constraints
    L = 1.5  # Wheel base (m)
    v = 15  # Constant velocity (m/s)
    u_max = np.pi / 4  # Maximum steering angle (rad)

    # Construct a MotionPrimitives object and generate the
    # motion primitives using the constructed lattice and
    # specification of the motion primitives
    mp = MotionPrimitives()
    mp.generate_primitives(theta_init, state_0, L, v, u_max)
    mp.save(file_name)


# Plot the computed motion primitives

_, ax = plt.subplots(num=10, clear=True)
mp.plot("b", lw=0.5)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Motion primitives")
despine()


# %% Define Planning Mission

# Create world with obstacles using the BoxWorld class

xx = np.arange(-2, 13)
yy = np.arange(-2, 13)
th = np.array(
    [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, -3 * np.pi / 4, -np.pi / 2, -np.pi / 4]
)

nb_of_missions = 10

# Example planning missions


arrow_length = 1.0
arrow_width = 0.075


# Define the initial and goal state for the graph search by finding the
# node number (column number in world.st_sp) in the world state space

mission_to_test = 3 # Change this to test different missions
missions = []
worlds = []
starts = []
goals = []
for mission_nbr in range(3, nb_of_missions):

    world = BoxWorld((xx, yy, th))
    if mission_nbr == 0:
        world.add_box(0, 1, 2, 4)
        world.add_box(0, 6, 6, 4)
        world.add_box(4, 1, 6, 4)
        world.add_box(7, 7, 3, 3)

        start = [0, 0, 0]
        goal = [7, 8, np.pi / 2]
        
    elif mission_nbr == 1:
        world.add_box(0, 1, 3, 4)
        world.add_box(0, 7, 10, 3)
        world.add_box(4, 1, 6, 4)

        start = [0, 0, 0]
        goal = [8, 6, np.pi / 2]

    elif mission_nbr == 2:
        world.add_box(-2, 0, 10, 5)
        world.add_box(-2, 6, 10, 4)

        start = [0, 5, 0]
        goal = [0, 6, np.pi]

    elif mission_nbr == 3:
        world.add_box(0, 3, 10, 2)
        world.add_box(0, 5, 4, 2)
        world.add_box(6, 5, 4, 2)

        start = [5, 7, 0]
        goal = [5, 6, 0]
    
    elif mission_nbr == 4:
        world.add_box(0, 3, 10, 2)
        world.add_box(0, 5, 4, 2)
        world.add_box(6, 5, 4, 2)

        start = [5, 7, 0]
        goal = [5, 7, 0]
    elif mission_nbr == 5:
        world.add_box(0, 3, 10, 2)
        world.add_box(0, 5, 4, 2)
        world.add_box(6, 5, 4, 2)

        start = [5, 7, 0]
        goal = [5, 8, 0]
    elif mission_nbr == 6:
        world.add_box(0, 3, 10, 2)
        world.add_box(0, 5, 4, 2)
        world.add_box(6, 5, 4, 2)

        start = [5, 7, 0]
        goal = [5, 9, 0]
    
    elif mission_nbr == 7:
        world.add_box(0, 3, 10, 2)
        world.add_box(0, 5, 4, 2)
        world.add_box(6, 5, 4, 2)

        start = [5, 7, 0]
        goal = [5, 10, 0]
    
    elif mission_nbr == 8:
        world.add_box(0, 3, 10, 2)
        world.add_box(0, 5, 4, 2)
        world.add_box(6, 5, 4, 2)

        start = [5, 7, 0]
        goal = [5, 11, 0]
    elif mission_nbr == 9:
        world.add_box(0, 3, 10, 2)
        world.add_box(0, 5, 4, 2)
        world.add_box(6, 5, 4, 2)

        start = [5, 7, 0]
        goal = [5, 12, 0]

    start_arrow = arrow_length * np.array([np.cos(start[2]), np.sin(start[2])])
    goal_arrow = arrow_length * np.array([np.cos(goal[2]), np.sin(goal[2])])    
    mission = {
    "start": {"id": np.argmin(np.sum((world.st_sp - np.array(start)[:, None]) ** 2, axis=0))},
    "goal": {"id": np.argmin(np.sum((world.st_sp - np.array(goal)[:, None]) ** 2, axis=0))},
    }
    starts.append(start)
    goals.append(goal)
    worlds.append(world)
    missions.append(mission)
    # Plot world and start and goal positions

    _, ax = plt.subplots(num=mission_nbr, clear=True)
    world.draw()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(*start[0:2], "bo", markersize=8, label="start")
    ax.plot(*goal[0:2], "ko", markersize=8, label="goal")
    ax.arrow(*start[0:2], *start_arrow[0:2], width=arrow_width, edgecolor="b", facecolor="b")
    ax.arrow(*goal[0:2], *goal_arrow[0:2], width=arrow_width, edgecolor="k", facecolor="k")
    _ = ax.axis([world.xmin, world.xmax, world.ymin, world.ymax])
    ax.legend()
    despine()


# %% Define State-Transition Function for Lattice Planner

# Define the state-transition function for the lattice planner


def next_state(x, world, mp, rev=True, tol=1e-5):
    """Input arguments:
     x - current state
     world - description of the map of the world
             using the class BoxWorld
     mp - object with motion primitives of the class MotionPrimitives
     rev - Allow reversing (default: True)
     tol - tolerance for comparison of closeness of states

    Output arguments:
     xi - List containing the indices of N possible next states from current
          state x, considering the obstacles and size of the world model

          To get the state corresponding to the first element in xi,
          world.st_sp[:, xi[0]]
     u - List of indices indicating which motion primitive used for reaching
         the states in xi. Each element in the list contains the two indices of the
         motion primitives used for reaching each state and the driving direction
         (1 forward, -1 reverse).

         If u_i = u[0] (first element), the corresponding motion primitive is
         mp.mprims[u_i[0], u_i[1]]
     d - List with the cost associated with each possible
         transition in xi"""

    state_i = world.st_sp[:, x]
    theta_i = state_i[2]
    mprims = mp.mprims

    xi = []
    u = []
    d = []

    # Iterate through all available primitives compatible with the current
    # angle state. Base set of motion primitives (nominally
    # corresponding to forward driving) is reversed for obtaining reverse
    # driving of the corresponding motion primitive.

    for i, j in mp.with_start_orientation_index(theta_i):
        mpi = mprims[i, j]

        # Create path to next state
        p = state_i[0:2, np.newaxis] + np.vstack((mpi["x"], mpi["y"]))
        state_next = np.vstack((p[:, -1:], mpi["th"][-1]))

        # Check if the path to next state is in the allowed area
        if not world.in_bound(state_next) or not world.obstacle_free(p):
            continue
        else:
            next_idx = np.argmin(np.sum((world.st_sp - state_next) ** 2, axis=0))
            xi.append(next_idx)
            d.append(mpi["ds"])
            u.append([i, j, 1])
    if rev:  # With reverse driving
        for i, j in mp.with_end_orientation_index(theta_i):
            mpi = mprims[i, j]

            # Create path to next state
            p = state_i[0:2, np.newaxis] + np.vstack(
                (np.flip(mpi["x"]) - mpi["x"][-1], np.flip(mpi["y"]) - mpi["y"][-1])
            )
            state_next = np.vstack((p[:, -1:], mpi["th"][0]))

            # Check if the path to next state is in the allowed area
            if not world.in_bound(state_next) or not world.obstacle_free(p):
                continue
            else:
                next_idx = np.argmin(np.sum((world.st_sp - state_next) ** 2, axis=0))
                xi.append(next_idx)
                d.append(mpi["ds"])
                u.append([i, j, -1])

    return (xi, u, d)


# The state-transition function is fully implemented. Apply it to the initial state and interpret the result.

# next_state(mission["start"]["id"], world, mp)


# # and do not allow reversing

# next_state(mission["start"]["id"], world, mp, rev=False)


# %% Call Planners

# Get number of nodes in the state space

n = worlds[mission_to_test].num_nodes()


# Define cost-to-go heuristic for planner

heuristic_type = 2
def cost_to_go(x, xg):
    if heuristic_type == 1:
        return np.linalg.norm(worlds[mission_to_test].st_sp[0:2, x] - worlds[mission_to_test].st_sp[0:2, xg])


# Plan using all pre-defined planners from Hand-in Exercise 1

all_planners = [breadth_first, depth_first, dijkstra, astar, best_first]
res = [
    planner(
        n,
        missions[mission_to_test],
        lambda x: next_state(x, worlds[mission_to_test], mp, rev=True),
        heuristic=cost_to_go,
        num_controls=3,
    )
    for planner in all_planners
]

opt_length = [r["length"] for r in res if r["name"] == "Dijkstra"][0]  # Dijkstra is optimal
print(f"Optimal length: {opt_length:.3f}")


# %% Plots and Analysis

# Hint: For see function ```mp.plan_to_path``` for useful information on how to plot resulting paths

help(mp.plan_to_path)
for i in range(len(res)):
    res0 = res[i]  
    # YOUR CODE HERE

    p, sp = mp.plan_to_path(starts[mission_to_test], res0)

    _, ax = plt.subplots(num=i, clear=True)
    worlds[mission_to_test].draw()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(*starts[mission_to_test][0:2], "bo", markersize=8, label="start")
    ax.plot(*goals[mission_to_test][0:2], "ko", markersize=8, label="goal")
    ax.arrow(*starts[mission_to_test][0:2], *start_arrow[0:2], width=arrow_width, edgecolor="b", facecolor="b")
    ax.arrow(*goals[mission_to_test][0:2], *goal_arrow[0:2], width=arrow_width, edgecolor="k", facecolor="k")
    ax.plot(p[:, 0], p[:, 1], lw=2, color="blue", label="path")

    for k in range(sp.shape[0]):
        segment_range = range(sp[k, 1], sp[k, 2])
        color = "b" if sp[k, 0] == 1 else "g"
        ax.plot(p[segment_range, 0], p[segment_range, 1], color=color, lw=2)
    ax.legend()
    despine()
    plt.show()

# %% Plot comparison of path lengths, planning times, and number of expanded nodes


def plot_length_vs_time() : 
    for planner in all_planners:
        ress = []
        print(f"Running planner: {planner.__name__}")

        for i,mission in enumerate(missions):
            print(mission)
            result = planner(
                n,
                mission,
                lambda x: next_state(x, worlds[i], mp, rev=True),
                heuristic=cost_to_go,
                num_controls=3,
            )
            print (result)
            ress.append(result)

        lengths = [r["length"] for r in ress]
        planning_times = [r["time"] for r in ress]
    
        combine = list(zip(lengths, planning_times))
        combine_sorted = sorted(combine, key=lambda x: x[0])
        lengths_sorted, planning_times_sorted  = map(list, zip(*combine_sorted))

        plt.plot(lengths_sorted, planning_times_sorted, label = planner.__name__)
        plt.xlabel('Path Length')
        plt.ylabel('Planning Time [s]')
        plt.legend()
        plt.title(f'Path Length vs Planning Time for {planner.__name__} Planner')
    plt.savefig(f'length_vs_time_handin2.pdf')
    plt.show()

plot_length_vs_time()
# %%
def plot_time_vs_expanded_nodes() : 
    for planner in all_planners:
        ress = []
        print(f"Running planner: {planner.__name__}")

        for i,mission in enumerate(missions):
            print(mission)
            result = planner(
                n,
                mission,
                lambda x: next_state(x, worlds[i], mp, rev=True),
                heuristic=cost_to_go,
                num_controls=3,
            )
            print (result)
            ress.append(result)

        
        planning_times = [r["time"] for r in ress]
        exp_nodes = [r["num_expanded_nodes"] for r in ress]
        combine = list(zip(planning_times, exp_nodes))
        combine_sorted = sorted(combine, key=lambda x: x[0])
        planning_times_sorted, exp_nodes_sorted  = map(list, zip(*combine_sorted))

        plt.plot(planning_times_sorted, exp_nodes_sorted, label = planner.__name__)
        plt.xlabel('time [s]')
        plt.ylabel('expanded nodes')
        plt.legend()
        plt.title(f'time vs expanded nodes for Planner')
    plt.savefig(f'time_vs_expanded_nodes_handin21.pdf')
    plt.show()

plot_time_vs_expanded_nodes()
# %%
plt.show()


# %%
