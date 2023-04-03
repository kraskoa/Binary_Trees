import time
import gc
import random
from bst_tree import BST_tree, Node
from avl_tree import AVL_Tree
from graph_maker import graph_maker, combined_2_graph_maker


def main():
    BST_insert_times = {}
    BST_search_times = {}
    BST_remove_times = {}
    AVL_insert_times = {}
    AVL_search_times = {}
    number_list = [
        1000,
        2000,
        3000,
        4000,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
    ]

    random_number_list = []
    for _ in range(10000):
        random_number_list.append(random.randint(1, 30000))

    for number_of_numbers in number_list:
        new_list = random_number_list[:number_of_numbers]
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
        BST_insert_times[number_of_numbers] = insert_time
    graph_maker(BST_insert_times, "BST creation times")
    print("BST creation times: ", BST_insert_times)

    for number_of_numbers in number_list:
        new_list = random_number_list[:number_of_numbers]
        root = Node(random_number_list[0])
        bst_tree = BST_tree(root)
        for number in random_number_list[1:]:
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
        BST_search_times[number_of_numbers] = search_time
    graph_maker(BST_search_times, "BST search times")
    print("BST search times: ", BST_search_times)

    for number_of_numbers in number_list:
        new_list = random_number_list[:number_of_numbers]
        root = Node(random_number_list[0])
        bst_tree = BST_tree(root)
        for number in random_number_list[1:]:
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
        BST_remove_times[number_of_numbers] = remove_time
    graph_maker(BST_remove_times, "BST remove times")
    print("BST remove times: ", BST_remove_times)

    for number_of_numbers in number_list:
        new_list = random_number_list[:number_of_numbers]
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        avl_tree = AVL_Tree()
        root = None
        for number in new_list[1:]:
            avl_tree.insert_node(root, number)
        stop = time.process_time()
        insert_time = stop - start
        if gc_old:
            gc.enable()
        AVL_insert_times[number_of_numbers] = insert_time
    graph_maker(AVL_insert_times, "AVL creation times")
    print("AVL creation times: ", AVL_insert_times)

    for number_of_numbers in number_list:
        new_list = random_number_list[:number_of_numbers]
        avl_tree = AVL_Tree()
        root = None
        for number in random_number_list[1:]:
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
        AVL_search_times[number_of_numbers] = search_time
    graph_maker(AVL_search_times, "AVL search times")
    print("AVL search times: ", AVL_search_times)

    combined_2_graph_maker(
        BST_insert_times,
        "BST creation times",
        AVL_insert_times,
        "AVL creation times",
        "Combined creation times"
    )

    combined_2_graph_maker(
        BST_search_times,
        "BST search times",
        AVL_search_times,
        "AVL search times",
        "Combined search times"
    )



if __name__ == "__main__":
    main()
