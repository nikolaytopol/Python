# import sys
# input = sys.stdin.read
# data = input().split()

# index = 0
# n = int(data[index])
# index += 1
# m = int(data[index])
# index += 1
# q = int(data[index])
# index += 1

# # Read the matrix
# M = []
# for _ in range(n):
#     M.append(list(map(int, data[index:index + m])))
#     index += m

# # Function to calculate Euclidean distance
# def euclidean_distance(v1, v2):
#     return sum((x - y) ** 2 for x, y in zip(v1, v2) if x != 0 and y != 0) ** 0.5

# # Handling queries
# results = []
# for _ in range(q):
#     query_type = data[index]
#     query_num = int(data[index + 1])
#     index += 2

#     if query_type == 'u':
#         # User-based recommendation
#         user_id = query_num - 1
#         max_similarity = float('inf')
#         most_similar_user = None

#         # Find the most similar user
#         for i, user_ratings in enumerate(M):
#             if i != user_id:
#                 distance = euclidean_distance(M[user_id], user_ratings)
#                 if distance < max_similarity:
#                     max_similarity = distance
#                     most_similar_user = i

#         # Recommend the highest-rated movie from the most similar user that user_id hasn't watched
#         recommendation = None
#         max_rating = -1
#         for j in range(m):
#             if M[user_id][j] == 0 and M[most_similar_user][j] > max_rating:
#                 max_rating = M[most_similar_user][j]
#                 recommendation = j + 1

#         results.append(recommendation if recommendation else -1)

#     elif query_type == 'v':
#         # Movie-based recommendation
#         movie_id = query_num - 1
#         max_similarity = float('inf')
#         most_similar_movie = None

#         # Find the most similar movie
#         for j in range(m):
#             if j != movie_id:
#                 # Extract the column for each movie
#                 movie_j_ratings = [M[i][j] for i in range(n)]
#                 movie_query_ratings = [M[i][movie_id] for i in range(n)]
#                 distance = euclidean_distance(movie_query_ratings, movie_j_ratings)
#                 if distance < max_similarity:
#                     max_similarity = distance
#                     most_similar_movie = j

#         results.append(most_similar_movie + 1 if most_similar_movie is not None else -1)

# # Output the results
# print(len(results))
# for result in results:
#     print(result)

# 


from itertools import zip_longest

# Open and read from 'input.txt'
with open('kinopoisk_input.txt', 'r') as file:
    data = file.read().split()

index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
q = int(data[index])
index += 1

# Initialize matrix M
M = []
for _ in range(n):
    M.append(list(map(int, data[index:index + m])))
    index += m

# Define the Euclidean distance function
def euclidean_distance(v1, v2):
    # Using zip_longest to handle vectors of different lengths
    return sum((x - y) ** 2 for x, y in zip_longest(v1, v2, fillvalue=0)) ** 0.5

# Initialize results list
results = []
for _ in range(q):
    query_type = data[index]
    query_num = int(data[index + 1])
    index += 2

    if query_type == 'u':
        user_id = query_num - 1
        max_similarity = float('inf')
        most_similar_user = None

        # Find the most similar user
        for i, user_ratings in enumerate(M):
            if i != user_id:
                distance = euclidean_distance(M[user_id], user_ratings)
                if distance < max_similarity:
                    max_similarity = distance
                    most_similar_user = i

        # Recommend the highest-rated movie that the user hasn't seen
        recommendation = None
        max_rating = -1
        for j in range(m):
            if M[user_id][j] == 0 and M[most_similar_user][j] > max_rating:
                max_rating = M[most_similar_user][j]
                recommendation = j + 1

        results.append(recommendation if recommendation is not None else -1)

    elif query_type == 'v':
        movie_id = query_num - 1
        max_similarity = float('inf')
        most_similar_movie = None

        # Find the most similar movie
        for j in range(m):
            if j != movie_id:
                movie_j_ratings = [M[i][j] for i in range(n)]
                movie_query_ratings = [M[i][movie_id] for i in range(n)]
                distance = euclidean_distance(movie_query_ratings, movie_j_ratings)
                if distance < max_similarity:
                    max_similarity = distance
                    most_similar_movie = j

        results.append(most_similar_movie + 1 if most_similar_movie is not None else -1)

# Output the results
with open('kinopoisk_output.txt', "w") as output_file:
    output_file.write(f"{len(results)}\n")  # First line is the number of results
    for result in results:
        output_file.write(f"{result}\n")  # Write each result on a new line
