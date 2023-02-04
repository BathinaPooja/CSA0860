def display_lexicographic(string):
    words=string.split()
    sorted_string =sorted(words)
    for i in sorted_string:
        print(i) 
print (display_lexicographic("welcome to python"))
