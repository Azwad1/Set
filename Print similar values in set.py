"""
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
"""
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
common_values = set1.intersection(set2)
print(' '.join(map(str, sorted(common_values))))
