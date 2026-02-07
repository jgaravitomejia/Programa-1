#Juan Sebsastian Garavito
def main():
    nombres=[]
    notas=[]
    estudiantes=input("Ingresa los nombres y notas de los esrudiantes: ")
    a=estudiantes.split()
    for i in range(0,len(a),2):
        nom=a[i]
        no=a[i+1]
        nombres.append(nom)
        notas.append(float(no))
    for i in range(len(notas)):
        if notas[i]>=3.0:
            print(nombres[i])
main()