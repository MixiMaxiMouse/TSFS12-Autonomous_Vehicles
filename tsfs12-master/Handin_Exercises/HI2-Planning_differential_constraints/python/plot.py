import matplotlib.pyplot as plt
from motionprimitives import MotionPrimitives
import numpy as np
from lattice_planning import BoxWorld, cost_to_go, next_state, n, world, mp
from planners import *


all_planners = [breadth_first, depth_first, dijkstra, astar, best_first]
res = [
    planner(
        n,
        mission,
        lambda x: next_state(x, world, mp, rev=True),
        heuristic=cost_to_go,
        num_controls=3,
    )
    for planner in all_planners
]

lengths = [r["length"] for r in res]
planning_times = [r["time"] for r in res]
exp_nodes = [r["expanded"] for r in res]
planner_names = [r["name"] for r in res]

combine = list(zip(lengths, planning_times, exp_nodes, planner_names))

combine_sorted = sorted(combine, key=lambda x: x[0])
lengths_sorted, planning_times_sorted, exp_nodes_sorted, planner_names_sorted  = map(list, zip(*combine_sorted))

# Plot results

plt.plot(lengths_sorted, planning_times_sorted)
plt.xlabel('Path Length')
plt.ylabel('Planning Time [s]')
plt.title('Path Length vs Planning Time for Different Planners')
plt.show()