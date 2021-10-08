
print("zijn we aan het coderen?")
choice = input()
if choice == 'ja':
    def begin():
        print("in welke taal?")
        taal = input()
        if taal == 'python':
                print('dat klopt')
                exit()
        else:
            print('fout!')
            begin()


begin()
        
