# Bias
```diff
+ The inability of a machine learning algorithm to capture the true relationship is called bias.   
```
- high  bias = low performance on train set , low on dev too = underfitting  

- low bias  = good performance on train set   

# variance
```diff
+ The difference in fits between datasets is called variance
```
- high variance  = best performance on train set and very bad on dev = overfitting
-  Low variance  = better performance on dev set


# dev set

- used for hyper parameter tuning , gets biased after tuning

# train set

 - unbiased performance status of model.


# How to reduce variance?  -> Regularization

so we introduce another parameter lambda which penalizes the value of W to reduce overfitting,   
it can be thought of like this -   
z = w*a +b   
so we increase lambda  which inturn decreases w which decreases z and that shifts  it from exponential to somewhat linear for all layers.   
which is ultimatly reducing overfitting.



# DropOut

randomly zeroing out some hidden units to avoid overfitting.