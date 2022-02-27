from nltk.tokenize import RegexpTokenizer

from nltk.stem.porter import PorterStemmer

from nltk.corpus import stopwords
import sys


#Init object

ps = PorterStemmer()

en_stopwords = set(stopwords.words('english'))

tokenizer = RegexpTokenizer(r'\w+')

def getStemmedReview(review):
    review = review.lower()
    
    review = review.replace("<br /><br />"," ")
    #tokenization
    tokens = tokenizer.tokenize(review)
    
    #removing stopwords
    new_word = [token for token in tokens if token not in en_stopwords]
        
     #do stemming 
    stemmed_token = [ps.stem(token) for token in new_word ]
    
    cleaned_review = ' '.join(stemmed_token)
    
    return cleaned_review
    
