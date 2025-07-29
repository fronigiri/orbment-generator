import unittest
from skills import Skill


class TestSkill(unittest.TestCase):

    def test_skill_init(self):
        stone_hammer = Skill(name="Stone Hammer", earth=1, description="Drops a large boulder on enemies.")
        self.assertEqual(stone_hammer.name, "Stone Hammer")
        self.assertEqual(stone_hammer.earth, 1)
        self.assertEqual(stone_hammer.description,"Drops a large boulder on enemies." )


if __name__ == "__main__":
    unittest.main()
