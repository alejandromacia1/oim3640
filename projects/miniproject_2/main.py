
""" 
Mini Project #2: A Dialogue Dominance Analyzer
Who speaks most in the novel Wuthering Heights, Heathcliff or Catherine?

Wuthering Heights, by Emily Brontë
"""

import re
import string
from collections import Counter

FILEPATH = "C:/Users/amacia1/Documents/Github/oim3640/projects/miniproject_2/wuthering_heights.txt"


HEATHCLIFF_SPEECH_MARKERS = [
    'heathcliff said', 'said heathcliff', 'heathcliff replied', 'replied heathcliff',
    'heathcliff cried', 'cried heathcliff', 'heathcliff asked', 'asked heathcliff',
    'heathcliff muttered', 'heathcliff returned', 'returned heathcliff',
    'heathcliff exclaimed', 'heathcliff continued', 'heathcliff interrupted',
]

CATHERINE_SPEECH_MARKERS = [
    'catherine said', 'said catherine', 'catherine replied', 'replied catherine',
    'catherine cried', 'cried catherine', 'catherine asked', 'asked catherine',
    'catherine exclaimed', 'catherine continued', 'catherine returned', 'catherine muttered',
    'cathy said', 'said cathy', 'cathy cried', 'cried cathy',
    'cathy asked', 'asked cathy', 'cathy replied', 'replied cathy',
]

STOP_WORDS = {
    "i", "me", "my", "we", "you", "your", "he", "him", "his", "she", "her",
    "it", "its", "they", "them", "their", "this", "that", "am", "is", "are",
    "was", "were", "be", "been", "have", "has", "had", "do", "does", "did",
    "will", "would", "could", "should", "can", "a", "an", "the", "and", "but",
    "or", "if", "in", "on", "at", "to", "of", "by", "as", "not", "with",
    "from", "then", "than", "when", "here", "there", "said", "oh", "so",
    "what", "who", "how", "all"
}

def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    start = text.find("*** START OF THE PROJECT GUTENBERG")
    end = text.find("*** END OF THE PROJECT GUTENBERG")

    return text[start:end]

def split_into_chapters(text):
    parts = re.split(r"CHAPTER\s+[IVXLCDM]+", text)
    chapters = parts[1:]
    return chapters

def get_speaker(context):
    context = context.lower()

    for marker in HEATHCLIFF_SPEECH_MARKERS:
        if marker in context:
            return "Heathcliff"

    for marker in CATHERINE_SPEECH_MARKERS:
        if marker in context:
            return "Catherine"

    return "Unknown"

def extract_dialogue(chapter_text):
    quotes = re.findall(r'“([^”]+)”', chapter_text)
    matches = list(re.finditer(r'“([^”]+)”', chapter_text))

    results = []

    for i in range(len(matches)):
        quote = quotes[i]
        start = matches[i].start()
        end = matches[i].end()

        context_before = chapter_text[max(0, start - 100):start]
        context_after = chapter_text[end:end + 100]
        context = context_before + context_after

        speaker = get_speaker(context)
        results.append((speaker, quote))

    return results


def clean_words(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()


    clean_list = []
    for word in words:
        if word not in STOP_WORDS and len(word) > 1:
            clean_list.append(word)

    return clean_list


def analyze_dialogue(dialogue_list):
    full_text = " ".join(dialogue_list)
    cleaned_words = clean_words(full_text)

    total_words = len(full_text.split())
    unique_words = len(set(cleaned_words))

    if len(cleaned_words) > 0:
        richness = round(unique_words / len(cleaned_words), 3)
    else:
        richness = 0

    top_words = Counter(cleaned_words).most_common(10)

    return total_words, unique_words, richness, top_words


def main():
    text = load_text(FILEPATH)
    chapters = split_into_chapters(text)

    heathcliff_dialogue = []
    catherine_dialogue = []

    chapter_word_counts = []

    for chapter in chapters:
        lines = extract_dialogue(chapter)

        heathcliff_words = 0
        catherine_words = 0

        for speaker, quote in lines:
            if speaker == "Heathcliff":
                heathcliff_dialogue.append(quote)
                heathcliff_words += len(quote.split())

            elif speaker == "Catherine":
                catherine_dialogue.append(quote)
                catherine_words += len(quote.split())

        chapter_word_counts.append((heathcliff_words, catherine_words))

    h_total, h_unique, h_richness, h_top = analyze_dialogue(heathcliff_dialogue)
    c_total, c_unique, c_richness, c_top = analyze_dialogue(catherine_dialogue)

    print("WUTHERING HEIGHTS DIALOGUE ANALYSIS")
    print("-" * 40)

    print("\nHeathcliff")
    print("Lines:", len(heathcliff_dialogue))
    print("Total words:", h_total)
    print("Unique words:", h_unique)
    print("Vocabulary richness:", h_richness)
    print("Top words:", h_top)

    print("\nCatherine")
    print("Lines:", len(catherine_dialogue))
    print("Total words:", c_total)
    print("Unique words:", c_unique)
    print("Vocabulary richness:", c_richness)
    print("Top words:", c_top)

    print("\nCHAPTER BY CHAPTER WORD COUNT")
    print("-" * 40)
    print("Chapter | Heathcliff | Catherine")

    for i in range(len(chapter_word_counts)):
        h_count = chapter_word_counts[i][0]
        c_count = chapter_word_counts[i][1]
        print(i + 1, "     |", h_count, "       |", c_count)


main()