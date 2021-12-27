import test
from functionality import Trajectory, find_max_solutions


class TestExample(object):
    def test_number_solutions(self):
        xlim = (20, 30)
        ylim = (-10, -5)

        solutions = find_max_solutions(xlim, ylim, (6, 9))

        for sol in solutions:
            print(sol)
        max_solutions = len(solutions)
        assert max_solutions == 112


class TestTrajectory(object):
    def test_success(self):
        xlim = (20, 30)
        ylim = (-10, -5)
        solution = (6, 9)

        Traj = Trajectory(*solution, xlim, ylim)

        assert Traj.hit == True
        assert Traj.t_solution == 20

    def test_success_2(self):
        xlim = (269, 292)
        ylim = (-68, -44)
        solution = (23, 67)

        Traj = Trajectory(*solution, xlim, ylim)

        assert Traj.hit == True
        assert Traj.t_solution == 136

    def test_success_3(self):
        xlim = (20, 30)
        ylim = (-10, -5)
        solution = (61, 9)

        Traj = Trajectory(*solution, xlim, ylim)

        assert Traj.hit == False
        assert Traj.t_solution == 20

    def test_success_4(self):
        xlim = (20, 30)
        ylim = (-10, -5)
        solution = (29, -7)

        Traj = Trajectory(*solution, xlim, ylim)

        assert Traj.hit == True

    def test_success_5(self):
        xlim = (20, 30)
        ylim = (-10, -5)
        solution = (23, -10)

        Traj = Trajectory(*solution, xlim, ylim)

        assert Traj.hit == True

