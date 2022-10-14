# 1.

lst = [1, 2, -3, -4, 5]
lst = list(filter(lambda x: x>=0, lst))
print(lst)

# 2. 
lst_numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = list(filter(lambda x: x%2 == 1, lst_numbs))
print("Original list: ", lst_numbs)
print("New list of odd numbers: ", lst2)

# 3. 
str1 = "My name is SHIKHA PANCHAl."

lst3 = list(filter(lambda x: True if x.lower() in "aeiou" else False, str1))
print("old: ", str1)
print("New: ", lst3)

#4. 
str2 = "My name is SHIKHA PANCHAl. Born in 01.07.2002"
lst4 = list(filter(lambda x: True if x in "0123456789" else False, str2))
print("old: ", str2)
print("New: ", lst4)

# 5.
lst5=[-10, 40, -5]
lst5_5 =  list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, lst5)))
print("old: ", lst5)
print("New: ", lst5_5)