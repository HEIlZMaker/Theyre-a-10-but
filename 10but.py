import random
import time 

def plaintext(filename):
    with open (filename,'r', encoding='UTF-8') as File:
        lines=[]
        for i in File:
            i=i.rstrip()
            lines.append(i)
    return lines

epoch_time = int(time.time())
random.seed(epoch_time)

positive = plaintext("positive.txt")
negative= plaintext("negative.txt")
neutral= plaintext("neutral.txt")
wtf = plaintext("WTF.txt")

blocklist = [positive,negative,neutral,wtf]

player = ''
while player != 'q':
    block = random.choice(blocklist)
    question = random.choice(block)
    
    print(question)
    index = block.index(question)
    block[index], block[-1] = block[-1], block[index] #swap question with last index
    block.pop(-1)
    if len(block)==0:
        blocklist.remove(block)
    if blocklist==0:
        print("game finished! There are no more questions")
        break
    print("___________________________________________")

    player = input()
#thank you darq for helping me :)
#thank you straightline for helping 