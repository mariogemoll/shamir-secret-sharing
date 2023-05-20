from byteshares import create_shares, reconstruct_secret
import galois
import random

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
