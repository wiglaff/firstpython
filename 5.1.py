import random
def passw_generator(count_char=8):
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
    'P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
    passw=[]
    for i in range(count_char):
        passw.append(random.choice(arr))
    return "".join(passw)
print(passw_generator(10))
print(passw_generator())
input()
