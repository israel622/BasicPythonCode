str = input('Enter a message: ')
def replace_word(str):
    word_to_replace = input('Enter a word to replace: ')
    word_replacement = input('Enter a word replacement: ')
    print(str.replace(word_to_replace, word_replacement))

replace_word(str)