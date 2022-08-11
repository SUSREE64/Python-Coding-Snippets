# sorting a list with a function as the key .
# Sort a list of strings, based on thier length of the string.

words_lst = ['a', "i love you", 'he', 'hello', "name", 'hell with you']
def len_func(word):
    return (len(word))
sorted_words_lst = sorted(words_lst, key = len_func)
print(sorted_words_lst)

words = ['aaaaa', 'bb bb bb', 'a b c', 'the world is very beautiful let me see this', 'hey john', 'ssss']
def word_count(word):
    return len(word.split(' '))

result = sorted(words, key = word_count)  
print(result)
