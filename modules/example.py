#random module example

import random 

#generating a random number between 1 to 10
number = random.randint(1,10)
print('I am Random number:', number)



#Example of picking random item from a list
fruits = ['apple', 'orange', 'mango']
choice = random.choice(fruits)
print('I am a Random Fruit Called:', choice)


#shuffle fruits 
random.shuffle(fruits)
print("Hey i am Shuffled List:", fruits)







