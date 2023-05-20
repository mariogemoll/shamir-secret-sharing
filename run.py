from byteshares import create_shares, reconstruct_secret
import random

def test():
    secret = random.randint(0, 255)
    print(f'Secret: {secret}')
    
    k = 3
    n = 5
    shares = create_shares(3, 5, secret)
    
    for (i, share) in shares:
        print(f'Share {i}: {share}')
    
    subset = random.sample(shares, 3)
    reconstructed_secret = reconstruct_secret(subset)
    assert(reconstructed_secret == secret)
    print(f'Reconstructed secret: {reconstructed_secret}')

test()
