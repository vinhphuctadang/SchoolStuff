import tensorflow as tf
import matplotlib.pyplot as plt

W = tf.Variable([[1.0],[2.0]]) # weights
b = tf.Variable(3.0) # bias

# Aggeration function
def g(x):
    return tf.matmul(x,W)+b
# Predict using 'sigmoid' activation
def predict(x):
    return tf.sigmoid(g(x))
# Loss function (using polynomial loss function)
def loss(y_pred, y_actual):
    return tf.reduce_mean(tf.square(y_pred-y_actual))
'''
Train function where:
	X: Shape(n,2): Training attribute
	Y: Labels(n,1): Training label
'''
def train(X, Y, rate):
    with tf.GradientTape() as t:
        current_loss = loss(Y, predict(X))
        # print(current_loss)
        dW, db = t.gradient(current_loss, [W,b])
        W.assign_sub(rate*dW)
        b.assign_sub(rate*db)
        return current_loss.numpy()

'''
Render function, where:
	axLoss: axes of showing loss
	lossValues: 1-D list: values of loss through epoches
	axData: axes of showing data and prediction values
	X: Shape(n,2): Training attribute
	Y: Labels(n,1): Training label
	pred: Labels(n,1): Predict label
'''

def doRender(axLoss, lossValues, axData, X, Y, pred):

    axData.cla()
    axLoss.cla()
    axData.set_title('Data presentation')
    axLoss.set_title('Loss through epoches')
    axLoss.set_xlabel('Epoch')
    axLoss.set_ylabel('Loss')
    for _ in range(len(Y)):
        axData.scatter(X[_][0], X[_][1], Y[_][0], c='b', marker='o')
    for _ in range(len(Y)):
        axData.scatter(X[_][0], X[_][1], pred[_][0], c='g', marker='x')

    
    axLoss.set_ylim(0, 1)
    axLoss.set_xlim(0, epoch)
    axLoss.plot(lossValues)
    plt.pause(0.01)

'''
Prepair data, where X contains attributes, Y contains labels (which is in {0,1})
'''
X = [
    [0., 0.],
    [0., 1.],
    [1., 0.],
    [1., 1.]
]
Y = [[0], [0], [0], [1]]


'''
Prepair for plotting data
'''
(axData, axLoss) = plt.subplot(121, projection='3d'), plt.subplot(122)

# Now render initial values
for _ in range(len(Y)):
    axData.scatter(X[_][0], X[_][1], Y[_][0], marker='o')
plt.show(block=False)

'''
Training config
'''
epoch = 5000
learning_rate = 0.3

'''
Visualization config
'''
renderEvery = 20
lossValues = []

'''
Now, go train and paint training result periodically
'''
for ep in range(epoch):
    lossValues.append(train(X, Y, learning_rate))
    if ep % renderEvery == 0:
        pred = predict(X).numpy()
        doRender(axLoss, lossValues, axData, X, Y, pred)
'''
Call rendering for the last frame :)
'''
doRender(axLoss, lossValues, axData, X, Y, pred)

plt.ioff()
plt.show()

'''
Print trainnig result
'''
print('Predict values:\n', predict(X).numpy(), sep='')
