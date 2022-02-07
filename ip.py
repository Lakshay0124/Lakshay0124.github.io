import random
ip = ".".join(map(str,(random.randint(0,255)
                        for i in range(4))))


with open("ip_true.txt","w") as f:
    f.write(ip)
    
print(ip)
