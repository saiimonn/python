n = int(input())
arr = map(int, input().split())

arr = list(set(arr))
sortedList = sorted(arr)
print(sortedList[-2])