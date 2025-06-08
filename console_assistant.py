from assistant import Assistant

def main():
    assistant = Assistant()

    print("Асистент запущено. Команди: /add, /list, /search, /exit")

    while True:
        command = input(">>> ")

        if command == "/add":
            note = input("Введіть нотатку: ")
            assistant.add_note(note)
            print("Нотатку додано.")
        elif command == "/list":
            notes = assistant.list_notes()
            if notes:
                print("\n".join(f"{i+1}. {n}" for i, n in enumerate(notes)))
            else:
                print("Список нотаток порожній.")
        elif command == "/search":
            keyword = input("Ключове слово: ")
            found = assistant.search_notes(keyword)
            if found:
                print("\n".join(f"- {n}" for n in found))
            else:
                print("Нічого не знайдено.")
        elif command == "/exit":
            print("До побачення!")
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()
