# Making a NN from scratch

Done as part of deep learning course, week 3   
>Intialize values for weights and biases randomly   
the dimentions of each weights between layers will be (no of neurons in next layer) * (no of neurons in previous layer) or even the other way round, you can take transpose to match them...


>then there is forward pass where   
z = W.X + b
a = activation(z)  
for all the layers

>next this is to calculate the cost that is  
J=(−1/m) * ∑(i=0 to m) (y(i)log(a[](i))+(1−y(i))log(1−a[](i)))  
this is for all the layers that is when we sum , we get for all the layers...




>Next is the BACKPROPAGATION STEP  
Now take the derivative of weights and biases.
Use this formula to update the weights and biases- 
X = X - (learning_date * X_derivative ) 
formula to derivatives----  
![derivatives formula](grad1.png)

>Final step is to update the parameters that we got using backprop step,  we keep doing it untill value of cost function is sufficiently low.


And that's it , a NN model is done.