import re

def checks():
    example1="C:\ML\Words2.txt"
    searchElement="care"
    k=0
    finalList=[]
    with open(example1,"r") as file1:
        for line in file1:

             temp = []
             j=0
             if (len(line)<=7):
                temp = permute_string(searchElement)

                for i in temp:
                    #print("The string " + searchElement + " and the " + line)
                    
                    if((i==line)):
                        
                        #print(re.search(searchElement, line))
                        
                        j+=1
                        k+=1
                    
    

               



def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

checks()
