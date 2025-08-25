
#EJERCICIO 1
# Your code goes here. Define a function called 'sign'

def sign(num = 1):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1

print(sign(1))


# EJERCICIO 2
def to_smash(total_candies):
    """Devuelve la cantidad de caramelos que deben ser aplastados 
    después de repartirlos equitativamente entre 3 amigos.
    
    >>> to_smash(91)
    1
    """
    print("Repartiendo", total_candies, "caramelo" if total_candies == 1 else "caramelos")
    return total_candies % 3

print(to_smash(91))


#EJERCICIO 3

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 6
have_hood = True
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)


#EJERCICIO 4'

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0

print(concise_is_negative(3))


#EJERCICIO 5a

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

# Check your answer
print (wants_all_toppings(True, True, True))


#EJERCICIO 5b

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion
    
print (wants_all_toppings(True, True, True))


#EJERCICIO 5C

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (not ketchup and mustard)

print (wants_all_toppings(True, True, True))



#EJERCICIO 6

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    sum = int(ketchup) + int(mustard) + int (onion)

    if sum == 1 :
        return True
    else :
        return False

print (exactly_one_topping(True, False, True))