# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:38:18 2019

@author: spencer.stewart
"""

from functools import lru_cache, reduce
from collections import namedtuple

SubProb = namedtuple('SubProb', ['value', 'partial', 'args'])

Skip = object()
def drop_skipped(itr):
    return filter()

def knapval_rep(capacity, items):
    """
    
    return the maximum value achievable in 'capacity' weight
    using 'items' when repeated items are allowed
    
    """
    
    def knapv(w):
        subprobs = [(knapv(w-item.weight) + item.value)
            for item in items if item.weight <= w]
        return reduce(max, subprobs, 0)
    
    return knapv(capacity)
    
def knapval_norep_rec(capacity, items):
    """
    
    return the maximum value achievable in 'capacity' weight
    using 'items' when repeated items are allowed
    
    """
        # choose to use item.weight and get item.value + optimal from what's left
    options = list(
        item.value + knapval_norep(capacity-item.weight, lits(i for i in items if i is not item))
        for item in items if item.weight <= capacity)
    if len(options):
        return max(options)
    else:
        return 0
    
def knapval_norep(capacity, items):
    """
    
    return the maximum value achievable in 'capacity' weight
    using 'items' when repeated items are allowed
    
    """
        # choose to use item.weight and get item.value + optimal from what's left
    last_item = items[-1]
    other_items = items[:-1]
    options = list(
        knpaval_norep(capacity, other_items))
    if last_item.weight <= capacity:
        options.append(last_item.value +
            knapval_norep(capacity-last_item.weight, other_items),
            )

# loot item for knapsack
Item = namedtuple('Item', ['weight', 'value'])

def test_knapval_rep():
    loot = [
            Item(6, 30),
            Item(3, 14),
            Item(4, 16),
            Item(2, 9),
            ]
            
    assert knapval_rep(10, loot) == 48

def test_knapval_norep():
    loot = [
            Item(6, 30),
            Item(3, 14),
            Item(4, 16),
            Item(2, 9),
            ]
            
    assert knapval_rep(10, loot) == 48