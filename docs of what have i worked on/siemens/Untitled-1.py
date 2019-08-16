
#%%
import pandas as pd
import numpy as np
import json
import re
import string
from string import digits
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
stopword_eng = set(stopwords.words('english'))


#%%
stopword_eng.difference_update({'which', 'why' , 'where' , 'who' , 'what' , 'whom' , 'how' , 'when' , 'can' , 'should'})
print(stopword_eng)


#%%
# outputY = ["why did you kill" , "what is the name of that road" , "where was the elephant killed" ,
#              "how did you die" , "when is the movie gonna play" , "why did the phone explode" , "who ate the pie" ,
#             "how will the earth finish" , "where is the model needed"]

# inputX = ["why you kill" , "what is name road" , "where elephant killed" , "how you die"  , "when movie play" ,
#           "why phone explode" , "who ate pie" , "how earth finish" , "where model needed"]
with open('squad_train.json') as file:
    df1 = json.load(file)


#%%
question_list = []
print(df1['data'][105]['paragraphs'][1]['qas'][0]['question'])
len(df1['data'])  * len(df1['data'][0]['paragraphs']) * len(df1['data'][0]['paragraphs'][0]['qas'])
for i in range(len(df1['data'])):
    for j in range(len(df1['data'][i]['paragraphs'])):
        for k in range(len(df1['data'][i]['paragraphs'][j]['qas'])):
            question_list.append( df1['data'][i]['paragraphs'][j]['qas'][k]['question'] )


#%%
input_list = question_list[:10000]


#%%
df = pd.DataFrame(columns=['input','output'])




#%%
df['input'] = input_list
df['output'] = input_list


#%%
df.input=df.input.apply(lambda x: x.lower())
df.output=df.output.apply(lambda x: x.lower())



# Take the length as 50
df.input= df.input.apply(lambda x: re.sub("'", '', x)).apply(lambda x: re.sub(",", ' COMMA', x))
df.output = df.output.apply(lambda x: re.sub("'", '', x)).apply(lambda x: re.sub(",", ' COMMA', x))


#punctuations
exclude = set(string.punctuation)
df.input = df.input.apply(lambda x: ''.join(ch for ch in x if ch not in exclude))
df.output =df.output.apply(lambda x: ''.join(ch for ch in x if ch not in exclude))

remove_digits = str.maketrans('', '', digits)
df.input = df.input.apply(lambda x: x.translate(remove_digits))
df.output = df.output.apply(lambda x: x.translate(remove_digits))

df.output = df['output'].apply(lambda x : 'START_ '+ x + ' _END')


#%%
df.head()


#%%
df.input = df.input.apply(lambda x: x.split())
df.output = df.output.apply(lambda x: x.split())


#%%
# sent = "what was the name of the console discovered"
# sent1 = "when were plans for twilight princess hd revealed"
# print(nltk.pos_tag( nltk.word_tokenize(sent)) )
# print(nltk.pos_tag( nltk.word_tokenize(sent1)) )
question_words = ['what','when','where','which','who','whom','whose','why','how']
verb_tag_list = ['VB','VBD','VBG','VBN','VBP','VBZ']
noun_tag_list = ['NN','NNS','NNP','NNPS','PRP','PRP$']
 
def change_input(sent):
    new_sent = []
    pos = nltk.pos_tag(sent) 
    for index,word in enumerate(sent):
        if word in question_words:
            new_sent.append(word)
        if pos[index][1] in verb_tag_list:
            new_sent.append(word)
        if pos[index][1] in noun_tag_list:
            new_sent.append(word)
    return new_sent

print(nltk.pos_tag(['which', 'issue', 'of', 'the', 'wii', 'menu', 'fixed', 'the', 'issue', 'with', 'the', 'wii', 'menu']))
change_input(['which', 'issue', 'of', 'the', 'wii', 'menu', 'fixed', 'the', 'issue', 'with', 'the', 'wii', 'menu'])



#%%

