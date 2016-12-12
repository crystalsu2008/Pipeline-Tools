import pymel.core as pm
import maya.mel as mel
import maya.cmds as cmds

class fixRotKey180Flip(object):
    '''This is used to fix rotation keyframes 180 degree flip. Usually the keyframes are baked from some animation contrals.'''
    tol = 50
    minStep = 1

    @staticmethod
    def getSelectedChannels():
        mainChannelBox = mel.eval('global string $gChannelBoxName;\
                                   $temp=$gChannelBoxName;')
        selAttrs = pm.channelBox(mainChannelBox, q=True, sma=True)
        selObjs = pm.ls(sl=True)
        result = []

        if not selAttrs or not selObjs:
            animCurves = pm.keyframe(q=True, n=True)
            for animCurve in animCurves:
                plugs = cmds.listConnections(animCurve+'.output', d=True, s=False, p=True, scn=True)
                if plugs:
                    for plug in plugs:
                        node, attr = plug.split('.')
                        result.append({'node': node, 'attr': attr})
        else:
            for node in selObjs:
                for attr in selAttrs:
                    if pm.attributeQuery(attr, n=node, ex=True):
                        plug = node+'.'+attr
                        if pm.getAttr(plug, k=True) and not pm.getAttr(plug, l=True):
                            result.append({'node': node, 'attr': attr})
        return result

    @staticmethod
    def fix():
        plugs = fixRotKey180Flip.getSelectedChannels()
        if not plugs:
            pm.error("Please select any Keys on animCurves those are you want to be corrected in Graph Editor, or select Attributes those have animCurves need to be corrected in the Channel Box.")

        for plug in plugs:
            node = plug['node']
            attr = plug['attr']
            keyCount = pm.keyframe(node, at=attr, q=True, keyframeCount=True)

            for idx in range(keyCount-1):
                time = pm.keyframe(node, at=attr, index=(idx), q=True)[0]
                nextTime = pm.keyframe(node, at=attr, index=(idx+1), q=True)[0]

                if nextTime-time <= fixRotKey180Flip.minStep:
                    value = pm.keyframe(node ,at=attr, index=(idx), q=True, eval=True)[0]
                    nextValue = pm.keyframe(node ,at=attr, index=(idx+1), q=True, eval=True)[0]

                    diff = nextValue-value
                    print diff
                    sign = -1 if diff > 0 else 1
                    diff = abs(diff)
                    if diff > 180-fixRotKey180Flip.tol:
                        mult = int(diff / 180)
                        diff = diff % 180
                        if diff > 180-fixRotKey180Flip.tol:
                            mult += 1
                        move = sign * mult * 180
                        pm.keyframe(node, at=attr, r=True, e=True, index=(idx+1, keyCount-1), vc=move)

def fixRotationKeyframes180Flip():
    fixRotKey180Flip.fix()
