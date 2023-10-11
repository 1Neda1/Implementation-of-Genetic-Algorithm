import random

class Gene:

    # build constructor to initiate sample chromosome
    def __init__(self) :
        self.samp = '1001' #'100110101110111110111010' کروموزوم نمونه اصلی با طول 24
   
    #initialize function to create chromosomes with len 24 randomly
    def initialize():
        chrom = ''
        for i in range (4): # کروموزوم رو 4 تایی تعریف کردم که راحت تر خروجی بگیرم. طبق صورت سوال اینجا باید 24 تایی باشه
            chrom += str(random.randint(0, 1))
        return chrom
    
    #fitness function to evalute similarity between target and sample chromosomes and return the similarity percentage
    def fitness(target, sample):
        mismatch = 0
        for i in range(len(sample)):
            if target[i] != sample[i]:
                mismatch += 1
        return ((len(sample) - mismatch) / len(sample)) * 100
    
    #population functoin to generate a population of 100 chromosomes and return as a dictionary : {fitness percentage : chromosome}
    def population(self):
        gene_source = {}
        for i in range(10):
            value = Gene.initialize()
            key = Gene.fitness(self.samp ,value)
            gene_source[key] = value
        return gene_source

    #crossover function that use half of each parent chromosome and create the offspring
    def crossover(self, parent1, parent2):
        offspring1 = parent1[0:len(parent1)//2] + parent2[len(parent2)//2:]
        offspring2 = parent2[0:len(parent2)//2] + parent1[len(parent1)//2:]
        if Gene.fitness(self.samp, offspring1) > Gene.fitness(self.samp, offspring2):
            return offspring1
        else:
            return offspring2
    
    #mutation function to apply random mutations in parents chromosomes and create the offspring 
    def mutation(self, parent):
        indx = random.randint(0, len(parent) - 1)
        mut_parent = list(parent)
        mut_parent[indx] = str(1 - int(parent[indx]))
        return "".join(mut_parent)