#1.Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea 
#într-un text care conține mai multe cuvinte separate prin ” ” (spațiu). De ex. 
#ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".


#Funtia(facuta de mine) calculeaza untimul cuvant din punct de vedere alfabetic dintr-o propozitie
#Parametrii de intrare: string-ul din care cautam ultimul cuvant
#Parametrii de iesire: int- ultimul cuvant (dpdv alfabetic)
#Complexitate timp si spatiu O(n), unde n reprezinta nr de cuvinte
def functi_mea(text):
    words = text.split(" ")
    max=""

    for word in words:
        if word > max:
            max = word
    return max



#Functia generata de ai
#Complexitate timp si spatiu O(n), unde n reprezinta nr de cuvinte
def ultimul_alfabetic(text):
    cuvinte = text.split()
    return max(cuvinte)

text = "Bravo ai terminat problema!"
print(ultimul_alfabetic(text))


#Funtia(facuta de mine) calculeaza untimul cuvant din punct de vedere alfabetic dintr-o propozitie
#Parametrii de intrare: string-ul din care cautam ultimul cuvant
#Parametrii de iesire: int- ultimul cuvant (dpdv alfabetic)
#Complexitate timp O(n), unde n reprezinta nr de cuvinte
#Complexitate de spatiu O(1): nu se creaza efectiv o lista, doar se itireaza elem din text.split
def functi_mea_imbunatatita(text):
    max = ""
    for word in text.split():
        if word > max:
            max = word
    return max



#Teste
assert(functi_mea("Ana are mere rosii si galbene") == "si")
assert(functi_mea("Ana are mere") == "mere")
assert(functi_mea("anna ana") == "anna")
assert(functi_mea("zara zare") == "zare")
assert(functi_mea("Bravo ai terminat problema!") == "terminat")

assert(functi_mea_imbunatatita("Ana are mere rosii si galbene") == "si")
assert(functi_mea_imbunatatita("Ana are mere") == "mere")
assert(functi_mea_imbunatatita("anna ana") == "anna")
assert(functi_mea_imbunatatita("zara zare") == "zare")
assert(functi_mea_imbunatatita("Bravo ai terminat problema!") == "terminat")



def main():
    while True:
        text = input("Scrie textul sau 0 pentru exit: ")
        if text == '0':
            break
        print(functi_mea(text))
main()
