import moviepy.editor as me
import os.path

"""
Calculate bias if both dub and sub version is present
"""


def cal():
    curdir = os.getcwd()
    sep = os.path.sep * 2
    if not os.path.basename(curdir) == 'anime':
        os.chdir('vids' + sep + 'anime')
    bias_dict = {}
    path = '%s' + sep + '%s' + sep + '%s'
    for a, b, fn in os.walk('dub'):
        for file in fn:
            subpath = path % ('sub', file[0:3], file)
            dubpath = path % ('dub', file[0:3], file)
            subvid = me.VideoFileClip(subpath)
            dubvid = me.VideoFileClip(dubpath)
            val = int(dubvid.duration - subvid.duration)
            bias_dict[file[:-4]] = val if val != 0 else 12  # sometimes bias wont be calculated
    os.chdir(curdir)                                        # so manually calculate and assign to 'val'
    return bias_dict

