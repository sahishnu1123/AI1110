import random

#change k here for checking probability of k successes
k = 510

toss = ['H','T']
positive_results = 0

for i in range(1,10000):
    heads = 0
    tails = 0
    for j in range(1,1000):
        value = random.choices(toss)
        if(value == ['H']):
            heads = heads + 1
        else:
            tails = tails + 1
    if (heads == k):
        positive_results = positive_results + 1

result = positive_results/10000

print("The probability that the coin shows heads", end =" ")
print(k, end = " ")
print("times is", end = " ")
print(result)
