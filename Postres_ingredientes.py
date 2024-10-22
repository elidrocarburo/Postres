class Postres:
    def __init__(self):
        self.recetas = {}

    def mostrar_recetas(self, receta):
        if receta in self.recetas:
            print(f"Ingredientes de {receta}: {', '.join(self.recetas[receta])}")
        else:
            print(f"No existe la receta para {receta}.")

    def recetario_completo(self):
        if not self.recetas:
            print("Aún no hay recetas, introduzca una con la opción '3. Agregar receta'.")
        else:
            print("Recetario:")
            for receta in sorted(self.recetas):
                print (f"- {receta}: {", " .join(self.recetas[receta])}")

    def agregar_receta(self):
        receta = input("¿Qué receta desea agregar?: ")
        if receta in self.recetas:
            print(f"La receta {receta} ya existe, ingrese otra receta.")
            return
        
        ingredientes = []
        while True:
            ingrediente = input(f"¿Qué ingredientes lleva la receta {receta}?: ")
            if ingrediente.lower() == '':
                break
            ingredientes.append(ingrediente)

        self.recetas[receta] = ingredientes
        print(f"Receta {receta} agregada con los siguientes ingredientes: {", ".join(ingredientes)}")

    def eliminar_receta(self):
        receta = input("¿Qué receta desea eliminar?: ")
        if receta in self.recetas:
            del self.recetas[receta]
            print(f"Receta {receta} eliminada.")
        else:
            print("La receta no existe / ya fue eliminada, intente de nuevo.")

    def agregar_ingrediente(self):
        receta = input("¿A qué receta desea agregarle un ingrediente?: ")
        if receta in self.recetas:
            ingrediente = input(f"¿Qué ingrediente desea agregarle a la receta {receta}?")
            self.recetas[receta].append(ingrediente)
            print(f"Ingrediente {ingrediente} agregado a la receta {receta}")
        else:
            print(f"No existe la receta {receta}")
    
    def eliminar_ingrediente(self):
        receta = input("¿A qué receta desea eliminarle un ingrediente?: ")
        if receta in self.recetas:
            ingrediente = input(f"¿Qué ingrediente desea eliminar a la receta {receta}?")
            if ingrediente in self.recetas[receta]:
                self.recetas[receta].remove(ingrediente)
                print(f"Ingrediente {ingrediente} eliminado de la receta {receta}")
            else:
                print(f"Ya ha eliminado / No existe ese ingrediente dentro de la receta {receta}.")
        else:
            print(f"No existe la receta {receta}")

    def eliminar_ingredientes_repetidos(self):
        todos_los_ingredientes = {}
        for receta, ingredientes in self.recetas.items():
            for ingrediente in ingredientes:
                if ingrediente in todos_los_ingredientes:
                    todos_los_ingredientes[ingrediente] += 1
                else:
                    todos_los_ingredientes[ingrediente] = 1
    
        ingredientes_a_eliminar = {ingrediente for ingrediente, cuenta in todos_los_ingredientes.items() if cuenta > 1}

        for receta in self.recetas:
            self.recetas[receta] = [ingrediente for ingrediente in self.recetas[receta] if ingrediente not in ingredientes_a_eliminar]

        print("Se han eliminado los ingredientes repetidos de todas las recetas.")

recetario = Postres()

while True:
    opción = input("Recetario de postres. Ingrese una de nuestras siguientes opciones:"
                   "\n 1. Mostrar ingredientes"
                   "\n 2. Mostrar recetario completo"
                   "\n 3. Agregar receta"
                   "\n 4. Agregar ingrediente"
                   "\n 5. Eliminar ingrediente"
                   "\n 6. Eliminar receta"
                   "\n 7. Eliminar ingredientes iguales"
                   "\n 8. Cerrar programa"
                   "\n")
    if opción == "1":
        receta = input("¿Qué receta desea ver?: ")
        recetario.mostrar_recetas(receta)
    if opción == "2":
        recetario.recetario_completo()
    elif opción == "3":
        recetario.agregar_receta()
    elif opción == "4":
        recetario.agregar_ingrediente()
    elif opción == "5":
        recetario.eliminar_ingrediente()
    elif opción == "6":
        recetario.eliminar_receta()
    elif opción == "7":
        recetario.eliminar_ingredientes_repetidos()
    elif opción == "8":
        break
    else:
        print("Opción incorrecta, introduzca una de las ya establecidas.")