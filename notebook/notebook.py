#!/usr/bin/python
import datetime

last_id = 0
class Note:
    '''
    为其他note存储序号
    '''
    def __init__(self, memo, tags = ''):
        '''
        自动设置ID和创建时间
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    def match(self, filter):
        return filter in self.memo or filter in self.tags

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, note_id, memo):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break
    
    def modify_tags(self, note_id, tags):
        for note in self.notes:
            '''
            find the note with the given id and change its
            tags to the given values.
            '''
            if note.id == note_id:
                note.tags = tags
                break
    def search(self, filter):
        return [ note for note in self.notes if note.match(filter)]

