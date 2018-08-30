import rsa

crypt = input('加密文件：')

with open('private.pem', 'r') as file_pri:
    f_pri = file_pri.read()
    prikey = rsa.PrivateKey.load_pkcs1(f_pri)
with open(crypt, 'rb') as file:
    crypt = file.read()

de_crypt = rsa.decrypt(crypt, prikey)  # 用私钥去解密
print(de_crypt.decode(encoding = "utf-8"))
