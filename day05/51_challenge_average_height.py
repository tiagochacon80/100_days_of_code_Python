student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#La somme de tous les hauteurs
total_heights = 0
for heights in student_heights:
  total_heights += heights #Para saber o total de alturas dos alunos
print(total_heights)


#La quantite d'étudiants
number_of_students = 0
for student in student_heights:
  number_of_students += 1 #Para saber a quantidade de interaçoes do loop
print(number_of_students)


average_students = round(total_heights / number_of_students)
print(f"The average students height is {average_students}")




