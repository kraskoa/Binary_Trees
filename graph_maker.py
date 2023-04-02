from matplotlib import pyplot as plt


def graph_maker(times, tree_operation_name):
    plt.plot(
        list(times.keys()),
        list(times.values()),
        label=tree_operation_name,
        markersize=3,
    )
    plt.legend()
    plt.title(label=tree_operation_name)
    figure = plt.gcf()
    plt.show()
    tree_operation_name += ".png"
    figure.savefig(tree_operation_name, format="png")


def combined_graph_maker(
    times_1,
    times_1_name,
    times_2,
    times_2_name,
    times_3,
    times_3_name,
    times_4,
    times_4_name,
):
    plt.plot(
        list(times_1.keys()),
        list(times_1.values()),
        label=times_1_name,
        markersize=3,
    )
    plt.plot(
        list(times_2.keys()),
        list(times_2.values()),
        label=times_2_name,
        markersize=3,
    )
    plt.plot(
        list(times_3.keys()),
        list(times_3.values()),
        label=times_3_name,
        markersize=3,
    )
    plt.plot(
        list(times_4.keys()),
        list(times_4.values()),
        label=times_4_name,
        markersize=3,
    )
    plt.legend()
    plt.title(label="All sorts")
    figure = plt.gcf()
    plt.show()
    figure.savefig("all_sorts.png", format="png")
