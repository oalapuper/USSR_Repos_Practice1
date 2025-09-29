import os
while True:
    print(">>", end ='')
    answ = input()
    
    if(answ == "exit"):
        print("leaving from programm")
        break
    elif(answ == "clear"):
        os.system("cls")
    elif(answ == "echo"):
        cl = input()
        print(cl)