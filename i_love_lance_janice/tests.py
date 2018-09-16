from solution import answer
import unittest


class SolutionTest(unittest.TestCase):

    def test_1(self):
        x = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
        e = "did you see last night's episode?"
        y = answer(x)
        self.assertEqual(e, y)

    def test_2(self):
        x = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
        e = "Yeah! I can't believe Lance lost his job at the colony!!"
        y = answer(x)
        self.assertEqual(e, y)
