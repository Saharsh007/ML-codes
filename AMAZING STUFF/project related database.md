### https://stanfordnlp.github.io/coqa/

so this is conversational question answering dataset   
cons - it has follow up questions and answers which is what we want   
ex - 

Q		What color was Cotton?  
A		white || a little white kitten named Cotton  

Q		Where did she live?  
A		in a barn || in a barn near a farm house, there lived a little white kitten




### http://quac.ai/
RecipeQA

another dataset with followup questions  
.  
.  
.  
.  
.  
.  
# The dataset won't work



# New Approach --
take a sentence and use dependecy tree to ask questions  
generate questions using verb with the question_words = {what,when,who,what,where,how,etc}  
Now to choose which question to take ,  this will be done by dependency tree ,  
it can be used to know if question with that specific keyword is already answered   in the sentence or not    

For this we can use grammer rules to generate question without using ML model.

# New Approach 2 --- (Brand new idea and not implemented yet we guess)
for each answer , keep appending it and make a context and try to generate question from it.  
ex - I am amine, i live in banaglore , i work at siemens .  
    question - how is siemens at bangalore


# 