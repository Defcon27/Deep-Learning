# NOT Perceptron

import pandas as pd

def step(x):
    return 1 if x>1 else 0;


inputs = [(0), (1)]
weight0 = -2
bias = 1.1
outputs = []

for inp in inputs:
    y = (inp*weight0) + bias
    output = step(y)
    outputs.append([inp, y, output])


df = pd.DataFrame(outputs, columns=['Input', 'Activation Output', 'Output',])
print(df)

