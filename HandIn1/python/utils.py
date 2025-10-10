import matplotlib.pyplot as plt
def plot_plan(plan,osm_map, label, title):
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