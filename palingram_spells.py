"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load('C:/Users/naaom/Downloads/2of4brif.txt')


def find_palingrams():
    """Find dictionary palingrams"""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - 1:] in words:
                    pali_list.append((word, rev_word[end - 1:]))
                if word[:i] == rev_word[end - 1:] and rev_word[:end - 1] in words:
                    pali_list.append((rev_word[:end - 1], word))
    return pali_list


palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
