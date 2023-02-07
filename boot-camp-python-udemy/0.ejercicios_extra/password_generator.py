import random

def run():
    password = password_generator()
    print(f'tu contraseña es : {password}')


def password_generator():
    
    cappitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    letters         = [word.lower() for word in cappitalLetters]
    numbers         = ['1','2','3','4','5','6','7','8','9','0']
    simbols         = ['!','@','#','$','%','&','/','_','-']

    characters = cappitalLetters+letters+numbers+simbols
    return ''.join(random.choices(characters,k=15))
    

if __name__ == "__main__":
    run()