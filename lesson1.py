#Write a Python function that takes two arguments (a and b) and returns their sum.
def two_values(a,b):
    c=a+b
    return c
print(two_values(5,4))
#Write a Python function that takes a string as input and returns the string reversed.
def word(name):
    name=name[::-1]
    return name
print(word("miriam"))

#Write a Python function that takes a list of integers as input and returns the
# sum of all the integers in the list.
def values(numbers):
    sum=0
    for i in numbers:
            sum=sum +1
    
    return sum
print(values([1,4,6,8,12]))

#Write a Python function that takes a list of integers as input and
# returns a new list with all the even numbers removed.
def people(name):
    empty=[]
    for i in name:
        if i%2!=0:
            empty.append(i)
    return empty
print(people([1,3,4,6,7,8,9,14,12]))


#Write a Python function that takes a list of integers as input and 
#returns the highest value in the list.
def value_list(values):
    highest_value=max(values)
    return highest_value
print(value_list([50,33,45,8]))
#Write a Python function that takes a list of strings as input and 
#returns a new list with all the strings capitalized.
def peoples_name(name):
    capitalized=name.upper()
    return capitalized
print(peoples_name("python"))