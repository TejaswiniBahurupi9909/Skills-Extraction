import nltk
import os

#python -m spacy  download en_core_web_sm
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')
# nltk.download('wordnet')
# nltk.download('brown')
# nltk.download('maxent_ne_chunker')
from resume_parser import resumeparse
import json

path = "D:/Internship/Recorem/Project"
os.chdir(path)
filename = 'D:/Internship/Recorem/data.json'

def read_text_file(file_path):
    data = resumeparse.read_file(file_path)
    #print(data)
    with open(filename, 'a') as file_object:
        print("Appending data")
        json.dump(data, file_object, indent=3)
    print("Data Appended")


for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".pdf"):
        file_path = f"{path}\{file}"
        # call read text file function
        read_text_file(file_path)

