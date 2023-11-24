class VotacionApp:
    def __init__(self):
        self.votantes_registrados = set()
        self.votos = {'Candidato1': 0, 'Candidato2': 0, 'CandidatoC': 0}

    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registro del Votante")
            print("2. Ingreso al Sistema de Votación")
            print("3. Votar por un Candidato")
            print("4. Mostrar Ganador")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                self.registro_votante()
            elif opcion == '2':
                self.ingreso_sistema()
            elif opcion == '3':
                self.votar()
            elif opcion == '4':
                self.mostrar_ganador()
            elif opcion == '5':
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def registro_votante(self):
        votante_id = input("Ingrese el ID del votante: ")
        self.votantes_registrados.add(votante_id)
        print("Votante registrado exitosamente.")

    def ingreso_sistema(self):
        votante_id = input("Ingrese el ID del votante: ")
        if votante_id in self.votantes_registrados:
            print("Ingreso al sistema exitoso.")
        else:
            print("Votante no registrado. Regístrese antes de ingresar al sistema.")

    def votar(self):
        votante_id = input("Ingrese el ID del votante: ")
        if votante_id in self.votantes_registrados:
            if not self.ya_voto(votante_id):
                print("--- Candidatos ---")
                for candidato in self.votos:
                    print(candidato)

                candidato_elegido = input("Ingrese el nombre del candidato por el que desea votar: ")

                if candidato_elegido in self.votos:
                    self.votos[candidato_elegido] += 1
                    print("Voto registrado exitosamente.")
                else:
                    print("Candidato no válido.")
            else:
                print("Ya has votado. No se permite votar más de una vez.")
        else:
            print("Votante no registrado. Regístrese antes de votar.")

    def ya_voto(self, votante_id):
        # Verifica si el votante ya ha votado
        return votante_id in self.votantes_registrados and votante_id in [votante['votante_id'] for votante in self.votos]

    def mostrar_ganador(self):
        total_votos = sum(self.votos.values())
        if total_votos == 0:
            print("Aún no hay votos registrados.")
        else:
            ganador = max(self.votos, key=self.votos.get)
            votos_ganador = self.votos[ganador]
            print(f"\n--- Resultado de las Votaciones ---")
            print(f"El ganador es {ganador} con {votos_ganador} votos.")

if __name__ == "__main__":
    app = VotacionApp()
    app.menu_principal()
