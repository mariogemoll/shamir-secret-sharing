import galois
import numpy as np
from typing import Tuple

GF = galois.GF(2**8)

Share = Tuple[int, int]


def create_shares(k: int, n: int, secret: int) -> list[Share]:
    assert (1 <= k <= n < GF.order - 1)
    assert (0 <= secret <= 255)
    # Select a random polynomial p of degree k-1 with p(0) = secret
    coefficients = np.append(GF.Random(k - 1), secret)
    p = galois.Poly(coefficients, field=GF)
    assert (p(0) == secret)
    # The secret shares are the evaluations of the polynomial at points 1, 2, ...n
    return [(i, int(p(i))) for i in range(1, n + 1)]


def reconstruct_secret(shares: list[Share]) -> int:
    # Split up the points into lists of x and y coordinates and convert them into field elements
    xs, ys = map(GF, zip(*shares))
    # Reconstruct the polynomial using Lagrange interpolation
    p = galois.lagrange_poly(xs, ys)
    # The secret is the evaluation of the reconstructed polynomial at x=0
    return int(p(0))
