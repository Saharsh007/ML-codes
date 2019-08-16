# Hardcord to find question words.

The attention model performed well , at least when trained on 1000 examples it was able to generate sentence which made some sence.  
Now we'll train it on some 200k examples from squad dataset.

Now all that remains is finding (question word + noun* + verb + noun*)

For this I'm gonna look at all the prepositions and adjectives(which are mostly used) to generate question word.  

I found that each prepostion answers a particular question word. If "to" is answering where and when in different sentences then the pos tags before and after it will differ in both cases. If it doesn't then both question words will have same answer.

So I'll find all the question words which are being answered and remove them , and generate a broken sentence of format as mentioned above and feed that into the neural network. 
 
Let's see how that works out.


# Talk with amlaan

so i just taled with amlan about the idea i thought .
TLDR - the model should'nt ask the same thing again , so for now try with "why". Generate a questions and find some scoring mechanism to select the best question out of all the possible questions.

Task1 . Generate questions which aren't already answered in context.  
Task2 . scoring mechanism to select the best question  
Task3 . Questions asked shouldn't repeat again.


question_words = ['what','when','where','which','who','whom','whose','why','how']  
 
# Solution...
## Task 2
                 *
              /  |  \
             *   *    * 

ex - This packet comes with extra cheese!
### relevent questions  
    Q - Where does this packet comes from?  
    Q - how does this packet comes?
    Q - why does this packet comes?

### irrelevant questions
    Q - whom does this packet come ?(although this is relevant - "whom does this packet comes to?")
    Q - which this packet comes ?
    Q - whose this packet comes ?


# Formation of model

>   remove stopwords  
>   extract verb and convert to base form  
>   extract object and attatch with question word , verb and object.




