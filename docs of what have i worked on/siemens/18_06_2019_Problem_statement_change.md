# Another New Idea

## Idea   
We'll ask questions in a specific domain..  
Using a specific domain look for its instance in wikipedia dataset, and extract all its attributes...   
ex - look for mount everest if we are talking about mountains    
use those attributes to ask questions about another instance of that object..   

## task breakdown  

    1.extract all attributes about a object given a wikipedia dataset about it  
    1.1.    Will need to sentence tokenize the article and break into triples...   


    2.Ask questions using the triples and store answers as graph or some other dataset....  

    3.Don't ask the things which the user already has told.
    3.1. Figure out how to do it...   


## Result

We have another graph with all the properties as the first one.


## How

    1.nltk sentence tokenizer and standford's open IE
    2.using question generation model (look for the best one)
    3.Will think about it...