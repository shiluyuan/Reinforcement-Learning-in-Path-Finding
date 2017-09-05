
import csv

def get_dict(data):
    A_0 = data["original"].values.tolist()
    Z_0 = data["connected"].values.tolist()
    weight = data["weight"].values.tolist()
    
    A = A_0 + Z_0
    Z = Z_0 + A_0
    weight = weight + weight
    A = list(map(lambda x:int(x), A))
    Z = list(map(lambda x:int(x), Z))
    
    A_key = sorted(set(A))
    A_Z_dict={}
    
    for i in range(len(A_key)):
        A_Z_dict[A_key[i]] = []
    
    for i in range(len(A)):
        if Z[i] not in A_Z_dict[A[i]]:
            A_Z_dict[A[i]].append(Z[i])
    
    mydict = A_Z_dict
    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in mydict.items():
           writer.writerow([key, value])
    
    return{"A":A,
           "Z":Z,
           "weight": weight,
           "A_Z_dict":A_Z_dict}