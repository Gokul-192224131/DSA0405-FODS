from collections import Counter
import re
reviews = [
    "The product is amazing. I love it!",
    "Not satisfied with the quality. Disappointing.",
    "Great value for the price. Highly recommended.",
    "Terrible experience. Would not buy again."
]
all_reviews = ' '.join(reviews)

cleaned_reviews = re.sub(r'[^a-zA-Z\s]', '', all_reviews).lower()

words = cleaned_reviews.split()
word_freq = Counter(words)
print("Word Frequency Distribution:")
for word, count in word_freq.items():
    print(f"{word}: {count}")
