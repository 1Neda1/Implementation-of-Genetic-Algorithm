import Gene

#define an object of class Gene
sina = Gene.Gene()

#main program
pool = sina.population()
#print(pool)
keys = sorted(list(pool.keys()))
#print(keys)
parent1 = pool[keys[-1]]
parent2 = pool[keys[-2]]
#print(parent1, parent2)
offcross = sina.crossover(parent1, parent2)
#print(offcross)
offmute1 = sina.mutation(parent1)
#print(offmute1)
offmute2 = sina.mutation(parent2)
#print(offmute2)

#a loop to find how many mutations is needed to create offspring from its parents
while True:
    offcross = sina.crossover(parent1, parent2)
    if offcross == sina.samp:
        print("Crossover!")
        print("Parents are = ", parent1, " and ", parent2)
        print("Offspring is = ", offcross )
        break
    else:
        sa = offcross
        count = 0
        while offcross != sina.samp:
            offcross = str(sina.mutation(offcross))
            count += 1
        print("Mutations!")
        print("Parents are = ", parent1, " and ", parent2)
        print("number of mutations = ", count)
        break

