import random
import time 
duplicateset = set(())
player = ''
blocklist = 60,60,47,11
combinations=[]
for block in range(len(blocklist)):
    for question in range(blocklist[block]):
        tuple = (block+1, question+1)
        combinations.append(tuple)

while player != 'q':
    epoch_time = int(time.time())
    random.seed(epoch_time)

    index = random.randint(0,len(combinations)-1)
    print(combinations[index])
    combinations[index], combinations[-1] = combinations[-1], combinations[index]
    combinations.pop(-1)
    if len(combinations) == 0:
        print("game finished! There are no more questions")
        break
    print("press q to exit, any other key to continue")
    player = input()
#thank you darq for helping me :)