balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 0
updatedBalance = balance
counter = 0

# Will loop through everything until we find a rate that will reduce updatedBalance to 0.
while updatedBalance > 0:
	# Was stated that payments needed to happen in increments of $10
	monthlyPayment += 10
	# To reset balance back to actual balance when loop inevitably fails.
	updatedBalance = balance
	month = 1
	
	# For 12 months and while balance is not 0...
	while month <= 12 and updatedBalance > 0:
		# Subtract the ($10*n) amount
		updatedBalance -= monthlyPayment
		# Compound the interest AFTER making monthly payment
		interest = monthlyInterestRate * updatedBalance
		updatedBalance += interest
		# Increase month counter
		month += 1
		counter += 1
		
print("Lowest Payment: ", monthlyPayment)
#print("Number of iterations: ", counter)