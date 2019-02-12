if __name__ == '__main__':
    s1 = input('Enter the 1st string: ')
    s2 = input('Enter the 2nd string: ')

    if len(s1) == len(s2):
        flag = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if flag > 0:
                    print('False')
                    quit()
                flag = 1
    elif abs(len(s1)-len(s2)) == 1:
        if len(s1) < len(s2):
            j = 0
            flag = 0
            for i in range(len(s1)):
                if s1[i] != s2[j]:
                    if flag > 0:
                        print('False')
                        quit()
                    flag = 1
                    j += 1
                j += 1
        else:
            j = 0
            flag = 0
            for i in range(len(s2)):
                if s2[i] != s1[j]:
                    if flag > 0:
                        print('False')
                        quit()
                    flag = 1
                    j += 1
                j += 1
    else:
        print('False')
        quit()
    print('True') 