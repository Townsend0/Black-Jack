import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
\n"""
def win(a,b,e):
    c=[0,0]
    for d in b:
        c[0]+=a[d]
    if 'A' in b and c[0]+10<=21:
        c[0]+=10
    for d in e:
        c[1]+=a[d]
    if c[1]>21:
        print("\n\nYou win")
    elif c[0]>21:
        print("\n\nYou lose")
    elif c[0]>c[1]:
        print("\n\nYou win")
    elif c[1]>c[0]:
        print("\n\nyou lose")
    else:
        print("\n\nDraw")

c=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
a={ 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }
b=[]
e=[]
print(logo)
for d in range(2):
    b.append(random.choice(c))
    e.append(random.choice(c))
print(f"Your cards:\n[{b[0]}][{b[1]}]\nComputer's first card:\n[{e[0]}][?]")
g=True
while g:
    d=input("\nType 'y' to get another card, type 'n' to pass: ").lower()
    if d=='n':
        print("\nYour final hand: ")
        for f in b:
            print(f"[{f}]",end="")
        print("\nComputer's final hand: ")
        d=0
        for f in e:
            d+=a[f]
        if 'A' in e and d+10<=21:
            d+=10
        while d<17:
            e.append(random.choice(c))
            d+=a[e[len(e)-1]]
        for f in e:
            print(f"[{f}]",end="")
        win(a,b,e)
        g=False
    elif d=='y':
        d=0
        b.append(random.choice(c))
        print("\nYour hand: ")
        for f in b:
            d+=a[f]
            print(f"[{f}]",end="")
        if d>21:
            print("\nYou lose")
            break
    else:
        print("( Invalid input! )")