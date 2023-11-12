from utils import *

while True:
    try:
        menu1 = menu()
        print(menu1)
        switch_case(menu1)
        break
    except FileNotFoundError:
        print("File not found. Try again.")
        continue
    except Exception as e:
        print(e)
        break