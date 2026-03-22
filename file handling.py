#write to file
with open ("sample.txt","w")as file:
    file.write("Hello this is my first github file!")
    #read file
with open("sample.txt","r")as file:
    content = file.read()
    print(content)