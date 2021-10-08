import datetime

print('hallo!')
print('ik ben kayran')

naam = input('')

print(f"hallo {naam}")
print(f"datum en tijd is {datetime.datetime.today()}")
print(f"{naam} wil jij dit programma nog een keer doen?\nType Y/N")

option = input ('')
if option.lower() == 'yes':
    print("wil je hem im stukjes?")
        
else:
    print("fout")

if option.lower() == 'ja':
    print("zit je in klas sd1d?")
        
else:
    print("fout")

if option.lower() == 'y':
    print("ben ik een mens?")
        
else:
    print("fout")        

