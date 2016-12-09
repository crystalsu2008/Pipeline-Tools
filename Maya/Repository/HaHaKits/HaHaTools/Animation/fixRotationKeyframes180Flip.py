'''
import sys
Dir = 'C:/Users/Administrator/Documents/DEV/Pipeline-Tools/maya_tools/scripts/animation'
if Dir not in sys.path:
    sys.path.append(Dir)

import fixRotationKeyframes180Flip;reload(fixRotationKeyframes180Flip)

fixRotationKeyframes180Flip.fixRotationKeyframes180Flip()
'''

import pymel.core as pm
import maya.mel as mel

class fixRotKey180Flip(object):
    '''This is used to fix rotation keyframes 180 degree flip. Usually the keyframes are baked from some animation contrals.'''
    tol = 60
    minStep = 1

    @staticmethod
    def getSelectedChannels():
        mainChannelBox = mel.eval('global string $gChannelBoxName;\
                                   $temp=$gChannelBoxName;')
        attrs = pm.channelBox(mainChannelBox, q=True, sma=True)
        if not attrs:
            return None
        return attrs

    @staticmethod
    def fix():
        attrs = fixRotKey180Flip.getSelectedChannels()
        objs = pm.ls(sl=True)

        if not objs:
            pm.error("No Objects selected.")

        if not attrs:
            pm.error("No Attributes selected in the Channel Box.")

        for obj in objs:
            for attr in attrs:
                keyCount = pm.keyframe(obj, at=attr, q=True, keyframeCount=True)

                for idx in range(keyCount-1):
                    time = pm.keyframe(obj, at=attr, index=(idx), q=True)[0]
                    nextTime = pm.keyframe(obj, at=attr, index=(idx+1), q=True)[0]

                    if nextTime-time <= fixRotKey180Flip.minStep:
                        value = pm.keyframe(obj ,at=attr, index=(idx), q=True, eval=True)[0]
                        nextValue = pm.keyframe(obj ,at=attr, index=(idx+1), q=True, eval=True)[0]

                        diff = nextValue-value
                        sign = -1 if diff > 0 else 1
                        diff = abs(diff)
                        if diff > 180-fixRotKey180Flip.tol:
                            mult = int(diff / 180)
                            diff = diff % 180
                            if diff > 180-fixRotKey180Flip.tol:
                                mult += 1
                            move = sign * mult * 180
                            pm.keyframe(obj, at=attr, r=True, e=True, index=(idx+1, keyCount-1), vc=move)

def fixRotationKeyframes180Flip():
    fixRotKey180Flip.fix()
