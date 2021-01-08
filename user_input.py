#please type your username here
def name():

    name=input("enter your name :").title()
    print("hello",name)
#enter a name less than 10

    if len(name)>10:
        print("please type a name less than 10 char ")
    else:
        print("welcome",name.title())

name()