
import view
import model


def program(init_file):
    while True:
        option = view.show_menu()

        # создать заметку
        if option == 1:
            title, body = view.add_note()
            data = model.read_file(init_file)
            list_of_notes = [item for item in data['notes']]  # сформировать список заметок
            new_note = model.create_new_note(title, body, list_of_notes)
            data['notes'].append(new_note)  # добавить заметку в конец списка
            model.write_file(init_file, data)
            view.warn_of_note_creation()

        # показать все заметки
        elif option == 2:
            view.show_all_notes(init_file)

        # редактировать заметку
        elif option == 3:
            note_id = view.get_id_for_edition()
            data = model.read_file(init_file)
            list_of_notes = [item for item in data['notes']]  # сформировать список заметок
            index = model.search_by_id(note_id, list_of_notes)

            if index is not None:   # проверяет, что index найден !в соответствии с введенным индексом!
                note_id, title, new_title, body, new_body = view.edit_note(
                    index, list_of_notes)
                new_data = model.update_note(
                    index, title, new_title, body, new_body, list_of_notes, data)

                if new_data is not None:    # если изменения внесены либо в заголовок, либо в текст
                    model.write_file(init_file, data)
                    view.warn_of_change_made()
                else:    # в случае, если нет изменений ни в заголовке, ни в тексте заметки
                    view.warn_of_no_change()
            else:
                view.warn_of_no_note()

        # удалить заметку
        elif option == 4:
            note_id = view.get_id_for_deletion()
            data = model.read_file(init_file)
            list_of_notes = [item for item in data['notes']]
            index = model.search_by_id(note_id, list_of_notes)
            if index is not None:
                new_data = model.delete_note(index, list_of_notes, data)
                model.write_file(init_file, new_data)
                view.warn_of_note_deletion()
            else:
                view.warn_of_no_note()

        # Закончить работу
        else:
            view.show_quit_message()
            break
