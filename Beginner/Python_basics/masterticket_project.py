TICKET_PRICE = 10
tickets_remaining = 100
service_charge = 2

def calculate_price(num_tickets):
	return num_tickets * TICKET_PRICE + service_charge


while tickets_remaining >=1 :
	print("There are {} tickets remaining.".format(tickets_remaining))
	name = input("What is your name?     ")
	number_of_tickets = input("Hey {}, how many tickets would you like?    ".format(name))
	try:
		number_of_tickets = int(number_of_tickets)
		if number_of_tickets > tickets_remaining:
			raise ValueError("There are only {} tickets left!".format(tickets_remaining))
	except ValueError as err:
		print("Sorry, we ran into an issue. {} Please try again!".format(err))
	else:
		total = calculate_price(number_of_tickets)	
		print("The price for the {} tickets is ${}".format(number_of_tickets, total))
		decision = input("Would you like to confirm the purchase? (Y/N)    " )
		
		if decision.lower() == "y":
			print("You have purchased {} tickets!".format(number_of_tickets))
			tickets_remaining = tickets_remaining - number_of_tickets
		else:
			print("Thank you for your interest {}!".format(name))
		
print("Sold out of tickets!")
	