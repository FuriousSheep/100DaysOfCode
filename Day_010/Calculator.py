import CalculatorData as C

def Calc(data):
    if data['op'] == "+":
        data['res'] = data['n1'] + data['n2']
    elif data['op'] == "-":
        data['res'] = data['n1'] - data['n2']
    elif data['op'] == "*":
        data['res'] = data['n1'] * data['n2']
    elif data['op'] == "/":
        if not data['n2'] == 0:
            data['res'] = data['n1'] / data['n2']
        else:
            print(C.zeroDivisionError)
    elif data['op'] == "%":
        if not data['n2'] == 0:
            data['res'] = data['n1'] % data['n2']
        else:
            print(C.zeroDivisionError)
    print(f"{data['n1']} {data['op']} {data['n2']} = {data['res']}")
    return data

def startCalc(data):
    data['n1'] = float(input(C.askNumber1Message))
    data['op'] = input(C.askOperatorMessage)
    data['n2'] = float(input(C.askNumber2Message))
    return Calc(data)

def main():
    print(C.pic)
    data = C.initData   
    data = startCalc(data)
    while (input(C.continueOperations) == "y"):
        temp = data["res"]
        data = C.initData
        data["n1"] = temp
        data["op"] = input(C.askOperatorMessage)
        data["n2"] = float(input(C.askNumber2Message))
        Calc(data)
        
            
if __name__ == "__main__":
    main()