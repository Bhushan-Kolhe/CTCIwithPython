if __name__ == '__main__':
    s = input('Enter the string: ')
    o = ''
    count = 0
    p = s[0]

    for char in s:
        if char != p:
            o += p + str(count)
            count = 1
        else:
            count += 1
        p = char
    o += p + str(count)
    
    if len(s) < len(o):
        print(s)
    else:
        print(o)