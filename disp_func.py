from random import randint
import os

def stack_disp(stack_list):
    print()
    for i in range(len(stack_list)):
        print("\n"+str(i+1)+": "+str(stack_list[i]))
    print()

def prompts(inp):
    if inp:
        prompts = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'inc_mv_prompts'), 'r').read().split('\n')[:-1]
        return prompts[randint(0,len(prompts) - 1)]
    else:
        prompts = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'new_game_prompts'), 'r').read().split('\n')[:-1]
        return prompts[randint(0,len(prompts) - 1)]
