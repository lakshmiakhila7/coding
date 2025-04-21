"""Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.



A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.


Examples1:
Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]

Explanation: 1 <= 3 <= 4 <= 5 <= 7.

Thus the array is sorted in non-decreasing order.
Examples2:
Input: nums = [5, 4, 4, 1, 1]

Output: [1, 1, 4, 4, 5]

Explanation: 1 <= 1 <= 4 <= 4 <= 5.

Thus the array is sorted in non-decreasing order."""

def selection_sort(nums):
    n=len(nums)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if(nums[j]<nums[mini]):
                mini=j
        nums[i],nums[mini]=nums[mini],nums[i]
    return nums
user_input = input("Enter numbers separated by space: ")
nums = list(map(int, user_input.split()))
sorted_nums = selection_sort(nums)
print(sorted_nums)

