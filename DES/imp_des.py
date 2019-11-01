import sys
from des import setKey, encryptBlock, decryptBlock, encrypt, decrypt
 
def sanityCheck1():
    """Tests single-block DES encryption & decryption
       using algorithm proposed by Ronald Rivest
       (http://people.csail.mit.edu/rivest/Destest.txt)"""
    x0 =  [0x94, 0x74, 0xb8, 0xe8, 0xc7, 0x3b, 0xca, 0x7d]
    x16 = [0x1b, 0x1a, 0x2d, 0xdb, 0x4c, 0x64, 0x24, 0x38]
    x = x0
    for i in range(16):
        setKey(x)
        if i % 2 == 0:
            x = encryptBlock(x)# if i is even, x[i+1] = E(x[i], x[i)
            print(x)
        else:
            x = decryptBlock(x) # if i is odd, x[i+1] = D(x[i], x[i)
    try:
        assert x == x16
    except AssertionError:
        return False
    return True
 
def sanityCheck2():
    """Tests multi-block DES encryption and decryption"""
    try:
        key = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59]
        plaintext = "The quick brown fox jumps over the lazy dog cat"
        ciphertext = encrypt(key, plaintext)
        print(ciphertext)
        assert decrypt(key, ciphertext) == plaintext
    except AssertionError:
        return False
    return True
 
def main():
    if sanityCheck1() and sanityCheck2():
        print("All DES tests ok!")
    else:
        sys.exit(1)
    sys.exit()
 
if __name__ == '__main__':
    main()
