import string

alphabet = string.ascii_lowercase


def is_pangram(sentence):
    for character in alphabet:
        if character not in sentence.lower():
            return False

    return True


if __name__ == '__main__':

    pangramExample = 'The quick brown fox jumps over the lazy dog.'

    if is_pangram(pangramExample):
        print(pangramExample + " is pangram")
    else:
        print(pangramExample + " is not pangram")

