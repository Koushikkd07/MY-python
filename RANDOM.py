import random                 # import is used to import a module to use functions inside that module

#print(random.choice(["heads","tails"]))


'''
# from is used to call a specific function from a module and when you call the specific function you dont need to write it as (scope."function name"())
# you just need to call the function by its name like in the code i have only called choice() not random.choice() as i have called it already 

'''


#from random import choice                   
#print(choice(["heads","tails"]))

"""
(1) random(): Returns a random floating point number in the range [0.0, 1.0).
    
(2) uniform(a, b): Returns a random floating point number in the range [a, b].

(3) randint(a, b): Returns a random integer in the range [a, b].

(4) choice(seq): Returns a random element from the non-empty sequence seq.

(5) sample(population, k): Returns a list of unique elements chosen from the population sequence.

(6) shuffle(x[, random]): Shuffles the elements in list x in place.

(7) getrandbits(k): Returns a non-negative int with k random bits.

(8)seed([x]): Sets the seed for the random number generator.

(9)randrange([start], stop[, step]): Returns a randomly selected element from range(start, stop, step).

(10)gauss(mu, sigma): Returns a Gaussian distribution with mean mu and standard deviation sigma.

(11)expovariate(lambd): Returns a random floating point number in an exponential distribution with rate parameter lambd.

(12)vonmisesvariate(mu, kappa): Returns a random floating point number in a von Mises distribution with mean mu and dispersion kappa.

(13)triangular(low, high, mode): Returns a random floating point number in a triangular distribution with mode between low and high.

(14)betavariate(alpha, beta): Returns a random floating point number in a beta distribution with parameters alpha and beta.

(15)paretovariate(alpha): Returns a random floating point number in a Pareto distribution with parameter alpha.

(16)weibullvariate(alpha, beta): Returns a random floating point number in a Weibull distribution with parameters alpha and beta.

    """
    
    

'''
    random.randint(starting point,  ending point)
    random.randint(1, 10) \\  (1,10)----> range, this means it will generate number between 1 to 10

'''
"""
number=random.randint(1,10)
print (number)
"""
'''
                                            \\\ SHUFFLE THE DECK OF CARDS\\\
'''         
'''
cards=["jack","king","queen"]     # initialize a deck of cards 
random.shuffle(cards)             # shuffling the cards in this line
for card in cards:
    print(card)                   # printing the shuffled deck of cards 
'''
