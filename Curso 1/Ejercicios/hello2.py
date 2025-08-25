
#EJERCICIO 1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14

    
    """
    return round(num, 2)

print(round_to_two_places(3.1416))


#EJERCICIO 2

print(round(1234,-1))


#EJERCICIO 3

def to_smash(total_candies,total_firends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % total_firends

print(to_smash(91))


