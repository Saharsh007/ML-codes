# EMOJIFY

## Emoji prediction from given a sentence using LSTMs.Completed as part of 5th Deep Learnig course on coursera. Wrote the whole code from scratch.

* Predicts upto 6 different emojis.
* Fairly Decent Accuracy of 87.5% on dataset provided in the course.

# Model structure


## Input -> Embedding  -> LSTM (128) -> Dropout(0.5) -> LSTM(128) -> Dropout(0.5) -> Dense(5) -> Activation(softmax)
