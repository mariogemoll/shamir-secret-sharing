# Shamir's secret sharing

This code demonstrates Shamir's secret sharing in Python. It can be used to divide a secret (like a 
root key for a crypto wallet, or a symmetric encryption key for a message) into multiple encrypted
shares. None of the shares on its own reveals anything about the secret, but any number of shares
above a certain threshold can be used to reconstruct the secret. For example, a user of a crypto
wallet can generate shares of her wallet key and give them to trusted family and friends. If she
ever loses the key, she can ask her friends to help her to recover it.

The scheme was first described in Adi Shamir's paper
[How to share a secret](https://dl.acm.org/doi/10.1145/359168.359176). This YouTube video gives a
simple and intuitive explanation: https://www.youtube.com/watch?v=kkMps3X_tEE

### Setup

#### Optional: Create virtual Python environment (YMMV)
```
python3 -m venv env
source env/bin/activate
```

#### Install dependencies
```
pip install -r requirements.txt
```

### Usage

#### Create a secret (if you don't have one)
```
python random_hex_string.py
```
Result:
```
82cd08204aba289a231d3d077d6eaf0981ec2291160a3005c4ab02afb85981bf
```

#### Create shares
You can specify how many shares you want to create (`n`) and how many of those should be needed to
reconstruct the secret later (`k`).
```
python create_shares.py k n SECRET
```
For example, to create a 3-out-of-5 sharing of the secret created above:
```
python create_shares.py 3 5 82cd08204aba289a231d3d077d6eaf0981ec2291160a3005c4ab02afb85981bf
```
Result:
```
01b48a050b30ba1a9fd6c9c97af3c344dbe7db0e1d673bbaccb2442101b902b5f1
02a96417b4b53b806fee09eb9b73becc935d1c537120b09dfb67b550dc9ca82aa6
039f231a9fcf3bb26a1bdd1fe6fd1327413b2b7ffd51811732115a73729df31ee8
04d51e223a859b72b64c8b00a75db5f3ac645364ff0d24dd3dbec4f68168a7e1a3
05e3592f11ff9b40b3b95ff4dad318187e026448737c1557f4c82bd52f69fcd5ed
```

#### Reconstruct the secret
You need `k` shares (as set during the creation of the shares) to reconstruct the secret. The order
of the shares doesn't matter.
```
python reconstruct_secret.py SECRET SECRET ...
```
For example:
```
python reconstruct_secret.py 02a96417b4b53b806fee09eb9b73becc935d1c537120b09dfb67b550dc9ca82aa6 \
05e3592f11ff9b40b3b95ff4dad318187e026448737c1557f4c82bd52f69fcd5ed \
039f231a9fcf3bb26a1bdd1fe6fd1327413b2b7ffd51811732115a73729df31ee8
```
Result:
```
82cd08204aba289a231d3d077d6eaf0981ec2291160a3005c4ab02afb85981bf
```
