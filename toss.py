import random

heads,tails=0,0
longh,longt=0,0
temph,tempt=0,0
coins=int(input("Enter the number of times you would like the coin to be flipped :"))
printcoin = input("Would you like to visually output the result of each toss? Y/N: ").lower()

for i in range(coins):
    flip = random.randrange(2)
   
    if flip == 0:
        tempt=0
        heads+=1
        temph+=1
        if longh<temph:
            longh=temph
    else:
        temph=0
        tails+=1
        tempt+=1
        if longt<tempt:
            longt=tempt
     
    if printcoin == "y":
        print(flip,end=' ')
print("")             
print("Heads was flipped ",heads , " times or ",heads/coins*100)
print("Tails was flipped ",tails , " times or ",tails/coins*100)
print("Longest times heads in a row :",longh)
print("Longest times tails in a row :",longt)
