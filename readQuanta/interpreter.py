
ARITHMATIC_OPERATORS = ['+', '-', '*', '/', '%', '**', '//']
COMPARISON_OPERATORS = ['==', '!=', '>', '<', '>=', '<=']
LOGICAL_OPERATORS = ['and', 'or', 'not']
GATE_OPERATORS = ['HGATE', 'XGATE', 'YGATE', 'ZGATE', 'SGATE', 'CGATE', 'CZGATE', 'SWAP', 'CUGATE', 'CYGATE']
QUANTUM_OPERATORS = ['MEASURE', 'RESET', 'INITIALIZE', 'QFT', 'SHOR']
CONTROL_FLOW = ['if', 'elif', 'else', 'for', 'while', 'break', 'continue', 'return']
DATA_TYPES = ['int', 'float', 'complex', 'str', 'bool', 'list', 'tuple', 'dict', 'set', 'None', 'Qubit']
KEYWORDS = ['import', 'from', 'as', 'class', 'def', 'return', 'pass', 'break', 'continue', 'if', 'elif', 'else', 'for', 'while', 'in', 'is', 'not', 'and', 'or', 'True', 'False', 'None', 'try', 'except', 'finally', 'raise', 'assert', 'lambda', 'with', 'yield', 'global', 'nonlocal', 'del', 'async', 'await']


i = 1
while True:
    get = input(f"{i}: ")
    i+=1
    if get == "exit":
        break
    
    else:
        pass
