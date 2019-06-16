# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_len(self):
        items = [Item("magic", 0, 0), Item("soldier", 6, 6), Item("major_tom", 3, 3)]
        gilded_rose = GildedRose(items)
        self.assertEqual(len(items), len(gilded_rose.items))

    def test_sell_in_is_decrease_by_one_per_day(self):
        items = [Item("cloath", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].sell_in, 0)

    def test_quality_is_decrease_by_one_per_day(self):
        items = [Item("lizard", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 9)

    def test_if_quality_not_less_zero(self):
        items = [Item("shield", 3, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 0)
    
    def test_if_quality_not_more_fifty_for_brie(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50)

    def test_if_quality_not_more_fifty_for_passes(self):
        items = [Item("Backstage passes", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50)

    def test_quality_passes_increase_per_one_for_more_than_10_days(self):
        items = [Item("Backstage passes", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 11)
    
    def test_quality_passes_increase_per_two_for_more_than_5_days(self):
        items = [Item("Backstage passes", 6, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 8)

    def test_quality_passes_increase_per_three_for_less_than_5_days(self):
        items = [Item("Backstage passes", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 13)

    def test_quality_passes_fall_down_to_zero_after_concert(self):
        items = [Item("Backstage passes", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 0)

    def test_decreas_quality_per_two_after_seven_day(self):
        items = [Item("Green wheels", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 3)

    def test_sulfuras_quality_is_eighty_forever(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 80)

    def test_quality_of_conjured_is_decreased_by_2_per_day(self):
        items = [Item("conjured", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 18)
        
    def test_quality_of_ticket_does_not_go_higher_than_50(self):
        items = [Item("Backstage passes", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50)
    

if __name__ == '__main__':
    unittest.main()

