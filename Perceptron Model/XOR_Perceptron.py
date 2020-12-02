# XOR Perceptron

import pandas as pd


def step(x):
    return 1 if x >= 1 else 0


def OR(input0, input1):
    weight0 = 1
    weight1 = 1
    bias = 0.1

    y = (input0*weight0+input1*weight1) + bias
    output = step(y)
    return output


def AND(input0, input1):
    weight0 = 0.5
    weight1 = 0.5
    bias = 0.4

    y = (input0*weight0 + input1*weight1) + bias
    output = step(y)
    return output


def NOT(input0):
    weight0 = -2
    bias = 1.1

    y = (input0*weight0) + bias
    output = step(y)
    output = step(y)
    return output




inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
outputs = []

for inp in inputs:
    hidden11 = AND(inp[0], inp[1])
    hidden12 = NOT(hidden11)
    hidden13 = OR(inp[0], inp[1])
    y = AND(hidden12, hidden13)
    output = step(y)    
    outputs.append([inp[0], inp[1], y, output])

df = pd.DataFrame(outputs, columns=['   Input 1', ' Input 2', ' Activation Output', 'Output',])
df.reset_index()
print(df)

