text = input("Введите пожалуйста фразу: ")

text_lower = text.lower()
keyword = "південь".lower()

if keyword in text_lower:
    print("True")
else:
    print("False")