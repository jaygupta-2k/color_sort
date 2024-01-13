#import stack_disp.stack_disp;
from create_stack import create_stack
from move_letters import move_letters
import re

if __name__ == "__main__":
    name = input("Hello Player!\n\n> What should I call you?\n> ")
    cont = ""
    while cont in ['Y','y',""]:
        stack_list = create_stack()
        print(stack_list)
        print("Note: You may enter 'R' at any time to reset the game.")
        while all([len(i) == 0 or i.count(i[0]) == 4 for i in stack_list]) == False:
            inp_req = True
            user_inp = re.split(r"[,\s]",input("Enter your move: "))
            try:
                orig, final = user_inp
            except ValueError:
                if user_inp[0] in ['R','r']:
                    inp_req = False
                    break
                else:
                    print("Incorrect Input!")
                    continue
            orig_ind = int(orig)-1
            final_ind = int(final)-1
            orig = stack_list[orig_ind]
            final = stack_list[final_ind]
            stack_list[orig_ind], stack_list[final_ind] = move_letters(orig, final)
            print(stack_list)
        if inp_req:
            print(inp_req)
            cont = input("> Another round?[Y/n]\n> ")
        else:
            print(inp_req)
            continue
    #cont = 'y'
    #while cont=='y':
    #stack_disp();
    #user_inp();
