from random import randint

def create_stack():
    stack_cnt = randint(3, 7)
    stack_list = []
    cnt_stack = [0] * stack_cnt
    i = 0
    while i < stack_cnt:
        stack = []
        while len(stack) != 4:
            ord_val = randint(65, 64 + stack_cnt)
            char = chr(ord_val)
            if cnt_stack[ord_val - 65] < 4:
                cnt_stack[ord_val - 65] += 1
                stack.append(char)
        if any([len(set(stack)) == 1]):
            i = 0
            stack_list = []
            cnt_stack = [0] * stack_cnt
        else:
            i += 1
            stack_list.append(stack)
    return stack_list + [[],[]]
