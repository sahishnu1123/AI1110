import random

#absolute function
def abs(x):
	if (x > 0):
		return x
	else:
		return -x

toss = ['H', 'T']
odd_results = 0
even_results = 0

#change the probability of heads here if the coin is biased
p = 0.5

for i in range(1,1000000):

	value = random.choices(toss, weights = [p, 1-p])

	a = 0

	while value != ['H']:
		a = a+1
		value = random.choices(toss, weights = [p, 1-p])
		
	a = a+1
	
	if  (a%2 == 1):
		odd_results = odd_results + 1
	else:
		even_results = even_results + 1

#experimental probability through random variables
exp_probability = (odd_results)/(odd_results + even_results)

#calculated probability found using theory
calc_probability = 1/(2-p)

difference = abs(exp_probability - calc_probability)

print("Difference in theoritical probability and calculated probability is", end = " ")
print(difference)
print()

if(difference < 0.001):
	print("The probability approaches 1/(2-p)")
