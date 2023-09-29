student = {'name': 'Aman', 'age': '16', 'city': 'Osh', 'pt': 'меня зовут', 'fr': 'и мне'} 
# print(student)  
# print(student['age']) 
# print(student['pt'], student['name'], student['fr'], student['age']) 
# student['surname'] = 'rfr' 
# print(student)  
# keys = student.keys() 
# print(keys) 
# items  = student.items
# print(items) 
# values = student.values 
# print(values)

# while True: 
    # num1 = int(input("Введите первое число: ")) 
    # num2 = int(input("Введите второе число: ")) 
    # print(f"результат сложеление: {num1+num2}") 
    # print(f"результат вычитание: {num1-num2}") 
    # print(f"результат умножение: {num1*num2}") 
    # print(f"результат деление: {num1//num2}")  
    
# n = 0 
# while True:  
    
#     n +=10000
#     print(n)  
    

# count = 0 
# while count < 5: 
#     print(count)
    
#     count+= 1 
import random 

user_health = 5
bot_health =5 
while True:
    if user_health ==0 or bot_health ==0:
        break
    else:
        bot = random.choice(["Камень", "Ножницы", "Бумага"])
        user = input("Введите выбор:")
        if user =="Камень":
            if bot =="Камень":
                print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Ножницы":
                bot_health-=1
                print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Бумага":
                user_health -=1
                print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
        elif user =="Ножницы":
            if bot =="Камень":
                user_health -=1
                print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
                
            elif bot =="Ножницы":
                print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Бумага":
                bot_health-=1
                print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
                
                
        elif user =="Бумага":
            if bot =="Камень":
                bot_health-=1
                print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Ножницы":
                user_health -=1
                print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
            elif bot =="Бумага":
                print("Ничья")
        else:
            print("Неверный вариант")