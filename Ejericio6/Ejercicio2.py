class Student:
    Nombre = None
    Calificacion = None

    def __init__(self,Nombre, Calificacion) :
        self.Nombre = Nombre
        self.Calificacion = Calificacion
    def imprimir(self):
       print(f"Nombre del alumno: {self.Nombre}")
       print(f"Nombre del alumno: {self.Calificacion}")

    def evaluar(self):
        if(self.Calificacion < 6):
            print('Reprobado')
        else:
            print('Aprobado')
        


Nombre = input('Ingresa el nombre del alumno \n')
Nota = int(input('Ingresa la calificacion del estudiante \n'))
Estudiante = Student(Nombre, Nota)
Estudiante.imprimir()
Estudiante.evaluar()
#print(Estudiante)