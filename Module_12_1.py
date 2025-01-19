import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run1 = runner.Runner('Bob')
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    def test_run(self):
        run1 = runner.Runner('Jane')
        for i in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    def test_challenge(self):
        run1 = runner.Runner('Bob')
        run2 = runner.Runner('Jane')
        for i in range(10):
            run1.walk()
            run2.run()

        self.assertNotEqual(run1.distance, run2.distance)

if __name__ == '__main__':
    unittest.main()