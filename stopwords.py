import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

with open("stopwords.txt", "w") as f:
    for word in stopwords.words("english"):
        f.write(word + "\n")