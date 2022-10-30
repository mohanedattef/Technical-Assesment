import json

#read input from a provided file
def read_input(file_name):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data

#sort data in reverese then push the values down and check for tie breakers
def handle_data(data):
    sorted_data= {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
    keys_list=list(sorted_data.keys())
    value_list=list(sorted_data.values())
    for i in range(len(value_list)-1):
        value_list[i]=value_list[i+1]
    value_list[-1]="lost"
    new_data=dict(zip(keys_list,value_list))
    check_case(new_data)
    return new_data

#tie breaker check function, checking for duplicates and printing them out 
def check_case(final_data):
    dict = {}
    for key, value in final_data.items():
        dict.setdefault(value, set()).add(key)
    res = filter(lambda x: len(x) >1, dict.values())
    x=list(res)
    if(len(x)>0):
        y=[]
        for i in x: y.append(sorted(i))
        print("tie breaker(s) exist and the alphabitical order is: ")
        for i in y: print (i)


#write to output file 
def write_data(final_data):
    with open("output.json", "w") as write_file:
        json.dump(final_data, write_file,indent=4)
 
 
 
        
if __name__ == '__main__':
    data=read_input("input.json")
    if len(data)==0:
        print("No Winners")
    elif len(data)==1:
        print("the winner is: "+list(data.keys())[0])
    else:
        final_data=handle_data(data)
        write_data(final_data)

