import byteshares
from typing import ByteString, Tuple

Share = Tuple[int, ByteString]


def create_shares(k: int, n: int, secret: ByteString) -> list[Share]:
    """Create n shares for byte string secret such that k shares can be used to reconstruct it."""
    assert (1 <= k <= n < 256)
    assert (len(secret) == 32)
    shares = {}
    for idx in range(1, n+1):
        shares[idx] = bytearray()
    for i in range(32):
        shares_for_byte = byteshares.create_shares(k, n, secret[i])
        for (idx, share) in shares_for_byte:
            shares[idx].append(share)
    return [(idx, bytes(arr)) for (idx, arr) in shares.items()]


def reconstruct_secret(shares: list[Share]) -> ByteString:
    """Reconstruct the secret byte string for a list of shares."""
    secret = bytearray()
    for i in range(32):
        shares_for_byte: list[byteshares.Share] = [(idx, val[i]) for (idx, val) in shares]
        secret.append(byteshares.reconstruct_secret(shares_for_byte))
    return bytes(secret)
