import argparse
from secret_sharing import create_shares

parser = argparse.ArgumentParser(
    description=("Creates n \"shares\" of a secret using Shamir's secret sharing algorithm. "
                 "A subset of k shares can be used to reconstruct the secret later."))
parser.add_argument("k", help="Number of shares necessary to reconstruct the secret", type=int)
parser.add_argument("n", help="Number of shares to create in total", type=int)
parser.add_argument("secret", help="The secret (hex encoded) you want to share", type=bytes.fromhex)
args = parser.parse_args()

shares = create_shares(args.k, args.n, args.secret)

for (idx, val) in shares:
    # Prepend the share with the index
    print(f'{idx:02x}{val.hex()}')
