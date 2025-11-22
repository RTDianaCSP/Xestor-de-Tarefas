from xestor_tarefas import engadir_tarefa, listar_tarefas, completar_tarefa

while True:
    print("\n=====XESTOR DE TAREFAS=====")
    print("1. Engadir tarefa")
    print("2. Listar tarefas")
    print("3. Completar tarefa")
    print("4. Saír")

    opcion = input("Elixe unha opción: ")

    if opcion == "1":
        texto = input("Introduce a tarefa: ")
        engadir_tarefa(texto)

    elif opcion == "2":
        listar_tarefas()

    elif opcion == "3":
        num = int(input("Número da tarefa: "))
        completar_tarefa(num)

    elif opcion == "4":
        print("Saíndo...")
        break

    else:
        print("Opción non válida.")
