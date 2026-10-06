import math


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


n = int(input("Enter number of points: "))

if n < 2:
    raise ValueError("At least two points are required.")

points = []

for i in range(n):
    x = float(input(f"Enter X coordinate of P{i + 1}: "))
    y = float(input(f"Enter Y coordinate of P{i + 1}: "))
    points.append((x, y))

k1 = points[0]
k2 = points[1]

print("\nInitial Values:")
print("K1 =", k1)
print("K2 =", k2)

for i in range(2, n):
    point = points[i]

    print("\n" + "-" * 40)
    print(f"Calculating P{i + 1} = {point}")

    d1 = distance(point, k1)
    d2 = distance(point, k2)

    print(f"Distance from K1 = {d1:.2f}")
    print(f"Distance from K2 = {d2:.2f}")

    if d1 < d2:
        print("P", i + 1, "belongs to K1")

        new_x = (k1[0] + point[0]) / 2
        new_y = (k1[1] + point[1]) / 2
        k1 = (new_x, new_y)

        print("New K1 =", k1)

    else:
        print("P", i + 1, "belongs to K2")

        new_x = (k2[0] + point[0]) / 2
        new_y = (k2[1] + point[1]) / 2
        k2 = (new_x, new_y)

        print("New K2 =", k2)

print("\n" + "=" * 40)
print("FINAL RESULT")
print("=" * 40)

print("Final K1 =", k1)
print("Final K2 =", k2)

# Sample input:
# 4
# 1
# 1
# 2
# 2
# 8
# 8
# 9
# 9
