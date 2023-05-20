from byteshares import create_shares, reconstruct_secret
import random
import unittest


class TestByteshares(unittest.TestCase):
    def test_secret_sharing(self):
        secret = random.randint(0, 255)
        n = random.randint(1, 255)
        k = random.randint(1, n)
        shares = create_shares(k, n, secret)
        subset = random.sample(shares, k)
        reconstructed_secret = reconstruct_secret(subset)
        self.assertEqual(reconstructed_secret, secret)


if __name__ == '__main__':
    unittest.main()
