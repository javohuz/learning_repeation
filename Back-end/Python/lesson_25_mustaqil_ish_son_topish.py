
"""
son topish uyini 

@author: User rashidovj
"""

import random as r
print('Salom son topish uyini uynaymiz ')
while True :

    k = r.choice(list(range(1,11)))
    user = int(input('1 dan 10 gacha son uyladim topishga harakat qiling \n >>> '))
    soni =[]
    soni.append(user)
    
    while k!=user :
        
        if k > user :
            user=int(input('XATO!, Men uylagain son bundan kata , yana harakat qilib kuring >> '))
            soni.append(user)

        if k < user :
            user=int(input('XATO!,Men uylagain son bundan kachik , yana harakat qilib kuring >> '))
            soni.append(user)

        
    print(f"Tabreklayman {len(soni)} urinishida topdingiz men {k} sonini uylagan edim !!!")
    print('Endi sizni galingiz 1 dan 10 gacha son uylang ')
    keraksiz=input('agar uylagan bulsangiz istalgan tugmani boshing : ')
    
    soni2=[]
    x=1
    y=10
    while True :

        n = r.randint(x,y)
        soni2.append(n)
        check = input(f'siz {n} sonini uyladingiz , agar tugri bulsa (t) , katta bulsa (+) , kichik bulsa (-) ni bosing > ')


        if check=='+' :
            x=n+1
                
        elif check=='-':
            y=n-1
        else:
            break
        
    b = len(soni2)
    a=len(soni)
    if a>b :
        print(f'YUTQAZDINGIZ !!! \n Siz {a} ta urinishda toptingiz men esa {b} ta shunish uchun yutqazdingiz ')
    elif a<b:
        print(f'QOYIL YUTDINGIZ  !!! \n Siz {a} ta urinishda toptingiz men esa {b} ta shunish uchun YUTDINGIZ ')
    else :
        print(f'DURRANG ! urinishlar soni teng yani {a} tadan')
    
    stop = input('Yana uynashni hohlaysizmi yes/no : ')
    if stop=='no' :
        break
    
    


