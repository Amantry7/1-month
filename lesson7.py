# num1 = 9 
# num2 = 0 
# print(num1 / num2) 

# исключение - try  
# try: 
#     num1 = 10 
#     num2 = 0 
#     print(num1 // num2)
# except ZeroDivisionError: 
#     print(num1) 
    
    
# while True:
#     try: 
#         num1 = int(input("Ввдиете первое число: ")) 
#         num2 = int(input("Ввдиете второе число: ")) 
#         print(f'результат сложение: {num1+num2}') 
#         print(f"результат вычитание: {num1-num2}") 
#         print(f"результат умножение: {num1*num2}") 
#         try: 
            
#             print(f"результат деление: {num1//num2}") 
#         except: 
#             print("ты чо совсем тово")     
        
#     except ValueError: 
#         print("Введите только число! ")


# name = "ваня" 
# try: 
#     print(name_1) 
# except: 
#     print("я не понимаю") 

# множество set frozen
# dicti = {"name": "Amina"}
# num = {"Amina", "Nurgeldi", "Nurbek", "Aman"}
# print(type(dicti),type(num))
# print(num) 
# try:
# нет индекса дебил
#     print(num[1])
# except: 
#     print("Nurgeldi")


# users = {"Amina", "Nurgeldi", "Nurbek", "Aman","Amina", "Aman"}  
# print(users)

# num = [4,32432,432,432,432,4,3243,432,4,324,3,4,23423,44,543,55,6,35,25,2] 
# duble = set(num)
# num = list(duble) 
# print(duble) 

# users = {1, "Amina", "Nurgeldi", "Nurbek", "Aman","Amina", "Aman"}  
# users.add("sany") 
# users.add("1")
# print(users)
# try: 
#     print(users[1,3])
# except: 
#     print("set  не может делать срезы") 
 
 
# set изменяемый тип данный 


#frozenset  тип данных 

# users = {1, "Amina", "Nurgeldi", "Nurbek", "Aman","Amina", "Aman"}  
# userf= frozenset({1, "Amina", "Nurgeldi", "Nurbek", "Aman","Amina", "Aman"}) 
# print(users) 
# print(userf)