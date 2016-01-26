#!/usr/bin/env python3
# encoding: utf-8
 
import sys
from pprint import pprint
from random import choice

 
EOS = ['.', '?', '!']
 
 
def build_dict(words):
    """
    Build a dictionary from the words.
 
    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    d = {}
    for i, word in enumerate(words):
        try:
            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (first, second)
        if key not in d:
            d[key] = []
        #
        d[key].append(third)
 
    return d
 
 
def generate_sentence(d):
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)
 
    li = []
    first, second = key
    li.append(first)
    li.append(second)
    while True:
        try:
            third = choice(d[key])
        except KeyError:
            break
        li.append(third)
        if third[-1] in EOS:
            break
        # else
        key = (second, third)
        first, second = key
 
    return ' '.join(li)
 
 
def main():
    fname = sys.argv[1]
    with open(fname, "rt", encoding="utf-8") as f:
        text = f.read()
 
    words = text.split()
    d = build_dict(words)
#    pprint(d)
#    print()

    fail_count = 0
    success_count = 0

    results = []
    word_count = 0
    character_count = 0

    sentence_target = int(input("How many sentences would you like to generate? "))

    while success_count < sentence_target:
        generated_sentences = generate_sentence(d)
        fail_count += 1
        is_substring_of_corpus = generated_sentences in text
        is_matching_other_results = generated_sentences in results

        if is_substring_of_corpus is False and is_matching_other_results is False:
            success_count += 1
            fail_count -= 1
            results.append(generated_sentences)
            print(str(success_count) + ": " + generated_sentences)
        if fail_count > sentence_target * 100:
            print("Failcount hit " + str(sentence_target * 100) + "! Breaking!")
            break

    if success_count == sentence_target:

        print("Writing results to output.txt")

        with open('output.txt', 'wt') as target_file:
            # target_file.truncate()

            for line in results:
                line_number = 1

                if line_number % 3 == 0:
                    target_file.write(line + "\n")
                    line_number += 1
                else:
                    target_file.write(line)
                    line_number += 1

                if line_number % 10 == 0:
                    target_file.write("\n\n")

            print("Generated " + str(sentence_target) + " sentences. Closing file.")

            target_file.close()

####################
 
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: provide an input corpus file.")
        sys.exit(1)
    # else
    main()

