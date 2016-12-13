import pymel.core as pm
import maya.mel as mel
import maya.cmds as cmds

class fixRotKey180Flip(object):
    '''This is used to fix rotation keyframes 180 degree flip. Usually the keyframes are baked from some animation contrals.'''

    @staticmethod
    def getSelectedChannels():
        mainChannelBox = mel.eval('global string $gChannelBoxName;\
                                   $temp=$gChannelBoxName;')
        selAttrs = pm.channelBox(mainChannelBox, q=True, sma=True)
        selObjs = pm.ls(sl=True)
        result = []

        if not selAttrs or not selObjs:
            animCurves = pm.keyframe(q=True, n=True)
            result = animCurves
        else:
            for node in selObjs:
                for attr in selAttrs:
                    if pm.attributeQuery(attr, n=node, ex=True):
                        plug = node+'.'+attr
                        if pm.getAttr(plug, k=True) and not pm.getAttr(plug, l=True):
                            animCurve = cmds.listConnections(plug, d=False, s=True, p=False, scn=True)[0]
                            result.append(animCurve)
        return result

    @staticmethod
    def fix(tol=50, minStep=1):
        animCurves = fixRotKey180Flip.getSelectedChannels()
        if not animCurves:
            pm.error("Please select any Keys on animCurves those are you want to be corrected in Graph Editor, or select Attributes those have animCurves need to be corrected in the Channel Box.")

        for animCurve in animCurves:
            keyCount = pm.keyframe(animCurve, q=True, keyframeCount=True)

            for idx in range(keyCount-1):
                time = pm.keyframe(animCurve, index=(idx), q=True)[0]
                nextTime = pm.keyframe(animCurve, index=(idx+1), q=True)[0]

                if nextTime-time <= minStep:
                    value = pm.keyframe(animCurve, index=(idx), q=True, eval=True)[0]
                    nextValue = pm.keyframe(animCurve, index=(idx+1), q=True, eval=True)[0]

                    diff = nextValue-value
                    print diff
                    sign = -1 if diff > 0 else 1
                    diff = abs(diff)
                    if diff > 180-tol:
                        mult = int(diff / 180)
                        diff = diff % 180
                        if diff > 180-tol:
                            mult += 1
                        move = sign * mult * 180
                        pm.keyframe(animCurve, r=True, e=True, index=(idx+1, keyCount-1), vc=move)

def fixRotationKeyframes180Flip():
    fixRotKey180Flip.fix()
