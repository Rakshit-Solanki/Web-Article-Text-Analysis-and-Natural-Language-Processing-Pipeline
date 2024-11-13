import os
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import textstat

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

def analyze_text(text):
    # Tokenize the text
    words = word_tokenize(text.lower())
    sentences = sent_tokenize(text)
    
    return {
        'POSITIVE SCORE': calculate_sentiment_scores(text)['pos'],
        'NEGATIVE SCORE': calculate_sentiment_scores(text)['neg'],
        'POLARITY SCORE': calculate_polarity_score(text),
        'SUBJECTIVITY SCORE': calculate_subjectivity_score(text),
        'AVG SENTENCE LENGTH': calculate_avg_sentence_length(sentences, words),
        'PERCENTAGE OF COMPLEX WORDS': calculate_percentage_complex_words(words),
        'FOG INDEX': calculate_fog_index(sentences, words),
        'AVG NUMBER OF WORDS PER SENTENCE': len(words) / len(sentences),
        'COMPLEX WORD COUNT': count_complex_words(words),
        'WORD COUNT': len(words),
        'SYLLABLE PER WORD': calculate_avg_syllables_per_word(words),
        'PERSONAL PRONOUNS': count_personal_pronouns(text),
        'AVG WORD LENGTH': calculate_avg_word_length(words)
    }

def calculate_sentiment_scores(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def calculate_polarity_score(text):
    scores = calculate_sentiment_scores(text)
    return (scores['pos'] - scores['neg']) / ((scores['pos'] + scores['neg']) + 0.000001)

def calculate_subjectivity_score(text):
    # Implement subjectivity calculation
    return len([word for word in word_tokenize(text) if word.lower() in ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours']]) / len(word_tokenize(text))

def calculate_avg_sentence_length(sentences, words):
    return len(words) / len(sentences)

def is_complex_word(word):
    return textstat.syllable_count(word) > 2

def calculate_percentage_complex_words(words):
    complex_words = [word for word in words if is_complex_word(word)]
    return (len(complex_words) / len(words)) * 100

def calculate_fog_index(sentences, words):
    avg_sentence_length = len(words) / len(sentences)
    percent_complex_words = calculate_percentage_complex_words(words)
    return 0.4 * (avg_sentence_length + percent_complex_words)

def count_complex_words(words):
    return sum(1 for word in words if is_complex_word(word))

def calculate_avg_syllables_per_word(words):
    return sum(textstat.syllable_count(word) for word in words) / len(words)

def count_personal_pronouns(text):
    pronouns = ['I', 'we', 'my', 'ours', 'us']
    words = word_tokenize(text)
    return sum(1 for word in words if word.lower() in pronouns)

def calculate_avg_word_length(words):
    return sum(len(word) for word in words) / len(words)

def main():
    processed_dir = 'E:\IP\Black Coffer assignment'
    results = []
    
    for filename in os.listdir(processed_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(processed_dir, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                analysis = analyze_text(text)
                analysis['URL_ID'] = filename.replace('.txt', '')
                results.append(analysis)
    
    # Create a DataFrame from the results
    df = pd.DataFrame(results)
    
    # Save the results to a CSV file
    df.to_csv('E:\IP\Black Coffer assignment/text_analysis_results.csv', index=False)
    print("Analysis complete. Results saved to E:\IP\Black Coffer assignment/text_analysis_results.csv")

if __name__ == "__main__":
    main()