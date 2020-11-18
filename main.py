import math as mt
import sys

previousAnswers = []
roundTo = 4
units = "degree"

def checkInput(x):
    symbolInputs = ['+', '-','/','*', '^', '!', '(',')', '|', '%']
    wordInputs = ["sin", "cos", "tan", "tan^-1", "sin^-1", "cos^-1", "log"]
    keyWords = ["exit", "settings", "calculator", "help", "printall"]
    acceptable = False
    inputType = False

    # Check if number first
    try:
        if x == "ans" or x == "preans":
            acceptable = True
            inputType = "Number"
            return acceptable, inputType

        num = float(x)
        acceptable = True
        inputType = "Number"
        return acceptable, inputType

    except:
        pass
    
    # Check if symbol 
    if str(x) in symbolInputs:
        acceptable = True
        inputType = "Symbol"


    # Check If it is a Mathematical phrase
    if str(x) in wordInputs:
        acceptable = True
        inputType = "Math Word"
    
    # Check if it is a key word 
    elif str(x) in keyWords:
        acceptable = True
        inputType = "Key Word"

    return acceptable, inputType

def calculate():
    global previousAnswers
    symbol = True
    y = True
    while y:
        print("\nNow you are in the calculator")
        print("Input your operation and then input your numbers.")
        x = input("\n Input your operation: ")
        acceptable, inputType = checkInput(x)
        if acceptable and inputType == "Math Word" or inputType == "Symbol":
            symbol = x
            y = False
        elif acceptable and inputType == "Key Word":
            if x == "exit":
                exit()
            elif x == "settings":
                settings()
            elif x == "help":
                helper()
            elif x =="printall":
                print("\n\n These are the previous answers")
                print("You can access these values by typing Ans and PreAns")
                for c in previousAnswers:
                    print("\t ", c)
        else:
            print("Your answer was not accepted. Type help for help.")

    if symbol == '+':
        print("\n You chose Addition")
        print("\n Enter your first Number")
        first = getInput("Number")
        print("\n Enter your second Number")
        second = getInput("Number")
        answer = float(first) + float(second)
        displayAnswer(answer)

    elif symbol == '-':
        print("\n You chose Subtraction")
        print("\n Enter your first number")
        print("first nuber - second number")
        first = getInput("Number")
        print("\n Now enter your second number.")
        print(first, " - second number")
        second = getInput("Number")
        answer = float(first) - float(second)
        displayAnswer(answer)


    elif symbol == '*':
        print("\n You chose Multiplication")
        print("\n Enter your first number")
        first = getInput("Number")
        print("\n Now enter your second number.")
        second = getInput("Number")
        answer = float(first) * float(second)
        displayAnswer(answer)


    elif symbol == '/':
        print("\n You chose Division")
        print("\n Enter your first number")
        print("first nuber / second number")
        first = getInput("Number")
        print("\n Now enter your second number.")
        print(first, " / second number")
        second = getInput("Number")
        if second != 0:
            answer = float(first) / float(second)
            displayAnswer(answer)
        else:
            print("Division by zero doesn't work")
    elif symbol == '^':
        print("\n You chose Exponents")
        print("\n Enter your base number")
        first = getInput("Number")
        print("\n Now enter your the power.")
        second = getInput("Number")
        answer = mt.pow(float(first), float(second))
        displayAnswer(answer)

    elif symbol == '!':
        print("\n You chose Factorial.")
        print("Enter the number you would like to do the factorial of")
        num = getInput("Number")
        if int(num) < 0:
            print("Factorial doesn't exist")
        else:
            factorial = 1
            for i in range(1,int(num) + 1):
                factorial = factorial*i
            if int(num) == 0:
                factorial = 1
            displayAnswer(factorial)
    elif symbol == '|':
        print("\n\nYou chose Absolute Value")
        print("Please enter the value you would like to calculate")
        val = getInput("Number")
        try:
            displayAnswer(abs(val))
        except:
            pass
    
    elif symbol == '%':
        print("\n\n You chose the Remainder Function")
        print("Enter the numbers you would like to calculate")
        print("\n Enter your first number")
        print("first nuber / second number")
        first = getInput("Number")
        print("\n Now enter your second number.")
        print(first, " / second number")
        second = getInput("Number")
        if second != 0:
            answer = float(first) % float(second)
            displayAnswer(answer)
        else:
            print("Division by zero doesn't work")
    elif symbol == "sin":
        print("\n You chose Sin")
        print("\n Enter your Angle. \n You can change this calculator to degree or radian mode. By default it is set to radian mode.")
        angle = getInput("Number")    
        try:    
        	answer = mt.sin(angle)
        except:
            print("This function does not work for this value.")
        displayAnswer(answer, True)
    elif symbol == "cos":
        print("\n You chose Cos")
        print("\n Enter your Angle. \n You can change this calculator to degree or radian mode. By default it is set to radian mode.")
        angle = getInput("Number")    
        try:    
        	answer = mt.cos(angle)
        except:
            print("This function does not work for this value.")
        displayAnswer(answer, True)
    elif symbol == "tan":
        print("\n You chose Tan")
        print("\n Enter your Angle. \n You can change this calculator to degree or radian mode. By default it is set to radian mode.")
        angle = getInput("Number")    
        try:    
        	answer = mt.tan(angle)
        except:
            print("This function does not work for this value.")
        displayAnswer(answer, True)
    elif symbol == "sin^-1":
        print("\n You chose Sin^-1")
        print("\n Enter your Angle. \n You can change this calculator to degree or radian mode. By default it is set to radian mode.")
        angle = getInput("Number")    
        try:    
        	answer = mt.asin(angle)
        except:
            print("This function does not work for this value.")
        displayAnswer(answer, True)
    elif symbol == "cos^-1":
        print("\n You chose Cos^-1")
        print("\n Enter your Angle. \n You can change this calculator to degree or radian mode. By default it is set to radian mode.")
        angle = getInput("Number")    
        try:    
        	answer = mt.acos(angle)
        except:
            print("This function does not work for this value.")
        displayAnswer(answer, True)
    elif symbol == "tan^-1":
        print("\n You chose Tan^-1")
        print("\n Enter your Angle. \n You can change this calculator to degree or radian mode. By default it is set to radian mode.")
        angle = getInput("Number")
		
        try:    
        	answer = mt.atan(angle)
        except:
            print("This function does not work for this value.")

        displayAnswer(answer, True)
    elif symbol == "log":
        print("\n You chose log.")
        print("Enter the Value")
        print("Example: log ?")
        val = getInput("Number")
        print("Example: log ", val)
        print("            ?  ")
        print("\n Enter the base.")
        base = getInput("Number")
        answer = mt.log(float(val), float(base))
        try:    
        	answer = mt.atan(angle)
        except:
            print("This function does not work for this value.")
        displayAnswer(answer)
    
