import pickle

numbers = [1,2,3,4,5,6,7]

with open("num_pik.dat", "wb") as file:
    pickle.dump(numbers,file)
    #No need to close with "with"

with open("num_pik.dat", "rb") as file:
    data = pickle.load(file)