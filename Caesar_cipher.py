a = input()

for i in range(26):
    print('Displacement '+str(i)+':')
    for j in range(len(a)):
        ans = ord(a[j])
        if 96 < ans < 123:
            if ans+i > 122:
                ans = ans - 26

            c = chr(ans+i)

            print(c,end='')
        elif 64 < ans < 91:
            if ans+i > 90:
                ans = ans - 26

            c = chr(ans+i)

            print(c,end='')
        else:
            print(a[j],end='')
    print('\n')
