import re
from tkinter import E

from numpy import true_divide

# without regex using eval
def regexCalcEval(syn):
    syn_list = syn.split(' ')
    

    try:
        res = eval(syn)
        return res
    except:
        return "Invalid syntax"


def regexCalcAlgo(syn):
    syn_list = list(syn.strip(' '))
    syn_list = [item for item in syn_list if item!=' ']

    if not syn_list or len(syn_list) <= 2: return "Invalid syntax"

    syn_list = syn.split(' ')

    f_t,res = True, 0
    while syn_list:
        if f_t:
            try:
                num1 = syn_list.pop(0)
                op = syn_list.pop(0)
                num2 = syn_list.pop(0)
                res = eval(f"{num1}{op}{num2}")
            except:
                return "Invalid syntax"
            f_t = False
        op = syn_list.pop(0)
        try:
            numnext = int(syn_list.pop(0))
        except:
            return "Invalid syntax"
        if op == "+":
            res = res + numnext
        elif op == "-":
            res = res - numnext
        elif op == "/":
            res = res / numnext
        elif op == "*":
            res = res * numnext
        else: return "Invalid syntax"

    return res


t0 = regexCalcAlgo('')
t1 = regexCalcAlgo("1 + ")
t2 = regexCalcAlgo("1 + 12 - 12 + 1 + 2 + 2")

print(t0,t1,t2)