for i in range(10):
    print(df.input[i+25] ,"!!!!output is!!!! ", df.output[i+25])
# for i in range(10):
#     print(df.input[i+2345] ,"!!!!output is!!!! ", df.output[i+2345])
for index,_ in enumerate(df.input):
    df['input'][index] = change_input(df.input[index])
    


#%%
for i in range(10):
    print(df.input[i+25] ,"!!!!output is!!!! ", df.output[i+25])


#%%
def remove_stopwords(token_sent):
    free_sent = []
    for word in token_sent:
        if word not in stopword_eng:
            free_sent.append(word)
    return free_sent


#%%
for index in range(len(df.input)):
    df.input[index] = remove_stopwords(df.input[index])
    


#%%
# sent = "what was the name of the console discovered"
# pos = nltk.pos_tag( ['which', 'company', 'is', 'responsible', 'for', 'the', 'hd', 'version', 'of', 'twilight', 'princess']) 
# pos


#%%
for i in range(10):
    print(df.input[i+25] ,"!!!!output is!!!! ", df.output[i+25])


#%%
def combine_all(tokens):
    token = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
    return token


for index in range(len(df.input)):
    df.input[index] = combine_all(df.input[index])
    df.output[index] = combine_all(df.output[index])


#%%
all_input_words=set()
for inp in df.input:
    for word in inp.split():
        if word not in all_input_words:
            all_input_words.add(word)
    

all_output_words=set()
for outp in df.output:
    for word in outp.split():
        if word not in all_output_words:
            all_output_words.add(word)


#%%
print(all_input_words)
print(all_output_words)


#%%
output_lenght_list=[]
for l in df.output:
    output_lenght_list.append(len(l.split(' ')))

input_lenght_list=[]
for l in df.input:
    input_lenght_list.append(len(l.split(' ')))
print(np.max(output_lenght_list))
print(np.max(input_lenght_list))
max_output = np.max(output_lenght_list)
max_input = np.max(input_lenght_list)


#%%

input_words = sorted(list(all_input_words))
target_words = sorted(list(all_output_words))
num_encoder_tokens = len(all_input_words)
num_decoder_tokens = len(all_output_words)
# del all_eng_words, all_french_words


#%%
input_token_index = dict(
    [(word, i) for i, word in enumerate(input_words)])
target_token_index = dict(
    [(word, i) for i, word in enumerate(target_words)])


#%%
len(df.output)*58*num_decoder_tokens


#%%
df.head()


#%%
df.to_csv('Finaldata.csv')


#%%
# for i, (input_text, target_text) in enumerate(zip(df.input, df.output)):
#     for t, word in enumerate(input_text.split()):
#         encoder_input_data[i, t] = input_token_index[word]
#     for t, word in enumerate(target_text.split()):
#         # decoder_target_data is ahead of decoder_input_data by one timestep
#         decoder_input_data[i, t] = target_token_index[word]
#         if t > 0:
#             # decoder_target_data will be ahead by one timestep
#             # and will not include the start character.
#             decoder_target_data[i, t - 1, target_token_index[word]] = 1.


#%%
embedding_size = 50
from keras.layers import Input, LSTM, Embedding, Dense
from keras.models import Model
from keras.utils import plot_model
from keras import optimizers 


#%%
encoder_inputs = Input(shape = (None,))
encoder_embeddings = Embedding(num_encoder_tokens,embedding_size)(encoder_inputs)
E_LSTM = LSTM(50,return_state=True)
encoder_output , hidden_state , memory_cell = E_LSTM(encoder_embeddings)
encoder_states = [hidden_state,memory_cell]


#%%
decoder_inputs = Input(shape = (None,))
decoder_embeddings = Embedding(num_decoder_tokens,embedding_size)
final_dex = decoder_embeddings(decoder_inputs)
decoder_LSTM = LSTM(50,return_sequences=True,return_state=True)
decoder_outputs ,_ , _ = decoder_LSTM(final_dex, initial_state = encoder_states)
decoder_dense = Dense(num_decoder_tokens,activation='softmax') # total no of unique words
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])


