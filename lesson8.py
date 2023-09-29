# summ = lambda num1, num2: num1 + num2  
# summ1 = lambda num1, num2: num1 - num2 
# summ2 = lambda num1, num2: num1 * num2 
# summ3 = lambda num1, num2: num1 // num2 
# nu1 =  int(input("Введите число: ")) 
# nu2 =  int(input("Введите число: ")) 
# result  = summ(nu1,nu2)
# result1  = summ1(nu1,nu2)
# result2 = summ2(nu1,nu2)
# result3  = summ3(nu1,nu2)
# print(f"результат сложение: {result}") 
# print(f"результат вычитание: {result1}") 
# print(f"результат умножение: {result2}") 
# print(f"результат деление: {result3}") 

spisok = [1,2,3,4,5,6,7,8,9,10] 
summ = list(map(lambda i: i*2, spisok))
print(summ)  

# name = ["Aman", "Mergul", "Erbol", "Bakai", 'Nuray'] 
# result = list(map(lambda i: f"{i} - {len(i)}букв",name )) 
# print(result)
# работа файлами 
# file_write = open('users.txt', 'w') 
# file_write.write("hello i`m geeks i`m 2 year ")
# file_write.close()
# file_read = open('users.txt', 'r') 
# result = file_read.read()
# print(f"Peзультат: {result}")


name = ["Aman", "Mergul", "Erbol", "Bakai", 'Nurai']  
# file_writee = open('names.txt', 'w') 
# for i in name: 
#     file_writee.write(f"Name: {i},\n") 
    
# file_writee.close()
# file_read = open('names.txt', 'r') 
# resul = file_read.read() 
# print(resul)


# 2 способ 

# with open("names.txt", 'w') as file_write: 
#     for i in name: 
#         file_write.write(f"Name: {i}. \n") 
        
# with open("names.txt", 'r') as file_read: 
    # result = file_read.read() 
    # print(result)  
    
    
with open("python.py", "w") as write: 
   write.write("""names = ["Aman", "Mergul", "Erbol", "Bakai", 'Nurai'] 
with open("names.txt", "w") asfile_write: 
      for i in names:
        file_write.write(f"Name: {i}. \n") 
        
with open("names.txt", 'r') as file_read: 
    result = file_read.read() 
    print(result)""")  
    
    
    
    
    