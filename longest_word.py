# One liner finding the lagest word in a sentence
sentence = "hello How do you do , I am the happiest"
word = [s for s in sentence.split() if len(s) == max(len(a) for a in sentence.split())]
print(word[0])
