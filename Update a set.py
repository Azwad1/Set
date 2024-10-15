"""
Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
"""
input_set1 = input("Enter the first set of values: ")
input_set2 = input("Enter the second set of values: ")
set1 = set(map(int, input_set1.split()))
set2 = set(map(int, input_set2.split()))
set1.update(set2)
print(" ".join(map(str, sorted(set1))))
