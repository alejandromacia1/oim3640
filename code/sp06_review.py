
#Variables and parameters are local. 

#print vs return: if function doesn't explicitly return any values, it will return none. 
#r/learnpython, community in reddit for beginners. 

#for loop i in range(n): 
#for i in range(4):
    #print ('Hi')

#for i in range(5):
    #print("Iteration:", i)

#for i in range(5):
    #print("Iteration:", i)
    #print("Square:", i*i)
    #print()

#for i in range(4,1,-1): #start, stop, step.
    #print("Iteration:", i)
    #print("Square:", i*i)
    #print()

#for i in range(1,6,2):
    #print(i)

#name = 'Python'
#print(name*3)
#rint(name + '3') #when concatenating, both need to be strings. 

#def double(x):
    #return x*2

#print(double(5))
#print(double('Hi '))
#print(double('5'))

#if we want to use escape, we can use /
#print('He said, \'Hello!\'')

#a = 5 #in programming, single = means assignment.
#b = a
#a = 10
#print(b)
#print(a)
#pythontutor, start visualizing: good resource. 

#immutable type vs mutable type: 
    #immutable types: int, float, string. Cannot be changed. 
    #mutable types: list, dict, set. Can be changed. 

#a = 5 
#b = a
#a = 10
#print(b)
#print(a)

#a = [1,2,3] #list is mutable. square brackets means list. 
#b = a
#a.append(4) #you will be adding 4 to the original list.
#print(b) #b will also show the updated list because both a and b point to the same list. 
#print(a)

#x = 10

#def foo():
    #message = "Hello"
    #x = 5
    #return x 

#print(foo())
#print(x)

# Draw a Triangle:

#Draw a square:
"""
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
"""

#def draw_square(n):
    #for i in range(n):
        #print('🧱'*n)

#draw_square(4)

#print('Hi ', end="")
#print('Hello')

#create a function to draw a triangle:
"""
🧱          1 = 0 + 1
🧱🧱        2 = 1 + 1 
🧱🧱🧱      3 = 2 + 1
🧱🧱🧱🧱    4 = 3 + 1 
"""

#for i in range(4):
    #print(i)

#def draw_triangle(n):
    #for i in range(n):
        #print('🧱'*(i+1))

#draw_triangle(6)

#in programming we always start counting from 0. 

#Draw a triangle like this (size = 5)

    #    4 spaces + 1 #
   ##    3 spaces + 2 #
  ###    2 spaces + 3 #
 ####    1 space + 4 #
#####    0 spaces + 5 #

#def draw_triangle(n):
    #for i in range(n):
        #print(' '*(n-i-1) + '#'*(i+1))

#draw_triangle(5)

#draw a pyramid
    #         4 spaces + 1 #
   ###        3 spaces + 3 #
  #####       2 spaces + 5 # 
 #######      1 spaces + 7 #

def draw_pyramid(n):
    for i in range(n):
        print(' '*(n-i-1) + '#'*(i*2+1))

draw_pyramid(4)



