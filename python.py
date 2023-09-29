names = ["Aman", "Mergul", "Erbol", "Bakai", 'Nurai'] 
with open("names.txt", "w") asfile_write: 
      for i in names:
        file_write.write(f"Name: {i}. 
") 
        
with open("names.txt", 'r') as file_read: 
    result = file_read.read() 
    print(result)