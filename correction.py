import textblob

from textblob import TextBlob
def correct_grammer(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

text = input("Enter your Sentence: ")
corrected_text = correct_grammer(text)
print(f"Corrected: {corrected_text}")
