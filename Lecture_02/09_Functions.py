
# from functions import fct_square
import functions

def square(x):
    return x  * x

for i in range(10):
    print( f"The square of {i} is {square(i)}")
    print( f"The square of {i} is {functions.fct_square(i)}")     