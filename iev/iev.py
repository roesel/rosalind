# situation  chance  avg_exp_w_2_offspr
# AA-AA -> 1    -> 2
# AA-Aa -> 1    -> 2
# AA-aa -> 1    -> 2
# Aa-Aa -> 0.75 -> 1.5
# Aa-aa -> 0.5  -> 1
# aa-aa -> 0    -> 0
p = [2, 2, 2, 1.5, 1, 0]
inp = '19540 17604 16265 16514 18972 19184'
inp = [int(i) for i in inp.split(' ')]
exp = sum([a*b for a,b in zip(inp,p)])

print(exp)