#%%
model.summary()


#%%
for index in range(0,1000,100):

    
    encoder_input_data = np.zeros(
        (len(df.input),max_input ),
        dtype='float32')

    decoder_input_data = np.zeros(
        (len(df.output), max_output),
        dtype='float32')

    decoder_target_data =np.zeros(
        (len(df.output), max_output, num_decoder_tokens),
        dtype='float32')

    for i, (input_text, target_text) in enumerate(zip(df.input[index:index+100], df.output[index:index+100])):
        for t, word in enumerate(input_text.split()):
            encoder_input_data[i, t] = input_token_index[word]
        for t, word in enumerate(target_text.split()):
            # decoder_target_data is ahead of decoder_input_data by one timestep
            decoder_input_data[i, t] = target_token_index[word]
            if t > 0:
                # decoder_target_data will be ahead by one timestep
                # and will not include the start character.
                decoder_target_data[i, t - 1, target_token_index[word]] = 1.
                
    model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=20,
          epochs=5,
          validation_split=0.05)


#%%
# model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
#           batch_size=32,
#           epochs=5,
#           validation_split=0.05)


#%%
encoder_model = Model(encoder_inputs, encoder_states)
encoder_model.summary()


decoder_state_input_h = Input(shape=(50,))
decoder_state_input_c = Input(shape=(50,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

final_dex2=decoder_embeddings(decoder_inputs)

decoder_outputs2, state_h2, state_c2 = decoder_LSTM(final_dex2, initial_state=decoder_states_inputs)
decoder_states2 = [state_h2, state_c2]
decoder_outputs2 = decoder_dense(decoder_outputs2)
decoder_model = Model(
    [decoder_inputs] + decoder_states_inputs,
    [decoder_outputs2] + decoder_states2)

# Reverse-lookup token index to decode sequences back to
# something readable.
reverse_input_char_index = dict(
    (i, char) for char, i in input_token_index.items())
reverse_target_char_index = dict(
    (i, char) for char, i in target_token_index.items())


#%%
def decode_sequence(input_seq):
    #input_seq is  [[1607.   80. 3062.    0.    0.]] for 14077
    print("input is ",input_seq)
    
    # Encode the input as state vectors.
    states_value = encoder_model.predict(input_seq)
#     print("state_value is ", states_value)
    '''
    state_value is  [array([[-0.7356597 , -0.9993317 , -0.8581535 ,  0.9991428 ,  0.86860234,
        -0.88219815,  0.6262745 , -0.9992849 ,  0.9986833 ,  0.99975616,
        -0.96406317, -0.8911646 , -0.93668246,  0.8071924 , -0.9070601 ,
        -0.9983337 , -0.6851529 , -0.5785509 ,  0.9981099 , -0.45333877,
        -0.9723586 , -0.92026615, -0.5631677 , -0.9855832 ,  0.53639436,
         0.7567345 ,  0.8314614 ,  0.98461056, -0.02521831, -0.90126914,
         0.9989688 ,  0.8336466 , -0.9887398 , -0.7309139 , -0.52631956,
        -0.6803367 , -0.9744914 , -0.9639372 ,  0.8591712 , -0.07826253,
         0.9617582 , -0.7269689 , -0.9957466 , -0.6216118 , -0.9720878 ,
         0.89779437,  0.93081397, -0.9966131 ,  0.9854572 ,  0.9793006 ]],
      dtype=float32), array([[-3.2502072 , -4.0018077 , -2.370447  ,  3.8773093 ,  3.6909149 ,
        -3.2669096 ,  3.1789834 , -3.9679527 ,  3.662548  ,  4.506039  ,
        -2.5889246 , -1.4275558 , -2.4326057 ,  1.1189184 , -3.5042324 ,
        -3.5447226 , -3.0464299 , -2.1128592 ,  3.4816515 , -2.5415885 ,
        -2.1338346 , -1.5907625 , -0.63746005, -2.462637  ,  4.776198  ,
         3.2632422 ,  3.4211106 ,  2.429748  , -0.02522366, -1.4789395 ,
         3.7848165 ,  1.8303449 , -2.5869899 , -0.9306867 , -0.8429435 ,
        -2.9611928 , -2.174526  , -1.9987224 ,  1.2901706 , -0.0784229 ,
         1.9688332 , -3.3909166 , -3.0755305 , -2.5341778 , -2.1288924 ,
         1.4607303 ,  1.664449  , -3.1896398 ,  2.4582543 ,  2.2801971 ]],
      dtype=float32)]
      
     ''' 
    
      
    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1,1)) 
    # Populate the first character of target sequence with the start character.
    target_seq[0, 0] = target_token_index['START_']
