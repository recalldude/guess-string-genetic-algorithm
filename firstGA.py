import random
import string 

alphabet = string.ascii_letters + "!'."
SOLUTION = 'fart'

def get_answer():
    return SOLUTION

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    chro = ''
    for i in range(size):
        chro += get_letter()
    return chro

def get_score(chrom):
    key = get_answer()
    score = 0
    for i in range(len(chrom)):
        if chrom[i] == key[i] : score += 1
    return score / len(chrom)

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
    print(selection)
    return selection
