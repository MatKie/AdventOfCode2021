from functionality import read_input
from functionality import Graph


class TestInput:
    def test_input(self):
        graph, lower_nodes = read_input("exampleinput.txt")

        assert lower_nodes == set(("c", "b", "end", "start", "d"))

        assert set(graph.get("A")) == set(("c", "b", "end", "start"))


class TestGraph:
    def test_find_all_paths_lower_nodes(self):
        graph, lower_nodes = read_input("exampleinput.txt")

        ThisGraph = Graph(graph, lower_nodes)
        paths = ThisGraph.find_all_paths_loop()

        assert len(paths) == 10

        for path in paths:
            print(path, type(path))
        paths = set(tuple(tuple(path) for path in paths))
        sol = set(
            (
                ("start", "A", "end"),
                ("start", "A", "b", "end"),
                ("start", "b", "end"),
                ("start", "b", "A", "c", "A", "end"),
                ("start", "A", "c", "A", "end"),
                ("start", "A", "c", "A", "b", "end"),
                ("start", "A", "b", "A", "c", "A", "end"),
                ("start", "A", "b", "A", "end"),
                ("start", "b", "A", "end"),
                ("start", "A", "c", "A", "b", "A", "end"),
            )
        )
        print("sol dif paths")
        print(sol.difference(paths))
        assert paths == sol

    def test_find_all_paths_lower_nodes_2(self):
        graph, lower_nodes = read_input("exampleinput_2.txt")

        OtherGraph = Graph(graph, lower_nodes)

        other_paths = OtherGraph.find_all_paths_loop()
        # for item in other_paths:
        #    print(item)
        assert len(other_paths) == 19


class TestGraph_2:
    def test_find_all_paths_lower_nodes(self):
        graph, lower_nodes = read_input("exampleinput.txt")

        ThisGraph = Graph(graph, lower_nodes)
        paths = ThisGraph.find_part_2()

        assert len(paths) == 36

    def test_find_all_paths_lower_nodes_2(self):
        graph, lower_nodes = read_input("exampleinput_2.txt")

        OtherGraph = Graph(graph, lower_nodes)

        other_paths = OtherGraph.find_part_2()
        # for item in other_paths:
        #    print(item)
        assert len(other_paths) == 103


TestGraph_2().test_find_all_paths_lower_nodes()
