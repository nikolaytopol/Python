# # Read input from file
# with open('pursuit_of_profit_input.txt', 'r') as file:
#     n, ccost, C = map(int, file.readline().split())
#     houses = [tuple(map(int, file.readline().split())) for _ in range(n)]

# # Function to calculate the cross product
# def cross(o, a, b):
#     return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# # Function to compute the convex hull of a set of points
# def convex_hull(points):
#     points = sorted(points, key=lambda x: x[0])
#     lower = []
#     for p in points:
#         while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
#             lower.pop()
#         lower.append(p)
#     upper = []
#     for p in reversed(points):
#         while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
#             upper.pop()
#         upper.append(p)
#     return lower[:-1] + upper[:-1]

# # Function to place a delivery point at the centroid of a convex hull
# def place_delivery_point(hull):
#     cx = sum(p[0] for p in hull) / len(hull)
#     cy = sum(p[1] for p in hull) / len(hull)
#     return cx, cy

# # Function to calculate the squared Euclidean distance between two points
# def distance_squared(a, b):
#     return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

# # Function to calculate the profit for a set of houses and a delivery point
# def calculate_profit(houses, delivery_point, ccost, C):
#     profit = C
#     for house in houses:
#         dist_sq = distance_squared(house, delivery_point)
#         profit -= (ccost * (dist_sq ** 0.5 + 1))
#     return profit

# # Function to calculate the total profit for a given number of delivery points
# def total_profit_for_p(p, houses, ccost, C):
#     delivery_points = [place_delivery_point([house]) for house in houses[:p]]
#     assignments = [[] for _ in range(p)]
#     for house in houses:
#         distances = [distance_squared(house, dp) for dp in delivery_points]
#         closest_dp_index = distances.index(min(distances))
#         assignments[closest_dp_index].append(house)
#     for i in range(p):
#         if assignments[i]:  # Avoid division by zero
#             delivery_points[i] = place_delivery_point(assignments[i])
#     total_profit = p * C
#     for i in range(p):
#         for house in assignments[i]:
#             total_profit -= ccost * ((distance_squared(house, delivery_points[i]) ** 0.5) + 1)
#     return total_profit

# # Find the optimal number of pickup points by iterating and calculating profits
# max_profit = float('-inf')
# optimal_p = 0
# for p in range(1, n + 1):  # Assuming at most one delivery point per house
#     current_profit = total_profit_for_p(p, houses, ccost, C)
#     if current_profit > max_profit:
#         max_profit = current_profit
#         optimal_p = p

# # Write the results to 'output.txt'
# with open('c_output.txt', 'w') as output_file:
#     output_file.write(f"{optimal_p}\n")
#     output_file.write("{:.6f}\n".format(max_profit))




######### Solutiuons with clusters 
# from scipy.cluster.vq import kmeans, vq
# import numpy as np

# # Read input from file
# with open('pursuit_of_profit_input.txt', 'r') as file:
#     n, ccost, C = map(int, file.readline().split())
#     houses = np.array([list(map(int, file.readline().split())) for _ in range(n)])

# # Function to calculate the distance
# def distance(a, b):
#     return np.sqrt(np.sum((a - b) ** 2))

# # Determine the optimal number of delivery points and calculate profit
# max_profit = float('-inf')
# optimal_p = 0
# optimal_centroids = None
# optimal_max_dist = float('inf')

# # Iterate over possible numbers of delivery points
# for p in range(1, min(n, 103) + 1):
#     centroids, _ = kmeans(houses, p)
#     assignments, _ = vq(houses, centroids)

#     # Calculate the maximum distance any house is from its assigned delivery point
#     max_dist = max(distance(houses[i], centroids[assignment]) for i, assignment in enumerate(assignments))

#     # Calculate profit: subtract delivery cost for each house and add revenue for each delivery point
#     profit = p * C - np.sum(ccost * (max_dist + 1))

#     # Check if this is the best profit we have found so far
#     if profit > max_profit or (profit == max_profit and max_dist < optimal_max_dist):
#         max_profit = profit
#         optimal_p = p
#         optimal_centroids = centroids
#         optimal_max_dist = max_dist

# # Write the results to 'output.txt'
# with open('output.txt', 'w') as output_file:
#     output_file.write(f"{optimal_p}\n")
#     output_file.write("{:.6f}\n".format(optimal_max_dist))



from scipy.cluster.vq import kmeans, vq
import numpy as np

# Read input from file
with open('pursuit_of_profit_input.txt', 'r') as file:
    n, ccost, C = map(int, file.readline().split())
    houses = np.array([list(map(int, file.readline().split())) for _ in range(n)], dtype=np.float64)

# Function to calculate the distance
def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Determine the optimal number of delivery points and calculate profit
max_profit = float('-inf')
optimal_p = 0
optimal_centroids = None
optimal_max_dist = float('inf')

# Iterate over possible numbers of delivery points
for p in range(1, min(n, 103) + 1):
    centroids, _ = kmeans(houses, p)
    assignments, _ = vq(houses, centroids)

    # Calculate the maximum distance any house is from its assigned delivery point
    max_dist = max(distance(houses[i], centroids[assignments[i]]) for i in range(len(houses)))
    
    # Calculate delivery costs for each house individually
    delivery_costs = np.array([ccost * (distance(houses[i], centroids[assignments[i]]) + 1) for i in range(len(houses))])
    
    # Calculate total profit
    profit = p * C - np.sum(delivery_costs)

    # Check if this is the best profit we have found so far
    if profit > max_profit or (profit == max_profit and max_dist < optimal_max_dist):
        max_profit = profit
        optimal_p = p
        optimal_centroids = centroids
        optimal_max_dist = max_dist

# Write the results to 'output.txt'
with open('output.txt', 'w') as output_file:
    output_file.write(f"{optimal_p}\n")
    output_file.write("{:.6f}\n".format(optimal_max_dist))

