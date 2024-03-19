sent = "python is a programming language"

for word in sent.split():
    if len(word)%2== 0:
        print(word)