#Strings (immutable = do not change value aur character in string)

'''word = "Satyam"
print(len(word))'''

#Concatenate

'''word1 = "I Love"
word2 = "Satyam"
sentence = word1 + " " + word2
print(sentence)'''

#Slicing

'''word = "I study from ApnaCollege"

print(word[13:25]) # print(word[13:])
print(word[-11:])'''

#Formatting

#format()

'''a = 5
b = 10
sum = a + b

#normal formatting
print("sum of {} & {} is {}".format(a, b, sum))
print("language is {}".format("python"))

#index based formatting
print("sum  of {1} & {0} is {2}".format(a, b, sum))

#value based formatting
print("values of vars {a} & {b}".format(a = 5, b = 10))'''

#F-strings

'''a = 5
b = 10

print(f"sum of {a} & {b} is {a + b}")'''

#Lists (mutable = chnage the value in lists)

'''marks = [99, 89, 100, 65, 92]
marks[2] = 70

print(marks)'''

#slicing

'''marks = [99, 89, 100, 65, 92, "abc", 100.99]

print(marks[0 : 5])
print(marks[: 5])
print(marks[5 : len(marks)])
print(marks[5 :])
print(marks[-4 : -1])'''

#List Methods

#I.append(val) = add one element at the end
'''nums = [1, 2, 3]
nums.append(4)

print(nums)

#I.insert(idx, val) = insert element at idx
nums.insert(2, 10)
print(nums)

#I.sort() = arranges in increasing order
nums.sort()
nums.sort(reverse=True)
print(nums)

#I.reverse() = reverse order
nums.reverse()
print(nums)'''

#lists (loop)

#linear search
'''nums = [1, 2, 3, 10, 4]
x = 10
idx = 0

for val in nums:
    if(val == x):
        print(f"{x} found at idx = {idx}")
        break
    idx += 1'''

#Tuples (immutable sequence of value)

'''tup = (1, 2, 3, 4, 5)

print(tup)
print(len(tup))
print(tup[2])

tup = ("abc",)

print(type(tup))
#slicing are same list and string'''

'''tup = (1, 2, 3, 4, 5)

sum = 0
for val in tup:
    sum += val

print(f"sum of vals is {sum}")'''

#Tuple Methods

'''#t.index(val) = return 1st occurence idx
tup = (1, 2, 2, 3, 2, 4)

print(tup.index(2))

#t.count = counts total occurence
print(tup.count(2))'''

#Dictionary

'''info = {
    "name": "satyam",
    "cgpa": 6.4,
    "subject": ["math", "science"],
    3.14: "PI"
}

print(type(info))
print(info["name"])
print(info[3.14])

info["cgpa"] = 9.6
print(info["cgpa"])

#Dictionary Methods

#d.keys() = return all keys
print(info.keys())
dict_keys = list(info.keys())
print(dict_keys)

#d..values() = returns all values
dict_vals = list(info.values())
print(dict_vals)

#d.items() = returns (key, val) pairs
print(info.items())

#d.get(val) = returns val acc. to key
print(info.get("cgpa2"))
print("End of code")

#d.update(new_item) = adds new item to dict
info.update({
    "city": "Gorakhpur"
})
print(info)'''

#Sets

'''s = {1, 2, 2, 2, 3}
print(s)
print(type(s))
print(len(s))
#add value in set
s.add(5)
print(s)
#empty set print
empty_set = set()
print(type(empty_set))'''

#Set Methods

'''
s.add(val) = adds a val
s.remove(val) = removes val
s.clear() = empties the set
s.pop() = removes a random val
s.union(set2) = returns new union
s.intersection(set2) = return new intersection
'''