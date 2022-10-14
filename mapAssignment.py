import math
from collections import OrderedDict
from operator import add 
# 1. tripling all the number in a list
number = (1, 2, 3, 4, 5)
print("The list is - ", number)
result = map(lambda x: x + x + x, number) 
print("\ntripling all the number in a list: ")
print(list(result))

#3. convertinng all string to lowercase from a tuple
def tup(s):
    return s.lower()

tuple_ = ('SHIKHA','PANCHAL')

new_tup = map(tup, tuple_)
print("Old tuple: ", tuple_)
print("New Tuple: ", tuple(new_tup))

# 4. square root of number in a given list
def square(s):
    return math.sqrt(s)

list_= [4, 16]

new_list = list(map(square, list_))
print("Original list: ", list_)
print("New list: ", new_list)


# 6. table of any number

def table(s):
     for i in range(1, 11):
        print(s*i)

set_numb = {2}

output = map(table, set_numb)
print(set(output))

# 7. adding two lists
list1 = [4, 8, 12, 16, 20, 24]  
list2 = [2, 4, 6, 8, 10, 12]  

res_lt = list( map (add, list1, list2))

print("The original two lists are: ", list1, '\n', list2)
print("Adding the two lists: ", res_lt)


# 8. converting floats to int
a = [2.3, 3.9, 37.2]
print(list(map(int, a)))

# 9. reversing a set

sets_ =  {1, 2, 3, 4, 5, 6} 
def reverse_(x):
    print(sorted(x, reverse = True))

print("Old set: ", sets_)
print("Reversed set: ", map(reverse_, sets_))

#10. adding '@gmail.com to all the values of the dictionary

mail_dict ={'a': 'shikha', 'b': 'suraj'}
new_mail_dict = dict(map(lambda x: (x[0], x[1] + '@gmail.com'), mail_dict.items() ))
print("Old modified dictionary is: ", mail_dict)

print('The modified dictionary is : ', new_mail_dict)




