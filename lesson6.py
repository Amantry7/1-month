# def hello(): 
#     print("hello") 
    
# hello() 

# def sum(name):
#     print(f"Привет {name}") 
# name_user = "aman" 
 
 
# sum(name_user) 

# def sum(nam1,nam2):   
    
#     print(f"результат сложение{nam1+nam2}")  
    
# def sub(nam1,nam2): 
    
#     print(f"результат сложение{nam1-nam2}")   
    
# def mult(nam1,nam2): 
    
#     print(f"результат сложение{nam1*nam2}")   
    
# def dev(nam1,nam2): 
#     print(f"результат сложение{nam1//nam2}")  
    
    

# def main():
#     while True: 
#         nam1 = int(input("Введите первое число: ")) 
#         nam2 = int(input("Введите второе число: "))
#         a = input("1 - сложение, 2 - вычитание 3 - умножение 4 - деление")
#         if a =="1": 
#             sum(nam1, nam2)
#         elif a == "2":
#             sub(nam1,nam2) 
#         elif a == "3": 
#             mult(nam1,nam2)
#         elif a == '4': 
#             dev(nam1,nam2) 
            
            
# main()
            
            
            
# def sound(title,animal_sound): 
#     print(f"Я {title}. {animal_sound}") 
    
# sound("корова ", 'Мууууу муууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууу') 
# sound("собака", " гав гав гав")
# sound("змея","ssssssssss")    
    
        

# def users(*user): 
#     for i in user: 
#         print(f"здраствуйте {i}") 
         

# users("Аман", "geeks", "osh", "go")
 


# def users(**data): 
#     for key, value in data.items(): 
        #         print(f"{key}: {value}") 
        
# users(name = "Alina", age = "18", city = "Osh", language = "English") 

# def math(*nums): 
#     print(f"Средние арифмитическое число: {sum(nums) // len(nums)}")
    
# math(20,3123,213213,34324,32421,2113,21)  
    
# def summ(*num):  
#     print(f'сумма числел {sum(num)}') 
     
# summ(12,12,12,12,1,21,2,12,1,21,)    


# def summ(*nums): 
#     n = 0 
#     for i in nums: 
#         n+=1 
#         print(f"cymma: {n}") 
# summ(3123,312,312,3123,123,21,3,312,312,312,312,3,3,13,13,13,12,312,312,23,3,3,3,1)        
    
# def len1(*nums): 
#     print(f"длина чисел: {len(nums)}")
    
# len1(21,12,2,13,1,3,123,12,312)    
    
    
    
def min1(*nums): 
    print(f"минимальное число: {min(nums)}") 
    print(f"самое большое число {max(nums)}")
min1(23123,312,321,312,33123,1)
    
    
    
    
    
    
    
    