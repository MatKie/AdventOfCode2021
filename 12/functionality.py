import copy
import sys


def read_input(filename):
    """
    Parse the graph from the input

    Parameters
    ----------
    filename : str
        path to file

    Returns
    -------
    dict and a list
        each key is a node with adjacent nodes given as set.
        The list holds all lower nodes, which can only be visited once.
    """
    graph = dict()
    lower_nodes = set()
    with open(filename, "r") as f:
        for line in f:
            start, end = [item.strip() for item in line.rstrip().split("-")]
            if start.islower():
                lower_nodes.add(start)
            if end.islower():
                lower_nodes.add(end)
            for a, b in zip([start, end], [end, start]):
                adj_nodes = graph.get(a, set())
                adj_nodes.add(b)
                graph.update({a: adj_nodes})

    return graph, lower_nodes


class Graph(object):
    def __init__(self, graph, lower_nodes=set()):
        self.graph = graph
        self.lower_nodes = lower_nodes

    def find_all_paths_loop(self):
        """DFS wrapper"""
        return self.depth_first_search(self.graph, "start", "end", [], [])

    @staticmethod
    def depth_first_search(graph, start, end, path=[], paths=[]):
        """
        DFS algorithm: Explore one path till you find end, then backtrack
        until there is a node with another possible way to go except 
        the backtracked way.

        Parameters
        ----------
        graph : dict
            bidirectional graph
        start : str
            current location in the graph
        end : str
            end node
        path : list, optional
            current path, by default []
        paths : list, optional
            all paths found so far, by default []

        Returns
        -------
        list (paths)
            all paths found
        """
        path = path + [start]
        if start == end:
            paths.append(copy.deepcopy(path))
            # paths.append(path)
        else:
            # if there ewas start == target we backtrack (pop) items
            # from the path, until we reach a node with vertices
            # leading down other paths.
            # dead ends will be automatically popped as there are no
            # nodes at that graph[start].
            for node in graph[start]:
                if not (node in path and node.islower()):
                    Graph.depth_first_search(graph, node, end, path, paths)
        path.pop()
        return paths

    def find_part_2(self):
        """DFS wrapper"""
        return self.dfs_part_2(self.graph, "start", "end", [], [])

    @staticmethod
    def dfs_part_2(graph, start, end, path, paths=[]):
        """
        Same DFS as before, but allowing to visit one node twice and
        not keeping track of pahts.
        """
        path = path + [start]
        # Check if we visited a small cave before
        small_caves = [item for item in path if item.islower()]
        if len(set(small_caves)) < len(small_caves):
            visited_twice = True
        else:
            visited_twice = False
        if start == end:
            # paths.append(copy.deepcopy(path))
            paths.append(path)
        else:
            for node in graph[start]:
                if not (node in path and (node.islower() and visited_twice)):
                    if node != "start":
                        Graph.dfs_part_2(graph, node, end, path, paths)
        path.pop()
        return paths
