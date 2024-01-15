from disp_func import inc_move

def move_letters(orig, final):
    if len(final)<4:
        if len(final)==0 or final[-1]==orig[-1]:
            prev_val = orig[-1]
            while len(final)<5 and orig[-1]==prev_val:
                prev_val=orig[-1]
                final.append(orig.pop())
                if len(orig)==0:
                    break
        else:
            #print(inc_move())
            return None
    else:
        #print(inc_move())
        return None
    return orig, final
