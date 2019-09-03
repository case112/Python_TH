import os

shopping_list = []

def clear_screen():
	os.system("clear")
	
def remove_from_list():
	show_list()
	what_to_remove = input("What would you like to remove? \n> ")
	try:
		shopping_list.remove(what_to_remove)
	except ValueError:
		pass
	show_list()

def add_to_list(item):
	clear_screen()
	show_list()
	if len(shopping_list):
		position = input("Where should I add {}?\n"
						 "Press ENTER to add to the end of the list\n"
						 "> ".format(item))
	else:
		position = 0
		
	try:
		position = abs(int(position))
	except ValueError:
		position = None
	if position is not None:
		shopping_list.insert(position-1, item)
	else:
		shopping_list.append(item)
	print("Item '{}' added to the list! You have {} items total in the list.".format(item, len(shopping_list)))
	show_list()
	

def show_help():
	clear_screen()
	print("What should we pick up at the store?")
	print("""
Enter 'SHOW' to see the list.
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'REMOVE' to remove item from list.
""")
	
	
def show_list():
	clear_screen()
	print("Shopping list: ")
	index = 1
	for item in shopping_list:
		print("{}.  {}".format(index, item))
		index += 1
	print("-" * 12)
	
	
show_help()
while True:
	new_item = input("> ")
	
	if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
		show_list()
		break
	elif new_item.upper() == "HELP":
		show_help()
		continue
	elif new_item.upper() == "SHOW":
		show_list()
		continue
	elif new_item.upper() == "REMOVE":
		remove_from_list()
	else:
		add_to_list(new_item)
	