import numpy as np
import matplotlib.pyplot as plt
# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# output dataset
y = np.array([[0,1,1,0]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

err1 = []
err2 = []
for iter in range(10000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    # how much did we miss?
    l2_error = y - l2
    l2_delta = l2_error*nonlin(l2, deriv=True)

    l1_error = np.dot(l2_delta,syn1.T)
    l1_delta = l1_error*nonlin(l1, deriv=True)

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1

    err1.append(np.sqrt(np.mean(np.square(l1_error))))
    err2.append(np.sqrt(np.mean(np.square(l2_error))))

    if np.sqrt(np.mean(np.square(l2_delta))) < 0.0003:
        pass

    # update weights
    syn0 += np.dot(l0.T, l1_delta)
    syn1 += np.dot(l1.T, l2_delta)

def plot_err(err):
    y=err
    x = np.linspace(0, 10, len(y))
    plt.scatter(x, y, marker='o')
    plt.show()

print ("Output After Training:")
print(l2_error)
plot_err(err2)
