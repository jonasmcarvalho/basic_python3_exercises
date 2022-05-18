from random import choice

list_of_student = []

student1 = str(input('Primeiro aluno: '))
list_of_student.append(student1)

student2 = str(input('Segundo aluno: '))
list_of_student.append(student2)

student3 = str(input('Terceito aluno: '))
list_of_student.append(student3)

student4 = str(input('Quarto aluno: '))
list_of_student.append(student4)

raffled = choice(list_of_student)

print('O aluno escolhido foi {}'.format(raffled))
