username = ("Mastergamer35")
password = ("Hi1234")

userinput = input("Type your username " "\n")
   
if userinput == username:
    passwordtype = input("Type password " "\n")
    if passwordtype == password:
        print((" Login successful!"), ("\n"))
        print(("Hello"), (username))
    else:
        print("Wrong password or username ")
else:
    print("Wrong password or username ")        
