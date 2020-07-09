def inf_tree(string, crr_val):
    if string == '':
        return crr_val
    
    crr_pos = string[0]
    string = string[1:]
        
    if crr_pos == 'P':
        return inf_tree(string, crr_val)
    elif crr_pos == 'L':
        return inf_tree(string, crr_val*2)
    elif crr_pos == 'R':
        return inf_tree(string, crr_val*2 + 1)
    elif crr_pos == '*':
        return inf_tree(string, crr_val*2) + inf_tree(string, crr_val*2 + 1) + inf_tree(string, crr_val)


print(inf_tree('L*R', 1))