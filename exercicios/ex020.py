from random import shuffle

list_of_student = []

student1 = str(input('Primeiro aluno: '))
list_of_student.append(student1)

student2 = str(input('Segundo aluno: '))
list_of_student.append(student2)

student3 = str(input('Terceito aluno: '))
list_of_student.append(student3)

student4 = str(input('Quarto aluno: '))
list_of_student.append(student4)

shuffle(list_of_student)

print('A ordem escolhida foi {}'.format(list_of_student))
