import numpy as np

bias = 1

def activation(value):
    if value >= 0:
        return 1
    else: 
        return 0
    
def neural_network(inputs,weights):
    return np.matmul(inputs,weights)

def func_or(x1,x2):
    weights = np.array([[1],[1],[-1]])
    inputs = np.array([x1,x2,bias])

    prediction = activation(neural_network(inputs,weights))
    print(str(x1)," v ",str(x2)," = ",str(prediction))

    return prediction

def func_and(x1,x2):
    weights = np.array([[1],[1],[-1.5]])
    inputs = np.array([x1,x2,bias])

    prediction = activation(neural_network(inputs,weights))
    print(str(x1)," ^ ",str(x2)," = ",str(prediction))

    return prediction

def func_not(x1):
    weights = np.array([[-1],[0]])
    inputs = np.array([x1,bias])

    prediction = activation(neural_network(inputs,weights))
    print("¬ ",str(x1)," = ",str(prediction))

    return prediction

def func_xor(a,b):
    prediction = func_and(func_not(func_and(a,b)),func_or(a,b))
    print(a," XOR ",b," = ",prediction)

### function checks

def checks():
    # OR
    print("\nOR\n")
    func_or(0,0)
    func_or(0,1)
    func_or(1,0)
    func_or(1,1)

    # AND
    print("\nAND\n")
    func_and(0,0)
    func_and(0,1)
    func_and(1,0)
    func_and(1,1)

    # NOT
    print("\nNOT\n")
    func_not(0)
    func_not(1)

#checks()

print("-"*90)
func_xor(0,0)
print("-"*90)
func_xor(0,1)
print("-"*90)
func_xor(1,0)
print("-"*90)
func_xor(1,1)