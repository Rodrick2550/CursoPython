class Student:
    Nombre = None
    Calificacion = None

    def __init__(self, Calificacion) :
        self.Nombre = 'Rodrigo'
        self.Calificacion = Calificacion
        if(Calificacion < 6):
            print('Alumno reprobado')
        else:
            print('Alumno Aprobado')
   
Nota = int(input('Ingresa la calificacion del estudiante \n'))
Estudiante = Student(Nota)
#print(Estudiante)