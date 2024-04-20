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
        elif get[0:3] == 'let':
            get = get[4:]
            kID = get.index('=')
            varDats = get[0:kID]
            varValue = get[kID+1:]
            typeDat = varDats.split(" ")
            print(varValue)
            print(typeDat)
            method = getattr(var, typeDat[0])
            init = method(typeDat[1], varValue)
           

        elif get[0:5] == 'probe':
            print(Probe.Probe(get[5:]))
        else:
            pass
