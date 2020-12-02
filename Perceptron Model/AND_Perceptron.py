# AND Perceptron

import pandas as pd

def step(x):
    return 1 if x>1 else 0;


inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
weight0 = 0.5
weight1 = 0.5
bias = 0.4
outputs = []

for inp in inputs:
    y = (inp[0]*weight0 + inp[1]*weight1) + bias
    output = step(y)
    outputs.append([inp[0], inp[1], y, output])


df = pd.DataFrame(outputs, columns=['   Input 1', ' Input 2', ' Activation Output', 'Output',])
df.reset_index()
print(df)

