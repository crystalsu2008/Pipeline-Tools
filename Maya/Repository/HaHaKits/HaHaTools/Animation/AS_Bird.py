import pymel.core as pm
import maya.mel as mel

def AS_Bird():
    fixFitSkeleton()

def fixFitSkeleton():
    pm.move('Root', 0, 15.457028, -5.948403, rpr=True)

    # Leg
    pm.move('backRump', -2.88102, 14.475566, -5.4264, rpr=True)
    pm.move('backHip', -2.88102, 13.254783, -0.904738, rpr=True)
    pm.move('backKnee', -2.88102, 6.962669, -2.064865, rpr=True)
    pm.move('backAnkle', -2.88102, 1.948935, 1.136064, rpr=True)
    pm.move('backHeel', -2.88102, 1, -0.55596, rpr=True)
    pm.move('backToes', -2.88102, 1, 3.190018, rpr=True)
    pm.move('backToesEnd', -2.88102, 0.813392, 5.082496, rpr=True)

    # Tail
    pm.move('Tail0', 0, 14.066408, -7.410079, rpr=True)
    pm.move('Tail1', 0, 13.671565, -7.729606, rpr=True)
    pm.move('Tail2', 0, 13.453142, -7.956723, rpr=True)
    pm.move('Tail3', 0, 13.255721, -8.183839, rpr=True)
    pm.move('Tail4', 0, 12.972178, -8.44456, rpr=True)
    pm.move('Tail5', 0, 12.820962, -8.696587, rpr=True)
    pm.move('Tail6', 0, 12.888169, -9.93572, rpr=True)

    # Spine
    pm.move('Spine1', 0, 16.529027, -4.206971, rpr=True)
    pm.move('Chest', 0, 17.066826, -2.969545, rpr=True)
    pm.move('Neck', 0, 18.391344, 0.326219, rpr=True)
    pm.move('Head', 0, 27.782901, 3.483267, rpr=True)

    tmpjoint = pm.insertJoint('Neck')
    pm.rename(tmpjoint, 'Neck1')
    pm.joint('Neck1', e=True, co=True, p=(0, 18.696437, 1.095583))
    tmpjoint = pm.insertJoint('Neck1')
    pm.rename(tmpjoint, 'Neck2')
    pm.joint('Neck2', e=True, co=True, p=(0, 19.213769, 2.077187))
    tmpjoint = pm.insertJoint('Neck2')
    pm.rename(tmpjoint, 'Neck3')
    pm.joint('Neck3', e=True, co=True, p=(0, 19.678041, 2.899611))
    tmpjoint = pm.insertJoint('Neck3')
    pm.rename(tmpjoint, 'Neck4')
    pm.joint('Neck4', e=True, co=True, p=(0, 20.500465, 3.576122))
    tmpjoint = pm.insertJoint('Neck4')
    pm.rename(tmpjoint, 'Neck5')
    pm.joint('Neck5', e=True, co=True, p=(0, 21.641248, 3.668976))
    tmpjoint = pm.insertJoint('Neck5')
    pm.rename(tmpjoint, 'Neck6')
    pm.joint('Neck6', e=True, co=True, p=(0, 22.596321, 3.576122))
    tmpjoint = pm.insertJoint('Neck6')
    pm.rename(tmpjoint, 'Neck7')
    pm.joint('Neck7', e=True, co=True, p=(0, 23.684044, 3.257764))
    tmpjoint = pm.insertJoint('Neck7')
    pm.rename(tmpjoint, 'Neck8')
    pm.joint('Neck8', e=True, co=True, p=(0, 24.678912, 2.979201))
    tmpjoint = pm.insertJoint('Neck8')
    pm.rename(tmpjoint, 'Neck9')
    pm.joint('Neck9', e=True, co=True, p=(0, 25.554396, 2.833287))
    tmpjoint = pm.insertJoint('Neck9')
    pm.rename(tmpjoint, 'Neck10')
    pm.joint('Neck10', e=True, co=True, p=(0, 26.416615, 2.766962))
    tmpjoint = pm.insertJoint('Neck10')
    pm.rename(tmpjoint, 'Neck11')
    pm.joint('Neck11', e=True, co=True, p=(0, 27.13292, 3.072055))

    # Head
    pm.move('Jaw', 0, 27.233845, 4.684155, rpr=True)
    pm.move('JawEnd', 0, 27.343004, 8.089177, rpr=True)
    pm.move('Eye', -0.702294, 28.482938, 5.56851, rpr=True)
    pm.move('EyeEnd', -1.776226, 28.43113, 5.776239, rpr=True)
    pm.move('Ear', -1.070843, 28.702831, 4.284751, rpr=True)

    # Wing
    pm.move('frontRump', -0.666333, 15.298425, 1.362798, rpr=True)
    pm.rename('frontRump', 'Scapula')
    pm.move('frontHip', -1.643369, 18.64079, 0.838308, rpr=True)
    pm.rename('frontHip', 'Shoulder')
    pm.move('frontKnee', -6.397075, 18.277728, 0.120228, rpr=True)
    pm.rename('frontKnee', 'Elbow')
    pm.move('frontAnkle', -6.695856, 23.580604, -0.582982, rpr=True)
    pm.deleteAttr( 'frontAnkle.worldOrient' )
    pm.rename('frontAnkle', 'Wrist')
    pm.move('frontToes', -9.598403, 23.358922, -1.021432, rpr=True)
    pm.rename('frontToes', 'IndexFinger1')
    pm.move('frontToesEnd', -11.673251, 23.200457, -1.334852, rpr=True)
    pm.rename('frontToesEnd', 'IndexFinger2')

    mel.eval('asFitModeManualUpdate')
