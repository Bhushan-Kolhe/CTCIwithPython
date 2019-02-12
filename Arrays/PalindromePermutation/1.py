if __name__ == '__main__':
    s = input('Enter the string: ')
    s = s.replace(' ','')
    s = s.replace('.','')
    s = s.replace("'",'')
    s = s.replace(':','')
    s = s.replace(',','')
    s = s.lower()
    
    h = [0 for i in range(26)]
    oddCount = 0

    for char in s:
        h[ord(char)%26] += 1
    
    for i in h:
        if i % 2 != 0:
            if oddCount > 0:
                print('False')
                quit()
            oddCount +=1
    
    print("True")