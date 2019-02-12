def toggle(b, x):
    if x < 0:
        return b
    
    mask = 1 << x
    if b & mask == 0:
        b |= mask
    else:
        b &= ~mask
    return b

if __name__ == '__main__':
    s = input('Enter the string: ')
    s = s.replace(' ','')
    s = s.replace('.','')
    s = s.replace("'",'')
    s = s.replace(':','')
    s = s.replace(',','')
    s = s.lower()
    b = 0

    for char in s:
        x = ord(char)%26
        b = toggle(b, x)
    
    if b & (b-1) == 0:
        print('True')
    else:
        print('False')
