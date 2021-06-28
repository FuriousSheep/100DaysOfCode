pic = """
                       CCCCCC       AA       L             CCCCCC
|---|---|---|---|    CCC           A  A      L           CCC     
| + | - | / | * |   CCC           A    A     L          CCC      
|---|---|---|---|   CCC           A    A     L          CCC      
| % | 7 | 8 | 9 |   CC           A      A    L          CC       
|---|---|---|---|   CC           A      A    L          CC       
| . | 4 | 5 | 6 |   CCC          AAAAAAAA    L          CCC      
|---|---|---|---|   CCC         AA      AA   L          CCC      
| 0 | 1 | 2 | 3 |    CCC        AA      AA   L           CCC     
|---|---|---|---|      CCCCCC   AA      AA   LLLLLLLL      CCCCCC
"""

initData = {
        "n1": 0,
        "n2": 0,
        "op": "",
        "res": 0
    }

askNumber1Message = "Enter the first number:\n"
askNumber2Message = "Enter the second number:\n"
askOperatorMessage = "Enter the operator:\n"
zeroDivisionError = "You can't divide by zero!\n"
continueOperations = "Do you want to continue the operations with this result? (y) (n)"