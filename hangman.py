from random import choice
def word_generator():
    with open("wordlist.txt","r") as f:
        lines = f.readlines()
        #print(lines)
    f.close()
    lines = [i.strip("\n") for i in lines]
    #print(lines)
    return choice(lines)
    
word = word_generator()
print("LENGTH : {}".format(len(word)))
guess = ""
turns = int(len(word)*1.5)
unguessed=0
while True:
    print("You are left with {} turns".format(turns))
    inp = input("Make a guess: ")
    turns-=1
    unguessed=0
    if inp in word:
        guess = guess+inp
    for i in word:
        if i in guess:
            print(i,end="")
        else:
            unguessed+=1
            print('*',end="")
    if unguessed==0:
        print("WOn")
        break
    if turns ==0:
        print("Ran out of turns")
        break
