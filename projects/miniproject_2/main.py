
""" 
Mini Project #2: A Dialogue Dominance Analyzer
Who speaks most in the novel Wuthering Heights, Heathcliff or Catherine?

Wuthering Heights, by Emily Brontë
"""

import re

HEATHCLIFF_MARKERS = ['heathcliff said', 'said heathcliff', 'heathcliff replied','replied heathcliff', 'heathcliff cried', 'cried heathcliff', 'heathcliff asked', 'asked heathcliff', 'heathcliff muttered', 'heathcliff returned', 'returned heathcliff', 'heathcliff exclaimed', 'heathcliff continued', 'heathcliff interrupted',]

CATHERINE_MARKERS = ['catherine said', 'said catherine', 'catherine replied', 'replied catherine', 'catherine cried', 'cried catherine', 'catherine asked', 'asked catherine', 'catherine exclaimed', 'catherine continued', 'catherine returned', 'catherine muttered', 'cathy said', 'said cathy', 'cathy cried', 'cried cathy', 'cathy asked', 'asked cathy', 'cathy replied', 'replied cathy']

def load_novel():
    """Load the novel Wuthering Heights"""
    with open('wuthering_heights.txt', 'r') as f:
        novel = f.read()
        return novel

def roman_to_int(roman):
    """Convert Roman numeral string to integer."""
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    total, prev = 0, 0
    for ch in reversed(roman):
        v = vals.get(ch, 0)
        total += v if v >= prev else -v
        prev = v
    return total