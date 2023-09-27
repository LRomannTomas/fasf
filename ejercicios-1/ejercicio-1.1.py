otros_cursos_min = 2.5
otros_cursos_max = 7
promedio = 4
este_curso = 1.5

diferencia_con_min = 100 - este_curso * 100 / otros_cursos_min

diferencia_con_max = 100 - este_curso * 100 // otros_cursos_max

diferencia_con_promedio = 100 - este_curso * 100 / promedio
print("-----------------------")
print(f" - Este curso dura un {diferencia_con_min}% menos que el mas rápido")
print(f" - Este curso dura un {diferencia_con_max}% menos que el mas lento")
print(f" - Este curso dura un {diferencia_con_promedio}% menos que el promedio")

promedio_crudo = 5
este_curso_crudo = 3.5

material_inservible_promedio = 100 - promedio * 100 / 5

material_inservible_este_curso = 100 - este_curso * 100 // 3.5

print("------------------------")
print(f" - un curso promedio elimina un {material_inservible_promedio}% de tiempo vacio") 
print(f" - este curso elimino el {material_inservible_este_curso}% de tiempo vacio") 

print("------------------------")
print(f" - Ver 10 horas de este curso equivale a ver {promedio * 10 // este_curso} horas del promedio")
print(f" - Ver 10 horas de otros cursos equivale a ver {este_curso * 10 / promedio} horas del promedio")