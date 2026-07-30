# Mathematical Operations and Build in Functios
 

sets_0 = {10,20,40,7,9,100}

print(f"Maximum Number from the Set : {max(sets_0)}")
print(f"Minimum Number from the Set : {min(sets_0)}")
print(f"Lenght of the Set : {len(sets_0)}")
print(f"Sum of the Set Elements : {sum(sets_0)}")
print(f"Sorted List : {sorted(sets_0)}")
print(all(sets_0))
print(any(sets_0))


#Mathematical Operations

sets_011 = {10,20,30,40,50}
sets_012 = {100,30,10,60}

print(f"\n\nUnion of two Sets : {sets_011.union(sets_012)}")
print(f"Intersection Of two Sets : {sets_011.intersection(sets_012)}")
print(f"difference between two Sets : {sets_011.difference(sets_012)}") 
print(f"Symmetric Difference : {sets_011.symmetric_difference(sets_012)}")