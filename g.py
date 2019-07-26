import random
m=1
n=6
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
 print("Rolling the dice....")
 print("the values are..")
 print(random.randint(m,n))
 print(random.randint(m,n))
 print(random.randint(m,n))
 break
roll_again = input("enter yes or y to continue...Roll the dices again?")
print(random.randint(m,n))
print(random.randint(m,n))
print(random.randint(m,n))
