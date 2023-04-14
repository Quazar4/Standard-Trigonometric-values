# 0, 30, 45, 60, 90
sin = {"sin 0": "0", "sin 30": "1/2", "sin 45": "1/√2", "sin 60": "√3/2", "sin 90": "1"}
cos = {"cos 0": "1", "cos 30": "√3/2", "cos 45": "1/√2", "cos 60": "1/2", "cos 90": "0"}
tan = {"tan 0": "0", "tan 30": "1/√3", "tan 45": "1", "tan 60": "√3", "tan 90": "Infinity(1/0)"}
cosec = {"cosec 0": "Infinity(1/0)", "cosec 30": "2", "cosec 45": "√2",
         "cosec 60": "2/√3", "cosec 90": "1"}
sec = {"sec 0": "1", "sec 30": "2/√3", "sec 45": "√2", "sec 60": "2", "sec 90": "Infinity(1/0)"}
cot = {"cot 0": "Infinity(1/0)", "cot 30": "√3", "cot 45": "1", "cot 60": "1/√3", "cot 90": "0"}


a = int(input("Press 1 to continue or press 2 to quit: "))

while(True):
    if (a == 1):

        x = str(input("Enter a value: "))

        # Sine ---------------------------------
        if(x == "sin 0"):
            print(sin["sin 0"])

        elif(x == "sin 30"):
            print(sin["sin 30"])

        elif(x == "sin 45"):
            print(sin["sin 45"])

        elif(x == "sin 60"):
            print(sin["sin 60"])

        elif(x == "sin 90"):
            print(sin["sin 90"])

        # Cosine ---------------------------------
        elif (x == "cos 0"):
            print(cos["cos 0"])

        elif (x == "cos 30"):
            print(cos["cos 30"])

        elif (x == "cos 45"):
            print(cos["cos 45"])

        elif (x == "cos 60"):
            print(cos["cos 60"])

        elif (x == "cos 90"):
            print(cos["cos 90"])

        # Tangent ---------------------------------
        elif (x == "tan 0"):
            print(tan["tan 0"])

        elif (x == "tan 30"):
            print(tan["tan 30"])

        elif (x == "tan 45"):
            print(tan["tan 45"])

        elif (x == "tan 60"):
            print(tan["tan 60"])

        elif (x == "tan 90"):
            print(tan["tan 90"])

        # Cosecant ---------------------------------
        elif (x == "cosec 0"):
            print(cosec["cosec 0"])

        elif (x == "cosec 30"):
            print(cosec["cosec 30"])

        elif (x == "cosec 45"):
            print(cosec["cosec 45"])

        elif (x == "cosec 60"):
            print(cosec["cosec 60"])

        elif (x == "cosec 90"):
            print(cosec["cosec 90"])

        # Secant ---------------------------------
        elif (x == "sec 0"):
            print(sec["sec 0"])

        elif (x == "sec 30"):
            print(sec["sec 30"])

        elif (x == "sec 45"):
            print(sec["sec 45"])

        elif (x == "sec 60"):
            print(sec["sec 60"])

        elif (x == "sec 90"):
            print(sec["sec 90"])

        # Cotangent ---------------------------------
        elif (x == "cot 0"):
            print(cot["cot 0"])

        elif (x == "cot 30"):
            print(cot["cot 30"])

        elif (x == "cot 45"):
            print(cot["cot 45"])

        elif (x == "cot 60"):
            print(cot["cot 60"])

        elif (x == "cot 90"):
            print(cot["cot 90"])

        elif (x == "2"):
            break

        else:
            print("Does not exist")

    elif(a == 2):
        break

    else:
        print("Not an option")
        a = int(input("Press 1 to continue or press 2 to quit: "))
