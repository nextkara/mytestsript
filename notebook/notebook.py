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

