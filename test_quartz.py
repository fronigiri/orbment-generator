import unittest
from quartz import Quartz, line_total


class TestQuartz(unittest.TestCase):
    def test_quartz(self):
        cloak = Quartz("Cloak", mirage=3, fire=2)
        self.assertEqual(cloak.mirage, 3)
        self.assertEqual(cloak.fire, 2)
        self.assertEqual(cloak.name, "Cloak")
    
    def test_get_sepith(self):
        ep_3 = Quartz("EP 3", time=2, space=2, mirage=5)
        value = ep_3.get_sepith("time")
        value_2 = ep_3.get_sepith("space")
        value_3 = ep_3.get_sepith("mirage")
        self.assertEqual(value, 2)
        self.assertEqual(value_2, 2)
        self.assertEqual(value_3, 5)
        
    def test_line_total(self):
        hp_1 = Quartz("HP 1", water=1)
        shield_3 = Quartz("Shield 3", wind=5)
        haze = Quartz("Haze", mirage=3, earth=2)
        ep_2 = Quartz("EP 2", mirage=3, time=2, space=2)
        ep_cut_1 = Quartz("EP Cut 1", space=2, time=1, mirage=1)
        action_1 = Quartz("Action 1", time=1)
        line = (hp_1, shield_3, haze, ep_2, ep_cut_1, action_1)
        total = line_total(line)
        self.assertEqual(total["water"], 1)
        self.assertEqual(total["mirage"], 7)
        self.assertEqual(total["time"], 4)


        


if __name__ == "__main__":
    unittest.main()