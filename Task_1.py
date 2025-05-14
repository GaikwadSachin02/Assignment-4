try:
    file1 = open('sample.txt','r')
    read = file1.readlines()
    print('Reading file content:')
    for i in range(len(read)):
        print('Line',i+1,':',read[i].strip())
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
