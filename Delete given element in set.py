"""
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
"""
set_values = set(map(int, input().split()))
value_to_delete = int(input())
if value_to_delete in set_values:
    set_values.remove(value_to_delete)
    print(' '.join(map(str, sorted(set_values))))
else:
    print("Given value is not present in the set list.")
