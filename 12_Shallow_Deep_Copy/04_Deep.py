# A deep copy creates a completely independent copy of the original object, including all nested objects.
# So the deep copy overcomes with the problem  of the shallow copy

# It creates the full copy i.e deep we say it copies all the things like nested things also
import copy

a = [10, 20, 30, 40, [100, 200, 300, 400], 50]

b = copy.deepcopy(a)

print(id(a))
print(id(b))

b[4][3] = 999
print(b)
print(a)  # So in the Deep copy the original copy does not get effect
