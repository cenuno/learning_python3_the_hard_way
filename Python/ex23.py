#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 23: Strings, Bytes, and Character Encodings
# Date:     February 24, 2019
#
# Using a list of humang languages to demonstrate a few concepts:
#
# 1) How modern computers store human languages to display and processing
#    and how Python 3 calls this 'strings'
# 2) Need to 'encode' and 'decode' Python's strings into a type called 'bytes'
# 3) How to handle errors in your string and byte handling
# 4) How to read code and understand it even if you've never seen it before
#
import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    # without this if statement, the loop would continue forever
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("raw_data/languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)

# end of script #
