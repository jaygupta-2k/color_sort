from random import randint

def create_stack():
    stack_cnt = randint(3,7)
    stack_list = [[] for i in range(stack_cnt)]
    cnt_stack = [0]*stack_cnt
    for i in stack_list:
        while len(stack_list[stack_list.index(i)])!=4:
            ord_val = randint(65,64+stack_cnt)
            char = chr(ord_val)
            #print(char)
            if cnt_stack[ord_val-65]+1<5:
                cnt_stack[ord_val-65]+=1
                i.append(char)
            #print(cnt_stack)
            #print(stack_list)
    return stack_list+[[],[]]
