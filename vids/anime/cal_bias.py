import moviepy.editor as me
import os.path
import pprint as p

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
    if not os.path.isdir('dub'):
        raise Exception('dub directory not found.')
    if not os.path.isdir('sub'):
        raise Exception('sub directory not found.')
    for ((a, b, fn), (x, y, z)) in zip(os.walk('dub'), os.walk('sub')):
        for (file, f) in zip(fn, z):
            if file.endswith('.mp4'):
                if f != file:
                    raise Exception(file, 'does not exist.')
                subpath = path % ('sub', file[0:3], file)
                dubpath = path % ('dub', file[0:3], file)
                subvid = me.VideoFileClip(subpath)
                dubvid = me.VideoFileClip(dubpath)
                val = int(dubvid.duration - subvid.duration)
                bias_dict[file[:-4]] = val if val != 0 else 12

                """
                # sometimes bias wont be calculated
                so manually calculate and assignto'val'
                """

    os.chdir(curdir)
    return bias_dict


if __name__ == '__main__':
    p.pprint(cal())
