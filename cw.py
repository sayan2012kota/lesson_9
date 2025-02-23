#sets

list = ["sayan" , "sayan" , "nishtha" , "sam"]
for name in list:
    print(name)
print(list)


#set --> unique values
set = ("sayan" , "sayan" , "nishtha" , "sam")
#unordered and it is mutable
print(set)


#modify

#adding the element to the set
set.add("dhwani")
print(set)

#remove -->
set.remove("nishtha")
print(set)

#iterating through the set
for names in set:
    print(names)

#exercise:
#create a set --> with 5 names two repeated
#print --> entire
#print ---> every element one by one
#add ---> 2 more names into the set
#print

#check if element is there in the set or not
if "nishtha" in set :
    print("Nishtha is there in the set")
else :
    print("Nishtha is not there in the set")



set2 = ("sayan" , "sayan" , "nishtha" , "arjun" , "dhruv")
print(set2)
for names in set2:
    print(names)
set2.add("hanushaan")
set2.add("sulloch")
if "sayan" in set2 :
    print("Sayan is in the set")
else :
    print("Sayan is not in the set")



#operations of set -->

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5, 2, 1, 7}

#union
#--> 3, 6, 2, 5, 4, 1, 7
print[set1.union(set2)]


#intersection
print[set1.intersection(set2)]

#difference
print[set1.difference(set2)]

print[set2.difference(set1)]

#symmetric difference
print[set1.symmetric_differencce(set2)]