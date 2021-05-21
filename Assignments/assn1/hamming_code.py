def matmult(H, y):
    l = len(H)
    result = [0]*l
    for i in range(0,l):
        for j in range(0,7):
            result[i] += int(H[i][j])*int(y[j])
            result[i] %= 2
    return result

H = [[1,0,1,0,1,0,1],[0,1,1,0,0,1,1],[0,0,0,1,1,1,1]]
R = [[0,0,1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]

f = open("input.txt","r")
filedata = f.read().splitlines()
firsttime = 0
for data in filedata:
    if data!="":
        if len(data)%14!=0:
            if firsttime == 1:
                print('\n')
            print("INVALID",end='')
            firsttime = 1
            continue
        ans = ""
        error = 0
        for i in range(0,len(data),14):
            fi = data[i:i+7]
            se = data[i+7:i+14]
            flag = 0
            result = matmult(H,fi)
            allzero = [0,0,0]
            if result != allzero:
                error += 1
                flag = 1
                for j in range(0,7):
                    temp = [x[j] for x in H]
                    if temp == result:
                        if fi[j]=='0':
                            fi = fi[0:j]+"1"+fi[j+1:]
                        else:
                            fi = fi[0:j]+"0"+fi[j+1:]
                        break
            result = matmult(H,se)
            if result != allzero:
                if flag == 0:
                    error += 1
                for j in range(0,7):
                    temp = [x[j] for x in H]
                    if temp == result:
                        if se[j]=='0':
                            se = se[0:j]+"1"+se[j+1:] 
                        else:
                            se = se[0:j]+"0"+se[j+1:]
                        break
            trans_fi = matmult(R,fi) 
            trans_se = matmult(R,se)
            total = "".join([str(x) for x in trans_fi+trans_se])
            ans += chr(int(total,2))
        if firsttime == 1:
            print('\n')
        print(ans)
        print(error*100//(len(data)//14), "%",end='')
        firsttime = 1




