from collections import Counter
import json
import os


def sorted_list_word(description, len_word):
    words = []
    for word in description:
        if len(word) > len_word:
            words.append(word)
    return words


def most_popular_words(words, top):
    return Counter(words).most_common(top)


def json_import(path, len_word):
    all_words = []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    items = data["rss"]["channel"]["items"]
    for item in items:
        description = item["description"].split()
        all_words.extend(sorted_list_word(description, len_word))
    all_words.sort()
    return all_words


file_path_json = os.path.join(os.getcwd(), "newsafr.json")
print(most_popular_words(json_import(file_path_json, 6), 10))