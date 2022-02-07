from random import choices, sample, seed
from collections import Counter
from math import factorial as fact

seed(123)

# six spins of American double zero roulette wheel 
# American roulette wheel containes 18 red slots, 18 black slots, and 2 green
population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
print(Counter(choices(population=["red", "black", "green"], weights=[18, 18, 2], k=6)))
print(Counter(choices(population=population, k=6)))

# deal 20 cards without replacement 
# A deck is 16 ten cards and 36 low cards
# ten cards Ace, King, Queen, and Jack of club, diamond, heart, and spade
# numbered cards of ay suit is low card
# a deal is a random sample without replacement

deck = Counter(tens=16, lows=36)
deck = list(deck.elements())
deal = sample(population=deck, k=20)
print(Counter(deal))
# card counting
deal = sample(population=deck, k=52) # shuffling the deck
print(Counter(deal[:20])) # random deal
print(Counter(deal[20:])) # remainder of cards

# five or more heads from 7 spins of a biased coin
trial = lambda h,t: (choices(['H', 'T'], cum_weights=[h,t], k=7)).count('H') >= 5
print(trial(0.6, 1.0))
print(sum(trial(0.6,1.0) for _ in range(100000)) / 100000)

# Analytic approach
# number of different combinations of r items taken from the total of n items
def comb(n, r):
    return fact(n) // fact(r) // fact(n-r)

print(comb(10, 3))
print(comb(10, 2))

# probability of >= 5 heads out 7 spins
# probability of heads in a single spin on a weighted coin
ph = 0.6
# probability of 5 heads out 7 spins using bernoulli's formula
print(
    sum(
        (ph ** 5 * (1 - ph) ** 2 * comb(7, 5),
        ph ** 6 * (1 - ph) ** 1 * comb(7, 6),
        ph ** 7 * (1 - ph) ** 0 * comb(7, 7))
    )
)
