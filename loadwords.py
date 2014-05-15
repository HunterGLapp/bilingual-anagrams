from collections import Counter
import random
def loadwords():
    eng_file = open('english', 'r')
    eng_words = eng_file.readlines()
    stripped_eng_words = [word.rstrip("\r\n") for word in eng_words]
    eng_word_counters = [Counter(word) for word in stripped_eng_words]

    span_file = open('spanish', 'r')
    span_lines = span_file.readlines()
    stripped_span_lines = [line.split(',')[1].split(' ')[0] for line in span_lines]
    span_word_counters = [Counter(word) for word in stripped_span_lines]
    return eng_word_counters, span_word_counters, stripped_eng_words, stripped_span_lines

def getword(eng_word_counters, span_word_counters, stripped_eng_words, stripped_span_lines):
    eng = ""
    span = ""
    while not eng:
        starti = random.randint(0, len(eng_word_counters))
        startj = random.randint(0, len(span_word_counters))
        class Found(Exception): pass
        try:
            for i in range(starti, len(eng_word_counters)):
                for j in range(startj, len(span_word_counters)):
                    if eng_word_counters[i] == span_word_counters[j] and stripped_eng_words[i] != stripped_span_lines[j]:
                        raise Found
        except Found:
            eng, span =  stripped_eng_words[i], stripped_span_lines[j]
            return eng, span
