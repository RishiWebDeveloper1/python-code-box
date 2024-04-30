import os

R_D = "D:\\"
F_T_S = ""

for R_P,D,F in os.walk(R_D):
    if (F_T_S in F):
        F_P = os.path.join(R_D,R_P,F_T_S)

print(F_P)