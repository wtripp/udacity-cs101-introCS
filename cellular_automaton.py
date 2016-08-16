
def cellular_automaton(string,pnum,gen):
    values = [128,64,32,16,8,4,2,1]
    strings = ['xxx','xx.','x.x','x..','.xx','.x.','..x','...']
    pattern = {}
    
    i = 0
    while i < len(values):
        if pnum - values[i] >= 0:
            pnum -= values[i]
            values[i] = 1
        else:
            values[i] = 0
        pattern[strings[i]] = values[i]
        i += 1
    generations = {}
    
    j = 0
    while j < gen:
        j += 1
        generations[j] = 'None'
        
    k = 0    
    while k < gen:
        k += 1
        newstring = string[-1] + string + string[0]
        stringline = ''
        for i in range(1,len(newstring)-1):
            char = newstring[i-1] + newstring[i] + newstring[i+1]
            if pattern[char] == 0:
                stringline += '.'
            if pattern[char] == 1:
                stringline += 'x'
        generations[k] = stringline
        string = stringline
    return generations[gen]
