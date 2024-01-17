student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max = -1
#no incluye el ultimo si usas range(1, 10), no incluye el 10, para incluir el 10 deberias usar range(1, 11, x) x es i+=x
for n in student_scores:
    if(n > max):
        max = n 

print(f"The highest score in the class is : {max}. ")