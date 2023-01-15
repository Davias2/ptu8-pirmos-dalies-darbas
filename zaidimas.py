import random
while True:

    def zaidimas():
        zaidejas = input("Ka renkates: 's' yra sulinys, 'l' yra lapas, 'z' yra zirkles?: ")
        kompiuteris = random.choice(['s', 'l', 'z'])

        if zaidejas == kompiuteris:
            return 'Lygiosios'
        
        if pergale(zaidejas, kompiuteris):
            return 'JUS LAIMEJOTE'
        
        return 'Jus pralaimejote!'

    def pergale(dalyvis, priesininkas):

        if (dalyvis == 's' and priesininkas == 'z') or (dalyvis == 'z' and priesininkas == 'l') or (dalyvis == 'l' and priesininkas == 's'):
            return True

    pakartoti = input('Pradedame zaidima? y/n: ')
    if pakartoti.lower() != 'y':
        break

    print(zaidimas())
