my_set = {2,4,5}
my_set.add(42)
my_set.remove(2)

#tries to remove, if not possible, does nothing
my_set.discard(0)

# .update({3,5}, {9,7}) adds to the current set

#    | or .union(*others) - all of the items from all of the sets
#    & or .intersection(*others) - all of the common items between all of the sets
#    - or .difference(*others) - all of the items in the first set that are not in the other sets
#    ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets
