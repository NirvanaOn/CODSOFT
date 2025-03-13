search = input("Enter what you want to search: ")
text = "hello world i am text you can search me q w e r t y u i o p a s d f g h j k l z x c v b n m"

if search in text:
    highlighted_text = text.replace(search, f"\033[93m{search}\033[0m") 
    print(highlighted_text)
else:
    print("Search not found")