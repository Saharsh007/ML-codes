
# How to reduce variance?  -> Regularization

so we introduce another parameter lambda which penalizes the value of W to reduce overfitting,   
it can be thought of like this -   
z = w*a +b   
so we increase lambda  which inturn decreases w which decreases z and that shifts  it from exponential to somewhat linear for all layers.   
which is ultimatly reducing overfitting.


**What is L2-regularization actually doing?**:

L2-regularization relies on the assumption that a model with small weights is simpler than a model with large weights. Thus, by penalizing the square values of the weights in the cost function you drive all the weights to smaller values. It becomes too costly for the cost to have large weights! This leads to a smoother model in which the output changes more slowly as the input changes. 


**How to do it in code?**  
Take a new martix D and initialize it randomly as 0 with prob (1-keep_prob) or 1 with probability (keep_prob). Now multiply D and A(A*D) and scale using keep_prob.



# DropOut - another regularization technique

randomly zeroing out some hidden units to avoid overfitting.


# Data Augmentation

Making more training data by manipulating the image such as rotating , flipping , tilting , removing R or G or B from the image.
