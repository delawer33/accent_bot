word_file = open("words.txt", "r", encoding="utf-8")
words = []
while True:
    
    line = word_file.readline()
    if not line:
        break
    words.append(line.strip())


word_file.close()