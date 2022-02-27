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
    
    
#Write one function that accept input file and return clean output file or movie review
 
def getStemmedDocument(inputFile,outputFile):
   out=open(outputFile,'w',encoding = "utf8")
   
   with open(inputFile,encoding = "utf8") as f:
      reviews= f.readlines()
      
   for review in reviews:
      cleaned_review = getStemmedReview(review)
      print((cleaned_review),file=out)
      
   out.close()
   
   
#Review command line argument

inputFile = sys.argv[1]
outputFile = sys.argv[2]

getStemmedDocument(inputFile,outputFile)
