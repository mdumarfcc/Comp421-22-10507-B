#Name: Muhammad Umar Ali
#Roll no: 22-10507

import rsa
 

publicKey, privateKey = rsa.newkeys(512)
 

message = str(input("What is required to encrypt :"))
 
#rsa encription
encMessage = rsa.encrypt(message.encode(),
                         publicKey)
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
#rsa decription
decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
print("decrypted string: ", decMessage)
