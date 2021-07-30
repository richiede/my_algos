# Input is taken from the user and added to the "my_list" list

print('Welcome! Please create a list one word at a time.')
print('Please enter a word or press "q" to quit!')
word = input()
my_list = []

while word != 'q':
	my_list.append(word)
	print('Please enter another word or press "q" to quit!')
	word = input()

print(f'My unsorted list is {my_list}. Now let\'s use the Bubble Sort algo to sort them into alphabetical order!')

# This function takes a numerical value and swaps that list value with the next
def swap(num):
	temp = my_list[num + 1]
	my_list[num + 1] = my_list[num]
	my_list[num] = temp

# This function will compare the values and swap them if the previous is greater than the latter
def do_swapping_pass():
	position = 0
	for i in range(len(my_list) - 1):
		if my_list[i] > my_list[i+1]:
			swap(position)
		position += 1

# This runs the algo using the mylist input
for i in range(len(my_list) - 1):
	do_swapping_pass()

print(f'My bubble sorted list is now {my_list}')


