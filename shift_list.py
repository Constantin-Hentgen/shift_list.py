liste = ['h','e','l','l','o']
temp = liste[0]

for i in range(0,len(liste)-1):
    liste[i] = liste[i+1]
liste[-1] = temp

print(liste)
