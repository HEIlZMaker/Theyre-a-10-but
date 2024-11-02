import random
import time 
duplicateset = set(())
player = ""

while player != 'q':
    epoch_time = int(time.time())
    random.seed(epoch_time)
    block = random.randint(1,4)

    if block == 1:
        max = 60
    elif block == 2:
        max = 60
    elif block == 3:
        max = 47
    elif block == 4:
        max = 11
    
    question = random.randint(1, max)
    result = block, question

    if result not in duplicateset:
        duplicateset.add(result)
        print(block)
        print(question)
        print("press q to exit, any other key to continue")
        player = input()
#thank you darq for helping me :)
#help!