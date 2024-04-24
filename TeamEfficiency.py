# Since there was an internal issue with the previous attempt to run the code, let's try again.

def getTotalEfficiency(skills):
    skills.sort()
    n = len(skills)
    # The sum for each team should be the same, let's check it using the first and last skill value
    expected_sum = skills[0] + skills[-1]
    total_efficiency = 0

    for i in range(n // 2):
        # If the sum of this team doesn't match the expected sum, return -1
        if skills[i] + skills[n - i - 1] != expected_sum:
            return -1
        # Else add their product to the total efficiency
        total_efficiency += skills[i] * skills[n - i - 1]

    return total_efficiency

# Example test cases
print(getTotalEfficiency([5, 4, 2, 1]))  # Expected output: 13
print(getTotalEfficiency([2, 1, 1, 4, 3, 5]))  # Expected output: -1

