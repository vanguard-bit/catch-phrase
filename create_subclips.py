import moviepy.editor as me
import extract_catch_phrase as catch_phrase
import os.path
import vids.anime.cal_bias as cal_bias


def run():
    obj_list = catch_phrase.search_list()

    i = 1
    sep = os.path.sep * 2
    path = 'vids' + sep + 'anime' + sep + '%s' + sep + '%s' + sep + '%s_%s' + '%s'
    file = 'result' + sep + 'anime' + sep + '%s' + sep + '%s' + sep + '%s..._' '%s_%s_%s' + '%s'
    curr = 'sub'

    for obj in obj_list:
        vidpath = path % (curr, obj.se, obj.se, obj.ep, '.mp4')
        outfile = file % (curr, obj.se, obj.text.title()[:8], obj.se, obj.ep, f'{i:02d}', '.mp4')
        i += 1
        dir = 'result' + sep + 'anime' + sep + '%s' + sep + '%s'
        if not os.path.isdir(dir % (curr, obj.se)):
            os.makedirs(dir % (curr, obj.se))
        vf = me.VideoFileClip(vidpath)

        start = (obj.start[0] * 60 + obj.start[1])
        startlen = start - 3 if start - 3 > 0 else start

        end = (obj.end[0] * 60 + obj.end[1])
        endlen = end + 3 if end + 3 < vf.duration * 60 else end

        vf = vf.subclip(startlen, endlen)
        vf.write_videofile(outfile)

    curr = 'dub'
    bias = cal_bias.cal()
    i = 1

    for obj in obj_list:
        vidpath = path % (curr, obj.se, obj.se, obj.ep, '.mp4')
        outfile = file % (curr, obj.se, obj.text.title()[:8], obj.se, obj.ep, f'{i:02d}', '.mp4')
        i += 1
        dir = 'result' + sep + 'anime' + sep + '%s' + sep + '%s'
        if not os.path.isdir(dir % (curr, obj.se)):
            os.makedirs(dir % (curr, obj.se))
        vf = me.VideoFileClip(vidpath)

        start = (obj.start[0] * 60 + obj.start[1]) + bias[obj.se + '_' + obj.ep] - 3
        startlen = start if start > 0 else start + 3

        end = (obj.end[0] * 60 + obj.end[1]) + bias[obj.se + '_' + obj.ep] + 3
        endlen = end if end < vf.duration * 60 else end - 3

        vf = vf.subclip(startlen, endlen)
        vf.write_videofile(outfile)
