def chebyshev_distance(p1, p2):
    """Docstring..."""
    cbdist = []
    for p in zip(p1, p2):
        cbdist.append(p[0] - p[1])
    return max(abs(pdist) for pdist in cbdist)


if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
