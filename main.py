from create_stack import create_stack
from letter_func import move_letters, solvable_check
from disp_func import stack_disp, prompts
import re

if __name__ == "__main__":
    name = input("Hello Player!\n\n> What should I call you?\n> ")
    cont = ""
    cnt = 0
    while cont in ['Y','y',""]:
        stack_list = create_stack()
        if not cnt:
            print("\nNote:\n  R: Reset\n  Q: Quit\n  H: Hint")
        cnt+=1
        print(f"\nGame {cnt} begins!")
        stack_disp(stack_list)
        while all([len(i) == 0 or i.count(i[0]) == 4 for i in stack_list]) == False:
            s = solvable_check(stack_list, len(stack_list))
            if not s:
                break
            inp_req = True
            user_inp = re.split(r"[,\s]",input("\nEnter your move: "))
            try:
                orig, final = list(filter(lambda x: x!='', user_inp))
            except ValueError:
                if user_inp[0] in ['R','r']:
                    inp_req = False
                    break
                elif user_inp[0] in ['Q','q']:
                    inp_req = False
                    cont = 'N'
                    break
                elif user_inp[0] in ['H','h']:
                    print(f"\n{s}")
                    continue
                else:
                    print(f"\n> {prompts(True)}, {name}!")
                    continue
            orig_ind = int(orig)-1
            final_ind = int(final)-1
            try:
                stack_list[orig_ind], stack_list[final_ind] = move_letters(stack_list[orig_ind], stack_list[final_ind])
                stack_disp(stack_list)
            except TypeError:
                print(f"\n> {prompts(True)}, {name}!")
            except IndexError:
                print(f"\n> {prompts(True)}, {name}!")
        if inp_req and s:
            cont = input(f"> {prompts(False)}, {name}?[Y/n]\n> ")
        elif not s:
            cont = input(f"> The game has become unsolvable. {prompts(False)}, {name}?[Y/n]\n> ")
        else:
            continue
