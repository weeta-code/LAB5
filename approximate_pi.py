# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497
import math

def approximate_pi():
    num = int(input('Enter a positive integer: '))
    sum = 0
    i = 0

    while i <= num:
        sum += 1 / (i ** 2)
        i += 1
    
    pi = math.sqrt(6 * sum)

    return print(f'sum = {sum}\napproximate value of pi is: {pi}')