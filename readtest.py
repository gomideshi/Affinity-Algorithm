import time, random

gate = 'notcool'
again = 'y'
while again=='y':
    
    handle = open("quotebank.txt", "r")
    data = handle.readlines()

    while gate == 'notcool':
        X=random.randint(1,109)
        if str(X) in open('CHECKPOINT.txt').read():
            gate = 'notcool'
        else:
            gate = 'cool'

    checkpoint = open("CHECKPOINT.txt", "a")    
    checkpoint.write(str(X)+'\n')   
    print(data[X].strip())
    handle.close()
    checkpoint.close() 

    again = raw_input('again? y/n')
    gate = 'notcool'


#LOGIC: Creating a second txt file that will be appended with every read attempt
#... num getting the dice to check this second (ongoing total) list to see which
#... quotes have been used / not.
