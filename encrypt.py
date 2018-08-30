import rsa

string = input('输入你想说的话：')
with open('public.pem', 'r') as file_pub:
    f_pub = file_pub.read()
    pubkey = rsa.PublicKey.load_pkcs1(f_pub)

crypt = rsa.encrypt(string.encode('utf-8'), pubkey)
file_crypt = open("树的加密文件", 'wb+')
file_crypt.write(crypt)
file_crypt.close()
