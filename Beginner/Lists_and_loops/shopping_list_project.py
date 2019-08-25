shopping_list = []

def add_to_list(item):
	shopping_list.append(item)
	print("Item '{}' added to the list! You have {} items total in the list.".format(item, len(shopping_list)))
	

def show_help():
	print("What should we pick up at the store?")
	print("""
Enter 'SHOW' to see the list.
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")
	
	
def show_list():
	print("Shopping list: ")
	for item in shopping_list:
		print("* " + item)
	print()
	
	
show_help()
while True:
	new_item = input("> ")
	
	if new_item == "DONE":
		show_list()
		break
	elif new_item == "HELP":
		show_help()
		continue
	elif new_item == "SHOW":
		show_list()
		continue
	
	
	add_to_list(new_item)
	