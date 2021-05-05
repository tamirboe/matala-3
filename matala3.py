import json
import re 

def read():
    conver= open("C:/Users/Tamir/מבוא להנדסת ידע ונתונים/מטלה 3/Whatsapp.txt", encoding='utf-8')
    print(read_list(conver))
    

def read_list(conver:str): 
    dic=dict()
    dic1=dict()
    count=1
    list1=list()
    diction2=dict()
    line2=1
    down_line=0
    metadata=dict()
    for line in conver:
        line=line.rstrip()
        start=line.find('-')
        end=line.find(':',start)        
        if end>0:    
            name=line[start+1:end]
            if name not in dic:
                dic[name]=count
                count=count+1
            date = re.findall(r'\d{1}.\d{1}.\d{4}', line)
            time = re.findall(r'\d{2}:\d{2}', line)
            datetime=""
            if len(date)>0: 
                datetime+=date[0]+" "
            if len(time)>0: 
                datetime+=time[0]
            dic1["datetime"]=datetime
           # dic1['datetime']= line[0:15]
            dic1['id']=dic[name]

            t = line.split(':')
            dic1['text'] = t[2].strip()
            # print(diction['text'])
            list1.append(dic1)
        if down_line == line2:
            # print(line)
            sta2=line.find('"')
            end2=line.find('"',sta2+1)
            metadata['conver_name']=line[sta2+1:end2]
            metadata['creation_date']=line[0:15]
            sta=line.find('+')
            metadata['creator']=line[sta+1:]
        if end<0 and '-' not in line : 
            list1.append(dic1)
            list1.append(dic1.copy())
        down_line += 1
    metadata['num_of_participants']=len(dic)
    # print(dicid)
    diction2={'Massege':list1,'metadata':metadata}
    

    
    #json_string = json.dumps(lst2)
    convert_json = json.dumps(diction2, ensure_ascii=False)
    with open(os.path.join('C:/Users/Tamir/מבוא להנדסת ידע ונתונים/מטלה 3','conver_name'+".txt"),'w',encoding='utf-8')as f:
        f.write(convert_json)
    return(convert_json)

read()
