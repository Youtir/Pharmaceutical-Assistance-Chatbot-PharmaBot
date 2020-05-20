import pandas as pd
import nltk

import re
from nltk.stem import wordnet  # to perform lemmatization
from sklearn.feature_extraction.text import CountVectorizer  # to perform bow
from nltk import pos_tag # for parts of speech
from sklearn.metrics import pairwise_distances  # to perfrom cosine similarity
from nltk.corpus import stopwords  # for stop words



def text_normalization(text):    
        text = str(text).lower()  # text to lower case
        spl_char_text = re.sub(r'[^ a-z]', '', text)  # removing special characters
        tokens = nltk.word_tokenize(spl_char_text)  # word tokenizing
        lema = wordnet.WordNetLemmatizer()  # intializing lemmatization
        tags_list = pos_tag(tokens, tagset=None)  # parts of speech
        lema_words = []   # empty list
        for token, pos_token in tags_list:
            if pos_token.startswith('V'):  # Verb
                pos_val = 'v'
            elif pos_token.startswith('J'):  # Adjective
                pos_val = 'a'
            elif pos_token.startswith('R'):  # Adverb
                pos_val = 'r'
            else:
                pos_val = 'n'  # Noun
            lema_token = lema.lemmatize(token, pos_val)  # performing lemmatization
            lema_words.append(lema_token)  # appending the lemmatized token into a list
        
        return " ".join(lema_words)  # returns the lemmatized tokens as a sentence



df = pd.read_excel('Data\dialog_talk_agent.xlsx')

df.ffill(axis=0, inplace=True)

df['lemmatized_text'] = df['Context'].apply(text_normalization)  # applying the function to the dataset to get clean text

cv = CountVectorizer()  # intializing the count vectorizer
X = cv.fit_transform(df['lemmatized_text']).toarray()

features = cv.get_feature_names()
df_bow = pd.DataFrame(X, columns=features)

def stopword_(text):
    text = text.lower()
    tag_list = pos_tag(nltk.word_tokenize(text), tagset=None)
    stop = stopwords.words('english')
    lema = wordnet.WordNetLemmatizer()
    lema_word = []
    for token, pos_token in tag_list:
        if token in stop:
            continue
        if pos_token.startswith('V'):
            pos_val = 'v'
        elif pos_token.startswith('J'):
            pos_val = 'a'
        elif pos_token.startswith('R'):
            pos_val = 'r'
        else:
            pos_val = 'n'
        lema_token = lema.lemmatize(token, pos_val)
        lema_word.append(lema_token)
    return " ".join(lema_word)


def chat_bow(text):
    s = stopword_(text)
    lemma = text_normalization(s)  # calling the function to perform text normalization
    bow = cv.transform([lemma]).toarray()  # applying bow
    cosine_value = 1 - pairwise_distances(df_bow, bow, metric='cosine')
    index_value = cosine_value.argmax()  # getting index value
    return df['Text Response'].loc[index_value]






