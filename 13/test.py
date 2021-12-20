from functionality import Folder


class TestFolder:
    def test_init(self):
        A = Folder("exampleinput.txt")

        assert type(A.folds[0]) == tuple
        assert A.folds[0][0] == "y"
        assert A.folds[1][1] == 5
        assert A.tuples[2][1] == 10
        assert A.tuples[3][1] == 3
        assert A.max_folds == 2

    def test_matrix(self):
        A = Folder("exampleinput.txt")
        A.construct_matrix()

        assert A.n_rows == 15
        assert A.n_cols == 11
        assert A.map[3, 4] == 0
        print(A.map)
        assert A.map[4, 3] == 1
        assert A.map[10, 8] == A.map[10, 9] == 1

    def test_fold(self):
        A = Folder("exampleinput.txt")
        A.construct_matrix()
        A.fold()
        A.count_dots()
        assert A.dots == 17

    def test_double_fold(self):
        A = Folder("exampleinput.txt")
        A.construct_matrix()
        A.fold()
        print(A.map)
        A.fold()
        A.count_dots()
        print(A.map)
        assert A.dots == 16

