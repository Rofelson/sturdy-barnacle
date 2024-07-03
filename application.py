def chebyshev_distance(p1, p2):
    """Docstring..."""
    cbdist = []
    for x, y in zip(p1, p2):
        cbdist.append(abs(x - y))
    return max(cbdist)


if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
