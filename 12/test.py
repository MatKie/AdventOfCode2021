from functionality import read_input, Graph


class TestInput:
    def test_input(self):
        graph, lower_nodes = read_input("exampleinput.txt")

        assert lower_nodes == set(("c", "b", "end", "start", "d"))

        assert set(graph.get("A")) == set(("c", "b", "end"))


class TestGraph:
    def test_find_all_paths(self):
        graph, lower_nodes = read_input("exampleinput.txt")

        ThisGraph = Graph(graph)
        paths = ThisGraph._find_all_paths_no_loop("start", "end")

        print(paths)
        assert set(tuple(tuple(path) for path in paths)) == set(
            (("start", "A", "end"), ("start", "A", "b", "end"), ("start", "b", "end"))
        )

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

        ThisGraph = Graph(graph, lower_nodes)
        paths = ThisGraph.find_all_paths_loop()

        assert len(paths) == 19

