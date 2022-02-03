# AWAIT TO CHECK 

# Recursive Algorithm
# An algorithm that calls itself repeatedly until the problem is solved
# Example: To determine the sum of first n natural numbers
int fact(int n)
{
  if (n <= 1) // base case
    return 1;
  else
    return n * fact(n-1);
}


# Divide and Conquer Algorithm
# An algorithm that first divides the problem into smaller parts and solve them, then combine to get final solution
# Example: Merge Sort
def merge_sort(arr):
  if len(arr) < 2:
    return arr
  else:
    mid = len(arr) // 2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])
    return join_sorted(left_part, right_part)

# Brute-Force Algorithm
# An algorithm that tries every possibilities
# Example: Native Algorithm to find a pair sums up to k (tries every possible layer)
def find_pair(arr, k):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if (arr[i]+arr[j]) == k:
        return (i, j)
  return(-1, -1)


# Backtracking Algorithm
# An algorithm that tries all the possible candidates and goes back as soon as it's defects that the actual candidate can't be valid
# Example: Count subsets that sum up to k
def subsets_k(arr, k, i = 0)
  if k == 0:
    return 1 # valid candidate
  elif k < 0 or i == len(arr):
    return 0 # invalid candidate
  else:
    return subsets_k(arr[i], i+1) + subsets_k(arr, k, i+1)
#
      
      
# Dynamic Programming Algorithm
# Dynamic programming is an optimization techniques for recursive solutions that have overlapping sub-problem, 
# we use dp to solve a sub-problem, we use dp to solve a sub-problem only sequence
# Example: nth term of Fibonacci sequence
def fibonacci(n):
  dp = [0]*(n+1)
  dp[0] = 0
  dp[1] = 1
  for i in range(2, len(dp)):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]
  

# Greedy Algorithm
# An algorithm that chooses the most optional move at each step
# Example: Activity selection problem (Maximum number of activities infinite amount of time)
def max_nb_activities(activities, time_limit):
  activities.sort()
  count = 0
  time = 0
  for activity in activities:
    if (time + activity) > time_limit:
      break
    else:
      count += 1
      time += activity
    return



      

 
