if __name__ =='__main__':
    s = input('Enter a string: ')
    s2 = s.lower()
    h = [0 for i in range(26)]
    res = "Unique"

    for char in s2:
        if h[ord(char) - ord('a')] == 1:
            res = "Not Unique"
            break
        else:
            h[ord(char) - ord('a')] = 1

    print("{} is {}".format(s,res))