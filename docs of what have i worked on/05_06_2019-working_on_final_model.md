# Model to convert {question word + noun+ verb } combination to a meaningfull sentence
### 5th June 2019

so i took squad dataset , extracted all the questions from it , removed everything excpet
<b>   
verb_tag_list = ['VB','VBD','VBG','VBN','VBP','VBZ']  
noun_tag_list = ['NN','NNS','NNP','NNPS','PRP','PRP$']  
question_words = ['what','when','where','which','who','whom','whose','why','how'] </b>   
all the verbs , nouns and question words. verb and noun were retained using pos tags.  
later removal of stopwords , punctuation marks , lower case and all the preprocessing parts.  
after that I have the processed data as input and unprocessed as output . 
now use a encoder-decoder model , which is currently being trained. Let's see how it works.


### <font color="yellow">Important Note</font>
### <font color="red">Don't try to make the matrix for all example at once , there will be memory error , instead divide it in batches</font>


btw model being trained fine  and we have high hopes.