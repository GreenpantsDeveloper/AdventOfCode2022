def read_calories(fname):
	with open(fname, 'r') as fp:
		data = fp.read()

	# Split newlines into lists of calories per elf
	elf_data = data.split('\n\n')  # Get the data for each elf
	elves = [elf.split('\n') for elf in elf_data]  # Split calories per elf
	calories = [[int(calorie) for calorie in elf if calorie] for elf in elves]  # Get calories as integers

	return calories


if __name__ == '__main__':
	calories = read_calories('input.txt')

	top_three_calories = 0

	elves = {elf:sum(cals) for elf, cals in enumerate(calories)}  # Get calories summed per elf
	highest_calories_elf = max(elves, key=elves.get)
	print(f"The elf with the highest amount of calories is elf #{highest_calories_elf} with a total of {elves[highest_calories_elf]} calories.")
	top_three_calories += elves[highest_calories_elf]

	# Remove the highest calorie elf and try again.
	del elves[highest_calories_elf]
	second_highest_calories_elf = max(elves, key=elves.get)
	print(f"The elf with the second highest amount of calories is elf #{highest_calories_elf}with a total of {elves[second_highest_calories_elf]} calories.")
	top_three_calories += elves[second_highest_calories_elf]

	# Remove the second highest calorie elf and try again.
	del elves[second_highest_calories_elf]
	third_highest_calories_elf = max(elves, key=elves.get)
	print(f"The elf with the third highest amount of calories is elf #{third_highest_calories_elf} with a total of {elves[third_highest_calories_elf]} calories.")
	top_three_calories += elves[third_highest_calories_elf]

	print(f"The top three calories combined make {top_three_calories} calories.")
