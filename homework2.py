set_a = {1 , 2 , 3 , 4 , 5}
set_b = {4 , 5 , 6 , 7 , 8}

set_a.add("9")
set_b.remove("4")

if 3 in set_b:
    print(3 is in set b)
else:
    print(3 is not in set b)

set_c = set_a.union(set_b)
print(set_c)