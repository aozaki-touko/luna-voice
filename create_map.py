import random


if __name__=="__main__":
    file=open('./save.txt','r',encoding='utf-8')
    train=open('./train.txt','w',encoding='utf-8')
    val=open('./val.txt','w',encoding='utf-8')
    for each in file:
        if random.random()<0.1:
            val.write(each)
        else:
            train.write(each)
    train.close()
    val.close()
    file.close()
