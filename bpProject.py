import Gene

#define an object of class Gene
Var = Gene.Gene()

#main program
pool = Var.population()
#print(pool)
keys = sorted(list(pool.keys()))
#print(keys)
parent1 = pool[keys[-1]]
parent2 = pool[keys[-2]]
#print(parent1, parent2)
offcross = Var.crossover(parent1, parent2)
#print(offcross)
offmute1 = Var.mutation(parent1)
#print(offmute1)
offmute2 = Var.mutation(parent2)
#print(offmute2)

#a loop to find how many mutations are needed to create offspring from its parents
while True:
    offcross = Var.crossover(parent1, parent2)
    if offcross == Var.samp:
        print("Crossover!")
        print("Parents are = ", parent1, " and ", parent2)
        print("Offspring is = ", offcross )
        break
    else:
        sa = offcross
        count = 0
        while offcross != Var.samp:
            offcross = str(Var.mutation(offcross))
            count += 1
        print("Mutations!")
        print("Parents are = ", parent1, " and ", parent2)
        print("number of mutations = ", count)
        break

