import random

def get_determiner(quantity):   
        if quantity == 1:
            words = ["a", "one", "the"]
        else:
            words = ["some", "many", "the"]

        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word

def get_noun(quantity):
        if quantity==1:
            words =["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        else:
            words=["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        word=random.choice(words)
        return word

def get_verb(quantity, tense):
        if tense=="past":
            words =["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        elif tense=="present"and quantity==1:
            words=["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

        elif tense =="present" and quantity !=1:
            words =["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

        elif tense=="future":
            words=["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        word=random.choice(words)
        return word

 
for i in range(6):
        quantity = random.randint(1, 3)
        tense = random.choice(['past', 'present', 'future'])
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense)
        sentence = f"{determiner.capitalize()} {noun} {verb}."
        print(sentence)








