import random
for i in range(0,10):          #10 randomized values in range of 1 till 1000000
    k=random.randint(0,1000000)
#for k in range(0,102):  #output list of 101 values
#k = int(input ("please enter K: \n "))   # manual output
    if k in [0,11,12,13,14]:
        print ("Мы нашли {} грибов".format(k))
    elif k%10 == 1:
        print ("Мы нашли {} гриб".format(k))
    elif k%10 in range (2,5):
        print("Мы нашли {} гриба".format(k))
    else:
        print ("Мы нашли {} грибов".format(k))