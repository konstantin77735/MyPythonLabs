print("Чтобы isSpecial стала равна True," +"\n"
      +"сумма последней цифры целой части "+"и 1-ой цифры дробной части должна быть чётным числом"+"\n"
      "ИЛИ"+"\n"+"1-я цифра целой части больше 1-й цифры дробной части. "+"\n"+"_____")


isSpecial = False

x = float(input("Введите переменную x: "))
print("_____")

# Разделим целую и дробную части числа x
int_part = int(x)
float_part = round(x - int_part, 2) # дробная часть после точки

print(f"int part: {int_part}")
print(f"float part: {float_part}")
print("_____")

# Вычислим последнюю цифру целой части
last_num_of_int= int_part % 10

# Вычислим первую цифру дробной части
first_num_of_float = int(float_part * 10)

# Проверим условие:

# Если сумма последней цифры целой части  и 1-й цифры дробной частей x является чётным числом 
# ИЛИ Если 1-я цифра целой части больше 1-й цифры дробной части. 
    
_sum = last_num_of_int+ first_num_of_float # это сумма последней цифры целой части  и 1-й цифры дробной частей 

print(f"Последняя цифра целой части: {last_num_of_int}")
print(f"1-ая цифра дробной части: {first_num_of_float}")
print("\n")
print(f"Их сумма: {_sum}")
print("_____")


if (_sum) % 2 == 0:
    print("Условие выполняется, сумма чётная.")
elif(int(last_num_of_int / 10) > first_num_of_float):
    print("Условие выполняется, 1-я цифра целой части больше 1-й цифры дробной части. ")
else:
    print("Условие не выполняется.")
    
print("_____")