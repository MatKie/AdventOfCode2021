import pytest
from functionality import read_input, AltMap


class TestInput:
    def test_read_input(self):
        A = read_input("exampleinput.txt")

        assert A.shape == (5, 10)
        assert A[1, 1] == 9


class TestAltMap:
    def test_derivatives(self):
        A = read_input("exampleinput.txt")

        B = AltMap(A)

        B.derivatives()

        assert B.up[0, 0] == -11
        assert B.up[0, 5] == -11
        assert B.up[1, 1] == 8
        assert B.up[4, 3] == 2

        assert B.down[-1, 0] == -11
        assert B.down[1, 1] == 1
        assert B.down[0, 3] == 2

        assert B.left[-1, 0] == -11
        assert B.left[2, -1] == -7
        assert B.left[1, 1] == 6

        assert B.right[0, -1] == -11
        assert B.right[1, 1] == 1
        assert B.right[1, 3] == -1

        for arr in [B.right, B.left, B.down, B.up]:
            assert arr.shape == (5, 10)

    def test_risk_points(self):
        A = read_input("exampleinput.txt")

        B = AltMap(A)

        B.derivatives()

        risk_points = B.find_low_points()

        print(risk_points)

        assert risk_points == 15

    def test_basins(self):
        A = read_input("exampleinput.txt")
        B = AltMap(A)
        B.derivatives()
        risk_points = B.find_low_points()

        cluster_list = []
        for x, y in zip(*B.low_index):
            cluster = B._grow_cluster((x, y))
            cluster_list.append(cluster)

        assert cluster_list[0] == set(((0, 1), (0, 0), (1, 0)))

    def test_merge_clusters(self):
        A = read_input("exampleinput.txt")
        B = AltMap(A)
        B.derivatives()
        risk_points = B.find_low_points()

        cluster_list = []
        for x, y in zip(*B.low_index):
            cluster = B._grow_cluster((x, y))
            cluster_list.append(cluster)

        cluster_list.append(cluster)
        print(len(cluster_list))
        cluster_list = B._merge_cluster(cluster_list)

        assert len(cluster_list) == 4

    def test_basin_score(self):
        A = read_input("exampleinput.txt")
        B = AltMap(A)
        B.derivatives()
        risk_points = B.find_low_points()

        basin_score = B.find_basin_value()

        assert basin_score == 1134

