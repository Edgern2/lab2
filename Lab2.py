def display_main_menu(): 

	print("display_main_menu")
	print("“Enter some numbers separated by commas (e.g. 5, 67, 32)”")

def calc_average(): 
	print('calc_average')

def get_user_input():
	numbers=[float(x) for x in input().split(",")]
	return numbers

def calc_average_temperature(numbers):
	return sum(numbers)/len(numbers)

def calc_min_max_temperature(numbers):
	return [min(numbers),max(numbers)]

def calc_median_temperature(numbers):
	if len(numbers) %2 == 1:
		return numbers[((len(numbers) +1 )// 2 ) -1 ]
	else:
		return (numbers[(len(numbers) // 2 ) -1 ]+numbers[((len(numbers))// 2 )])/ 2
	
def main():

	print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
	display_main_menu()

	num_list = get_user_input()

	print("the average of the numbers are: "+str(calc_average_temperature(num_list)))

	mintemp,maxtemp=calc_min_max_temperature(num_list)

	print("the minimum temperature is "+ str(mintemp)+" and the maximum teperature is "+str(maxtemp))
	print("the median number is "+str(calc_median_temperature(num_list)))

if __name__=="__main__":
	main()
