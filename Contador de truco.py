cantidad_de_manos=0
pnos=0
pellos=0
gana=int(input("A cuanto se juega?: "))
print("Se juega a",gana)
print("-------------------------------------------------------")
print(f"\nNosotros: {pnos} \nEllos: {pellos}\n")
print("-------------------------------------------------------")

while pnos<gana and pellos<gana:
    p_mano = int(input("Puntos para Nosotros: "))
    pnos=pnos+p_mano
    p_mano= int(input("Puntos para Ellos: "))
    pellos= pellos + p_mano
    cantidad_de_manos = cantidad_de_manos + 1
    print("-------------------------------------------------------")
    print(f"Resultados hasta el momento: Mano {cantidad_de_manos}")
    print(f"\nNosotros: {pnos} \nEllos: {pellos}\n")
    print("-------------------------------------------------------")
    
else:
    print("Fin del juego")