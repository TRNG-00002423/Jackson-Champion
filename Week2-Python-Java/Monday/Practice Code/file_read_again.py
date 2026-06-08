try:
    file = open("abc.txt", "r")
    
    content = file.read()
    print(content)
    
    file.close()
except Exception as e:
    print(f"Unexpected error: {e}")

