# This is a program that will take multiple string inputs from a user to create a list
# The algo will then sort the list in alphabetical order.

# 3 lists are initialised
my_list = []
my_temp_list = []
sorted_list = []

# Input is taken from the user and added to the "my_list" list
print('Welcome! Please create a list one word at a time.')
print('Please enter a word or press "q" to quit!')
word = input()

while word != 'q':
	my_list.append(word)
	print('Please enter another word or press "q" to quit!')
	word = input()

# The list is copied to a list called "my_temp_list" in order to preserve the state of the original list
my_temp_list = my_list.copy()

# The algo goes through and gets the lowest alphabetical word from the "my_temp_list"
# Assigns it to the a variable called "the_value"
# Adds the value to the next position in the "sorted_list" and deletes the value from the "my_temp_list"
while len(sorted_list) < len(my_list):
	for i, v in enumerate(my_temp_list):
		if i == 0:
			the_value = v
			the_index = i
		else:
			if v < the_value:
				the_value = v
				the_index = i
	del my_temp_list[the_index]			
	sorted_list.append(the_value)
	


print(f'FINAL!! My list was {my_list}.')
print(f'FINAL!! My interim list is now {my_temp_list} (empty).')
print(f'FINAL!! My sorted list is {sorted_list}.')
