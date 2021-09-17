# returns: dict(k,v) k - classes v - frequency
import math
def compute_frequency(sample):
	frequency_table = {
		'A': 0,
		'B': 0,
		'C': 0,
	}
	for letter in sample:
		if letter is 'A':
			frequency_table[letter] += 1
		if letter is 'B':
			frequency_table[letter] += 1
		if letter is 'C':
			frequency_table[letter] += 1
	return frequency_table

# returns: dict(k,v) k - classes v - relative frequency
def compute_relative_frequency(sample):
	result = {}
	totalsamples = sum(sample.values())
	for k,v in sample.items():
		result[k] = round(v/totalsamples, 1)
	return result

# reads in a file and returns a list of letters	
def get_frequencylist():
	letters = []
	with open('sample.txt', 'rt') as file:
		lines = file.readlines()
		for line in lines:
			line = line.split()
			letters.extend(line)
	return letters

def number_2():
	bmi_sample = [19.5, 20.9, 17.1, 27.0, 24.1, 16.2, 19.8, 25.1, 23.7, 27.5]
	bmi_sample.sort()
	print (bmi_sample)

	def classify_weight(sample):
		result = {
		'under weight': 0, 
		'normal': 0,
		'over weight': 0,}

		for number in sample:
			print(number)
			if number < 18.5:
				result['under weight'] += 1
			elif 18.5 <= number <= 25:
				result['normal'] += 1
			else:
				result['over weight'] += 1
	
		return result
	print(classify_weight(bmi_sample))	

def number_3():
	sample = {
	'x1' : 4,
	'x2' : 1,
	'x3' : 5,
	'x4' : -2,
	'x5' : -3,
	}


	def summation_a(sample):
		i = 1
		upperbound = 5
		totalSum = 0
		for k,v in sample.items():
			totalSum += (v-1)**2
		return totalSum

	def summation_b(sample):
		i = 1
		upperbound = 5
		totalSum = 0
		for k,v in sample.items():
			compute = ((3 * (i**2)) - v)
			totalSum += compute
			i += 1

		return totalSum	

	def summation_c(sample):
		i = 1
		upperbound = 5
		totalSum = 0
		for k,v in sample.items():
			compute = i * (v)**2
			totalSum += compute
			i += 1

		return totalSum

	print('summation of a: ', summation_a(sample))
	print('summation of b: ', summation_b(sample))
	print('summation of c: ', summation_c(sample))

def number_4():
	sample = [61, 27, 54, 108, 64, 40, 58, 21, 73, 44]
	
	def calculate_sample_mean(sample):
		total = 0
		for number in sample:
			total += number
		sample_mean = total/len(sample)
		return sample_mean

	print(calculate_sample_mean(sample))
	

	def calculate_sample_standard_deviation(sample):
		sample_mean = calculate_sample_mean(sample)
		sample_std = 0
		summation = 0
		n = len(sample) - 1
		for number in sample:
			compute = (number - sample_mean) ** 2
			summation += compute

		sample_std = round(math.sqrt(summation/n))
		return sample_std

	print(calculate_sample_standard_deviation(sample))

def main():
	# sample = get_frequencylist()
	# frequency_table = compute_frequency(sample)
	# print(compute_relative_frequency(frequency_table))
	# number_2()
	# number_3()
	number_4()

if __name__ == '__main__':
	main()


	