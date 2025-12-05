''' Action 2 '''
''' Action 3 '''
def ecrire(chaine):
    print(chaine).upper()

ecrire("hello world")

def ecrireXFois(x, chaine):
    for i in range(x):
        ecrire(chaine)