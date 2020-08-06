#! /usr/bin/env python3

import unittest
from truck import Truck

verbose_tests = False


class TruckTests(unittest.TestCase):
    def setUp(self):
        self.obj = Truck()

    def test_object(self):
        self.assertIsInstance(self.obj, Truck)
        if verbose_tests: print("TEST:ran test_object")

    def test_count(self):
        self.assertGreater(self.obj.count(), 0)
        if verbose_tests: print("TEST:ran test_count")

    def test_range(self):
        self.assertIsInstance(self.obj.range(), tuple)
        if verbose_tests: print("TEST:ran test_range")

    def test_locate(self):
        self.assertIsInstance(self.obj.locate(36.8, -89.5), dict)
        if verbose_tests: print("TEST:ran test_locate")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

