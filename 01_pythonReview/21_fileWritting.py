

#**** write mode ****
countries_file = open('./countries.txt', 'w') #open file

countries_file.write('This is a new text\n') #sobre escriboto TODO con el new text

countries_file.writelines('print(\'new file\')\n') #escribe esta línea en la posición que haya quedado

countries_file.close() #close file

#**** apprend  mode ****
countries_file = open('./countries.txt', 'a') #open file

countries_file.write('This is a new line \n') #sobre escriboto TODO con el new text

countries_file.close() #close file
