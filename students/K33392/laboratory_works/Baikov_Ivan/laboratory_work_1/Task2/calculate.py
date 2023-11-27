from math import sqrt

def calculate(cath1, cath2=None, hyp=None):
    if not (cath1 or hyp) or (hyp and cath1 >= hyp):
        return "Invalid input"
    if not cath2:
        return sqrt(hyp ** 2 - cath1 ** 2)
    if not hyp:
        return sqrt(cath1 ** 2 + cath2 ** 2)
    return "Something went wrong"