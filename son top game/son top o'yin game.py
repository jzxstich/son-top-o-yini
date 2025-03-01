def yutuq(a,b):
    """  a= odamni urinishibu funksiya kim yutganoini aniqlaydi"""
    if a==b:
        print('DURRANG')
    elif a>b:
        print(" Siz g'olibsiz")
    else:
        print(" Yutqazdiz")
def tekshir():
    """ bu funksiya o'yin yana o'ynaydimi yo'qmi shuni tekshiradi"""
    javob=input("Yana o'ynaysizmi")
    return javob=='ha'
def son_top():
    """bu funksiya kopyutyer o'ylagan sinni topish un"""
    k=0
    print("Men 1 dan 10 gacha bo'lgan bir son o'yladm toping:")
    while True:
        k+=1
        son==int(input(""))
        if son==x:
            break
        elif son>x:
            print("o'ylagan sonim bundan kichkina")
            continue
        else:
            print("o'ylagan sonim bundan katta")
            continue
    print(F" Qoyil siz {k} urinishda topdingiz")
    return k
import random as r

def son_top_pc():
    """bu funksiya biz o'ylagan sonni topadi"""
    print("1 dan 10 gacha bo'lgan son o'ylang:")
    a=1
    b=11
    k=r.sample(range(1,11),1)
    print(f" Siz 'ylagan son {k}")
    k=0
    while True:
        k+=1
        p=input()
        if p=='t':
            break
        elif p=='+':
            a=k
            k=r.sample(range(a,b),1)
            
            continue
        else :
            b=k
            k=r.sample(range(a,b),1)
            continue
    print(f" men sizzi sonizzi {k} ta urinishda topdm ")

    
