



#Ethan Yitzhaky

#step 1
import csv
dataset=open('Data.csv','r')
data=csv.reader(dataset)

for i in data:
    print(i)

#step 2

dataset.seek(0)
data=csv.reader(dataset)
with open('stats.txt','w') as stats:
    for i in data:
        if i[0]=='Month':
            continue
        elif i[0]=='2022':
            break
        sume=0
        for j in range(len(i)):
            if j==0:
                continue
            num=int(i[j])
            sume+=num
        stats.write(f'{i[0]},{sume}\n')

#step 3
import matplotlib.pyplot as plt
plt.figure(1)
stats=open('stats.txt','r+')
years=[]
values=[]
for i in stats:
    data=i.split(',')
    years.append(data[0])
    values.append(int(data[1].replace('\n','')))
plt.bar(years,values)
plt.title('total cars sold by year')
plt.xlabel('years')
plt.ylabel('amounts of cars')
plt.show()

#step 4
dataset.seek(0)
data=csv.reader(dataset)
num=0
sums=[]
for i in data:
    if i[0]=='2021' or i[0]=='2022':
        sume=[]
        for j in range(1,7):
            num=int(i[j])
            sume.append(num)
        sums.append(sum(sume))

growthrate=((sums[1]-sums[0])/sums[1])/100
stats.write(f'growth rate,{growthrate}\n')

dataset.seek(0)
data=csv.reader(dataset)
ans=[]
for i,li in enumerate(data):
    if i==0:
        months=li[7:13]
    elif i==10:
        for j in li[7:13]:
            sales=int(j)+int(j)*-0.017
            ans.append(sales)
stats.write(f'last 6 months of 2022,{ans}\n')

#step 5
plt.figure(2)
plt.barh(months,ans)
plt.xlabel('cars sold')
plt.ylabel('months')
plt.grid()
plt.show()


