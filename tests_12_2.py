import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result = 0
        cls.all_results = dict()

    def setUp(self):
        self.runner_1 = Runner('Усэйн', speed=10)
        self.runner_2 = Runner('Андрей', speed=9)
        self.runner_3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for i in list(TournamentTest.all_results.values()):
            print(i)

    def test_1(self):
        TournamentTest.result += 1

        tour = Tournament(90, self.runner_1, self.runner_3)
        r = tour.start()
        r_list1 = list(r.keys())
        r_list2 = [i.name for i in list(r.values())]
        r1 = dict(zip(r_list1, r_list2))
        self.all_results[f'resuit_{TournamentTest.result}'] = r1
        self.assertTrue(r[max(r.keys())] == r[max(r.keys())].name)

    def test_2(self):
        TournamentTest.result += 1

        tour = Tournament(90, self.runner_2, self.runner_3)
        r = tour.start()
        r_list1 = list(r.keys())
        r_list2 = [i.name for i in list(r.values())]
        r1 = dict(zip(r_list1, r_list2))
        self.all_results[f'resuit_{TournamentTest.result}'] = r1
        self.assertTrue(r[max(r.keys())] == r[max(r.keys())].name)

    def test_3(self):
        TournamentTest.result += 1

        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        r = tour.start()
        r_list1 = list(r.keys())
        r_list2 = [i.name for i in list(r.values())]
        r1 = dict(zip(r_list1, r_list2))
        self.all_results[f'resuit_{TournamentTest.result}'] = r1
        self.assertTrue(r[max(r.keys())] == r[max(r.keys())].name)


if __name__ == '__main__':
    unittest.main()
