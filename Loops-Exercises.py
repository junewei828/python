'''
LOOPS EXERCISES
'''
'''
Problem 1
Given a list (my_words) that has words as its elements, write a loop that will print out
only the words that are 5 or more letters long. For example your code will not print the word 'ok' but it
will print the word 'Python'.
Decide which type of loop is more suitable for this task. ('for' loop or 'while' loop)
'''

print '\n'
print "***** Starting Problem 1 ********"

my_words = ['Python', 'ok', 'selenium', 'integer', 'java', 'loop', 'webdriver', 'yes', 'Interactive']

# Your code goes here
for i in my_words:
    if len(i) > 5:
        print(i)
    else:
        continue


'''
Problem 2
Take the same list in problem 1, instead of printing the words that meet the criteria, add them to a new list called 'my_new_words'
and print the list.
'''

print '\n'
print "***** Starting Problem 2 ********"

my_words = ['Python', 'ok', 'selenium', 'integer', 'java', 'loop', 'webdriver', 'yes', 'Interactive']

# Your code goes here
new_list = []
for i in my_words:
    if len(i) > 5:
        new_list.append(i)
    else:
        continue
print(new_list)


'''
Problem 3
Using a while loop print the string "abc" 10 times. Also print the count right after the string on the next line. Do not use a 'for' loop.
Hint: use a counter variable
'''

print '\n'
print "***** Starting Problem 3 ********"

# Your code goes here
count = 0
while count < 10:
    print("abc")
    count += 1
    print("the count is {}").format(count)
    



'''
Problem 4
Given the dictionary 'population', which is city and population pair, iterate the the dictionary and print only the cities
with population more than 1.5 million. (the population is given in millions.
'''

print '\n'
print "***** Starting Problem 4 ********"

population = {'New York': 8.5, 'San Jose': .9, 'Phoenix': 1.6, 'Houston': 2.2, 'Chicago': 2.7, 'San Antonio': 1.3}

# Your code goes here
for i in population:
    if population[i] > 1.5:
        print(i +": " + str(population[i]))
    else:
        continue

'''
Problem 5
Given list of cities 'cities', iterate through the list and print the cities that population information is available in
the dictionary 'population'.
Example: Oakland will not be printed but Phoenix will be printed
'''

print '\n'
print "***** Starting Problem 5 ********"

cities = ['Oakland', 'Phoenix', 'Houston', 'New Mexico', 'Chicago', 'Boston', 'Los Angeles', 'San Jose']
population = {'New York': 8.5, 'San Jose': .9, 'Phoenix': 1.6, 'Houston': 2.2, 'Chicago': 2.7, 'San Antonio': 1.3}

# Your code goes here
for city in cities:
    if population.has_key(city):
        print(city+": " + str(population[city]))
    else:
        continue


'''
Problem 6
Given list of cities 'cities', and dictionary population, iterate though the list and print the city and population as
 shown in the example. If the population information is not available print "Population information not available for : <the city name>
 Example:
 >>> Chicago --> 2.7
 >>> Population information not available for : Oakland

'''

print '\n'
print "***** Starting Problem 6 ********"

cities = ['Oakland', 'Phoenix', 'Houston', 'New Mexico', 'Chicago', 'Boston', 'Los Angeles', 'San Jose']
population = {'New York': 8.5, 'San Jose': .9, 'Phoenix': 1.6, 'Houston': 2.2, 'Chicago': 2.7, 'San Antonio': 1.3}

# Your code goes here
for city in cities:
    if population.has_key(city):
        print(city + " --> " + str(population[city]))
    else:
        print("Population information not available for : " + city)

'''
Problem 7
Its snack time and we want to decide 3 fruits to eat from the available food in the kitchen.
All available foods in the kitchen are in the list 'available_foods', and foods considered fruits are in the list 'fruits'.
Iterate through the available foods list and print only 3 fruits for snack.
Hint: Stop printing as soon as you find 3 foods considered fruit.
'''

print '\n'
print "***** Starting Problem 7 ********"

available_foods = ['cheese', 'banana', 'orange', 'chicken', 'beef', 'apple', 'burrito', 'pizza', 'mango', 'pineapple', 'papaya', 'ham']
fruits = ['orange', 'mango', 'papaya', 'pineapple', 'banana', 'apple', 'peach', 'grape', 'avocado', 'pear']

# Your code goes here
count = 0
for food in available_foods:
    if food in fruits:
        print(food)
        count += 1

    if count == 3:
        break
      

'''
Problem 8
Given the list 'collection' print every single word in the list. The list contains another list that contains words. Print all
of the words.
'''

print '\n'
print "***** Starting Problem 8 ********"

collection = ['python', 'qa', 'selenium', ['java', 'ruby', 'pearl', 'c++'], 'dell', 'toshiba' ]

# Your code goes here
for i in collection:
    if type(i) == list:
        for j in i:
            print(j)

    else:
        print(i)
