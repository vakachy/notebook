import json
from datetime import datetime


# -------------------------------------------------------------------- #
# чтение файла

def read_file(init_file):
    with open(init_file, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data


# -------------------------------------------------------------------- #
# запись в файл

def write_file(init_file, data):
    with open(init_file, 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)


# -------------------------------------------------------------------- #
# поиск индекса заметки по id заметки в списке заметок

def search_by_id(note_id, list_of_notes):
    for note in list_of_notes:
        if note['id'] == note_id:
            index = list_of_notes.index(note)
            return index


# -------------------------------------------------------------------- #
# удаление заметки

def delete_note(index, list_of_notes, data):
    list_of_notes.pop(index)
    data['notes'] = list_of_notes
    return data


# -------------------------------------------------------------------- #
# создать заметку

def create_new_note(title, body, list_of_notes):
    quantity_of_notes = len(list_of_notes)
    last_note_index = quantity_of_notes - 1
    last_id = list_of_notes[last_note_index]['id']
    next_id = last_id + 1
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y %H:%M:%S")
    new_note = {'id': next_id, 'title': title,
                'date': current_date, 'body': body}
    return new_note


# -------------------------------------------------------------------- #
# обновить содержимое заметки (если изменений нет ни в заголовке,
# ни в тексте, то такая заметка не сохраняется)

def update_note(index, title, new_title, body, new_body, list_of_notes, data):
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y %H:%M:%S")
    note = list_of_notes[index]

    if new_title == title and new_body == body:
        return

    if new_title != title:
        note['title'] = new_title
        note['date'] = current_date

    if new_body != body:
        note['body'] = new_body
        note['date'] = current_date

    new_note = note
    list_of_notes[index] = new_note
    data['notes'] = list_of_notes
    return data
