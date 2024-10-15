"""
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
"""
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
difference = set1.difference(set2)
print(' '.join(map(str, sorted(difference))))
