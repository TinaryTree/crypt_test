import rsa


(publickey, privatekey) = rsa.newkeys(1001)  # 对数字1000加密得到公钥和私钥
pub = publickey.save_pkcs1()  # 获取公钥
# 将公钥保存到文件*************
filepub = open("public.pem", 'wb+')
filepub.write(pub)
filepub.close()

pri = privatekey.save_pkcs1()  # 获取私钥
# 将私钥保存到文件***********
filepri = open('private.pem', 'wb+')
filepri.write(pri)
filepri.close()
