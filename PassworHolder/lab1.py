from scipy import *
from scipy.optimize import linprog

obj = [1,1]

left_hand_side = [[1,0],[0,1]]
right_hand_side = [6,2]

bounds = [(0, float("inf")),(0, float("inf"))]

optimization = linprog(c=obj, A_ub=left_hand_side, b_ub=right_hand_side, bounds=bounds, method="highs-ds")
print(optimization.fun)
print(optimization.x)