import pymel.core as pm
import maya.mel as mel
import maya.cmds as cmds

class fixRotKey90Flip(object):
    '''This is used to fix rotation keyframes 90 degree flip. Usually the keyframes are baked from some animation contrals.'''

    @staticmethod
    def getSelectedChannels(useSelectedKeys):
        mainChannelBox = mel.eval('global string $gChannelBoxName;\
                                   $temp=$gChannelBoxName;')
        selAttrs = pm.channelBox(mainChannelBox, q=True, sma=True)
        selObjs = pm.ls(sl=True)
        result = {}

        if not selAttrs or not selObjs:
            animCurves = pm.keyframe(q=True, n=True)
            if useSelectedKeys:
                result = {x: pm.keyframe(x, q=True, sl=True, iv=True) for x in animCurves}
            else :
                result = {x: None for x in animCurves}
        else:
            for node in selObjs:
                for attr in selAttrs:
                    if pm.attributeQuery(attr, n=node, ex=True):
                        plug = node+'.'+attr
                        if pm.getAttr(plug, k=True) and not pm.getAttr(plug, l=True):
                            animCurve = cmds.listConnections(plug, d=False, s=True, p=False, scn=True)[0]
                            result[animCurve] = None
        return result

    @staticmethod
    #def fix(useSelectedKeys=True, tol=20, minStep=1, fixFlip=True, fixBreak=False, cycle=False):
    def fix(useSelectedKeys=True, tol=20, minStep=1, fixFlip=False, fixBreak=True, cycle=True):
        animCurves = fixRotKey90Flip.getSelectedChannels(useSelectedKeys)
        if not animCurves:
            pm.error("Please select any Keys on animCurves those are you want to be corrected in Graph Editor, or select Attributes those have animCurves need to be corrected in the Channel Box.")

        for animCurve, idxs in animCurves.iteritems():
            keyCount = pm.keyframe(animCurve, q=True, kc=True)
            if not idxs:
                idxs = range(keyCount)
            for idx in idxs:
                if idx==keyCount-1:
                    continue
                time, nextTime = pm.keyframe(animCurve, index=[idx, idx+1], q=True)
                if nextTime-time > minStep:
                    continue
#------------------------------------------------------------------------------#
                idx_pre = 0 if idx==0 else idx-1
                value_pre = pm.keyframe(animCurve, index=idx_pre, q=True, eval=True)[0]
                value = pm.keyframe(animCurve, index=idx, q=True, eval=True)[0]
                value_pos = pm.keyframe(animCurve, index=idx+1, q=True, eval=True)[0]

                diff_pre = value - value_pre
                if abs(diff_pre) > tol:
                    diff = value_pos - value
                else:
                    diff = value_pos - (value + diff_pre)

                sign = -1 if diff > 0 else 1
                diff = abs(diff)
                print 90-diff
                if fixFlip and 90-diff < tol:
                    mult = int(diff / 90)
                    diff = diff % 90
                    if diff > 90-tol:
                        mult += 1
                    move = sign * mult * 90
                    pm.keyframe(animCurve, r=True, e=True, index=(idx+1, keyCount-1), vc=move)
                elif fixBreak and diff > tol:
                    idx_pos2 = keyCount-1 if idx==keyCount-2 else idx+1
                    value_pos2 = pm.keyframe(animCurve, index=idx_pos2, q=True, eval=True)[0]
                    diff_pos = abs(2*value_pos - value_pos2 - value)

                    move = sign * (diff + diff_pos)/2.0
                    #move = sign * diff
                    #move = sign * diff_pos
                    pm.keyframe(animCurve, r=True, e=True, index=(idx+1, keyCount-1), vc=move)

                if cycle and (idx==idxs[-1] or idx==keyCount-2):
                    v_first = pm.keyframe(animCurve, index=0, q=True, eval=True)[0]
                    v_last = pm.keyframe(animCurve, index=keyCount-1, q=True, eval=True)[0]
                    if not v_first == v_last:
                        v_diff = v_last - v_first
                        t_array = pm.keyframe(animCurve, index=[0, keyCount-1], q=True)
                        t_diff = t_array[-1] - t_array[0]
                        v_step = v_diff / t_diff
                        for i in range(keyCount):
                            #v = pm.keyframe(animCurve, index=i, q=True, eval=True)[0]
                            t = pm.keyframe(animCurve, index=i, q=True)[0]
                            pm.keyframe(animCurve, r=True, e=True, index=i, vc=-v_step*(t - t_array[0]))

def fixRotationKeyframesFlip():
    fixRotKey90Flip.fix()
