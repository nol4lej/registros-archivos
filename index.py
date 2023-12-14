import os
import sys
import ast

class ManejadorEstudiantes:
    
    def __init__(self):
        self.estudiante = {}
        
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def main(self):
            print("\nAdministrador de estudiantes\n")
            print("[1.] Guardar estudiante")
            print("[2.] Listar estudiantes")
            print("[3.] Mostrar promedio de curso")
            print("[4.] Salir")
            
            while True:

                opcion = self.input_valido("\nSeleccione una opción (1-4): ", self.validar_numero)

                if opcion == 1:
                    self.guardar_estudiante()
                elif opcion == 2:
                    self.listar_estudiantes()
                elif opcion == 3:
                    self.mostrar_promedio()
                elif opcion == 4:
                    print("\nSaliendo del programa")
                    sys.exit(0)
                else:
                    print("\n[-] Opción no válida. Por favor, seleccione una opción válida.")
                
    
    def guardar_estudiante(self):
        self.limpiar_pantalla()
        print("\n[1] Guardar estudiante")
        print("[!] Para volver atrás escribe: 'salir'.\n")
        while True:
            
            rut = self.input_valido("[+] Ingrese el rut del estudiante (sin puntos, guiones ni dígito verificador): ", self.validar_rut)
            nombre = self.input_valido("[+] Ingrese el nombre del estudiante: ", self.validar_cadena)
            apellido = self.input_valido("[+] Ingrese el apellido del estudiante: ", self.validar_cadena)
            edad = self.input_valido("[+] Ingrese la edad del estudiante: ", self.validar_edad)
            nota = self.input_valido("[+] Ingrese la nota del estudiante (1-7): ", self.validar_nota)
        
            self.estudiante = {
                "rut": rut,
                "nombre": nombre, 
                "apellido": apellido,
                "edad": edad,
                "nota": nota
            }
            
            self.guardar_en_archivo()
            
    def input_valido(self, mensaje, validador):
        while True:
            try:
                valor = validador(input(mensaje))
                return valor
            except ValueError as e:
                print(e)
    
    def validar_rut(self, valor):
        if valor == "salir": self.limpiar_pantalla(), self.main()
        if len(valor) not in {7, 8} or not valor.isdigit():
            raise ValueError("[-] El RUT es inválido, debe tener entre 7 y 8 dígitos.")
        return int(valor)

    def validar_cadena(self, valor):
        if valor == "salir": self.limpiar_pantalla(), self.main()
        if not valor.isalpha():
            raise ValueError("[-] Has ingresado caracteres inválidos. Inténtelo nuevamente.")
        return valor

    def validar_edad(self, valor):
        if valor == "salir": self.limpiar_pantalla(), self.main()
        valor = int(valor)
        if not 1 <= valor <= 100:
            raise ValueError("[-] Has ingresado una edad no válida. Inténtelo nuevamente.")
        return valor
    
    def validar_nota(self, valor):
        if valor == "salir": self.limpiar_pantalla(), self.main()
        try:
            valor_float = float(valor)
            if not 1 <= valor_float <= 7:
                raise ValueError("[-] Has ingresado una nota no válida. Inténtelo nuevamente.")
            return valor_float
        except ValueError:
            raise ValueError("[-] Has ingresado una nota no válida. Inténtelo nuevamente.")

    def validar_numero(self, valor):
        if valor == "salir": self.limpiar_pantalla(), self.main()
        if not valor.isnumeric():
            raise ValueError("[-] Has ingresado un carácter no válido. Inténtelo nuevamente.")
        return int(valor)
    
    def guardar_en_archivo(self):
        try:
            # modo 'a' para agregar al final
            with open("estudiantes.txt", "a") as archivo:
                # convierte el diccionario a una cadena en formato JSON y escribe en una línea
                archivo.write(str(self.estudiante) + '\n')
                
            self.limpiar_pantalla()
            print("\n[+] Estudiante guardado correctamente.")
            self.preguntar_nuevo_estudiante()
        except Exception as e:
            print("[-] Error al guardar el estudiante en el archivo:", e)
    
    def preguntar_nuevo_estudiante(self):
        while True:
            opcion = input("\n¿Deseas ingresar un nuevo estudiante? (Sí/No): ").lower()
            if opcion == 'si' or opcion == 's':
                self.limpiar_pantalla()
                self.guardar_estudiante()
                break
            elif opcion == 'no' or opcion == 'n':
                self.limpiar_pantalla()
                self.main()
                break
            else:
                print("[-] Opción no válida. Por favor, ingresa 'Sí' o 'No'.")
    
    def listar_estudiantes(self):
        self.limpiar_pantalla()
        try:
            with open("estudiantes.txt", "r") as archivo:
                lineas = archivo.readlines()
                print("\nListado de todos los estudiantes guardados:\n")
                for i, linea in enumerate(lineas, start=1):
                    # Convierte la cadena del diccionario a un diccionario real utilizando el módulo ast
                    estudiante = ast.literal_eval(linea.strip())
                    print(f"[ {i} ] Nombre: {estudiante['nombre']} - Apellido: {estudiante['apellido']} - Rut: {estudiante['rut']} - Edad: {estudiante['edad']} - Nota: {estudiante['nota']}")
        except Exception as e:
            print("[-] Error al leer el archivo de estudiantes:", e)
        
        input("\nPresiona Enter para volver al menú principal...")
        self.limpiar_pantalla()
        self.main()
        
    def mostrar_promedio(self):
        self.limpiar_pantalla()
        try:
            with open("estudiantes.txt", "r") as archivo:
                lineas = archivo.readlines()
                notas = [ast.literal_eval(linea.strip())["nota"] for linea in lineas]
                promedio = sum(notas) / len(notas) if len(notas) > 0 else 0
                print(f"El promedio de notas de todos los estudiantes es: {promedio}")
        except Exception as e:
            print("[-] Error al calcular el promedio de notas:", e)
        input("\nPresiona Enter para volver al menú principal...")
        self.limpiar_pantalla()
        self.main()
            
manejador = ManejadorEstudiantes()
manejador.main()