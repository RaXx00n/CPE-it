import json
import re
import Levenshtein

with open('Got-Combined.json', 'r') as f:
    data = json.load(f)

for obj in data:
    display_version = obj['DisplayVersion']
    display_name = obj['DisplayName']

    # Remove version number from DisplayName
    display_name = re.sub(r'(\d+\.)+\d+', '', display_name).strip()

    # Split DisplayName into words, omitting DisplayVersion substring and special characters
    display_name = re.sub(r'\(.*?\)', '', display_name)  # Remove parentheses and their contents
    display_name = re.sub(r'[^A-Za-z0-9 ]+', '', display_name)  # Remove special characters

    if display_version is not None:
        display_name = display_name.replace(display_version, '')  # Remove DisplayVersion substring

    words = display_name.split()[:3]  # Get first three words

    # Calculate Levenshtein distance between DisplayVersion and each word in DisplayName
    for word in words:
        if display_version is not None:
            distance = Levenshtein.distance(display_version, word)
            if distance <= 2:  # If word is similar to DisplayVersion, omit it
                words.remove(word)

    # Combine remaining words into Keyword, omitting special characters
    keyword = ' '.join(words)
    keyword = re.sub(r'[^A-Za-z0-9 ]+', '', keyword)

    obj['Keyword'] = keyword

with open('Got-Keywords.json', 'w') as f:
    json.dump(data, f, indent=4)
