from transformers import pipeline
import pickle
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.decomposition import PCA

nlp = pipeline("ner", model="dslim/bert-large-NER", tokenizer="dslim/bert-large-NER")

def product_subject(subject):
    bert_token = nlp(subject)   
    product = " ".join([el["word"] for el in bert_token]).replace(" ##", "")
    if len(product) > 1:
        return product
    else:
        return False
    
def product_body(body):
    bert_token = nlp(body)
    product = " ".join([el["word"] for el in bert_token]).replace(" ##", "")
    if len(product) > 1:
        return product
    else:
        return False