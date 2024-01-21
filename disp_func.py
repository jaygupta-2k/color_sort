from random import randint
import os

def stack_disp(stack_list):
    print()
    for i in range(len(stack_list)):
        print("\n"+str(i+1)+": "+str(stack_list[i]))
    print()

def prompts(inp):
    if inp:
        #prompts = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'inc_mv_prompts'), 'r').read().split('\n')[:-1]
        prompts = [
    	"That's not how you do it",
	    "You're doing it wrong",
    	"That's not how it's done",
	    "You're making a mess of it",
    	"That's not the right way",
	    "You're doing it backwards",
    	"That's not how it works",
	    "You're doing it upside down",
    	"That's not how it's supposed to be done",
	    "That's not the right technique",
    	"You're doing it the wrong way around",
	    "That's not how it's meant to be done",
    	"That's not the proper method",
	    "That's not how it's done in this universe"
        ]
        return prompts[randint(0,len(prompts) - 1)]
    else:
        #prompts = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'new_game_prompts'), 'r').read().split('\n')[:-1]
        prompts = [
    	"Ready for a rematch",
	    "Fancy another game",
    	"Up for another round",
	    "How about another go",
    	"Wanna play again",
	    "Another round",
    	"Care for another game",
	    "Want another round",
    	"How about a rematch",
	    "Up for it again",
    	"Ready for another round"
        ]
        return prompts[randint(0,len(prompts) - 1)]
