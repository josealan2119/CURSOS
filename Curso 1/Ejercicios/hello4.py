#EJERCICIO 1

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) > 1:
        return L[1]
    else:
        return None
    
#EJERCICIO 2

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """

    players = teams[-1]
    return players[1]


#EJERCICO 3

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """

    racers[0] , racers[-1] = racers[-1] , racers[0]
    pass


#EJERCICIO 4

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]


#EJERCICIO 5

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """

    if  len(arrivals)%2 == 0 :
         mitad = len(arrivals) // 2
    else:
        mitad = len(arrivals) // 2 + 1

    lugar = arrivals.index(name)

    return  lugar >= mitad and arrivals[lugar] != arrivals[-1]
        
