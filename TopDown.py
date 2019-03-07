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
    
    # def knapv(w):
    #     subprobs = [(knapv(w-item.weight) + item.value)
    #         for item in items if item.weight <= w]
    #     return reduce(max, subprobs, 0)
    #
    # return knapv(capacity)

    result = 0


    if len(items) == 0:
        result = 0

    elif capacity == 0:
        result = 0

    elif items[0][0] > capacity:
        items.pop()
        result = knapval_rep(capacity, items)

    else:

        print("Went through")

        tempValue = items[len(items) - 1][1]
        tempWeight = items[len(items) - 1][0]
        items.pop()

        temp1 = knapval_rep(capacity, items)

        temp2 = tempValue + knapval_rep(capacity - tempWeight, items)
        result = max(temp1, temp2)

    return result
    
def knapval_norep_rec(capacity, items):
    """
    
    return the maximum value achievable in 'capacity' weight
    using 'items' when repeated items are allowed
    
    """
    #     # choose to use item.weight and get item.value + optimal from what's left
    # options = list(
    #     item.value + knapval_norep(capacity-item.weight, lits(i for i in items if i is not item))
    #     for item in items if item.weight <= capacity)
    # if len(options):
    #     return max(options)
    # else:
    #     return 0
    
def knapval_norep(W, wt):
    """
    
    return the maximum value achievable in 'capacity' weight
    using 'items' when repeated items are allowed
    
    """
        # choose to use item.weight and get item.value + optimal from what's left
    # last_item = items[-1]
    # other_items = items[:-1]
    # options = list(
    #     knpaval_norep(capacity, other_items))
    # if last_item.weight <= capacity:
    #     options.append(last_item.value +
    #         knapval_norep(capacity-last_item.weight, other_items),
    #         )
    #

    """Find max weight that can fit in knapsack size W."""
    # Create n nested arrays of 0 * (W + 1)
    max_vals = [[0] * (W + 1) for x in range(len(wt))]
    # Set max_vals[0] to wt[0] if wt[0] <= j
    max_vals[0] = [wt[0] if wt[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(wt)):
        for j in range(1, W + 1):
            value = max_vals[i - 1][j]  # previous i @ same j
            if wt[i] <= j:
                val = (max_vals[i - 1][j - wt[i]]) + wt[i]
                if value < val:
                    value = val
                    max_vals[i][j] = value
                else:
                    max_vals[i][j] = value  # set to [i - 1][j]
            else:
                max_vals[i][j] = value  # set to [i - 1][j]

    return max_vals[-1][-1]



# loot item for knapsack

Item = namedtuple('Item', ['weight', 'value'])

def test_knapval_rep():
    loot = [Item(6, 30),
            Item(3, 14),
            Item(4, 16),
            Item(2, 9),]

    assert loot[0][0] == 6
    assert loot[0][1] == 30

    assert loot[1][0] == 3
    assert loot[1][1] == 14

    assert loot[3][0] == 2
    assert loot[3][1] == 9

    loot.pop()

    assert loot[0][0] == 6
    assert loot[0][1] == 30



    assert knapval_rep(10, loot) == 48

def test_knapval_norep():

    loot = [Item(6, 30),
            Item(3, 14),
            Item(4, 16),
            Item(2, 9),]

    # assert knapval_norep(10, loot) == 46

def test_edit_distance():

    pass
    # assert edit_distance("exponential", "polynomial") == 6
