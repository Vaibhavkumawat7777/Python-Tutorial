import random
import os
terminalWidth = int(os.get_terminal_size().columns)

print()
print()
print("This programme can encrypt or decrypt your data.".center(terminalWidth))
print("By Vaibhav Kumawat".center(terminalWidth))
print()
print("1.  Encrypt Text           2. Decrypt Text           3. Exit")
mode = int(input("What do you want to do? "))

endata = []
dedata = []
alphabetsAndNumbers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","^","&","*","(",")","<",">","?","/","_","|"]

def randomNumber():
    randNumber = ""
    for i in range(0,6):
        randNumber += random.choice(alphabetsAndNumbers)
    return randNumber
def randomSymbol():
    return random.choice(symbols)

def encode():
    inputText = input("Enter text here to encrypt: ".center(10))
    l = inputText.split(" ")
    for i in l:
        endata.append(randomNumber())
        endata.append(randomSymbol())
        endata.append(i[::-1])
        endata.append(randomSymbol())
        endata.append(randomNumber())
    entxt = ""
    for i in range(1 , len(endata)+1):
        entxt += endata[i-1]
        if(i%5==0):
            entxt += " "
    print()
    print("Encrypted Text:",entxt)
    endata.clear()

def decode():
    inputText = input("Enter text here to decrypt: ".center(10))
    l = inputText.split(" ")

    for i in range(0,len(l)):
        dedata.append(l[i][7:-7][::-1])

    print("Decrypted Text:"," ".join(dedata))
    dedata.clear()

while True:
    if(mode < 4 and mode > 0):
        if(mode == 3):
            print()
            print()
            print("----------Thank You :)----------".center(terminalWidth))
            exit()
        elif(mode == 1):
            encode()
        else:
            decode()
    elif(mode > 4 or mode < 0):
        raise IndexError("Your reply is not valid!!!")
    else:
        raise ValueError("Your can only enter a valid number!!!")

    
    print()
    print("1.  Encrypt Text           2. Decrypt Text           3. Exit".center(10))
    mode = int(input("What do you want to do? ").center(10))