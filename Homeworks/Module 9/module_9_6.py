def all_variants(text):
    for i in range(len(text)):
        for k in range(i+1, len(text) + 1):
            yield text[i:k]


a = all_variants("abc")
for i in a:
    print(i)