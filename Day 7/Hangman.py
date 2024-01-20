import random
import words
import logos

word = words.world_list[random.randint(0, 2)]
lista = []
palabras =[]

lives = 6

for i in word:
    lista.append("_")
print(logos.logo)
print(f"Pssst, the solution is {word}")


while True:
    if lives == 0:
        print("YOU LOSE.")
        print(logos.stages[0])
        break
    
    if not "_" in lista:
        print("You WON.")
        break
    
    letter = input("Guess a letter: ").lower()
    
    var = 0
    if letter in palabras:
        var = 2
    
    for i in range(0,len(word)):
        if letter==word[i].lower() and var!=2:
            lista[i]=letter
            palabras.append(letter) 
            var = 1
    
    
    
    #x = mySeparator.join(myDict)
    print(f"{' '.join(lista)}")
    if var==0 or var==2:
        if var==2 :
            print("Ya habia adivinado esa letra. -1 vida.")
            
        print(logos.stages[lives])
        lives-=1
        
        

              

