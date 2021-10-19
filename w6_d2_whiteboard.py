# A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

# Return the number of indices where heights[i] != expected[i].


# ex.1
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# ex.2
# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.

def students_in_line(heights):
  heights1 = sorted(heights)
  count = 0
  for i in range(len(heights)):
    if heights[i] != heights1[i]:
      count += 1
      heights1[i] + 1
  print(count)

students_in_line([1,1,2,1,3,4])
students_in_line([1,2,3,4,5])
students_in_line([5,4,5,2,1])
