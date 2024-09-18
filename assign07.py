# Write a program* to remove all the odd numbers from an array.
def remove_odds(arr):
    return [num for num in arr if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = remove_odds(numbers)

print("Original array:", numbers)
print("Array without odd numbers:", filtered_numbers)










# Implement a program* that takes a list of temperatures in Celsius as 
# input from the user. Convert each temperature to Fahrenheit using the
# formula F = (C * 9/5) + 32 and store the converted temperatures in an array.
# Use a while loop to perform the conversion for each temperature.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(celsius_list):
    fahrenheit_list = []
    index = 0
    while index < len(celsius_list):
        fahrenheit = celsius_to_fahrenheit(celsius_list[index])
        fahrenheit_list.append(fahrenheit)
        index += 1
    return fahrenheit_list
celsius_temperatures = list(map(float, input("Enter temperatures in Celsius (separated by space): ").split()))
fahrenheit_temperatures = convert_temperatures(celsius_temperatures)
print("Temperatures in Fahrenheit:", fahrenheit_temperatures)





# Create a function* that takes an array of numbers as a parameter. 
# Use a while loop to calculate and return the sum of all the numbers in the array.
def sum_gen(arr):
    total = 0
    index = 0
    while index < len(arr):
        total += arr[index]
        index += 1
        yield total
        
numbers = [1, 2, 3, 4, 5]
sum_generator = sum_gen(numbers)

for partial_sum in sum_generator:
    print(partial_sum)


# Write a program* that has an array of numbers;
# if the number is negative, it should remove the
# negative number from the array.

def remove_negatives(arr):
    return [num for num in arr if num >= 0]

numbers = [5, -3, 9, -1, 0, 12, -8]
filtered_numbers = remove_negatives(numbers)

print("Original array:", numbers)
print("Array without negatives:", filtered_numbers)
    

# Write a program* that uses a while loop to print the first 10 even numbers.
counter = 1
even_number_count = 0
while even_number_count < 10:
  if counter % 2 == 0:
    print(counter)
    even_number_count += 1
  counter += 1



# Write a program* that uses a while loop to print the first 25 integers.
counter = 1
while counter <= 25:
  print(counter)
  counter += 1


#  *Create a function* that takes an array, an index, and a value as parameters.
#  Inside the function,use the insert method to insert 
#  the value at the specified index in the array. Return the modified array.

array = [1,2,3,4,5]
def insert_value(arr,index,value):
    arr.insert(index,value)
    return arr

modified_array = insert_value(array,2,10)
print(modified_array)


# count:int = 1
# while count <= 10:
#     print("2 *", count, "="  , 2 * count)
#     count += 1