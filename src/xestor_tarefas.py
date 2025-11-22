import json
import os

DB_FILE = "data/tareas.json"

def cargar_tarefas():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def gardar_tarefas(tarefas):
    with open(DB_FILE, "w") as f:
        json.dump(tarefas, f, indent=4)


def engadir_tarefa(texto):
    tarefas = cargar_tarefas()
    tarefas.append({"texto": texto, "feito": False})
    gardar_tarefas(tarefas)


def listar_tarefas():
    tarefas = cargar_tarefas()
    if not tarefas:
        print("Non hai tarefas pendentes!")
        return

    print("\n📌 Lista de tarefas:")
    for i, t in enumerate(tarefas, 1):
        estado = "✔️" if t["feito"] else "⏳"
        print(f"{i}. {t['texto']}  | {estado}")


def completar_tarefa(num):
    tarefas = cargar_tarefas()
    if 1 <= num <= len(tarefas):
        tarefas[num - 1]["feito"] = True
        gardar_tarefas(tarefas)
        print("Tarefa completada!")
    else:
        print("Número inválido.")
