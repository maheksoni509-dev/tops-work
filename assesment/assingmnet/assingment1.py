
#  9 Write a Python program to find the second smallest number in a list.

numbers = [10, 20, 4, 45, 99]
numbers.sort()
print(numbers[1])

# 10 Write a Python program to get unique values from a list.


lst1 = [1, 2, 3, 45, 6, 7, 2, 34, 5]
lst2 = []

for i in lst1:
    if i not in lst2:
        lst2.append(i)

print("Unique values list:", lst2)

 # 6 Write a Python program to find the first appearance of the substring 'not' and
 #poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
 # substring with 'good'. Return the resulting string
# Input string
s = input("Enter a string: ")

not_pos = s.find("not")
poor_pos = s.find("poor")

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    s = s.replace(s[not_pos:poor_pos+4], "good")

print("Result:", s)


#8 sublist
lst=[1,2,3]
lst2=[1,2,3,4,[3,4]]
for i in lst:
    if(type(i)==list):
     print("list contain sublist")
     break
    else:
       print("not contaiin sublist")






#11 unzip
lstnames=["netra","mahek","rahul"]
lstmarks=[23,56,78]
ans=zip(lstnames,lstmarks)
print(list(ans))

lst_com=[("ahmedabad","ranip"),("mumbai","juhu"),("koolkata","bridge")]
lstcity,lstplace=zip(*lst_com)
print(lstcity)
print(lstplace)

# 12 write a python program to convert a list of tupples into individual list

data = [(1,2), (3,4), (5,6)]

list1 = []
list2 = []

for i, j in data:
    list1.append(i)
    list2.append(j)
print( list1)
print( list2)




# 13 to sort a dictonary asec/dec acc to value

data = {"a":30, "b":10, "c":20, "d":40}

asc = dict(sorted(data.items(), key=lambda i: i[1]))

desc = dict(sorted(data.items(), key=lambda i: i[1]))

print("Ascending:", asc)
print("Descending:", desc)


#14 write a pythob program to  fing highest 3 values in a dictonary

data = {"a":50, "b":20, "c":80, "d":40, "e":70}

values = sorted(data.values())

print("Highest 3 values are:", values[:3])

# 16 counting frequences in a list in python
lst = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)


# 18   fact using recursion 
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
# 19  func takes list and returns new list with unique element
def unique_list(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

print(unique_list([1, 2, 2, 3, 4, 4]))

