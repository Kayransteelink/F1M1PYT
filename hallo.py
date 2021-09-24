import datetime
from os import name

    print('hallo!')
    print('ik ben kayran')

    print("hier mag je je naam zetten") 
    naam = input('')

    print(f"hallo {naam}")
    print(f"datum en tijd is {datetime.datetime.today()}")
    print(f"hier komt vraag 1 {naam}.Ben ik een full time gamer?\nType ja/Nee")

    option = input ('')
    if option.lower() == 'ja':
        print("dat was goed")
        
    else:
        exit()
    print(f"hier komt vraag 2 {naam}.waar werk ik? A McDonalds B supermarks C niks")
       option = input ('')
    if option.lower() == 'A':
        print("dat was goed")
    else:
        exit()
    print(f"hier komt vraag 3 {naam}.hoeveel broertjes of zusjes heb ik? A 3 B 1 C 2")
     option = input ('')
    if option.lower() == 'A':
        print("dat was goed")
