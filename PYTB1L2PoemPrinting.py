def start():
    vers1= "ik ben kayran steelink"
    vers2= "en ik ben best flink"
    vers3= "ik heb leuke vrienden"
    vers4= "waar ik het goed mee kan vinden"
    print(vers1, vers2, vers3, vers4)
    print("wat een mooi gedicht heb je geschreven")
    print("wil jij dit programma nog een keer doen?\nType Y/N")
    
    option = input ('')
    if option.lower() == 'y':
        start()
    else:
        exit()

start()