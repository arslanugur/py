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

