#EJERCICIO 1

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    
    return len([num for num in nums if (num % 7) == 0]) > 0

# Check your answer
print(has_lucky_number([1,3,6,7]))


#EJERCICIO 2
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
 
   [False, False, True, True]

    
    """
    i = 0
    lista = []
    while i < len(L):
        lista.append(L[i] > thresh)
        i += 1
    return lista
    
print (elementwise_greater_than([1,2,3,4],3))


#EJERCICIO 3
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    pass

    for i in range(len(meals) - 1):  # -1 para no pasarnos del final
        if meals[i] == meals[i + 1]:
            return True
    return False

print (menu_is_boring(['pizza', 'sopa', 'sopa', 'ensalada', 'pasta']))


#EJERCICIO 4
"""def estimate_average_slot_payout(n_runs):
    Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    

    total_ganancia = 0

    for t in range(n_runs):
       resultado = play_slot_machine()
        ganancia_neta = resultado - 1  
        total_ganancia += ganancia_neta

    return total_ganancia / n_runs
    
    pass"""