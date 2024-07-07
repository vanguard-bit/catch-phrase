import pysubs2 as pys
import os as os
import re as re


class anime:
    def __init__(self, event, info):
        self.start = self.to_min_sec(event.start)
        self.end = self.to_min_sec(event.end)
        self.se = info[0:3]
        self.ep = info[4:7]
        self.text = event.plaintext

# TODO: Add a option to add bias for start and end time is audio is english

    @staticmethod
    def to_min_sec(ms):
        min = int(ms / 60000)
        sec = int((ms - (min * 60000)) / 1000)
        return [min, sec]

    def __str__(self):
        return f'{self.start[0]:02d}:{self.start[1]:02d}\t{self.end[0]:02d}:{self.end[1]:02d}\t{self.se}_{self.ep}\n{self.text}\n'

# TODO: add a parameter so that type of vid is selected


optlist = []
optlist.append('anime')
obj_list = []

for curdir, subdir, filename in os.walk('subs\\' + optlist[0]):
    for file in filename:
        if file.endswith('.srt'):
            subs = pys.load(curdir + '\\' + file)
            for line in subs:
                a = anime(line, file)
                obj_list.append(a)

regobj = re.compile(r'^(.*)?(it\'s|quite|how|very|really)? (cute).*?$', re.I)
# regobj1 = re.compile(r'^(.*)?(oh my|oh, my|oh dear|oh, dear).*?$', re.I)
# regobj2 = re.compile(r'^(.*)? how .*[^,\?]$', re.I)
sear_result = []
for i in range(len(obj_list)):
    mo = regobj.search(obj_list[i].text)
    if mo is not None:
        sear_result.append(obj_list[i])

sear_result = list(dict.fromkeys(sear_result))
