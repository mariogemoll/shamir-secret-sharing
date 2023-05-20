import os
import random
from secret_sharing import create_shares, reconstruct_secret
import unittest


class TestSecretSharing(unittest.TestCase):
    def test_secret_sharing(self):
        secret = os.urandom(32)
        n = random.randint(1, 255)
        k = random.randint(1, n)
        shares = create_shares(k, n, secret)
        subset = random.sample(shares, k)
        reconstructed_secret = reconstruct_secret(subset)
        self.assertEqual(reconstructed_secret, secret)


if __name__ == '__main__':
    unittest.main()
