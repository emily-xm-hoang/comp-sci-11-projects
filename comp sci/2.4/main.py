file = open("2.4/responses.csv")

junk = file.readline()
data = file.readline()
datalist = data.split(",")
print(datalist)

