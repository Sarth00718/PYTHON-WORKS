# Text Preprocessing 

import pandas as pd
import numpy as np
import re  # for working with regular expressions
import nltk  # for natural language processing (nlp)
# Auto-download necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('omw-1.4')
import spacy  # also for nlp
import string  # Module for string operations
from collections import Counter

# Read training data
trdf = pd.read_csv('NLC/train.csv', header='infer')

# Display basic info about the dataset
print(trdf.head(3))
print("Dataset info:")
trdf.info()

# =============================================================================
# 1. CASE CONVERSION
# =============================================================================

# Convert all text to lowercase for consistency
trdf['lowered_text'] = trdf['text'].str.lower()

# Confirm the case conversion
print("After case conversion:")
print(trdf['lowered_text'].head(3))

# =============================================================================
# 2. REMOVING PUNCTUATION
# =============================================================================

# Get all punctuation characters
punctuation = string.punctuation
print(f"Punctuation type: {type(punctuation)}, Content: {punctuation}")

# Create mapping dictionary for translation
# str.maketrans with 3 arguments maps each char in 3rd argument to None
mapping = str.maketrans("", "", punctuation)
print(f"Mapping type: {type(mapping)}, Sample: {dict(list(mapping.items())[:5])}")

# Apply punctuation removal
print("Before punctuation removal:")
print(trdf['lowered_text'].head(3))

trdf['lowered_text'] = trdf["lowered_text"].str.translate(mapping)

print("After punctuation removal:")
print(trdf['lowered_text'].head(3))

# Alternative method using function
def remove_punctuation(in_str):
    return in_str.translate(mapping)

# =============================================================================
# 3. REMOVING STOPWORDS
# =============================================================================

from nltk.corpus import stopwords

# Get English stopwords
print(f"Total stopwords available: {len(stopwords.words())}")
print(f"English stopwords: {len(stopwords.words('english'))}")

stopwords_eng = stopwords.words('english')
print(f"Sample stopwords: {stopwords_eng[:10]}")

# Function to remove stopwords
def remove_stopwords(in_str):
    new_str = ''
    words = in_str.split()  # Split string into words
    for word in words:
        if word not in stopwords_eng:
            new_str = new_str + word + " "
    return new_str

# Apply stopword removal
print("Before stopword removal:")
print(trdf["lowered_text"].head(3))

trdf['lowered_text_stop_removed'] = trdf["lowered_text"].apply(lambda x: remove_stopwords(x))

print("After stopword removal:")
print(trdf["lowered_text_stop_removed"].head(3))

# =============================================================================
# 4. IDENTIFY AND REMOVE FREQUENT WORDS
# =============================================================================

# Count frequency of every word
counter = Counter()
for text in trdf["lowered_text_stop_removed"]:
    for word in text.split():
        counter[word] += 1

print(f"Counter type: {type(counter)}")

# Get 10 most frequent words
most_cmn_list = counter.most_common(10)
print(f"Most common words: {most_cmn_list}")

# Extract just the words (not frequencies)
most_cmn_words_list = [word for word, freq in most_cmn_list]
print(f"Most common words list: {most_cmn_words_list}")

# Function to remove frequent words
def remove_frequent(in_str):
    new_str = ''
    for word in in_str.split():
        if word not in most_cmn_words_list:
            new_str = new_str + word + " "
    return new_str

# Apply frequent word removal
print("Before frequent word removal:")
print(trdf['lowered_text_stop_removed'].head(3))

trdf["lowered_text_stop_removed_freq_removed"] = trdf['lowered_text_stop_removed'].apply(lambda x: remove_frequent(x))

print("After frequent word removal:")
print(trdf["lowered_text_stop_removed_freq_removed"].head(3))

# =============================================================================
# 5. IDENTIFY AND REMOVE RARE WORDS
# =============================================================================

# Get 10 most rare words (often typos or URLs)
most_rare_list = counter.most_common()[-10:]  # Last 10 items
most_rare_words = [word for word, freq in most_rare_list]
print(f"Most rare words: {most_rare_words}")

# Function to remove rare words
def remove_rare(in_text):
    new_text = ""
    for word in in_text.split():
        if word not in most_rare_words:
            new_text = new_text + word + " "
    return new_text

# Apply rare word removal
trdf["lowered_stop_freq_rare_removed"] = trdf["lowered_text_stop_removed_freq_removed"].apply(lambda x: remove_rare(x))
print("After rare word removal:")
print(trdf["lowered_stop_freq_rare_removed"].head(3))

# =============================================================================
# 6. STEMMING USING PORTER STEMMER
# =============================================================================

from nltk.stem.porter import PorterStemmer

# Create PorterStemmer instance
stemmer = PorterStemmer()

