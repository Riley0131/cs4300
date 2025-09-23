#https://www.geeksforgeeks.org/python/python-program-to-count-words-in-text-file/
import re

with open("task6_read_me.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Count words while ignoring punctuation-only tokens
words = len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", data))