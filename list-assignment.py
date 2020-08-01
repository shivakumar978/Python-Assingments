books = ["Biology", "Maths", "Physics", "chemistry"] #list
print(books)

#list modification can be done as follows:
# 1. Add an item to our list..we can use append method.
books.append("History")
print(books)

# 2. To add item at a specific location to our list ..we can use insert method.
books.insert(1, "Geography")
print(books)

# 3. To add values or new list to our existing list by using Insert method.
magazines = ["Forbes", "Frontline", "Reader's Digest"]
books.insert(0, magazines)
print(books)

# 4. we can add the items of a new list to our old list by extend method.
books.extend(magazines)
print(books)

# 5. To sort the list we can use sort method
numbers = [8, 5, 2, 9, 7, 4]
books = ["Biology", "Maths", "Physics", "Chemistry"]
         
numbers.sort() # sorts the numbers in Ascending order 
books.sort() # sorts in alphabetical order. It is case sensitive
         
print(books)
print(numbers)

#6. split method can be used to convert the string in to list.
user_information = ("Shiva 25")
user_information = ("Shiva 25").split()
print(user_information)

#----------------------------------------------------------------

# difference between append and extended methods
# 1. In Append method we can add an item to list at the end of the list
# 2. we can add the items of a new list to our old list by extend method.
books.append("English")
print(books)

cartoon_books = ["Batman", "Spiderman"]
books.extend(cartoon_books)
print(books)

# -----------------------------------------------------


# difference between remove and pop methods
# To remove items from the list we can use remove method
books.remove("History")
print(books)

# we can also use pop method to remove values/ items at the end of list
books.pop()
print(books)
# we can get the value of the popped item
popped = books.pop()
print(popped)
print(books)
