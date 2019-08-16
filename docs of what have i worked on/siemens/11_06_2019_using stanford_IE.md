# using stanford IE

so finally when question words are extracted we'll use stanford's Information Extractor to find triples and then connect the question_words + triples .   
This will be fed into the NN which will produce meaningfull sentence.  
So today's task is to refine the combining to produce the question_word + triples.

# Update 

the preprocess part worked is working fine i guess  

print(give_questions("this is so wrong"))  

['what this is so wrong', 'when this is so wrong', 'where this is so wrong', 'which this is so wrong', 'who this is so wrong', 'whom this is so wrong', 'whose this is so wrong', 'why this is so wrong', 'how this is so wrong']  
