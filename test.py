import galois
import numpy as np
import random

def create_shares(field, k: int, n: int, secret):
    assert(k < n)
    assert(n < field.order - 1)
    # Select a random polynomial p of degree k-1 with p(0) = secret
    coefficients = np.append(field.Random(k - 1), secret)
    p = galois.Poly(coefficients, field=field)
    assert(p(0) == secret)
    # The secret shares are the evaluations of the polynomial at points 1, 2, ...n
    return [(i, int(p(i))) for i in range(1, n + 1)]

def reconstruct_secret(field, shares):
    # Split up the points into lists of x and y coordinates and convert them into field elements
    xs, ys = map(field, zip(*shares))
    # Reconstruct the polynomial using Lagrange interpolation
    p = galois.lagrange_poly(xs, ys)
    # The secret is the evaluation of the reconstructed polynomial at x=0
    return p(0)

def test():
    GF = galois.GF(2 ** 8)
    secret = GF.Random()
    print(f'Secret: {secret}')
    
    k = 3
    n = 5
    shares = create_shares(GF, 3, 5, secret)
    
    for (i, share) in shares:
        print(f'Share {i}: {share}')
    
    subset = random.sample(shares, 3)
    reconstructed_secret = reconstruct_secret(GF, subset)
    assert(reconstructed_secret == secret)
    print(f'Reconstructed secret: {reconstructed_secret}')

test()