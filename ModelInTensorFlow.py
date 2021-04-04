##Optimizer in TF
#let's define f as a square of variable x:
import numpy as np
import tensorflow as tf

tf.reset_default_graph()
x = tf.get_variable("x", shape = (), dtype = tf.float32)
f = x ** 2

#let's say we ant to minimize the value of f w.r.t x:
optimizer = tf.train.GradientDescentOptimizer(0.1)
step = optimizer.minimize(f, var_list = [x])

##Trainable variables
#u dont have to specify all the optimized variables:

step = optimizer.minimize(f, var_list = [x])
step = optimizer.minimize(f)

#Because all variables are trainable by default:
x = tf.get_variable("x", shape = (), dtype = tf.float32)
x = tf.get_variable("x", shape = (), dtype = tf.float32, trainable = True)

#u can get all of them
	tf.trainable_variables()

"""
output:
[<tf.Variable'x:0'shape=()dtype=float32_ref>]
"""


##MAKING GRADIENT DESCENT STEPS
#Now e nned to create a session and initialize variables:
s = tf.InteractiveSession()
s.run(tf.global_variables_initializer())

#we are ready to make 10 gradient descent steps:
for i in range(10):
	_, curr_x, curr_f = s.run([step, x, f])
	print(curr_x, curr_f)

"""
output:
	0.448929 0.314901
	0.359143 0.201537
	...              -----> GD step is already applied to x
	0.0753177 0.00886368
	0.0602542 0.00567276
"""

##LOGGING WITH TF.PRINT
#we can evaluate tensors and print em like this:
for i in range(10):
	_, curr_x, curr_f = s.run([step, x, f])
	print(curr_x, curr_f)
#or we can pass our tensor of interest thro tf.print
...
f = x ** 2
f = tf.Print(f, [x, f], "x, f:")
...
for i in range(10):
	s.run([step,f])

#this is Jupyter Server stdout.Not visible in the Notebook!

##LOGGING WITH TENSORBOARD
#we can ass so called summaries:
tf.summary.scalar('curr_x', x)
tf.summary.scalar('curr_f', f)
summaries = tf.summary.merge_all()

#this is ho we log these summaries:
s = tf.InteractiveSession()
summary_writer = tf.summary.FileWriter("logs/1", s.graph)   #run number
s.run(tf.global_variable_initializer())
for i in range(10):
	_, curr_summaries = s.run([step, summaries])
summary_writer.add_summary(curr_summaries, i)
summary_writer.flush()

##LAUNCHING TENSORBOARD
#now u can launch TensorBoard via bash:
tensorboard --logdir=./logs
#and open http://127.0.0.1:6006 in ur browser

#VISUALIZING GRAPH in TENSORBOARD
#you can see that gradients computation is a part of our graph

#SOLVING A LINEAR REGRESSION
#Let's generate a model dataset:
N = 1000
D = 3
x = np.random.random((N, D))
w = np.random.random((D, 1))
y = x @ w + np.random.randn(N,1) * 0.20


#We will need placeholders for input data:
tf.reset_default_graph()
features = tf.placeholder(tf.float32, shape = (None, D))
target = tf.placeholder(tf.float32, shape = (None, 1))

#this is how we make predictions:
weights = tf.get_variable("w", shape = (D, 1), dtype = tf.float32)
predictions = features @ weights

#and define our loss:
loss = tf.reduce_mean((target - predictions) ** 2)

#and optimizer:
optimizer = tf.train.GradientDescentOptimizer(0.1)
step = optimizer.minimize(loss)

