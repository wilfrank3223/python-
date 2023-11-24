import pickle

votantes = set()  # Cambiado a un conjunto para almacenar identificaciones únicas de votantes

n = int(input("¿Cuál sería la cantidad de votantes que deseas ingresar? "))
for i in range(n):
    nombreVotante = input("Nombre del votante: ")
    idVotante = int(input("Identificación del votante: "))
    
    votantes.add(idVotante)  # Añadir la identificación al conjunto de votantes

class Eleccion:
    def __init__(self):
        self.votantes_que_han_votado = set()  # Conjunto para almacenar las identificaciones de los votantes que han votado
        self.candidatos = self.cargarResultados()
#Nombre de cantidatos y con el contador en ceros
    def inicializarCandidatos(self):
        return {
            'Nicolas': 0,
            'Wilfrank': 0,
            'Martin': 0,
            'Marlon': 0,
            'Voto Blanco': 0
        }

    def registrarVoto(self, candidato, id_votante):
        if id_votante not in self.votantes_que_han_votado:
            if candidato in self.candidatos:
                self.candidatos[candidato] += 1
                self.votantes_que_han_votado.add(id_votante)  # Añadir la identificación al conjunto de votantes que han votado
                print(f'Voto registrado para {candidato}.')
            else:
                print('Candidato no válido.')
        else:
            print('Este votante ya ha votado.')
#Mostrar resultado parciales
    def mostrarResultadosParciales(self):
        print('Resultados parciales:')
        for candidato, votos in self.candidatos.items():
            print(f'{candidato}: {votos} votos')
#Mostrar ganador
    def mostrarGanador(self):
        ganador = max(self.candidatos, key=self.candidatos.get)
        votos_ganador = self.candidatos[ganador]
        print(f'\nEl ganador es {ganador} con {votos_ganador} votos.')
#Guardar resultados
    def guardarResultados(self):
        with open('resultados.pkl', 'wb') as f:
            pickle.dump(self.candidatos, f)
#Cargar los resultados anteriores
    def cargarResultados(self):
        try:
            with open('resultados.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return self.inicializarCandidatos()

eleccion = Eleccion()
#Opciones de menu interactivo
while True:
    print("\n------ Menú ------")
    print("1. Registrar Voto")
    print("2. Mostrar Resultados Parciales")
    print("3. Mostrar Resultados Finales")
    print("4. Guardar y Salir")
    
    opcion = input("Seleccione una opción (1/2/3,4): ")
#Opciones del menu interactivo del votante
    if opcion == '1':
        candidato = input("Ingrese el nombre del candidato: ")
        id_votante = int(input("Ingrese la identificación del votante: "))
        eleccion.registrarVoto(candidato, id_votante)
    elif opcion == '2':
        eleccion.mostrarResultadosParciales()
    elif opcion == '3':
        eleccion.mostrarGanador()
        print("Resultados guardados. Muchas gracias por votar.")
        break
    elif opcion == '4':
        eleccion.guardarResultados()
        print("Resultados guardados. Saliendo.")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
