from data import get_data
import tensorflow as tf
# Parameters
learning_rate = 0.1
num_steps = 500
batch_size = 128
display_step = 100

list_words = get_data()

# Network Parameters
n_hidden_1 = 500 # 1st layer number of neurons
n_hidden_2 = 500 # 2nd layer number of neurons
num_input = len(list_words) # Bless data set size
num_classes = 2 # yes or no

# tf Graph input
X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, num_classes])

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([num_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, num_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([num_classes]))
}

# Create model
def neural_net(x):
    # Hidden fully connected layer with 500neurons
    layer_1 = th.tanh(tf.add(tf.matmul(x, weights['h1']), biases['b1']))
    # Hidden fully connected layer with 500 neurons
    layer_2 = tf.tanh(tf.add(tf.matmul(layer_1, weights['h2']), biases['b2']))
    # Output fully connected layer with a neuron for each class
    out_layer = tf.nn.softmax(tf.matmul(layer_2, weights['out']) + biases['out'])
    return out_layer