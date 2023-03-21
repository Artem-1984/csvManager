import os
import file
import list.function
import yi
def main():
    os.system('cls')
    yi.show_menu()
    try:
        choice = yi.choice_menu()
        print(choice)
        if choice==7:
            yi.show_data(file.read_file('data.csv'))
            input()
            main()
    except Exception as ex:
        print(str(ex))
        input()
        main()

print("start program")
main()

