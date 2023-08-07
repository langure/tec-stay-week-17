import re
from collections import Counter

def preprocess_text(text):
    # Remove special characters, digits, and extra spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

def sentence_score(sentence, word_freq):
    # Calculate the score of a sentence based on word frequency
    words = sentence.split()
    num_words = len(words)
    score = sum(word_freq[word] for word in words) / num_words
    return score

def extractive_summarization(text, num_sentences=3):
    # Preprocess the text
    preprocessed_text = preprocess_text(text)

    # Tokenize the text into sentences
    sentences = preprocessed_text.split('. ')

    # Count word frequency in the text
    word_freq = Counter(preprocessed_text.split())

    # Calculate sentence scores and rank them
    sentence_scores = [(sentence_score(sentence, word_freq), sentence) for sentence in sentences]
    ranked_sentences = sorted(sentence_scores, reverse=True)

    # Select the top n sentences for the summary
    summary_sentences = [sentence for score, sentence in ranked_sentences[:num_sentences]]
    summary = '. '.join(summary_sentences)

    return summary

# Example text for summarization
text = """
Artificial intelligence (AI) is the simulation of human intelligence processes by machines, 
especially computer systems. These processes include learning (the acquisition of information 
and rules for using the information), reasoning (using rules to reach approximate or definite 
conclusions), and self-correction. Particular applications of AI include expert systems, 
speech recognition, and machine vision.

Natural Language Processing (NLP) is a subfield of AI that focuses on the interaction between 
computers and humans through natural language. It involves the analysis and generation of human 
language by computers. NLP has various applications such as sentiment analysis, machine 
translation, and text summarization.

Text summarization is the process of creating a concise and coherent summary of a longer text 
while preserving its key information. There are two main approaches to text summarization: 
extractive and abstractive. Extractive summarization involves selecting and extracting important 
sentences or phrases from the original text, while abstractive summarization involves generating 
new sentences to capture the essence of the original text.
"""

# Perform extractive text summarization
summary = extractive_summarization(text)

# Print the summary
print(summary)
