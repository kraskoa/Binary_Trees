import time
import gc
import random
from bst_tree import BST_tree, Node
from avl_tree import AVL_Tree
from graph_maker import graph_maker, combined_2_graph_maker
from create_list import create_list


def create_list(n):
    return random.sample(range(1, 300000000000), k=n)


def main():
    BST_insert_times = {}
    BST_search_times = {}
    BST_remove_times = {}
    AVL_insert_times = {}
    AVL_search_times = {}

    test_lists = {}
    for i in range(1, 10):
        test_lists[100000 * i] = create_list(100000 * i)

    for key in test_lists.keys():
        new_list = test_lists[key]
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        root = Node(new_list[0])
        bst_tree = BST_tree(root)
        for number in new_list[1:]:
            bst_tree.insert(root, number)
        stop = time.process_time()
        insert_time = stop - start
        if gc_old:
            gc.enable()
        BST_insert_times[key] = insert_time
    graph_maker(BST_insert_times, "BST creation times")
    print("BST creation times: ", BST_insert_times)

    for key in test_lists.keys():
        new_list = test_lists[key]
        root = Node(test_lists[key][0])
        bst_tree = BST_tree(root)
        for number in test_lists[key]:
            bst_tree.insert(root, number)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for number in new_list:
            bst_tree.search(root, number)
        stop = time.process_time()
        search_time = stop - start
        if gc_old:
            gc.enable()
        BST_search_times[key] = search_time
    graph_maker(BST_search_times, "BST search times")
    print("BST search times: ", BST_search_times)

    for key in test_lists.keys():
        new_list = test_lists[key]
        root = Node(test_lists[key][0])
        bst_tree = BST_tree(root)
        for number in test_lists[key]:
            bst_tree.insert(root, number)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for number in new_list:
            bst_tree.remove(root, number)
        stop = time.process_time()
        remove_time = stop - start
        if gc_old:
            gc.enable()
        BST_remove_times[key] = remove_time
    graph_maker(BST_remove_times, "BST remove times")
    print("BST remove times: ", BST_remove_times)

    for key in test_lists.keys():
        new_list = test_lists[key]
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        avl_tree = AVL_Tree()
        root = None
        for number in test_lists[key]:
            avl_tree.insert_node(root, number)
        stop = time.process_time()
        insert_time = stop - start
        if gc_old:
            gc.enable()
        AVL_insert_times[key] = insert_time
    graph_maker(AVL_insert_times, "AVL creation times")
    print("AVL creation times: ", AVL_insert_times)

    for key in test_lists.keys():
        new_list = test_lists[key]
        avl_tree = AVL_Tree()
        root = None
        for number in test_lists[key]:
            avl_tree.insert_node(root, number)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for number in new_list:
            avl_tree.find_node(root, number)
        stop = time.process_time()
        search_time = stop - start
        if gc_old:
            gc.enable()
        AVL_search_times[key] = search_time
    graph_maker(AVL_search_times, "AVL search times")
    print("AVL search times: ", AVL_search_times)

    combined_2_graph_maker(
        BST_insert_times,
        "BST creation times",
        AVL_insert_times,
        "AVL creation times",
        "Combined creation times",
    )

    combined_2_graph_maker(
        BST_search_times,
        "BST search times",
        AVL_search_times,
        "AVL search times",
        "Combined search times",
    )


if __name__ == "__main__":
    main()
