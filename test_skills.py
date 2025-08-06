import unittest
from skills import Skill, get_skills, skill_list, print_skill_list
from quartz import *
from characters import characters


class TestSkill(unittest.TestCase):

    def test_skill_init(self):
        stone_hammer = Skill(name="Stone Hammer", earth=1, description="Drops a large boulder on enemies.")
        self.assertEqual(stone_hammer.name, "Stone Hammer")
        self.assertEqual(stone_hammer.earth, 1)
        self.assertEqual(stone_hammer.description,"Drops a large boulder on enemies." )

    def test_skill_eq(self):
        skill_1 = Skill(name="Stone Hammer", earth=1, description="Drops a large boulder on enemies.")
        skill_2 = Skill(name="Stone Hammer", earth=1, description="Drops a large boulder on enemies.")
        skill_3 = Skill(name="Earth Wall", earth=4, description="Forms a temporary earth shield perimeter. [Immunity]")
        self.assertEqual(skill_1, skill_2)
        self.assertEqual(skill_1, skill_2)
        self.assertNotEqual(skill_3, skill_1)

    def test_get_skills(self):
        test_char = characters["olivier"]
        line = [(ep_1, cast_1, attack_1, action_1, hp_2, sleep)]
        test_char.lines = line
        list = get_skills(test_char, skill_list)
        print_skill_list(list)
        





if __name__ == "__main__":
    unittest.main()
