# Here we will open the file using the simple using open using the read mode
file = open("file1.txt", "r")
data = file.read()
print(data)



# opening the file using the with open 
with open("file1.txt","r") as f:
    d = f.read()
    print(d)