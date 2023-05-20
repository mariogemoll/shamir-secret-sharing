import galois
import numpy as np

GF = galois.GF(2 ** 8)
print(type(GF))

def create_shares(field, k: int, n: int, secret):
    assert(k < n)
    assert(n < GF.order - 1)
    # Select a random polynomial p of degree k-1 with p(0) = secret
    coefficients = np.append(GF.Random(k - 1), secret)
    p = galois.Poly(coefficients, field=GF)
    assert(p(0) == secret)
    # The secret shares are the evaluations of the polynomial at points 1, 2, ...n
    return [p(i) for i in range(1, n + 1)]

secret = GF.Random()
k = 3
n = 5
shares = create_shares(GF, 3, 5, secret)

for i in range(n):
    print(f'Share {i+1}: {shares[i]}')
