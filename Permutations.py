# Task: Cycles in Permutations
#
# A permutation is a bijective function from a set of integers S = {1, 2, ..., n} onto itself.
# This means every integer in S is mapped to a unique integer in the same set.
# Given such a permutation, we are interested in finding its 'cycles'.
#
# A 'cycle' is a sequence in which we start with an integer i and repeatedly apply the permutation
# to it until we get back to i. Each cycle is represented by a tuple of the integers in the order
# they are visited.
#
# The task is to write a function that takes a permutation as input and outputs the cycles in a 
# specific format.
#
# Input:
# - A list of integers representing the permutation, where the i-th element in the list
#   is the image of i under the permutation function.
#   For example, for permutation f, the list [f(1), f(2), ..., f(n)].
#
# Output:
# - A list of strings representing the cycles. Each cycle is formatted as a space-separated
#   list of integers within parentheses.
# - The cycles are sorted first by length (longest to shortest) and then by the minimum element
#   within each cycle (smallest to largest).
#   For example, "[(2 4 6 8), (1 5 7), (3)]" where each tuple is a cycle.
#
# The output cycles are formatted as strings so that they are suitable for printing or further processing.



# Let's write a function to find the cycles in a permutation.
# The function will take a list of integers representing the permutation and
# return a list of strings representing the cycles.

def find_cycles(permutation):
    # Initialize an empty list to store the cycles
    cycles = []
    
    # Keep track of which elements have been visited
    visited = [False] * len(permutation)
    
    for i in range(len(permutation)):
        # If the element is not visited, it means we have a new cycle
        if not visited[i]:
            cycle = []
            j = i
            # Follow the cycle
            while not visited[j]:
                visited[j] = True
                cycle.append(j + 1)  # We add 1 because the permutation is 1-indexed
                j = permutation[j] - 1
            cycles.append(cycle)
    
    # Sort the cycles: first by length (descending), then by the smallest number in each cycle (ascending)
    cycles.sort(key=lambda x: (-len(x), x))
    
    # Convert cycles to the required string format
    cycle_strings = ['(' + ' '.join(map(str, cycle)) + ')' for cycle in cycles]
    
    return cycle_strings

# We'll use the example from the image to test the function
example_permutation = [1,2,4,6,8,3,5,7,9] # [5, 4, 3, 6, 7, 8, 1, 2]
example_cycles = find_cycles(example_permutation)

# Output the cycles
print(example_cycles)