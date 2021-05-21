import sys

def valid(data):
    divd = data[0:len(data)-8]
    ans = data[len(data)-8:len(data)-1]
    div1 = "10000011"
    div2 = "00000000"
    divd += "0000000"
    temp = divd[0:8]
    i = 8
    div = ""
    while i < len(divd)+1:
        rem = ""
        if temp[0]=='1':
            div = div1
        else:
            div = div2
        for j in range(0,8):
            if temp[j]==div[j]:
                rem += "0"
            else:
                rem += "1"
        if i == len(divd):
            rem = rem[1:8]
            break
        temp = rem[1:8]
        temp += str(divd[i])
        i += 1
    if rem == ans:
        return 1
    else:
        return 0

count = 0
FLAG = "10101001"
ESC = "10100101"
f = open(sys.argv[1], "r")
flag_read = 0
data = ""
invalid_list = ""
valid_data = ""
while True:
    temp = f.read(8)
    if not temp:
        break
    if flag_read==0 and temp == FLAG:
        flag_read=1
        data = ""
    elif temp == FLAG:
        count += 1
        flag_read = 0
        if(valid(data)==1):
            prev = data[0:8]
            if prev != ESC:
                valid_data += chr(int(prev,2))
            for i in range(8,len(data)-8,8):
                curr = data[i:i+8]
                if prev == ESC:
                    if curr[2]=='1':
                        curr = curr[0:2]+"0"+curr[3:8]
                    else:
                        curr = curr[0:2]+"1"+curr[3:8]
                    valid_data += chr(int(curr,2))
                elif curr!=ESC:
                    valid_data += chr(int(curr,2))
                prev = data[i:i+8]
        else:
            if len(invalid_list) == 0:
                invalid_list += str(count)
            else:
                invalid_list += ","+str(count)
    else:
        data += temp 
print(count)
print(invalid_list)
print(valid_data, end='')
f.close()
