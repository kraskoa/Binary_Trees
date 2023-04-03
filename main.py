import time
import gc
import random
from bst_tree import BST_tree
from avl_tree import AVL_Tree
from graph_maker import graph_maker, combined_graph_maker


def main():
    BST_instert_times = {}
    BST_search_times = {}
    AVL_insert_times = {}
    AVL_search_times = {}

    random_list = []
    for _ in range(10000):
        random_list.append(random.randint(1, 30000))






if __name__ == "__main__":
    main()