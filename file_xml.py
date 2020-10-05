from collections import Counter
import xml.etree.ElementTree as ET
import os


def sorted_list_word(description, len_word):
    words = []
    for word in description:
        if len(word) > len_word:
            words.append(word)
    return words


def most_popular_words(words, top):
    return Counter(words).most_common(top)


def xml_import(path, len_word):
    all_words = []
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(path, parser)
    root = tree.getroot()

    items = root.findall("channel/item")
    for item in items:
        description = item.find("description").text.split()
        all_words.extend(sorted_list_word(description, len_word))
    all_words.sort()
    return all_words


file_path_xml = os.path.join(os.getcwd(), "newsafr.xml")
print(most_popular_words(xml_import(file_path_xml, 6), 10))