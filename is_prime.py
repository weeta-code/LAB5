# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497

def is_prime(n: int) -> bool:
    sqrt = int(n ** .5)
    i = 2
    if n < 2:
        return False

    while i <= sqrt:
        if n % i == 0:
            return False
        
        i += 1
    return True