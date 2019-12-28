# Understanding Optimization
In Machine Learning, the goal is to optimize the weights of the model such that the error between the output given by our model aka the predictions and the groud truth aka labels/correct value for the input is minimum. To minimize this error, we use optimization algorithms which take function(called cost function) and tries to minimize the that function by altering the weights of the model.
Their are many optimization algorithms, but we are going to understand the process of optimization by the simplest of all <b>Gradient Decent</b>

## Gradient Decent
To have an intuitive idea about how Gradient Decent work, Imagine you're at the top of the highest peak in a park. Your friends have dared you to reach the lowest point in the park (assuming their is only one lowest point in whole park) blindfolded from the top. You accepted their challenge and you are ready to begin at the top of the peak. Their are two ways in which you can proceed:

- Naive Way: You start moving in the direction you feel is correct without much thought. You may reach the lowest point, if you are lucky, but their are no guarentees.
- Strategic Way: You hover your feet all around yourself and feel where is the lowest point around you in one step. You take a step in that direction and repeat the process until everything around you feel at the same heighjt and stop at that point. This way you are guarenteed to reach the lowest point.

The second alternative is known as Gredient Decent. The algorithm takes one step at a time in the direction of most negative gradient, the lowest point around current position along the cost function and repeat the process.

### Cost Function

In ML, cost functions are used to estimate how badly models are performing.Put simply, a cost function is a measure of how wrong the model is in terms of its ability to estimate the relationship between X and y.
The objective of a ML model, is to find weights that minimises the cost function.

<b>Mathematically</b>, Gradient descent is a first-order iterative optimization algorithm for finding the minimum of a function. To find a local minimum of a function using gradient descent, one takes steps proportional to the negative of the gradient (or approximate gradient) of the function at the current point.

In the jupyter notebook, you can see the algorithm in action and I highly encourage you to run the notebook on your own host machine or in Google Colab and start to experiment with different walues like learning rate, epochs or maybe you can also write your own function and optimize it.

### For Non-coders
Although I highly encourage you to start learning how to code, becuse according to me it gives you new ways to think about solving a problem. Anyways, for you guys specially i am currently creating a Simple GUI application that you can run on your system without installing anything extra and get the feel of experimenting with different values and observing their effects on the algorithm. Although you will not be able to define your own functions as Coders might do it.
The application is ready. Get ready Non-coders, you can play with ML too. Download link will be available soon.!!!!