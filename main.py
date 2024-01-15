from create_stack import create_stack
from move_letters import move_letters
from disp_func import stack_disp, inc_move, new_game
import re

if __name__ == "__main__":
    name = input("Hello Player!\n\n> What should I call you?\n> ")
    cont = ""
    cnt = 0
    while cont in ['Y','y',""]:
        stack_list = create_stack()
        if not cnt:
            print("\nNote:\n  R: Reset\n  Q: Quit")
        cnt+=1
        print(f"\nGame {cnt} begins!")
        stack_disp(stack_list)
        while all([len(i) == 0 or i.count(i[0]) == 4 for i in stack_list]) == False:
            inp_req = True
            user_inp = re.split(r"[,\s]",input("\nEnter your move: "))
            try:
                orig, final = user_inp
            except ValueError:
                if user_inp[0] in ['R','r']:
                    inp_req = False
                    break
                elif user_inp[0] in ['Q','q']:
                    inp_req = False
                    cont = 'N'
                    break
                else:
                    print(f"\n{inc_move()}, {name}!")
                    continue
            orig_ind = int(orig)-1
            final_ind = int(final)-1
            orig = stack_list[orig_ind]
            final = stack_list[final_ind]
            try:
                stack_list[orig_ind], stack_list[final_ind] = move_letters(orig, final)
                stack_disp(stack_list)
            except TypeError:
                print(f"\n{inc_move()}, {name}!")
        if inp_req:
            cont = input(f"> {new_game()}, {name}?[Y/n]\n> ")
        else:
            continue
