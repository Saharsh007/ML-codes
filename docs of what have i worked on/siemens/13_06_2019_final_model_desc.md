# Final Code for Model ready

so the whole project is divided into 3 parts   

### <font color="red">The Question generator </font>
  
    it is rule based method to generate question from a sentence
    uses prepostions



### <font color="red">The Question completor </font>
  
    Question recieved from the rule based system isn't meaningful one , so we complete the question grammatically using a seq2seq model

    For this we use squad dataset , strip of everything except verbs and nouns. We also remove stopwords and feed the stripped question and original question as input and output respectively.

    taken 200k examples, and attention model on seq2seq encoder-decoder model.


    

### <font color="red">The Relevency Checker </font>
  
    This many to one model with tell if a question makes sense or not.
    It uses LSTM networks.
    We take input question and replace its question words with all other 9 question words
    ['what','when','where','which','who','why','how','whose','whom']
    and lable all the others except the original as 0.

    taken 50k examples = 50k*8 = 400k total examples, and 10 epoochs,batch size 32 and glove 50dim embeddings.



# NEXT WORK 
train the networks and see how it works
    