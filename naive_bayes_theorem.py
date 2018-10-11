"""
This formula simply computes the probability of a bilief (B)
given a set of evidence (E) posterior probability
Although simple, serves a proof of concept
"""
#Author Osman D Morales

#advise user of how to enter inputs
print("Values must be entered in range of 0 to 1\n")

#declare variables to enter evidence
e_b = input("Enter prior probability: \n") #prior probability
b = input("Enter general probability: \n") #overall probability
e = input("Enter probability of observed evidence: \n") #probability of evidence

#function to computer naive's formula
def naive(e_b, b, e):

	#compute variables of naive formula
	p_of_E_B= float(e_b)
	p_of_b= float(b)
	p_of_E= float(e)
	
	#compute the naives formula
	p_of_b_e = (p_of_E_B * p_of_b / p_of_E)

	#return results
	result = p_of_b_e * 100
	prnt = str(result)
	prnt = print("Your probability estimate is: " + prnt[0:2] + "%")

	return prnt

bayes = naive(e_b, b, e)
print(bayes)
