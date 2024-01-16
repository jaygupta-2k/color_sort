def move_letters(orig, final):
    orig = orig.copy()
    final = final.copy()
    if len(final)<4 and len(orig)>0:
        if len(final)==0 or final[-1]==orig[-1]:
            prev_val = orig[-1]
            while len(final)<5 and orig[-1]==prev_val:
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
        for j in range(1,length):
            if move_letters(stack[i],stack[j]) or move_letters(stack[j],stack[i]):
                return f"Hint: {i+1}, {j+1}"
    return None
