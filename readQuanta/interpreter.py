import sys
import json
sys.path.insert(0, 'QuantaLang/core_lib')

from var import *
from probe import *
ARITHMATIC_OPERATORS = ['+', '-', '*', '/', '%', '**', '//']
COMPARISON_OPERATORS = ['==', '!=', '>', '<', '>=', '<=']
LOGICAL_OPERATORS = ['and', 'or', 'not']
GATE_OPERATORS = ['HGATE', 'XGATE', 'YGATE', 'ZGATE', 'SGATE', 'CGATE', 'CZGATE', 'SWAP', 'CUGATE', 'CYGATE']
QUANTUM_OPERATORS = ['MEASURE', 'RESET', 'INITIALIZE', 'QFT', 'SHOR']
CONTROL_FLOW = ['if', 'elif', 'else', 'for', 'while', 'break', 'continue', 'return']
DATA_TYPES = ['int', 'float', 'complex', 'str', 'bool', 'list', 'tuple', 'dict', 'set', 'None', 'Qubit']
KEYWORDS = ['import', 'from', 'as', 'class', 'def', 'return', 'pass', 'break', 'continue', 'if', 'elif', 'else', 'for', 'while', 'in', 'is', 'not', 'and', 'or', 'True', 'False', 'None', 'try', 'except', 'finally', 'raise', 'assert', 'lambda', 'with', 'yield', 'global', 'nonlocal', 'del', 'async', 'await']


interpretationFile = open("ipt.json", "w")

if __name__ == '__main__':
    i = 1
    while True:
        get = input(f"{i}: ")
        i+=1
        if get == "exit":
            break
        elif get[0:3] == 'var':
            get = get[4:]
            if get[0:3] == 'int':
                idv = get[4:].split('=')
                idv[0] = idv[0].strip()
                var.int(int(idv[1]))
            elif get[0:5] == 'float':
                get = get[6:]
                print(var.float(float(get)))
            elif get[0:6] == 'complex':
                get = get[7:]
                get = get.split(',')
                print(var.complex(float(get[0]), float(get[1])))
            elif get[0:3] == 'str':
                get = get[4:]
                print(var.str(get))
            elif get[0:4] == 'bool':
                get = get[5:]
                print(var.bool(bool(get)))
            elif get[0:4] == 'list':
                get = get[5:]
                get = get.split(',')
                print(var.list(get))
            elif get[0:4] == 'dict':
                get = get[5:]
                get = get.split(',')
                print(var.dict(get))
            else:
                print("Invalid data type")
        elif get[0:5] == 'probe':
            Probe.Probe(get[6:])
        else:
            pass
