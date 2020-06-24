"""

Description of my function is:
if a man goes 3 steps forward then it went back 2 steps . So Calculate the number_of_steps to reach the specific
number of steps and the total distance traveled by the man.

Some Given points :
1 step = 1 feet

"""



def calculate_steps(n):
    if n <= 3:
        number_of_steps = 1
    else :
        number_of_steps = ((n-3)*5)+3
    return (number_of_steps,number_of_steps*1)
 
 
 
    
    
n = int(input())
a = calculate_steps(n)
steps = a[0]
total_distance_traveled = a[1]
print('Total Steps taken by a man to reach the steps :', steps)
print('Total number of distance traveled(in feet)by a man to reach that step is :',total_distance_traveled)
