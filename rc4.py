import binascii
import struct

def KSA(key):
    S = list(range(256))
    # Add KSA implementation Here
    j = 0
    for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    K = 0
    i = 0
    j = 0
    # Add PRGA implementation here
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

if __name__ == '__main__':
    # RC4 algorithm please refer to http://en.wikipedia.org/wiki/RC4

    ## key = a list of integer, each integer 8 bits (0 ~ 255)
    ## ciphertext = a list of integer, each integer 8 bits (0 ~ 255)
    ## binascii.unhexlify() is a useful function to convert from Hex string to integer list
    
    #     Several test cases: (to test RC4 implementation only)
    #     1. key = '1A2B3C', cipertext = '00112233' -> plaintext = '0F6D13BC'
    #     2. key = '000000', cipertext = '00112233' -> plaintext = 'DE09AB72'
    #     3. key = '012345', cipertext = '00112233' -> plaintext = '6F914F8F'

    keys = ['1A2B3C', '000000', '012345']
    ciphertext = binascii.unhexlify('00112233')
    plaintexts = ['0F6D13BC', 'DE09AB72', '6F914F8F']

    for r in range(3):
            ## Use RC4 to generate keystream
        keystream = RC4(binascii.unhexlify(keys[r]))

        ## Cracking the ciphertext
        plaintext = ""
        for i in ciphertext:
            plaintext += ('{:02X}'.format(i ^ next(keystream)))
        assert plaintext == plaintexts[r], f'Case {i} failed'
        print(f'Case {r} passed: {keys[r]}, 00112233, {plaintexts[r]}') 

    IV = '46bcf4'
    key = binascii.unhexlify(IV+'1F1F1F1F1F')
    WEP_ICV = '8ba2536e'
    ciphertext = binascii.unhexlify('98999de0ce2db11eb2169a5d442143cdd0470a8832f6712745fb4ffacdcc9ff99681c1da2f8c479ef446300eaa68aaca018b6a0a985c'+WEP_ICV)

    ## Use RC4 to generate keystream
    keystream = RC4(key)
    
    ## Cracking the ciphertext
    plaintext = ""
    for i in ciphertext:
        plaintext += ('{:02X}'.format(i ^ next(keystream)))
    print(plaintext)
    plaintext = plaintext[:-len(WEP_ICV)]
    
    crcle = binascii.crc32(bytes.fromhex(plaintext)) & 0xffffffff
    crc = struct.pack('<L', crcle).hex()
    print(crc)
