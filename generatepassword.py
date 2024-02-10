import random

caracter='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@!#$%^&*._-/\?<>][{ }]'
taille=random.randint(8,23)
password=''   
test=False

while test==False:
    for i in range(taille):
        x=random.choice(caracter)
        password+=x

    maj=False
    mini=False
    number=False

    if len(password) <= 8:
        print("Password length should be more than 8")
    else:
        if any(i.islower() for i in password):
            mini=True
        if any(i.isupper() for i in password):
            maj=True
        for i in range(10):
            if str(i) in password:#number with string indefined
                number=True

    if maj==True and mini==True and number==True:
        print("Password is strong")
        test=True
    else:
        print('password is weak')
        
   
print("Mot de passe :",password)