def do_stemming(in_str):
    new_str = ""
    for word in in_str.split():
        new_str = new_str + stemmer.stem(word) + " "
    return new_str

print("Before Porter stemming:")
print(trdf["lowered_stop_freq_rare_removed"].head(3))

trdf["Stemmed"] = trdf["lowered_stop_freq_rare_removed"].apply(lambda x: do_stemming(x))

print("After Porter stemming:")
print(trdf["Stemmed"].head(3))

# =============================================================================
# 7. STEMMING USING SNOWBALL STEMMER
# =============================================================================

from nltk.stem.snowball import SnowballStemmer

# Print supported languages
print(f"Supported languages: {SnowballStemmer.languages}")

# Create SnowballStemmer instance for English
stemmer_sb = SnowballStemmer(language='english')

def do_stemming_sb(in_str):
    new_str = ""
    for word in in_str.split():
        new_str = new_str + stemmer_sb.stem(word) + " "
    return new_str

print("Before Snowball stemming:")
print(trdf["lowered_stop_freq_rare_removed"].head(3))

trdf["Stemmed_sb"] = trdf["lowered_stop_freq_rare_removed"].apply(lambda x: do_stemming_sb(x))

print("After Snowball stemming:")
print(trdf["Stemmed_sb"].head(3))

# =============================================================================
# 8. LEMMATIZATION
# =============================================================================

from nltk.stem import WordNetLemmatizer

# Create WordNetLemmatizer instance
lem = WordNetLemmatizer()

def do_lemmatizing(in_str):
    new_str = ""
    for word in in_str.split():
        new_str = new_str + lem.lemmatize(word) + " "
    return new_str

print("Before lemmatization:")
print(trdf["lowered_stop_freq_rare_removed"].head(3))

trdf["Lemmatized"] = trdf["lowered_stop_freq_rare_removed"].apply(lambda x: do_lemmatizing(x))

print("After lemmatization:")
print(trdf["Lemmatized"].head(3))

# =============================================================================
# 9. LEMMATIZATION WITH POS TAGGING
# =============================================================================

from nltk.corpus import wordnet

# Create POS tag mapping for better lemmatization
wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}

def do_lemmatizing_with_POS(in_str):
    new_str = ''
    for word in in_str.split():
        # Get POS tag for the word
        tag = nltk.pos_tag([word])[0][1][0]  # First character of POS tag
        # Use POS tag for better lemmatization
        new_str = new_str + lem.lemmatize(word, wordnet_map.get(tag, wordnet.NOUN)) + " "
    return new_str

trdf["Lemmatized_POS"] = trdf["lowered_stop_freq_rare_removed"].apply(lambda x: do_lemmatizing_with_POS(x))

print("After POS-based lemmatization:")
print(trdf["Lemmatized_POS"].head(3))

# =============================================================================
# 10. EMOJI HANDLING
# =============================================================================

# Function to remove emojis
def remove_emoji(in_str):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', in_str)  # Replace with empty string

# Test emoji removal
test_text = "game is on 🔥🔥"
print(f"Original: {test_text}")
print(f"After emoji removal: {remove_emoji(test_text)}")

# =============================================================================
# 11. URL REMOVAL
# =============================================================================

def remove_urls(text):
    # Pattern matches both https:// and www. URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

# Test URL removal
test_text = "Check this out: https://example.com and www.test.com"
print(f"Original: {test_text}")
print(f"After URL removal: {remove_urls(test_text)}")

# =============================================================================
# 12. HTML TAG REMOVAL
# =============================================================================

def remove_html(in_str):
    # Pattern matches any HTML tag
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', in_str)

# Test HTML removal
test_html = "<div>Hello <b>World</b></div>"
print(f"Original: {test_html}")
print(f"After HTML removal: {remove_html(test_html)}")

# =============================================================================
# 13. CHAT WORDS CONVERSION
# =============================================================================

# Dictionary of common chat abbreviations
chat_words_str = """
BRB=Be Right Back
LOL=Laughing Out Loud
BTW=By The Way
ASAP=As Soon As Possible
FYI=For Your Information
"""

# Create chat words dictionary
chat_words_expanded_dict = {}
chat_words_list = []
for line in chat_words_str.split("\n"):
    if line != "":
        chat_word = line.split("=")[0]
        chat_word_expanded = line.split("=")[1]
        chat_words_list.append(chat_word)
        chat_words_expanded_dict[chat_word] = chat_word_expanded

chat_words_list = set(chat_words_list)  # Convert to set for faster lookup

def convert_chat_words(in_str):
    new_str = ""
    for word in in_str.split():
        if word.upper() in chat_words_list:
            new_str = new_str + chat_words_expanded_dict[word.upper()] + " "
        else:
            new_str = new_str + word + " "
    return new_str

