import author
author.start("Calculate")
print("This programme can differentiate or intrigrate your expression!!!")
def info():
    print("\n\n1. Basic Calculation [+,-,x,\u00f7]")
    print("2. Differentiate")
    print("3. Intregrate")
    print("9. EXIT")
    print("Please enter what you want to do?")

def powerRule(variable, power):
    return f"{power}{variable}^{power-1}"
def reversePowerRule(variable, power):
    return f"({variable}^{power+1})/{power+1}"

def calculate(value):
    # 2+3+5*6/4-1
    if(value.find("/") != -1):
        num = value.split("/")
        calculate(num[0]/num[1])
    elif(value.find("*") != -1):
        num = value.split("*")
        i = 0
        while i<value.count("*"):
            ans = 1
            ansFinal = ans * num[i]
        calculate(ansFinal)
    elif(value.find("X") != -1):
        num = value.split("X")
        i = 0
        while i<value.count("X"):
            ans = 1
            ansFinal = ans * num[i]
        calculate(ansFinal)
    elif(value.find("x") != -1):
        num = value.split("x")
        i = 0
        while i<value.count("x"):
            ans = 1
            ansFinal = ans * num[i]
        calculate(ansFinal)
    
def diff():
    finalans = []
    print("Enter your expression:")
    expression = input("=> y = ")
    expList1 = expression.split(" ")
    if(len(expList1) == 1):
        expList2 = expList1[0].split("+")
        for i in expList2:
            if(i.find("^") != -1):
                finalans.append(powerRule(i[:i.find("^")],int(i[i.find("^")+1:])))
        print("+".join(finalans))
    else:
        print("Please enter without blank spaces and not a complex expression.")

def inte():
    print("COMMING SOON...")

while True:
    info()
    reply = int(input("--> "))
    if(reply == 1):
           print("Enter Your Input:")
           inputBox = input(">>> ")
           calculate(inputBox)
    elif(reply == 2):
        diff()   
    elif(reply == 3):
        inte()   
    elif(reply == 9):
        print("MORE FUNCTION WILL COME SOON...")
        break 
    else:
        ValueError("Invalid Enter!!")
        print("Please enter a valid number:=!!!")
        
author.end()