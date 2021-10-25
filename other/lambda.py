def exp(x):
    return lambda y: f"x: {x}  y: {y}"


exp_3 = exp(3)
exp_4 = exp(4)

print(f"exp_3(): {exp_3(42)}  exp_4(): {exp_4(47)}")
