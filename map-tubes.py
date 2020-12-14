import sys
import nltk
from nltk.corpus import stopwords 

nltk.download('stopwords')

for line in sys.stdin:
    line = line.strip()
    for x in [',','.','!','?',':',';','"','\'','#','$','ö','~','û','ù','à','&']:
        line = line.replace(x,'')
    
    line = line.lower()
    words = line.split()
    
    words = sorted(words, key=str.lower)
    stop = stopwords.words('english')
    words = [word for word in words if word not in stop]
    
    for word in words:
        print ("%s\t%s" % (word, 1))