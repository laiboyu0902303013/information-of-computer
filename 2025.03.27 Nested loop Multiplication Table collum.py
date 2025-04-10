result1 = ""
result2 = ""
for j in range(1,10):
    result1=""
    for i in range(1,10):
        result1 = result1 + str(i) + "*" +str(j) + "="+str(i*j) + '\t'
    result2 += result1 + '\n' #'\n' is mean new line
print(result2)