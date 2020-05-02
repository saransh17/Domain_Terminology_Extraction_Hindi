from nltk.tag import tnt
from nltk.corpus import indian
import nltk

def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger

def tagger1(sen):
    return model.tag(nltk.word_tokenize(sen))

model = hindi_model()
input = open("output.txt","r")
inp = input.read()
sentences = inp.split("\n")
sentences = sentences[:800]
new_tagged = map(tagger1,sentences)
print(list(new_tagged))
