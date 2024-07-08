import pysubs2 as pys
import os as os
import os.path
import re as re


class anime:
    def __init__(self, event, info):
        self.start = self.to_min_sec(event.start)
        self.end = self.to_min_sec(event.end)
        self.se = info[0:3]
        self.ep = info[4:7]
        cleaned_text = re.sub(r'[^a-zA-z ]', '', event.plaintext)
        self.text = cleaned_text

# TODO: Add a option to add bias for start and end time is audio is english - DONE

    @staticmethod
    def to_min_sec(ms):
        min = int(ms / 60000)
        sec = int((ms - (min * 60000)) / 1000)
        return [min, sec]

    def __str__(self):
        return f'{self.start[0]:02d}:{self.start[1]:02d}\t{self.end[0]:02d}:{self.end[1]:02d}\t{self.se}_{self.ep}\n{self.text}\n'

# TODO: add a parameter so that type of vid is selected


# optlist = []
# optlist.append('anime')


def search_list(reg):
    # regobj = re.compile(r'^(.*)?(it\'s|it\'s a|quite|how|very|really) (cute).*?$', re.I)
    regobj = reg
    obj_list = []
    sep = os.path.sep * 2

    for curdir, subdir, filename in os.walk('subs' + sep + 'anime'):
        for file in filename:
            if file.endswith('.srt'):
                subs = pys.load(curdir + sep + file)
                for line in subs:
                    a = anime(line, file)
                    obj_list.append(a)

    sear_result = []
    for i in range(len(obj_list)):
        mo = regobj.search(obj_list[i].text)
        if mo is not None:
            sear_result.append(obj_list[i])

    sear_result = list(dict.fromkeys(sear_result))
    return sear_result


if __name__ == '__main__':
    for obj in search_list(re.compile(r'^(.*)?(it\'s|it\'s a|quite|how|very|really) (cute).*?$', re.I)):
        print(obj)
