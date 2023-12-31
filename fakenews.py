# -*- coding: utf-8 -*-
"""FakeNews.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a0gLs-thLYtsjZfL8gOlpCYE_8lh5JwJ
"""

!pip install datasets

from datasets import load_dataset

# Load the train dataset
train_dataset = load_dataset("mohammadjavadpirhadi/fake-news-detection-dataset-english", "main", split="train")

# Load the test dataset
test_dataset = load_dataset("mohammadjavadpirhadi/fake-news-detection-dataset-english", "main", split="test")

# You can access the text and label columns as follows:
x_train = train_dataset['text']
y_train = train_dataset['label']
x_test = test_dataset['text']
y_test = test_dataset['label']

# Encode labels into integers (0 for fake, 1 for real)
y_train = [0 if label == "FAKE" else 1 for label in y_train]
y_test = [0 if label == "FAKE" else 1 for label in y_test]

# Now you can proceed with the rest of your classification code as previously discussed.

# Assuming you have already loaded the dataset
from datasets import load_dataset

# Load the train dataset
train_dataset = load_dataset("mohammadjavadpirhadi/fake-news-detection-dataset-english", "main", split="train")

# Access the text and label columns
x_train = train_dataset['text']
y_train = train_dataset['label']

# Print all examples in the training dataset with real/fake labels
for i in range(len(x_train)):
    real_or_fake = "Real" if y_train[i] == 1 else "Fake"
    print(f"Text: {x_train[i]}")
    print(f"Label: {y_train[i]} ({real_or_fake})\n")

from sklearn.feature_extraction.text import TfidfVectorizer

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

# Convert list elements to strings
x_train_str = [str(x) for x in x_train]
x_test_str = [str(x) for x in x_test]

# Vectorize the training data
x_train_vectorized = vectorizer.fit_transform(x_train_str)

# Vectorize the test data
x_test_vectorized = vectorizer.transform(x_test_str)

from sklearn.svm import LinearSVC

# Create and train a LinearSVC classifier
clf = LinearSVC()
clf.fit(x_train_vectorized, y_train)

# Calculate accuracy on the testing set
accuracy = clf.score(x_test_vectorized, y_test)
print(f"Accuracy on the testing set: {accuracy * 100:.2f}%")

# Make predictions for a new text
new_text = "This is a new text that you want to classify."
vectorized_text = vectorizer.transform([new_text])
predicted_label = clf.predict(vectorized_text)

# Convert the predicted label to human-readable form (Real or Fake)
predicted_label_human_readable = "Real" if predicted_label == 1 else "Fake"

print(f"Predicted Label: {predicted_label[0]} ({predicted_label_human_readable})")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the training data for cosine similarity
x_train_vectorized = vectorizer.fit_transform(x_train)

def cosine_similarity_score(news1, news2):
    # Transform news articles
    news1_vectorized = vectorizer.transform([news1])
    news2_vectorized = vectorizer.transform([news2])

    # Calculate cosine similarity
    similarity = cosine_similarity(news1_vectorized, news2_vectorized)[0][0]

    return similarity

# Example usage
news1 = "The moon landing was faked by the government."
news2 = "NASA successfully landed on the moon in 1969."

threshold = 0.6
similarity_score = cosine_similarity_score(news1, news2)

if similarity_score < threshold:
    print("The news articles are likely fake.")
else:
    print("The news articles are likely genuine.")

import re

def tokenize(text):
    """Converts a text string into a list of tokens (words)."""
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    return set(tokens)

def jaccard_similarity(text1, text2):
    """Calculates the Jaccard similarity coefficient between two sets of tokens."""
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)
    return len(intersection) / len(union)

def is_fake_news(text, threshold=0.5):
    # Load some example real news articles for comparison
    real_news_articles = x_train  # Assuming x_train contains real news articles

    # Calculate Jaccard similarity between the input text and each real news article
    similarities = [jaccard_similarity(text, article) for article in real_news_articles]

    # Determine whether the input text is more similar to fake news or real news
    avg_similarity = sum(similarities) / len(similarities)
    return avg_similarity <= threshold

# Example usage:
text = "The Prime Minister of India, Narendra Modi visits Punjab today (April 24, 2023)."

if is_fake_news(text):
    print("This news is likely fake!")
else:
    print("This news seems to be legitimate.")

import re
import math

def tokenize(text):
    """Converts a text string into a list of tokens (words)."""
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    return set(tokens)

def jaccard_similarity(text1, text2):
    """Calculates the Jaccard similarity coefficient between two sets of tokens."""
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)
    return len(intersection) / len(union)

def cosine_similarity(text1, text2):
    """Calculates the cosine similarity between two texts."""
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)

    # Create a set of all unique words in both texts
    all_words = tokens1.union(tokens2)

    # Create vectors of word frequencies for each text
    vector1 = [list(tokens1).count(word) for word in all_words]
    vector2 = [list(tokens2).count(word) for word in all_words]

    # Calculate the dot product and magnitudes of the vectors
    dot_product = sum([vector1[i] * vector2[i] for i in range(len(vector1))])
    magnitude1 = math.sqrt(sum([count**2 for count in vector1]))
    magnitude2 = math.sqrt(sum([count**2 for count in vector2]))

    # Calculate the cosine similarity between the vectors
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)

