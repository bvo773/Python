import math
def number_5():
	wasteSites = [1,2,0,8,3,9,0,6,3,5,10,1,0,7,8,1,2,0,8,9,2,4,43,3,1]
	wasteSites.sort()
	print("5) Waste Sites(L to H): ", wasteSites)

	# a
	kthpercentile = 10/100
	n = 25 + 1
	position = n * kthpercentile

	x1 = wasteSites[1]
	x2 = wasteSites[2]
	avg = math.floor(x1 + x2/2)
	position = wasteSites[avg]

	print("5) The 10th percentile of the data set is ",position)

	# b
	kthpercentile = 95/100
	position = wasteSites[math.floor(n * kthpercentile)]
	print("5) The 95th percentile of the data set is ", position)

def number_6():
	wasteSites = [1,2,0,8,3,9,0,6,3,5,10,1,0,7,8,1,2,0,8,9,2,4,43,3,1]
	mean = 0

	for wasteSite in wasteSites:
		mean += wasteSite
	mean = mean/len(wasteSites)
	print ("6c) mean = ", mean)

	def calculateStandardDeviation(sampledata, mean):
		sum_x_2 = 0
		y = 1/(len(sampledata) - 1)
		for number in sampledata:
			x = number - mean
			x = x * x
			sum_x_2 += x

		takeRoot = math.sqrt(sum_x_2 * y)
		return round(takeRoot,3)	

	def calculateZScore(mean):
		sd = calculateStandardDeviation(wasteSites, mean)
		zscore = (43 - mean)/sd
		return round(zscore,2)
	

	print("6c) standard deviation = ", calculateStandardDeviation(wasteSites, mean))	
	print("6c) zscore = ", calculateZScore(mean) )

def number_7():
	gpa_a = 2 * 0.6 + 2.6
	gpa_b = -1.0 * 0.6 + 2.6
	gpa_c = .5 * 0.6 + 2.6 
	gpa_d = -2.5 * 0.6 + 2.6
	print ("7a. GPA: ", gpa_a)
	print ("7a. GPA: ", gpa_b)
	print ("7a. GPA: ", gpa_c)
	print ("7a. GPA: ", gpa_d)

	probationgpa = -1.6 * 0.6 + 2.6
	print ("7b. GPA: ", round(probationgpa, 2))

def number_8():
	students_scores = [31,67,80,41,67,81,45,69,83,48,70,85,55,74,87,56
	,75,90,56,78,92,63,79,95,65,79,99]

	students_scores.sort()
	kthpercentile = 30/100
	position = len(students_scores) * kthpercentile
	print("Students scores: ", students_scores)
	print("Position of 10th percentile: ", position)

def number_21():
	downtime_hours = [11,6,8,8,10,11,6,9,5,16,10,16,26,17,10,12]
	mean = 11.31
	sd = 5.3 
	downtime_hours.sort()

	zscore_larger = round((downtime_hours[15] - mean)/sd, 3)
	zscore_smaller = round((downtime_hours[0] - mean)/sd, 3)
	print("downtime hours: ", downtime_hours)
	print("zscore_larger: ", zscore_larger)
	print("zscore_smaller: ", zscore_smaller)

def number_22():
	controlgroup = [23.1,26,26,26.7,28.7,29,31.6,31.7,35.4,36]
	totalsum = 0;
	for number in controlgroup:
		totalsum += number
	mean = round(totalsum/len(controlgroup),2)
	print ("Control group's mean: ", mean)

	treatmentgroup = [26,32.5,32.5,33,34.2,36.3,38.6,41,41.6,44.8]
	totalsum = 0;
	for number in treatmentgroup:
		totalsum += number
	mean = round(totalsum/len(treatmentgroup),2)
	print ("Treamtment group's mean: ", mean)


number_5()	
number_6()
number_7()
number_8()
number_21()
number_22()


