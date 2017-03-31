import pymel.core as pm

def HH_ComplexBlender():
    clips = pm.ls(type='animClip')
    poses = [clip for clip in clips if pm.getAttr(clip+'.pose')]
    print clips
    print poses
