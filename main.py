import os
import file
import list_function
import yi



def main():
    os.system('cls')
    yi.show_menu()
    try:
        choice = yi.choice_menu()
        print(choice)
        if choice == 7:
            yi.show_data(file.read_file('data.csv'))
            input()
            main()

        elif choice == 1:
            category=yi.show_category('data.csv')
            element=input("Введите значение для поиска: ")
            llist=list_function.search_in_file('data.csv',category,element)
            yi.show_list(llist)
            input()
            main()
        elif choice==4:
            list-yi.add_element('data,csv')
            file.write_line('data.csv',list)
            print("запись завершена")
        if print()


    except Exception as ex:
        print(str(ex))
        input()
        main()


print("start program")
main()
