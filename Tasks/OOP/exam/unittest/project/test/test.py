import unittest

from project.legendary_item import LegendaryItem


class TestLegendaryItem(unittest.TestCase):

    def setUp(self):
        self.item = LegendaryItem("Sword-123", 30, 50, 100)

    def test_constructor_valid(self):
        item = LegendaryItem("Sword-456", 40, 60, 200)
        self.assertEqual(item.identifier, "Sword-456")
        self.assertEqual(item.power, 40)
        self.assertEqual(item.durability, 60)
        self.assertEqual(item.price, 200)

    def test_identifier_property_valid(self):
        self.item.identifier = "Axe-789"
        self.assertEqual(self.item.identifier, "Axe-789")

    def test_identifier_property_invalid_chars(self):
        with self.assertRaises(ValueError):
            self.item.identifier = "Axe@789"

    def test_identifier_property_too_short(self):
        with self.assertRaises(ValueError):
            self.item.identifier = "Axe"

    def test_power_property_valid(self):
        self.item.power = 50
        self.assertEqual(self.item.power, 50)

    def test_power_property_invalid_negative(self):
        with self.assertRaises(ValueError):
            self.item.power = -10

    def test_durability_property_valid(self):
        self.item.durability = 80
        self.assertEqual(self.item.durability, 80)

    def test_durability_property_invalid_range(self):
        with self.assertRaises(ValueError):
            self.item.durability = 0

        with self.assertRaises(ValueError):
            self.item.durability = 101

    def test_price_property_valid(self):
        self.item.price = 150
        self.assertEqual(self.item.price, 150)

    def test_price_property_invalid_zero(self):
        with self.assertRaises(ValueError):
            self.item.price = 0

    def test_price_property_invalid_not_multiple_of_10(self):
        with self.assertRaises(ValueError):
            self.item.price = 55

    def test_is_precious_true(self):
        self.item.power = 60
        self.assertTrue(self.item.is_precious)

    def test_is_precious_false(self):
        self.item.power = 40
        self.assertFalse(self.item.is_precious)

    def test_enhance(self):
        initial_power = self.item.power
        initial_price = self.item.price
        initial_durability = self.item.durability

        self.item.enhance()
        self.assertEqual(self.item.power, initial_power * 2)
        self.assertEqual(self.item.price, initial_price + 10)
        self.assertEqual(self.item.durability, min(initial_durability + 10, 100))

    def test_evaluate_eligible(self):
        self.item.durability = 60
        self.item.power = 60
        result = self.item.evaluate(50)
        self.assertEqual(result, "Sword-123 is eligible.")

    def test_evaluate_not_eligible(self):
        self.item.durability = 40
        self.item.power = 30
        result = self.item.evaluate(50)
        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_not_eligible_durability(self):
        self.item.durability = 30
        self.item.power = 60
        result = self.item.evaluate(50)
        self.assertEqual(result, "Item not eligible.")

if __name__ == '__main__':
    unittest.main()