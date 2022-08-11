import os
def create_map(filepath,save_path):
    file=open(filepath,'r',encoding="utf-8")
    save=open(save_path,'a+',encoding="utf-8")
    counts=0
    lines=[]
    for each in file:
        counts+=1
        lines.append(each)
    file.close()
    for i in range(counts):
        if '％v_lun' in lines[i]:
            lines[i]=lines[i].rstrip()
            temp=lines[i+2]
            if '」' in temp :
                temp=temp.split('」')[0][1:]
            if len(lines[i][1:])!=14:
                save.write(lines[i][1:]+".wav|"+temp+'\n')
    save.close()
if __name__=="__main__":
    files=os.listdir('./text')
    for each in files:
        create_map("./text/"+each,'./map.txt')