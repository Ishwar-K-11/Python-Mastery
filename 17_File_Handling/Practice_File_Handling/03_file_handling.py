#print or read the content in the file line by line or directly all line

with open("file1.txt", "r") as f:
    txt = f.readline()
    print(txt)