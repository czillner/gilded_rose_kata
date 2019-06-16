# -*- coding: utf-8 -*-


def is_epic(item):
    return "Sulfuras, Hand of Ragnaros" in item.name


def is_increasable(item):
    return item.quality < 50


def is_ticket(item):
    return item.name in "Backstage passes to a TAFKAL80ETC concert"


def is_brie(item):
    return item.name == "Aged Brie"


def descrease_quality(item, delta=-1):
    return increase_quality(item, delta=delta)


def increase_quality(item, delta=1):
    item.quality += delta
    

def is_decreaseable(item):
    return item.quality > 0


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if is_epic(item):
                continue

            if is_brie(item) or is_ticket(item):
                if is_increasable(item):
                    increase_quality(item)
                if is_ticket(item):
                    if item.sell_in < 11 and is_increasable(item):
                        increase_quality(item)
                    if item.sell_in < 6 and is_increasable(item):
                        increase_quality(item)
            else:
                if is_decreaseable(item):
                    descrease_quality(item)
                    if "conjured" in item.name and is_decreaseable(item):
                        descrease_quality(item)


            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not is_brie(item):
                    if is_ticket(item):
                        item.quality = 0
                    elif is_decreaseable(item):
                        descrease_quality(item)
                elif is_increasable(item):
                    increase_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
