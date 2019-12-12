import os
def cleanFile(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)   

def findIndex(myString, ocurrence):
    substr = '.'

    # Finding nth occurrence of substring 
    val = -1
    for i in range(0, ocurrence): 
        val = myString.find(substr, val + 1)        
    # Printing nth occurrence 
    return val


def mainFunction():
    path_to_file = r"C:/Users/jose.m.yanez.nunez/OneDrive - Accenture/Documents/Scripts/names.txt"
    file_to_write = open("C:/Users/jose.m.yanez.nunez/OneDrive - Accenture/Documents/Scripts/ShortNames.txt",'w')
    index = 0
    with open(path_to_file) as file_object:
        for line in file_object:
            if(len(line)>=16):
                firstSubstring = 1
                i=1
                while len(line)> 16:
                    index = findIndex(line,i)
                    line = line[0:firstSubstring] + line[index:]
                    firstSubstring+=2
                    i+=1
                print(line.lower(),file= file_to_write)
            else:
                print(line.lower(),file= file_to_write)
    file_to_write.close()
                    
file = "C:/Users/jose.m.yanez.nunez/OneDrive - Accenture/Documents/Scripts/ShortNames.txt"

mainFunction()
cleanFile(file)
