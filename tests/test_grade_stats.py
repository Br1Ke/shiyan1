"""grade_stats 的单元测试（使用标准库 unittest，无需额外依赖）。"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import grade_stats as gs


class TestGradeStats(unittest.TestCase):

    def test_average(self):
        self.assertEqual(gs.average([80, 90, 100]), 90)
        self.assertEqual(gs.average([]), 0.0)

    def test_highest_lowest(self):
        self.assertEqual(gs.highest([70, 95, 60]), 95)
        self.assertEqual(gs.lowest([70, 95, 60]), 60)

    def test_grade_of(self):
        self.assertEqual(gs.grade_of(95), "优")
        self.assertEqual(gs.grade_of(85), "良")
        self.assertEqual(gs.grade_of(75), "中")
        self.assertEqual(gs.grade_of(65), "及格")
        self.assertEqual(gs.grade_of(59), "不及格")

    def test_grade_distribution(self):
        dist = gs.grade_distribution([95, 85, 75, 65, 30, 92])
        self.assertEqual(dist["优"], 2)
        self.assertEqual(dist["良"], 1)
        self.assertEqual(dist["不及格"], 1)

    def test_parse_scores(self):
        self.assertEqual(gs.parse_scores("88, 92 ,75"), [88.0, 92.0, 75.0])
        self.assertEqual(gs.parse_scores(""), [])

    def test_pass_rate(self):
        self.assertAlmostEqual(gs.pass_rate([90, 80, 50, 30]), 0.5)
        self.assertEqual(gs.pass_rate([]), 0.0)
        self.assertEqual(gs.pass_rate([100, 100]), 1.0)
    def test_to_csv(self):
        self.assertEqual(gs.to_csv([90, 80]), "score\n90\n80")
    def test_summarize(self):
        s = gs.summarize([90, 80])
        self.assertEqual(s["count"], 2)
        self.assertEqual(s["average"], 85.0)
        self.assertEqual(s["highest"], 90)


if __name__ == "__main__":
    unittest.main(verbosity=2)
