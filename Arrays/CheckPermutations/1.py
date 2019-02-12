if __name__ == '__main__':
    s1 = input('Enter the 1st string: ')
    s2 = input('Enter the 2nd string: ')
    res = "permutation"

    if len(s1) != len(s2):
        print('{} is not a permutation of {}'.format(s1,s2))
        quit()

    s3 = ''.join(sorted(s1))
    s4 = ''.join(sorted(s2))

    for i in range(len(s1)):
        if s3[i] != s4[i]:
            print('{} is not a permutation of {}'.format(s3,s4))
            quit()

    print('{} is a permutation of {}'.format(s1,s2))

