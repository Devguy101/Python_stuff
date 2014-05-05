#Program made by Devendra Singh to solve quadratic equations and punch out answers to given x values
#Solves for roots, stationary point and gives an x for a y
import math

def discriminant(a, b, c):
    return (b**2) - (4*a*c)
    
def quadratic(a, b, root_d):#actual quadratic formula
    return (-b+root_d)/(2*a)

def max_min(a, b):#this gives the x value for the stationary point or critical point
    return -b/(2*a)

def solve(a, b, c, x):#this solves for a y given an x
    return a*x*x + b*x + c
    
a= int(input('Enter the coefficient of x^2 '))
b= int(input('Enter the coefficient of x '))
c= int(input('Enter constant '))
print()

if a>0:#determining if the equation is a max or min function
    nature=('minimum')
else:
    nature=('maximum')
    
d= discriminant(a, b, c)
#Using the discriminant to determine the type of roots of the equation

if d>0:
    e=math.sqrt(d)
    x= quadratic(a, b, e)
    print('The roots of the equation are')
    print(x)
    x=quadratic(a,b,-e)
    print (x)

elif d==0:
    x=max_min(a, b)
    print ('Equation has 2 real and equal roots at', x)
    
elif d<0:
    print ('This equation has no real roots ')
    
x= max_min(a, b)

y=solve(a, b, c, x)#solving the y value of the stationary point

print()
print('The coordinate of the', nature, 'point is ', x, ',', y)
print()

counter = 0
while counter==0:#recurring loop for function
    x=int(input('Enter x value to solve for '))
    y=solve(a, b, c, x)
    print ('Corresponding y value = ', y)
    print()
    if x is None:
        counter = 1
