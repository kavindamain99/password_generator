import random
import string



def pw_generate(length=8):

    count=0
    pswrd=""
    while length>count:
        number=random.randrange(1,9)
        strnumber=str(number)
        pswrd=pswrd+strnumber
        count = count + 1


        lowletter=random.choice(string.ascii_lowercase)
        pswrd=pswrd+lowletter
        count = count + 1


        upletter=random.choice(string.ascii_uppercase)
        pswrd = pswrd + upletter
        count = count + 1

        digits=random.choice("#@%&*")
        pswrd = pswrd + digits
        count = count + 1


    print(''.join(random.sample(pswrd, len(pswrd))))



length=int(input("Hey, Welcome. Just say me how many characters do you want in your password? (default 8)"))

pw_generate(length)

