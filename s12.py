try:
    file = open("companyt.txt")
except:
    print("Invalid")
else:
    data = file.read()
    file.close()
data = data.split("\n")
count1 = 0
count2 = 0
count3 = 0
for i in range(len(data)):
    data[i] = data[i].split()
    data[i][-2] = int(data[i][-2])
    data[i][4] = data[i][4].split("-")
    data[i][-1][0] = int(data[i][-1][0])
  
    if data[i][-1][0] == 1:
        count1 += 1
    elif data[i][-1][0] == 2:
        count2 += 1
    elif data[i][-1][0] == 3:
        count3 += 1

for name,posit,salary,bonus,section in data:
    if bonus > 0 and count3 < count1 > count2:
        print("1-bo'lim")
        break
    elif bonus > 0 and count1 < count2 > count3:
        print("2-bo'lim")
        break
    elif bonus > 0 and count2 < count3 > count1:
        print("3-bo'lim")
        break
