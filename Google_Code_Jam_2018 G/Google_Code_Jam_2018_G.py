#Kuldeep Thakre kuldeep-kd@live.com
import math

def fact(x):
    ans = x
    while x > 1:
        temp = ans % 100
        ans = temp * (x - 1)
        x -= 1
    return ans


def calc(data_list):
    if data_list[0] == 1:
        return (data_list[0] % data_list[2])
    if data_list[1] > 9:
        return (data_list[0]**fact(data_list[1])) % data_list[2]
    return (data_list[0]**math.factorial(data_list[1])) % data_list[2]

def get_list(filename="input_file.txt"):
    ret_list = []
    file = open(filename,"r")
    line = file.readline()
#Generate list of elements as list of list of strs
    for _ in range(int(line)+1):
        if '\n' in line:
            ret_list.append((list( line.strip('\n').split(' ') )))
        else:
            ret_list.append((list( line.split(' ') )))
        line = file.readline()
    file.close()
    ret_list.pop(0) #Remove very First element i.e No. Test Cases
    # Using ListComprehension Converted list of string list tolist of int list
    print("Done")
    return [[int(i), int(j), int(k)] for [i,j,k] in ret_list] 
lst = get_list()


output = open("output_file.txt","w+")
for case in range(len( lst )):
    output.write( f"Case #{case+1}: {calc( lst.pop(0) )}\n") 
    print(f"Case {case+1} done\n")
output.close()