# Test chat word conversion
test_text = "I'll BRB, LOL that was funny"
print(f"Original: {test_text}")
print(f"After chat word conversion: {convert_chat_words(test_text)}")

# =============================================================================
# 14. SPELLING CORRECTION
# =============================================================================

# Note: Requires installation of pyspellchecker
# pip install pyspellchecker

from spellchecker import SpellChecker

# Create SpellChecker instance
spell = SpellChecker()

def correct_spellings(in_str):
    new_str = ""
    # Find misspelled words
    misspelled_words = spell.unknown(in_str.split())
    for word in in_str.split():
        if word in misspelled_words:
            # Correct the spelling
            new_str = new_str + spell.correction(word) + " "
        else:
            new_str = new_str + word + " "
    return new_str

# Test spelling correction
test_text = "speling correctin"
print(f"Original: {test_text}")
print(f"After spelling correction: {correct_spellings(test_text)}")

# =============================================================================
# 15. WORD CLOUD VISUALIZATION
# =============================================================================

from matplotlib import pyplot as plt
from wordcloud import WordCloud

def create_wordcloud(text_data, title="Word Cloud"):
    """Create and display a word cloud from text data"""
    
    # Combine all text into one string
    text = " ".join([str(word) for word in text_data])
    
    # Create WordCloud instance
    word_cloud = WordCloud(
        height=1080, 
        width=2048, 
        background_color='white',
        max_words=200,
        colormap='viridis'
    )
    
    # Generate word cloud
    word_cloud.generate(text)
    
    # Display the word cloud
    plt.figure(figsize=(12, 8))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.tight_layout()
    plt.show()
    
    return word_cloud

# Example usage:
# create_wordcloud(trdf["Lemmatized"], "Most Common Words After Preprocessing")

# =============================================================================
# COMPLETE PREPROCESSING PIPELINE FUNCTION
# =============================================================================

def preprocess_text(text, 
                   lower_case=True,
                   remove_punct=True,
                   remove_stopwords_flag=True,
                   remove_frequent_flag=False,
                   remove_rare_flag=False,
                   stemming_method=None,  # 'porter', 'snowball', or None
                   lemmatize=True,
                   pos_tagging=True,
                   remove_emojis=True,
                   remove_urls_flag=True,
                   remove_html_flag=True,
                   expand_chat_words=True,
                   spell_check=False):
    """
    Complete text preprocessing pipeline
    
    Parameters:
    - text: input text string
    - Various boolean flags to control which preprocessing steps to apply
    
    Returns:
    - processed_text: cleaned and preprocessed text
    """
    
    processed_text = text
    
    # 1. Convert to lowercase
    if lower_case:
        processed_text = processed_text.lower()
    
    # 2. Remove punctuation
    if remove_punct:
        processed_text = remove_punctuation(processed_text)
    
    # 3. Remove URLs
    if remove_urls_flag:
        processed_text = remove_urls(processed_text)
    
    # 4. Remove HTML
    if remove_html_flag:
        processed_text = remove_html(processed_text)
    
    # 5. Remove emojis
    if remove_emojis:
        processed_text = remove_emoji(processed_text)
    
    # 6. Expand chat words
    if expand_chat_words:
        processed_text = convert_chat_words(processed_text)
    
    # 7. Remove stopwords
    if remove_stopwords_flag:
        processed_text = remove_stopwords(processed_text)
    
    # 8. Spell correction
    if spell_check:
        processed_text = correct_spellings(processed_text)
    
    # 9. Stemming or Lemmatization
    if stemming_method == 'porter':
        processed_text = do_stemming(processed_text)
    elif stemming_method == 'snowball':
        processed_text = do_stemming_sb(processed_text)
    elif lemmatize:
        if pos_tagging:
            processed_text = do_lemmatizing_with_POS(processed_text)
        else:
            processed_text = do_lemmatizing(processed_text)
    
    return processed_text.strip()

# Example usage:
# sample_text = "Hello! Check out this URL: https://example.com BTW, this is AMAZING! 😀"
# processed = preprocess_text(sample_text)
# print(f"Original: {sample_text}")
# print(f"Processed: {processed}")

print("\n" + "="*50)
print("TEXT PREPROCESSING PIPELINE COMPLETE")
print("="*50)
print("Available functions:")
print("- preprocess_text(): Complete pipeline")
print("- remove_punctuation()")
print("- remove_stopwords()")
print("- remove_frequent() / remove_rare()")
print("- do_stemming() / do_stemming_sb()")
print("- do_lemmatizing() / do_lemmatizing_with_POS()")
print("- remove_emoji() / remove_urls() / remove_html()")
print("- convert_chat_words() / correct_spellings()")
print("- create_wordcloud()")
