import argparse
from secret_sharing import reconstruct_secret, Share

parser = argparse.ArgumentParser(description="Combines shares to reconstruct the secret.")
parser.add_argument(
    "shares", help="Hex-encoded shares separated by spaces", nargs='*', type=bytes.fromhex)
args = parser.parse_args()

# Split the index (first byte) from each share byte string
shares: list[Share] = [(share[:1][0], share[1:]) for share in args.shares]

secret = reconstruct_secret(shares)

print(secret.hex())
