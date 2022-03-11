f = open("ma-2015-02-05.txt", "r", encoding="utf-8")
ivos = []
for x in f:
    # print(x)
    if "ivo" in x:
        text = x.split()
        word = text[0]
        index = word.find("ivo")
        if index == len(word) - 3:
            if word not in ivos:
                ivos.append(word)
                print(word)            
# print(ivos)