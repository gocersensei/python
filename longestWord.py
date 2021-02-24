import os


def find_longest_word(filename):
    longest_word = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word


def find_all_longest_words(dirname):
    return {filename:
            # Gets the filename and its full path
                find_longest_word(os.path.join(dirname, filename))

            # Iterates over all of the files in dirname
            for filename in os.listdir(dirname)

            # We’re only interested in files, not directories or special files.
            if os.path.isfile(os.path.join(dirname, filename))}


print(find_all_longest_words('.'))
