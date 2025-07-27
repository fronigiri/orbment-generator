import unittest
from quartz import Quartz


class TestQuartz(unittest.TestCase):
    def test_quartz(self):
        cloak = Quartz("Cloak", mirage=3, fire=2)
        self.assertEqual(cloak.mirage, 3)
        self.assertEqual(cloak.fire, 2)
        self.assertEqual(cloak.name, "Cloak")
    
    def test_get_sepeth(self):
        ep_3 = Quartz("EP 3", time=2, space=2, mirage=5)
        value = ep_3.get_sepeth("time")
        value_2 = ep_3.get_sepeth("space")
        value_3 = ep_3.get_sepeth("mirage")
        self.assertEqual(value, 2)
        self.assertEqual(value_2, 2)
        self.assertEqual(value_3, 5)


        


if __name__ == "__main__":
    unittest.main()