n, m = map(int, input().split())

children = [tuple(map(int, input().split())) for _ in range(n)]
delivery_points = [list(map(int, input().split())) + [0] for _ in range(m)]  


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


for child in children:
    closest_point = None
    min_distance = float('inf')
    for point in delivery_points:
        dist = distance(child, point)
        if dist < min_distance and point[2] > point[3]:  
            min_distance = dist
            closest_point = point
    if closest_point:
        closest_point[3] += 1


max_distance = 0
for i, child in enumerate(children):
    assigned_point = None
    min_distance = float('inf')
    for point in delivery_points:
        dist = distance(child, point)
        if dist < min_distance and point[3] > 0:
            min_distance = dist
            assigned_point = point
    if assigned_point:
        max_distance = max(max_distance, min_distance)

print(f"{max_distance:.9f}")
