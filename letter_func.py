def move_letters(orig, final):
    orig = orig.copy()
    final = final.copy()
    if len(final)<4 and len(orig)>0:
        if len(final)==0 or final[-1]==orig[-1]:
            prev_val = orig[-1]
            while len(final)<4 and orig[-1]==prev_val:
                prev_val=orig[-1]
                final.append(orig.pop())
                if len(orig)==0:
                    break
        else:
            return None
    else:
        return None
    return [orig, final]

def solvable_check(stack_list, length):
    stack = stack_list.copy()
    for i in range(length-1):
        flag1 = False
        flag2 = False
        if len(stack[i]) == 4 and len(set(stack[i])) == 1:
            continue
        if len(set(stack[i])) == 1:
            flag1 = True
        elif len(stack[i]) == 0:
            flag2 = True
        for j in range(i+1,length):
            if len(stack[j]) == 4 and len(set(stack[j])) == 1:
                continue
            if len(set(stack[j])) == 1 and flag2:
                continue
            elif len(stack[j]) == 0 and flag1:
                continue
            if move_letters(stack[i], stack[j]):
                last = stack[i][-1]
                if move_letters(stack[j], stack[i]):
                    if stack[i].count(last) > stack[j].count(last) or (stack[i].count(last) == stack[j].count(last) and len(stack[i]) < len(stack[j])):
                        return f"Hint: {j+1}, {i+1}"
                return f"Hint: {i+1}, {j+1}"
            elif move_letters(stack[j], stack[i]):
                return f"Hint: {j+1}, {i+1}"
    return None
