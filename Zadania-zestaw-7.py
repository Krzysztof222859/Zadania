#7

file = open('countries.txt','r')
file_content = file.read()
print( file_content )
file.close()

#8

file = open('countries.txt', 'r')
a =1
for line in file:
    print(f"{a}: {line}", end="")
    a+= 1
    
file.close()

#9

file = open("numbers.txt" , "r")

sum = 0

for i in file:
    sum=sum+int(i)
file.close()

print(sum)

#10

file = open('personally.txt', 'w')

file.write("Krzysztof\nZiętek\nUniwersytet Ekonomiczny w Krakowie\nInformatyka stosowana")
file.close()

#11

file=open("filmtitles", "w")

film_titles= ["Ojciec chrzestny 1", "Ojciec chrzestny 2", "Ojciec chrzestny 3", "Batman", "Spiderman"]

for i in range(0,len(film_titles)):
    file.write(f"{film_titles[i]}\n")
file.close()

#12 

file= open("shopping", "r")

x=str(input("Dodaj produkt do listy: "))

file.write(f"{x}\n")

file.close()


#13

file=open("Paprotniki.txt", "r")
file_content = file.read()
print( file_content )
file.close()


#14

with open("personally.txt", "r") as f:
    for line in f:
        print(line, end="")
#15

x=str(input("Podaj nazwe swojego pliku: "))
file=open(f"{x}", "r")
sum=0
for line in file:
    sum+=1
print(f"File name: {x}, Number of lines: {sum}")    
file.close()


#16

with open("zadanie16.txt","r") as f:
    counter=0
    for line in f:
        print(line)
        counter+=1
        if counter==5:
            input("Press enter...")
            counter=0


#17

f1=open("zadanie18.txt","r")
f2=open("copyy.txt","w")
file_content=f1.read()
f2.write(file_content)
f1.close()
f2.close()

#18

f1=open("zadanie17.txt","r")
f2=open("copy.txt","w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()
    
#19

f1=open("MeatAndFish","r")
f2=open("GrainsAndBread","r")
f3=open("SummingTheTwoOfIt","w")
f1_content=f1.read()
f2_content=f2.read()
f3.write(f1_content + f2_content)
f1.close()
f2.close()
f3.close()

#20

f=open("text_file.txt","w")
liczba=""
for liczba in range(1,51):
    f.write(str(liczba)+"\n")
f.close()

#21

from random import randint
f=open("text_file_randomly.txt","w")
liczba=""
for liczba in range(1,51):
    f.write(str(randint)+"\n")
f.close()

albo

import random
f=open("text_file_randomly.txt","w")
liczba=""
for liczba in range(1,51):
    f.write(str(liczba(random.choice(100,999)))+"\n")
f.close()

to poprawnie

import random
f=open("text_file_randomly.txt","w")
for liczba in range(50):
    f.write(str(random.randint(100,999))+"\n")
f.close()

#22

f=open("superpotegaprogram.txt","w")
f_content=i*i
for i in range (1,11):
f.write(f_content)
f.close

f=open("superpotegaprogram.txt","w")
for i in range(1,11):
    f.write(str(i)+str(i**2)+str(i**3)+"\n")
f.close

inaczej dobrze

f=open("superpotegaprogram.txt","w")
for i in range(1,11):
    f.write(str(i)+', '+str(i**2)+', '+str(i**3)+"\n")
f.close()


#23

f=open("personalies.txt","r")
d=[]
for line in f:
    d.append(line.strip().split(','))

for i in range(1,len(d)):
    print(d[i][0].ljust(10)+d[i][1].ljust(15)+d[i][4].ljust(20))
f.close()


