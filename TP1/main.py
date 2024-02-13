file_path = "emd.csv"
emd = []

with open(file_path,'r') as file:
    lines = file.readlines()
    headers = lines[0].strip().split(',')
    
    for line in lines[1:]:
        data = line.strip().split(',')
        x = dict(zip(headers,data))
        emd.append(x)
    

def alphabetical_order():
    return sorted({user["modalidade"] for user in emd})

def fit_unfit():
    n_fit = sum([1 for user in emd if user["resultado"] == "true"],0)
    n_unfit = sum([1 for user in emd if user["resultado"] == "false"],0)
    return n_fit/(n_fit+n_unfit)*100, n_unfit/(n_fit+n_unfit)*100
          
def age_group():
    ages = [int(user["idade"]) for user in emd]
    idx_min = min(ages) // 10 * 10
    idx_max = max(ages)
    
    age_intervals = [f"{i}-{i+4}" for i in range(idx_min, idx_max + 1, 5)]
    
    age_group = {interval: 0 for interval in age_intervals}
    
    for user in emd:
        age = int(user["idade"])
        for interval in age_intervals:
            if age <= int(interval.split('-')[1]):
                age_group[interval] += 1
                break
    return age_group

    
print("Lista ordenada alfabeticamente das modalidades desportivas:\n ", alphabetical_order())
print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:\n ", fit_unfit())
print("\nDistribuição de atletas por escalão etário (escalão = intervalo de 5 anos):\n ", age_group())