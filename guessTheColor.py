import numpy as np
import os
# from numpy import random


def NN(m1, m2, w1, w2, b):
    z = m1*w1 + m2*w2 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1 + np.exp(-x))


phrases = ['seems like this', 'I guess', 'I think', 'possibly', 'Looks like', 'guessing ...']

data = [[3, 1.5, 1], [2, 1, 0], [4, 1.5, 1], [3, 1, 0], [3.5, 0.5, 1], [2, 0.5, 0], [5.5, 1, 1], [1, 1, 0]]

rand_data = data[int(np.random.randint(len(data)))]

m1 = rand_data[0]
m2 = rand_data[1]
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

prediction =  NN(m1, m2, w1, w2, b)
prediction_text = ['blue', 'red'][int(np.round(prediction))]
phrase = np.random.choice(phrases) + " " + prediction_text
print(phrase)

o = os.system('say ' + phrase)

print("it's really " + ["blue", "red"][rand_data[2]])