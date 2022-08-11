import pydub
import os
def trans(filepath="v_lun0001.ogg"):
    song=pydub.AudioSegment.from_ogg(filepath)
    temp=filepath.split('.')[1]
    print(temp)
    song.export("./wavs/"+temp[12:]+".wav",format='wav')
if __name__=="__main__":
    files=os.listdir('./luna_sound')
    count=0
    for file in files:
        trans('./luna_sound/'+file)
        print(file,'success')
    os.system('clear')
    print("trans success")#564 565
    files=os.listdir("./wavs")
    count=0
    for each_file in files:
        os.system(f"ffmpeg -i {f'wavs/{each_file}'} -ar 22050 {f'newwavs/{each_file}'}")
        print(each_file,'success')