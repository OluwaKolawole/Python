def family_member(father, mother, **children):
    print(father + " is the haed of the family")
    print(mother + " is the wife")
    for c in children.values():
        print("The children are: " + "\n" + c)
family_member(father = "kola", mother = "bisi", daugther = "iremide")
