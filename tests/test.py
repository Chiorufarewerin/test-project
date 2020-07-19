import test_project

from unittest import TestCase


class TestSimple(TestCase):
    def test_sum(self):
        s = test_project.sum(2, 2)
        self.assertEqual(s, 4)
