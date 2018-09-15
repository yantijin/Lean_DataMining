# from K_Means import fileread
from K_Means import k_means
from K_Means import generate_k
from Apriori import aprioriGen
from python_util import fileread
from Learn_Apriori import createInitCandidates
from Learn_Apriori import calSupport
if __name__ == "__main__":
    """
    data = fileread("D:/PycharmProjects/DataMining/input.txt")
    #print(data)
    assignment =[]

    zips, centers = k_means(data, 3)
    print(centers)
    for i in zips:
        print(i)

    generate_k(data, 3)
    """
    #assignment = zips[1]
    #point = zips[2]

    data =fileread("testInput.txt")
    print(data)
    c = createInitCandidates(data)
    print(c)
    support = calSupport(data, c)
    print(support)
