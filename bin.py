def main():
    nr1 ="1001"
    nr1 = int(nr1 ,2)

    nr2 = "0101"
    nr2 = int(nr2, 2)

    NR = str(bin(nr1 | nr2))
    nr = NR[2:]

    print(nr)

main()
