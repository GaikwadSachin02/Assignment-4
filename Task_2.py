#using only Write Mode
file1 = open('output.txt','w')
user=input('Enter text to write to the file: ')
store=file1.write(user+'\n')
print('Data successfully written to output.txt')
print('\n')
file1.close()

#using append mode
file1 = open('output.txt','a')
user2=input('Enter additional text to append: ')
store2= file1.write(user2+'\n')
print('Data successfully appended.')
print('\n')
file1.close()

#using read mode
file1 = open('output.txt','r')
read = file1.read()
print('Final content of output.txt')
print(read)
file1.close()




