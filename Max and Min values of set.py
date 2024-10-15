"""
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
"""
input_values = input("Enter the values: ")
values_list = list(map(int, input_values.split()))
unique_values_set = set(values_list)
max_value = max(unique_values_set)
min_value = min(unique_values_set)
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
 
