if __name__ == '__main__':
    s1 = input('Enter the 1st string: ')
    s2 = input('Enter the 2nd string: ')
    res = "permutation"
    counts = [0 for i in range(128)]

    if len(s1) != len(s2):
        print('{} is not a permutation of {}'.format(s1,s2))
        quit()

    for char in s1:
        counts[ord(char)] += 1
    
    for char in s2:
        counts[ord(char)] -= 1
        if counts[ord(char)] < 0:
            print('{} is not a permutation of {}'.format(s1,s2))
            quit()

    print('{} is a permutation of {}'.format(s1,s2))