def is_fake_news(text, threshold=0.1):
    # Load some example real news articles for comparison
    real_news_articles = x_train  # Assuming x_train contains real news articles

    # Calculate Jaccard and cosine similarities between the input text and each real news article
    jaccard_similarities = [jaccard_similarity(text, article) for article in real_news_articles]
    cosine_similarities = [cosine_similarity(text, article) for article in real_news_articles]

    # Determine whether the input text is more similar to fake news or real news
    avg_jaccard_similarity = sum(jaccard_similarities) / len(jaccard_similarities)
    avg_cosine_similarity = sum(cosine_similarities) / len(cosine_similarities)

    if avg_jaccard_similarity <= threshold:
        print("Jaccard similarity score: ", avg_jaccard_similarity)
        print("This news is likely fake according to Jaccard similarity!")
    else:
        print("Jaccard similarity score: ", avg_jaccard_similarity)
        print("This news seems to be legitimate according to Jaccard similarity.")

    if avg_cosine_similarity <= threshold:
        print()
        print("Cosine similarity score: ", avg_cosine_similarity)
        print("This news is likely fake according to Cosine similarity!")
    else:
        print()
        print("Cosine similarity score: ", avg_cosine_similarity)
        print("This news seems to be legitimate according to Cosine similarity.")

# Example usage:
text = "British Foreign Secretary Boris Johnson said on Wednesday that he was concerned about reports that U.S. President Donald Trump s would recognize Jerusalem as Israel s capital. Lets wait and see what the president says exactly. But, you know, we view the reports that we have heard with concern because we think that Jerusalem obviously should be part of the final settlement between the Israelis and the Palestinians, he told reporters in Brussels. Senior U.S. officials said on Tuesday that Trump will recognize Jerusalem as Israel s capital on Wednesday and set in motion the relocation of the U.S. Embassy to the city."

is_fake_news(text)

def is_fake_news(text, jaccard_threshold=0.2, cosine_threshold=0.2):
    # Load some example real news articles for comparison
    real_news_articles = x_train  # Assuming x_train contains real news articles

    # Calculate Jaccard and cosine similarities between the input text and each real news article
    jaccard_similarities = [jaccard_similarity(text, article) for article in real_news_articles]
    cosine_similarities = [cosine_similarity(text, article) for article in real_news_articles]

    # Determine whether the input text is more similar to fake news or real news based on thresholds
    avg_jaccard_similarity = sum(jaccard_similarities) / len(jaccard_similarities)
    avg_cosine_similarity = sum(cosine_similarities) / len(cosine_similarities)

    if avg_jaccard_similarity <= jaccard_threshold:
        print("Jaccard similarity score: ", avg_jaccard_similarity)
        print("This news is likely fake according to Jaccard similarity!")
    else:
        print("Jaccard similarity score: ", avg_jaccard_similarity)
        print("This news seems to be legitimate according to Jaccard similarity.")

    if avg_cosine_similarity <= cosine_threshold:
        print()
        print("Cosine similarity score: ", avg_cosine_similarity)
        print("This news is likely fake according to Cosine similarity!")
    else:
        print()
        print("Cosine similarity score: ", avg_cosine_similarity)
        print("This news seems to be legitimate according to Cosine similarity.")

# Example usage with adjusted thresholds:
text = "def is_fake_news(text, jaccard_threshold=0.2, cosine_threshold=0.2):
    # Load some example real news articles for comparison
    real_news_articles = x_train  # Assuming x_train contains real news articles

    # Calculate Jaccard and cosine similarities between the input text and each real news article
    jaccard_similarities = [jaccard_similarity(text, article) for article in real_news_articles]
    cosine_similarities = [cosine_similarity(text, article) for article in real_news_articles]

    # Determine whether the input text is more similar to fake news or real news based on thresholds
    avg_jaccard_similarity = sum(jaccard_similarities) / len(jaccard_similarities)
    avg_cosine_similarity = sum(cosine_similarities) / len(cosine_similarities)

    if avg_jaccard_similarity <= jaccard_threshold:
        print("Jaccard similarity score: ", avg_jaccard_similarity)
        print("This news is likely fake according to Jaccard similarity!")
    else:
        print("Jaccard similarity score: ", avg_jaccard_similarity)
        print("This news seems to be legitimate according to Jaccard similarity.")

    if avg_cosine_similarity <= cosine_threshold:
        print()
        print("Cosine similarity score: ", avg_cosine_similarity)
        print("This news is likely fake according to Cosine similarity!")
    else:
        print()
        print("Cosine similarity score: ", avg_cosine_similarity)
        print("This news seems to be legitimate according to Cosine similarity.")

# Example usage with adjusted thresholds:
text = "In a shocking incident, the Gujarat Titans team was found guilty of ball-tampering during their match against Delhi Capitals in TATA IPL 2023. The incident came to light after the match referee received a complaint from the umpires about the ball being tampered with during the match."

# Adjust the thresholds as needed
jaccard_threshold = 0.3
cosine_threshold = 0.3

is_fake_news(text, jaccard_threshold, cosine_threshold)
"

# Adjust the thresholds as needed
jaccard_threshold = 0.3
cosine_threshold = 0.3

is_fake_news(text, jaccard_threshold, cosine_threshold)