#     print("target_seq is ",target_seq[0,0] )
    
    #target_seq is  1.0

    
    
    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
      
      output_tokens, h, c = decoder_model.predict(
          [target_seq] + states_value)
#       print("output_tokens is ", output_tokens)

      # Sample a token
      sampled_token_index = np.argmax(output_tokens[0, -1, :])
      print("sampled_token_index is ",sampled_token_index)
      sampled_char = reverse_target_char_index[sampled_token_index]
      decoded_sentence += ' '+sampled_char

      print("decoded sentence is ",decoded_sentence)
      # Exit condition: either hit max length
      # or find stop character.
      if sampled_char == '_END' or len(decoded_sentence) > 52 :
        stop_condition = True

      # Update the target sequence (of length 1).
      target_seq = np.zeros((1,1))
      target_seq[0, 0] = sampled_token_index

      # Update states
      states_value = [h, c]
      
      '''
    output_tokens is  [[[1.9580897e-04 1.4204055e-10 3.0356929e-05 ... 3.8483760e-12
       1.3986213e-14 2.2031972e-09]]]
    sampled_token_index is  929
    decoded sentence is   cest
    output_tokens is  [[[4.6192162e-04 9.7681152e-07 1.8441869e-04 ... 1.9450983e-06
       1.9787763e-06 3.8920575e-06]]]
    sampled_token_index is  6753
    decoded sentence is   cest un
    output_tokens is  [[[4.5321140e-05 9.9775898e-06 2.7055165e-04 ... 3.3116699e-04
       7.6128467e-04 3.4273871e-05]]]
    sampled_token_index is  4784
    decoded sentence is   cest un peu
    output_tokens is  [[[2.2299837e-03 3.8076034e-06 2.4568696e-02 ... 7.3837878e-06
       6.9453758e-06 2.5249241e-05]]]
    sampled_token_index is  1566
    decoded sentence is   cest un peu de
    output_tokens is  [[[7.1985596e-05 3.0220974e-06 2.2143837e-04 ... 2.4737383e-05
       1.8406533e-04 3.3893932e-05]]]
    sampled_token_index is  1131
    decoded sentence is   cest un peu de colère
    output_tokens is  [[[4.6538683e-03 9.3184195e-07 7.0089167e-01 ... 5.0056883e-07
        2.9316115e-07 1.3825561e-05]]]
    sampled_token_index is  2
    decoded sentence is   cest un peu de colère _END
    -
   
    '''
      
    return decoded_sentence


#%%
def give_output(sent):
    input_seq = encode_data(sent)
    decoded_sentence = decode_sequence(input_seq)
    print('-')
    print('Input sentence:', sent)
    print('Decoded sentence:', decoded_sentence)
    return decoded_sentence


#%%
def encode_data(input_text):
    encoder_test_data = np.zeros(
    (1,max_input ),
    dtype='float32')
    for t, word in enumerate(input_text.split()):
        encoder_test_data[0, t] = input_token_index[word]
    return encoder_test_data


#%%
give_output("why play road ")


#%%
nltk.pos_tag((['who', 'is', 'Beyoncé', 'married', 'to']))


