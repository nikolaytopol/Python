# # Read the number of books in the library
# n = int(input())

# # Read the book titles
# books = [input().strip() for _ in range(n)]

# # Read the number of user queries
# m = int(input())

# # Read the user queries
# queries = [input().strip() for _ in range(m)]

# # Initialize the results list
# results = []

# # Process each query
# for query in queries:
#     # Placeholder for the best match book title and its score
#     best_match = ''
#     best_score = 0

#     # Compare the query with each book title
#     for book in books:
#         # Calculate a similarity score between the query and the book title
#         # This could be a count of matching words, Jaccard similarity, etc.
#         # Here we use a simple word match for illustration
#         book_words = set(book.split())
#         query_words = set(query.split())
#         common_words = book_words.intersection(query_words)
#         score = len(common_words) / len(book_words.union(query_words))

#         # Update the best match if this book has a higher score than the current best
#         if score > best_score:
#             best_match = book
#             best_score = score

#     # Add the best match to the results list
#     results.append((best_match, best_score))

# # Output the number of results
# print(len(results))

# # Output each result
# for result in results:
#     print(result[0])



# with open('library_input.txt', 'r', encoding='utf-8') as file:
#     n = int(file.readline().strip())
#     books = [file.readline().strip() for _ in range(n)]
#     m = int(file.readline().strip())
#     queries = [file.readline().strip() for _ in range(m)]

# results = []


# for query in queries:
#     matches = []
#     query_words = set(query.split())

   
#     for book in books:
#         book_words = set(book.split())
#         common_words = book_words.intersection(query_words)
#         jaccard_score = len(common_words) / len(book_words.union(query_words))

       
#         if jaccard_score > 0:
#             matches.append((book, jaccard_score))

    
#     matches = sorted(matches, key=lambda x: -x[1])[:5]
#     results.append((len(matches), [match[0] for match in matches]))


# with open('lib_output.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{m}\n')
#     for result in results:
#         file.write(f'{result[0]}\n')
#         for book in result[1]:
#             file.write(f'{book}\n')



# # Open and read from 'library_input.txt'
# with open('library_input.txt', 'r', encoding='utf-8') as file:
#     n = int(file.readline().strip())  # Number of books
#     books = [file.readline().strip() for _ in range(n)]  # Book titles
#     m = int(file.readline().strip())  # Number of queries
#     queries = [file.readline().strip() for _ in range(m)]  # Queries

# results = []

# # Process each query to find matches
# for query in queries:
#     matches = []
#     query_words = set(query.split())  # Split query into words

#     # Find matching books based on Jaccard score
#     for book in books:
#         book_words = set(book.split())  # Split book title into words
#         common_words = book_words.intersection(query_words)
#         jaccard_score = len(common_words) / len(book_words.union(query_words))

#         # If there's a match, add it to the list
#         if jaccard_score > 0:
#             matches.append((book, jaccard_score))

#     # Sort matches by Jaccard score and select the top 5
#     matches = sorted(matches, key=lambda x: -x[1])[:5]
#     # Add the number of matches and their titles to the results
#     results.append((len(matches), [match[0] for match in matches]))

# # Write the results to 'lib_output.txt'
# with open('libr_output.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{m}\n')  # Write the number of queries
#     for result in results:
#         file.write(f'{result[0]}\n')  # Write the number of matches
#         for book in result[1]:
#             file.write(f'{book}\n')  # Write each matching book title






from difflib import SequenceMatcher
from collections import Counter
import re


def words_similarity(book_words, query_words):
    # Count the occurrence of each word in both book title and query
    book_counter = Counter(book_words)
    query_counter = Counter(query_words)

    # Create sets of unique words for each
    book_words_set = set(book_words)
    query_words_set = set(query_words)

    # Calculate Jaccard similarity based on the unique words
    jaccard_sim = len(book_words_set.intersection(query_words_set)) / len(book_words_set.union(query_words_set))
    
    # For each word in the query, find the most similar word in the book title and sum their similarities
    word_similarity_sum = sum(max(SequenceMatcher(None, q_word, b_word).ratio() for b_word in book_words_set) for q_word in query_words_set)

    # Normalize the sum by the number of words in the query
    normalized_similarity = word_similarity_sum / len(query_words_set)

    # Combine Jaccard similarity with normalized word similarity
    combined_similarity = (jaccard_sim + normalized_similarity) / 2

    return combined_similarity

# Open and read from 'library_input.txt'
with open('library_input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())  # Number of books
    books = [file.readline().strip() for _ in range(n)]  # Book titles
    m = int(file.readline().strip())  # Number of queries
    queries = [file.readline().strip() for _ in range(m)]  # Queries

results = []

# Process each query to find matches
for query in queries:
    matches = []
    # Normalize query to word list, handling potential scrambled words
    query_words = re.findall(r'\w+', query.lower())

    # Find matching books based on a custom similarity function
    for book in books:
        # Normalize book title to word list
        book_words = re.findall(r'\w+', book.lower())
        similarity = words_similarity(book_words, query_words)

        # If the similarity is above a threshold, add it to the list
        if similarity >= 0.4:
            matches.append((book, similarity))

    # Sort matches by similarity and select the top 5
    matches.sort(key=lambda x: -x[1])
    top_matches = matches[:5]

    # Append the number of matches and book titles to the results
    results.append((len(top_matches), [match[0] for match in top_matches]))

# Write the results to 'lib_output.txt'
with open('libRO_output.txt', 'w', encoding='utf-8') as file:
    file.write(f'{m}\n')  # Write the number of queries
    for result in results:
        file.write(f'{result[0]}\n')  # Write the number of matches
        for book in result[1]:
            file.write(f'{book}\n')  # Write each matching book title
