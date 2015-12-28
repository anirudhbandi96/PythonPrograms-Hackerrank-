appendMe='\nNew bit of info'
appendFile = open('exampleFile.txt','a')
appendFile.write('\n')
appendFile.write(appendMe)
appendFile.close()
