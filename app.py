#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


#  has22([1, 2, 2]) → True
#  has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False


def has22(nums):
  if len(nums) < 2:
    return False
  if  nums[-2] == 2 and nums[-1] == 2:
    return True
  for i in range(len(nums)-2):
    if (nums[i] == 2 and nums[i+1] == 2) :
      return True
  return False
  
  
  # bad solution I found to a codingbat challenge. If you have better solution feel free to fork.
