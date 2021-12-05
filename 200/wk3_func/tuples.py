#  Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.

# lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

# t_check = []

# for i in lst_tups:
#     t_check.append(i[2])
   
#########

# Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.

# tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

# seconds = []

# for i in tups:
#     seconds.append(i[1])

    
##############

d = { "k1": 3, "k2": 7, "k3": "some other value"}

# for p in d.items():
#     print("key: {}, value: {}".format(p[0], p[1]))

# refactor 1
for p in d.items():
    k = p[0]
    v = p[1]
    print("key: {}, value: {}".format(k,v)) 


# refactor 2
# for k, v in d.items():
#     print("key: {}, value: {}".format(k,v))

###################

