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


def combined_2_graph_maker(
    times_1,
    times_1_name,
    times_2,
    times_2_name,
    graph_name="Combined graph",
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
    plt.legend()
    plt.title(label=graph_name)
    figure = plt.gcf()
    plt.show()
    figure.savefig(f'{graph_name}.png', format="png")
