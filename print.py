# 1. Стандартный вывод сообщения на экран:
print ("Пример №1")
print("Hello world!")
print()

# 2. Вывод в одной строке сообщения нескольких слов или предложений, которые будут разделены пробелом:
print ("Пример №2")
print("Hello","world!")
print()

# 3. Вывод в одной строке сообщения нескольких слов или предложений, которые будут разделены запятой и пробелом выставленным вручную после запятой, установленной внутри кавычек аргумента sep:
print ("Пример №3")
print("Hello","world!", sep=", ") 
print()

# 4. Вывод сообщения в две строки:
print ("Пример №4")
print("first row")
print("second row")
print()

# 5. Вывод сообщения в одной строке, с помощью аргумента end, в который требуется передать пробел:
print ("Пример №5")
print("first row", end=" ")
print("second row")
print()

# 6. Вывод сообщения в одной строке, в которой часть текста будет помещена в кавычки:
print ("Пример №6")
print ('Hello "white" world')
print()

# 7. Вывод сообщения в одной строке, в которой часть текста будет помещена в кавычки (метод Экранирования):
print ("Пример №7")
print("Hello \"white\" world")