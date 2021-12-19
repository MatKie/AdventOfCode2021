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
            adj_nodes = graph.get(start, set())
            adj_nodes.add(end)
            graph.update({start: adj_nodes})

    return graph, lower_nodes


class Graph(object):
    def __init__(self, graph, lower_nodes=set()):
        self.graph = graph
        self.rev_graph = self._get_rev_graph()
        self.lower_nodes = lower_nodes
        self.paths = []

    def _get_rev_graph(self):
        """
        Add the origin node to each graph end node. Making it bidirectional?

        Returns
        -------
        dict
            Bidirectional(?) graph.
        """
        rev_graph = copy.deepcopy(self.graph)  # clonky but need a real copy

        unique_keys = set(
            [this_item for item in rev_graph.values() for this_item in item]
        )
        for item in unique_keys:
            if item not in rev_graph.keys():
                rev_graph.update({item: set()})

        for start, ends in rev_graph.items():
            if start in ["start", "end"]:
                continue
            for end in ends:
                if end in ["start", "end"]:
                    continue
                adj_nodes_to_end = rev_graph.get(end)
                if start not in adj_nodes_to_end:
                    adj_nodes_to_end.add(start)
                    rev_graph.update({end: adj_nodes_to_end})

        return rev_graph

    def find_all_paths_loop(self):
        return self._find_all_paths_loop(self.rev_graph, "start", "end", [])

    def _find_all_paths_loop(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph.keys():
            return []
        # If visited a lower case node, remove it from all values
        if start in self.lower_nodes:
            for this_start, ends in graph.items():
                ends = ends.difference(set(start))
                graph.update({this_start: ends})

        paths = []
        for node in graph[start]:
            newpaths = self._find_all_paths_loop(copy.deepcopy(graph), node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

        return paths

    def _find_all_paths_no_loop(self, start, end, path=[]):
        """
        Recursive path finding, taken from:
        https://www.python.org/doc/essays/graphs/
        At each node the function is called recursively until the 
        end node is found or there is a 'terminal' without furhter connections.
        In the former case this is added to the list of paths, in the latter
        it's not.

        Parameters
        ----------
        start : str
            start node
        end : str
            end node
        path : list, optional
            [description], by default []

        Returns
        -------
        list
            list of paths.
        """
        path = path + [start]
        if start == end:
            return [path]
        if not start in self.graph.keys():
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self._find_all_paths_no_loop(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths
