entree = "le test logiciel est essentiel"
nombre_de_mot = 0
for mot in entree.split( ) :
    nombre_de_mot = nombre_de_mot + 1
print(nombre_de_mot)        
 

entree ="le test logiciel est essentiel"
nombre_de_mot = 1
for i in entree :
    if i == " " :
        nombre_de_mot = nombre_de_mot + 1
print(nombre_de_mot)     