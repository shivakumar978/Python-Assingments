# Reversing the key:value in a dict.
# There are 2 ways  to do it:

# 1. If we want to have unique values(no repeats of keys when reversed).
# This also can be done 2 ways:
# a. Use map function to reverse the items in the dict.
#    later convert this map into a dict.
# Eg:
my_dict = {'A':1, 'B':2, 'C':3, 'D':1}
my_reversed_dict = dict(map(reversed,  my_dict.items()))
print(my_reversed_dict)
# here we may lose 'A' or 'D' for the 1 once reversed.

# b. use dictionary comprehension:
my_reversed_dict = {value: key for key, value in my_dict.items()}
print(my_reversed_dict)
# here also we may lose 'A' or 'D' for the 1 once reversed.

#----------------------------------------------------------------------

# 2. If we want to have non-unique values:
# This also can be done 2 ways:
# a. Reverse the dict with defaultdict:
from collections import defaultdict
my_reversed_dict = defaultdict(list)
{my_reversed_dict[v].append(k) for k, v in my_dict.items()}
print(my_reversed_dict)

# b. Reverse the dict with a 'For' loop:
my_reversed_dict = dict()
for key, value in my_dict.items():
    my_reversed_dict.setdefault(value, list()).append(key)
print(my_reversed_dict)






