#4. Să se determine cuvintele unui text care apar exact o singură dată în acel text.
#De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.


#Functia mea.
#Determina cuvintele unui text care apar exact o singură dată 
#Parametrii de intrare: text - string
#Parametrii de iesire res - string 
#Complexitate timp O(n**2)
#Complexitate spatiu O(n), n - nr de cuvinte
def functia_mea(text):
    temp = text.split()
    res = ""
    for word in temp:
        if temp.count(word) == 1:
            res += word + " "
    return res

            

from collections import Counter
#Complexitate timp si spatiu O(n), n - nr de cuvinte
def cuvinte_unice(text):
    cuvinte = text.split()
    frecventa = Counter(cuvinte)
    cuvinte_unice = [cuvant for cuvant, count in frecventa.items() if count == 1]
    return cuvinte_unice

text = "ana are ana are mere rosii ana"
print(cuvinte_unice(text))



#Teste
assert(functia_mea("ana are ana are mere rosii ana") == "mere rosii ")
assert(functia_mea("catelul alerga repede prin parc") == "catelul alerga repede prin parc ")
assert(functia_mea("mere mere mere") == "")
assert(functia_mea("ana") == "ana ")



def main():
    while True:
        text = input("Scrie textul sau 0 pentru exit: ")
        if text == '0':
            break
        print(functia_mea(text))
main()

