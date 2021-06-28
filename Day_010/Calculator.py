import CalculatorData as C


def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if not b == 0:
        return a / b
    else:
        print(C.zeroDivisionError)
        return "ERROR"
def mod(a, b):
    if not b == 0:
        return a % b
    else:
        print(C.zeroDivisionError)
        return "ERROR"

calcDic = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": mod
}


def Calc(data):
    #return the appropriate result for the given operator
    data["res"] = calcDic[data['op']](data['n1'], data['n2'])
    print(f"{data['n1']} {data['op']} {data['n2']} = {data['res']}")
    return data

def startCalc(data):
    """Get the data needed for the first calculation"""
    data['n1'] = float(input(C.askNumber1Message))
    data['op'] = input(C.askOperatorMessage)
    data['n2'] = float(input(C.askNumber2Message))
    return Calc(data)

def main():
    print(C.pic)
    data = C.initData   
    data = startCalc(data)
    while (not data['res'] == "ERROR") and (input(C.continueOperations) == "y") :
        temp = data["res"]
        data = C.initData
        data["n1"] = temp
        data["op"] = input(C.askOperatorMessage)
        data["n2"] = float(input(C.askNumber2Message))
        Calc(data)
        
            
if __name__ == "__main__":
    main()