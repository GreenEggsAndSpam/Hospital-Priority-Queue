from BST import BS

if __name__ == "__main__":
    pokedex = BST()
    file = input("Enter a file name: ")

    with open(file) as file:
        for line in file:
            us_name, pokedex_num, jp_name = line.strip().split()
            pokemon = Pokemon(us_name, int(pokedex_num), jp_name)
            pokedex.insert(int(pokedex_num), pokemon)


    while True:
        print("1.Search pokemon")
        print("2.Add new pokemon")
        print("3.Print pokedex traversal order")
        print("4.Remove the the index with a poke index")
        print("5.Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pokedex_num = int(input("Enter Pokedex Number: "))
            result = pokedex.search(pokedex_num)
            if result:
                print(f"Pokemon Found: {result}")
            else:
                print("Pokemon not found!")

        elif choice == '2':
            us_name = input("Enter American Name: ")
            jp_name = input("Enter Japanese Name: ")
            pokedex_num = int(input("Enter Pokedex Number: "))
            pokemon = Pokemon(us_name, pokedex_num, jp_name)
            pokedex.insert(pokedex_num, pokemon)
            print("Pokemon added successfully!")


        elif choice == '3':
            order = input("choose an order to print in: ")
            if order == '1':
                pokedex.print_pre_order()
            elif order == '2':
                pokedex.print_in_order()
            elif order == '3':
                pokedex.print_post_order()
        
        elif choice == '4':
            inp = int(input("Enter a poke index to remove: "))
            pokedex.remove(inp)
            print("pokemon successfully removed!")

        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")