def getInput(targetInputType="Number"):
    global previousAnswers
    b = 0
    a = True
    while a:
        b = input("Enter your input: ").strip().lower()
        acceptable, inputType = checkInput(b)
        
        if acceptable and inputType == targetInputType:
            a = False
        elif acceptable and inputType == "Key Word":
            if b == "exit":
                mode = "exit"
                exit()
            elif b == "settings":
                mode = "settings"
                settings()
            elif b == "help":
                mode = "help"
                helper()
            elif b == "calculator":
                mode = "calculator"
                calculate()
            elif b =="printall":
                print("\n\n These are the previous answers")
                print("You can access these values by typing Ans and PreAns")
                for c in previousAnswers:
                    print("\t ", c)
                
                
        else:
            print("Input not valid. Try Again. ")
    if targetInputType == "Number":
        try:
            if b == "ans":
                b = previousAnswers[len(previousAnswers)-1]
            elif b == "preans":
                b = previousAnswers[len(previousAnswers)-2]
            elif b == "e":
                b = mt.e
            elif b == "pi":
                b = mt.pi
            elif b == "tau":
                b = mt.tau
            return float(b)
        except:
            return float(b)


def settings():
    print("\n\nYou are in settings now.")
    b = 0
    print("\nCurrently there are only 2 settings")
    print("To access them type radian, degree, or round")
    print("Otherwise you can type exit in order to leave this screen")
    print("\n\nYou can change the angle mode by typing degree or radians.")
    print("You can also type round to change the amount of digits the calculator rounds to.")
    a = True
    while a:
        b = input("Enter your input: ").strip().lower()
        acceptable, inputType = checkInput(b)
        possibleWords = ["radian", "degree", "round"]
        if b in possibleWords:
            a = False
        elif inputType == "Key Word":
            if b == "exit":
                mode = "exit"
                exit()
            elif b == "settings":
                mode = "settings"
                settings()
            elif b == "help":
                mode = "help"
                helper()
            elif b == "calculator":
                mode = "calculator"
                calculate()
            elif b =="printall":
                print("\n\n These are the previous answers")
                print("You can access these values by typing Ans and PreAns")
                for c in previousAnswers:
                    print("\t ", c)
                
                
        else:
            print("Input not valid. Try Again. ")
    global units, roundTo
    if b == "radian":
        print("\n Ok we changed the mode to radians.")
        units = "radian"
    elif b == "degree":
        print("\n Ok we changed the mode to degrees")
        units = "degree"
    elif b == "round":
        print("\n Enter the number of places you would like to rount to")
        num = getInput()
        roundTo = num
        print("We changed the rounding place to ", roundTo)


def displayAnswer(answer, checkIfRadian=False):
    global roundTo, units, previousAnswers
    displayAnswer = answer
    previousAnswers.append(answer)
    if checkIfRadian and units == "degree":
        displayAnswer = mt.degrees(displayAnswer)
    
    displayAnswer = round(displayAnswer, int(roundTo))
    print("\n\nYour answer is ", displayAnswer)

def exit():
    input("Click Enter to Exit")
    sys.exit(0)

def helper():
    symbolInputs = ['+', '-','/','*', '^', '!', '(',')', '|', '%']
    wordInputs = ["sin", "cos", "tan", "tan^-1", "sin^-1", "cos^-1", "log"]
    keyWords = ["exit", "settings", "calculator", "help"]
    
    print("\n\nThis is the help screen for this calculator.")
    print("""
    You can input symbols or key words in this calculator. 
    They will be listed below. In the calculator, you can use keywords
    such as pi, ans, e, PreAns, and Tau. This calculator records
    all of your answers. You can print all of the answers by typing
    printall in the calculator.

    Note: When you are dealing with certain functions, make sure 
    that the value exists before inputting into that calculator.
    """)

    print("These are symbols that you can use")
    for a in symbolInputs:
        print("\t ", a)
    
    print("\n These are some expressions that are words")
    for b in wordInputs:
        print("\t ", b)

    print("\n These are possibe keywords")
    for c in keyWords:
        print("\t ", c)

def main():
    print("\tWelcome to the Calculator!")
    print("You can set the mode to either caculator mode or settings mode.")
    print("You can check the default settings by typing settings.")
    mode = "ready"
    while mode != "quit":
        if mode == "ready":
            
            print("\n\nYou are in the ready screen. You can either go into calculator or settings mode from here.")
            getInput()
        
        elif mode == "calculator":
            calculate()
        
        elif mode == "settings":
            settings()


if __name__ == "__main__":
    main()



