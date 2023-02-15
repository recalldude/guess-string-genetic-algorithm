import random
import string 
import sys

alphabet = string.ascii_letters + "!'. "
SOLUTION = 'Hello World !'

def get_answer():
    return SOLUTION

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    chro = ''
    for i in range(size):
        chro += get_letter()
    return chro

def is_answer(chrom):
    return chrom == SOLUTION

def get_score(chrom):
    key = get_answer()
    score = 0
    for i in range(len(chrom)):
        if chrom[i] == key[i] : score += 1
    return score / len(chrom)

def get_mean_score(population):
    total = 0
    for chrom in population:
        total += get_score(chrom)
    return total / len(population)

def score(chrom):
    return get_score(chrom)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    # TODO: implement the selection function
    #  * Sort individuals by their fitting score
    #  * Select the best individuals
    #  * Randomly select other 
    #  here bubble sort algorithm
    selection = []
    rank = int(len(chromosomes_list) * 0.7) 
    for i in range(len(chromosomes_list) - 1):
        for j in range(len(chromosomes_list) - 1 - i):
            if score(chromosomes_list[j]) > score(chromosomes_list[j+1]):
                chromosomes_list[j], chromosomes_list[j+1] = chromosomes_list[j+1], chromosomes_list[j]
    selection.extend( chromosomes_list[rank:])
    for i in range(int(len(chromosomes_list) * 0.2)):
        selection.append(chromosomes_list[random.randint(0, rank - 1)])
    return selection

def crossover(parent1, parent2):
    return parent1[0:int(len(parent1)/2)] + parent2[int(len(parent2)/2):]

def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
    chrom = list(chrom)
    chrom[random.randint(0, len(chrom) - 1)] = get_letter() 
    return ''.join(chrom)


def create_population(pop_size, chrom_size):
    population = []
    for i in range(pop_size):
        population.append(create_chromosome(chrom_size))
    return population

def generation(population):
    select = selection(population)
    children = []
    while len(children) < len(select):
        parent1 = select[random.randint(0, len(select)-1)]
        parent2 = select[random.randint(0, len(select)-1)]
        child = crossover(parent1, parent2)
        if random.randint(1, 100) == 1:
            child = mutation(child)
        children.append(child)
    return select + children

def best_chrom(population):
    best = population[0]
    for i in population:
        if get_score(i) > get_score(best): best = i
    return best

def algorithm():
    chrom_size = len(SOLUTION)
    pop_size = int(input('taille population : '))
    population = create_population(pop_size, chrom_size)
    answers = []
    total = 0
    while not answers:
        population = generation(population)
        print(get_mean_score(population), file=sys.stderr)
        #print(population)
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
        total += 1
        print(best_chrom(population))
    print(answers)
    print(total)

algorithm()