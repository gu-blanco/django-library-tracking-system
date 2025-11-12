import random

# Create a list of 10 random numbers between 1 and 20.
rand_list = [random.randint(1, 20) for _ in range(10)]

# Filter Numbers Below 10 (List Comprehension)
list_comprehension_below_10 = [item for item in rand_list if item < 10]

# Filter Numbers Below 10 (Using filter)
def check_bellow_10(item):
    if item < 10:
        return True

list_comprehension_below_10_filter = filter(check_bellow_10, rand_list)


print(rand_list)
print(list_comprehension_below_10)
for item in list_comprehension_below_10_filter:
    print(item)
