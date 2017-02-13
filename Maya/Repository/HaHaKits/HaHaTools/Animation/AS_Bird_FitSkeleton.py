import pymel.core as pm
import maya.mel as mel

def AS_Bird_FitSkeleton():
    fixFitSkeleton()
    feathersFitSkeleton()

def fixFitSkeleton():
    pm.move('Root', 0, 15.457028, -5.948403, rpr=True); pm.refresh()

    # Leg
    pm.move('backRump', -2.88102, 14.475566, -5.4264, rpr=True); pm.refresh()
    pm.move('backHip', -2.88102, 13.254783, -0.904738, rpr=True); pm.refresh()
    pm.move('backKnee', -2.88102, 6.962669, -2.064865, rpr=True); pm.refresh()
    pm.move('backAnkle', -2.88102, 1.948935, 1.136064, rpr=True); pm.refresh()
    #pm.setAttr('backAnkle.worldOrient', 4)
    pm.move('backHeel', -2.88102, 0.8, -0.55596, rpr=True); pm.refresh()
    pm.move('backToes', -2.88102, 1, 3.190018, rpr=True); pm.refresh()
    pm.move('backToesEnd', -2.88102, 0.8, 5.082496, rpr=True); pm.refresh()

    # Tail
    pm.move('Tail0', 0, 14.066408, -7.410079, rpr=True); pm.refresh()
    pm.move('Tail1', 0, 13.671565, -7.729606, rpr=True); pm.refresh()
    pm.move('Tail2', 0, 13.453142, -7.956723, rpr=True); pm.refresh()
    pm.move('Tail3', 0, 13.255721, -8.183839, rpr=True); pm.refresh()
    pm.move('Tail4', 0, 12.972178, -8.44456, rpr=True); pm.refresh()
    pm.move('Tail5', 0, 12.820962, -8.696587, rpr=True); pm.refresh()
    pm.move('Tail6', 0, 12.888169, -9.93572, rpr=True); pm.refresh()

    # Spine
    pm.move('Spine1', 0, 16.529027, -4.206971, rpr=True); pm.refresh()
    pm.move('Chest', 0, 17.066826, -2.969545, rpr=True); pm.refresh()
    pm.setAttr('Chest.fat', 2.5)

    pm.move('Neck', 0, 18.391344, 0.326219, rpr=True); pm.refresh()
    pm.rename('Neck', 'Neck0')
    pm.setAttr('Neck0.type', 18)
    pm.setAttr('Neck0.otherType', '0Neck', type='string')
    pm.setAttr('Neck0.drawLabel', 1)
    pm.deleteAttr('Neck0.inbetweenJoints')
    pm.setAttr('Neck0.fat', 1.5)
    tmpjoint = pm.insertJoint('Neck0')
    pm.rename(tmpjoint, 'Neck1')
    pm.joint('Neck1', e=True, co=True, p=(0, 18.696437, 1.095583)); pm.refresh()
    pm.addAttr('Neck1', longName='fat', at='float', k=True)
    pm.setAttr('Neck1.fat', 1.1)
    tmpjoint = pm.insertJoint('Neck1')
    pm.rename(tmpjoint, 'Neck2')
    pm.joint('Neck2', e=True, co=True, p=(0, 19.213769, 2.077187)); pm.refresh()
    pm.addAttr('Neck2', longName='fat', at='float', k=True)
    pm.setAttr('Neck2.fat', 1.0)
    tmpjoint = pm.insertJoint('Neck2')
    pm.rename(tmpjoint, 'Neck3')
    pm.joint('Neck3', e=True, co=True, p=(0, 19.678041, 2.899611)); pm.refresh()
    pm.addAttr('Neck3', longName='fat', at='float', k=True)
    pm.setAttr('Neck3.fat', 0.95)
    tmpjoint = pm.insertJoint('Neck3')
    pm.rename(tmpjoint, 'Neck4')
    pm.joint('Neck4', e=True, co=True, p=(0, 20.500465, 3.576122)); pm.refresh()
    pm.addAttr('Neck4', longName='fat', at='float', k=True)
    pm.setAttr('Neck4.fat', 0.9)
    pm.setAttr('Neck4.type', 18)
    pm.setAttr('Neck4.otherType', '1', type='string')
    pm.setAttr('Neck4.drawLabel', 1)

    tmpjoint = pm.insertJoint('Neck4')
    pm.rename(tmpjoint, 'Neck5')
    pm.joint('Neck5', e=True, co=True, p=(0, 21.641248, 3.668976)); pm.refresh()
    pm.addAttr('Neck5', longName='fat', at='float', k=True)
    pm.setAttr('Neck5.fat', 0.85)
    tmpjoint = pm.insertJoint('Neck5')
    pm.rename(tmpjoint, 'Neck6')
    pm.joint('Neck6', e=True, co=True, p=(0, 22.596321, 3.576122)); pm.refresh()
    pm.addAttr('Neck6', longName='fat', at='float', k=True)
    pm.setAttr('Neck6.fat', 0.8)
    tmpjoint = pm.insertJoint('Neck6')
    pm.rename(tmpjoint, 'Neck7')
    pm.joint('Neck7', e=True, co=True, p=(0, 23.684044, 3.257764)); pm.refresh()
    pm.addAttr('Neck7', longName='fat', at='float', k=True)
    pm.setAttr('Neck7.fat', 0.75)
    tmpjoint = pm.insertJoint('Neck7')
    pm.rename(tmpjoint, 'Neck8')
    pm.joint('Neck8', e=True, co=True, p=(0, 24.678912, 2.979201)); pm.refresh()
    pm.addAttr('Neck8', longName='fat', at='float', k=True)
    pm.setAttr('Neck8.fat', 0.7)
    pm.setAttr('Neck8.type', 18)
    pm.setAttr('Neck8.otherType', '2', type='string')
    pm.setAttr('Neck8.drawLabel', 1)

    tmpjoint = pm.insertJoint('Neck8')
    pm.rename(tmpjoint, 'Neck9')
    pm.joint('Neck9', e=True, co=True, p=(0, 25.554396, 2.833287)); pm.refresh()
    pm.addAttr('Neck9', longName='fat', at='float', k=True)
    pm.setAttr('Neck9.fat', 0.65)
    tmpjoint = pm.insertJoint('Neck9')
    pm.rename(tmpjoint, 'Neck10')
    pm.joint('Neck10', e=True, co=True, p=(0, 26.364346, 2.819231)); pm.refresh()
    pm.addAttr('Neck10', longName='fat', at='float', k=True)
    pm.setAttr('Neck10.fat', 0.6)
    tmpjoint = pm.insertJoint('Neck10')
    pm.rename(tmpjoint, 'Neck11')
    pm.joint('Neck11', e=True, co=True, p=(0, 27.164281, 3.040694)); pm.refresh()
    pm.addAttr('Neck11', longName='fat', at='float', k=True)
    pm.setAttr('Neck11.fat', 0.55)
    pm.move('Head', 0, 27.782901, 3.483267, rpr=True); pm.refresh()
    pm.setAttr('Head.fat', 0.5)
    pm.move('HeadEnd', 0, 29.321882, 3.483267, rpr=True); pm.refresh()
    pm.setAttr('Head.type', 18)
    pm.setAttr('Head.otherType', '3', type='string')
    pm.setAttr('Head.drawLabel', 1)

    # Head
    pm.move('Jaw', 0, 27.233845, 4.684155, rpr=True); pm.refresh()
    pm.move('JawEnd', 0, 27.343004, 8.089177, rpr=True); pm.refresh()
    pm.setAttr('JawEnd.fat', 0.1)
    pm.move('Eye', -0.702294, 28.482938, 5.56851, rpr=True); pm.refresh()
    pm.move('EyeEnd', -1.776226, 28.43113, 5.776239, rpr=True); pm.refresh()
    pm.move('Ear', -1.070843, 28.702831, 4.284751, rpr=True); pm.refresh()

    # Wing
    pm.move('frontRump', -0.666333, 15.298425, 1.362798, rpr=True); pm.refresh()
    pm.rename('frontRump', 'Scapula')
    pm.setAttr('Scapula.type', 0)
    pm.setAttr('Scapula.drawLabel', 0)
    pm.parent('Scapula', w=True)
    pm.setAttr('Scapula.jointOrient', (90,0,180))

    pm.move('frontHip', -4.106932, 15.298425, 1.362798, rpr=True); pm.refresh()
    pm.rename('frontHip', 'Shoulder')
    pm.setAttr('Shoulder.type', 10)
    pm.setAttr('Shoulder.drawLabel', 1)
    pm.setAttr('Shoulder.jointOrient', (0,0,0))

    pm.move('frontKnee', -8.130809, 15.298425, 1.362798, rpr=True); pm.refresh()
    pm.rename('frontKnee', 'Elbow')
    pm.setAttr('Elbow.jointOrient', (0,0,0))
    pm.move('frontAnkle', -13.453836, 15.298425, 1.362798, rpr=True); pm.refresh()
    pm.deleteAttr('frontAnkle.worldOrient')
    pm.rename('frontAnkle', 'Wrist')
    pm.setAttr('Wrist.jointOrient', (0,0,0))
    pm.setAttr('Wrist.type', 12)
    pm.setAttr('Wrist.drawLabel', 1)

    pm.move('frontToes', -16.77636, 15.298425, 1.362798, rpr=True); pm.refresh()
    pm.rename('frontToes', 'IndexFinger1')
    pm.setAttr('IndexFinger1.jointOrient', (0,0,0))
    pm.setAttr('IndexFinger1.fat', 0.15)
    pm.setAttr('IndexFinger1.type', 0)
    pm.setAttr('IndexFinger1.drawLabel', 0)

    pm.move('frontToesEnd', -17.998683, 15.298425, 1.362798, rpr=True); pm.refresh()
    pm.rename('frontToesEnd', 'IndexFinger2')
    pm.setAttr('IndexFinger2.jointOrient', (0,0,0))
    pm.setAttr('IndexFinger2.fat', 0.15)
    pm.setAttr('IndexFinger2.type', 0)
    pm.setAttr('IndexFinger2.drawLabel', 0)

    pm.joint(p=(-18.998683, 15.298425, 1.362798), n='IndexFingerEnd'); pm.refresh()
    pm.parent('IndexFingerEnd', 'IndexFinger2')
    pm.joint('IndexFinger2', e=True, zso=True, oj='xyz', sao='yup')
    pm.setAttr('IndexFingerEnd.jointOrient', (0,0,0))
    pm.addAttr('IndexFingerEnd', longName='fat', at='float', k=True)
    pm.setAttr('IndexFingerEnd.fat', 0.15)

    pm.move('frontHeel', -13.746735, 15.298425, 1.876919, rpr=True); pm.refresh()
    pm.rename('frontHeel', 'Alula1')
    pm.setAttr('Alula1.jointOrient', (0,0,0))
    pm.setAttr('Alula1.fat', 0.15)
    pm.setAttr('Alula1.type', 0)
    pm.setAttr('Alula1.drawLabel', 0)

    pm.joint(p=(-15.070372, 15.298425, 2.061097), n='AlulaEnd'); pm.refresh()
    pm.parent('AlulaEnd', 'Alula1')
    pm.joint('Alula1', e=True, zso=True, oj='xyz', sao='yup')
    pm.setAttr('AlulaEnd.jointOrient', (0,0,0))
    pm.setAttr('Alula1.jointOrientX', 0)
    pm.addAttr('AlulaEnd', longName='fat', at='float', k=True)
    pm.setAttr('AlulaEnd.fat', 0.15)

    pm.setAttr('Scapula.jointOrient', (-180,0,110))
    #pm.setAttr('Shoulder.jointOrient', (0,0,-68))
    pm.setAttr('Shoulder.jointOrient', (-90,0,-70))
    pm.setAttr('Elbow.jointOrient', (0,0,55))
    pm.setAttr('Wrist.jointOrient', (0,0,-23))
    pm.parent('Scapula', 'Chest')

    # Claw
    pm.joint(p=(-2.88102, 2.485656, 0.575177), n='BigToe1'); pm.refresh()
    pm.parent('BigToe1', 'backAnkle')
    pm.joint('BigToe1', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('BigToe1', longName='fat', at='float', k=True)
    pm.setAttr('BigToe1.fat', 0.15)
    pm.joint(p=(-2.738667, 1.970201, 0.442352), n='BigToe2'); pm.refresh()
    pm.parent('BigToe2', 'BigToe1')
    pm.joint('BigToe2', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('BigToe2', longName='fat', at='float', k=True)
    pm.setAttr('BigToe2.fat', 0.15)
    pm.joint(p=(-2.5201, 1.178776, 0.238413), n='BigToe3'); pm.refresh()
    pm.parent('BigToe3', 'BigToe2')
    pm.joint('BigToe3', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('BigToe3', longName='fat', at='float', k=True)
    pm.setAttr('BigToe3.fat', 0.15)
    pm.joint(p=(-2.372034, 0.642633, 0.100257), n='BigToe4'); pm.refresh()
    pm.parent('BigToe4', 'BigToe3')
    pm.joint('BigToe4', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('BigToe4', longName='fat', at='float', k=True)
    pm.setAttr('BigToe4.fat', 0.15)

    pm.joint(p=(-2.539914, 1.948935, 0.991183), n='LongToe1'); pm.refresh()
    pm.parent('LongToe1', 'backAnkle')
    pm.joint('LongToe1', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('LongToe1', longName='fat', at='float', k=True)
    pm.setAttr('LongToe1.fat', 0.15)
    pm.joint(p=(-2.067113, 1.773852, 1.866707), n='LongToe2'); pm.refresh()
    pm.parent('LongToe2', 'LongToe1')
    pm.joint('LongToe2', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('LongToe2', longName='fat', at='float', k=True)
    pm.setAttr('LongToe2.fat', 0.15)
    pm.joint(p=(-1.603186, 1.602055, 2.725798), n='LongToe3'); pm.refresh()
    pm.parent('LongToe3', 'LongToe2')
    pm.joint('LongToe3', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('LongToe3', longName='fat', at='float', k=True)
    pm.setAttr('LongToe3.fat', 0.15)
    pm.joint(p=(-1.31542, 1.495492, 3.258678), n='LongToe4'); pm.refresh()
    pm.parent('LongToe4', 'LongToe3')
    pm.joint('LongToe4', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('LongToe4', longName='fat', at='float', k=True)
    pm.setAttr('LongToe4.fat', 0.15)

    pm.joint(p=(-2.877055, 1.948935, 1.446648), n='MiddleToe1'); pm.refresh()
    pm.parent('MiddleToe1', 'backAnkle')
    pm.joint('MiddleToe1', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('MiddleToe1', longName='fat', at='float', k=True)
    pm.setAttr('MiddleToe1.fat', 0.15)
    pm.joint(p=(-2.868815, 1.718236, 2.646697), n='MiddleToe2'); pm.refresh()
    pm.parent('MiddleToe2', 'MiddleToe1')
    pm.joint('MiddleToe2', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('MiddleToe2', longName='fat', at='float', k=True)
    pm.setAttr('MiddleToe2.fat', 0.15)
    pm.joint(p=(-2.863311, 1.564137, 3.448286), n='MiddleToe3'); pm.refresh()
    pm.parent('MiddleToe3', 'MiddleToe2')
    pm.joint('MiddleToe3', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('MiddleToe3', longName='fat', at='float', k=True)
    pm.setAttr('MiddleToe3.fat', 0.15)
    pm.joint(p=(-2.858005, 1.41556, 4.221158), n='MiddleToe4'); pm.refresh()
    pm.parent('MiddleToe4', 'MiddleToe3')
    pm.joint('MiddleToe4', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('MiddleToe4', longName='fat', at='float', k=True)
    pm.setAttr('MiddleToe4.fat', 0.15)
    pm.joint(p=(-2.852091, 1.249975, 5.082496), n='MiddleToe5'); pm.refresh()
    pm.parent('MiddleToe5', 'MiddleToe4')
    pm.joint('MiddleToe5', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('MiddleToe5', longName='fat', at='float', k=True)
    pm.setAttr('MiddleToe5.fat', 0.15)

    pm.joint(p=(-3.204497, 1.948935, 1.010468), n='RingToe1'); pm.refresh()
    pm.parent('RingToe1', 'backAnkle')
    pm.joint('RingToe1', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('RingToe1', longName='fat', at='float', k=True)
    pm.setAttr('RingToe1.fat', 0.15)
    pm.joint(p=(-3.772174, 1.75263, 1.87927), n='RingToe2'); pm.refresh()
    pm.parent('RingToe2', 'RingToe1')
    pm.joint('RingToe2', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('RingToe2', longName='fat', at='float', k=True)
    pm.setAttr('RingToe2.fat', 0.15)
    pm.joint(p=(-4.192402, 1.607313, 2.522409), n='RingToe3'); pm.refresh()
    pm.parent('RingToe3', 'RingToe2')
    pm.joint('RingToe3', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('RingToe3', longName='fat', at='float', k=True)
    pm.setAttr('RingToe3.fat', 0.15)
    pm.joint(p=(-4.551553, 1.483117, 3.072073), n='RingToe4'); pm.refresh()
    pm.parent('RingToe4', 'RingToe3')
    pm.joint('RingToe4', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('RingToe4', longName='fat', at='float', k=True)
    pm.setAttr('RingToe4.fat', 0.15)
    pm.joint(p=(-4.979216, 1.335229, 3.726591), n='RingToe5'); pm.refresh()
    pm.parent('RingToe5', 'RingToe4')
    pm.joint('RingToe5', e=True, zso=True, oj='xyz', sao='yup')
    pm.addAttr('RingToe5', longName='fat', at='float', k=True)
    pm.setAttr('RingToe5.fat', 0.15)



    mel.eval('asFitModeManualUpdate')
    pm.setAttr('backHeel.jointOrient', (0, 0, 0))
    pm.setAttr('backToesEnd.jointOrient', (0, 0, 0))
    pm.setAttr('Tail6.jointOrient', (0, 0, 0))
    pm.setAttr('HeadEnd.jointOrient', (0, 0, 0))
    pm.setAttr('JawEnd.jointOrient', (0, 0, 0))
    pm.setAttr('EyeEnd.jointOrient', (0, 0, 0))
    pm.setAttr('EarEnd.jointOrient', (0, 0, 0))
    pm.setAttr('IndexFinger1.jointOrientX', 0)
    pm.setAttr('IndexFinger2.jointOrientX', 0)
    pm.setAttr('IndexFingerEnd.jointOrient', (0, 0, 0))
    pm.setAttr('BigToe1.jointOrient', (180, 15, -40))
    pm.setAttr('LongToe1.jointOrientX', 0)
    pm.setAttr('MiddleToe1.jointOrientX', 0)
    pm.setAttr('RingToe1.jointOrientX', 0)
    pm.setAttr('BigToe4.jointOrient', (0, 0, 0))
    pm.setAttr('LongToe4.jointOrient', (0, 0, 0))
    pm.setAttr('MiddleToe5.jointOrient', (0, 0, 0))
    pm.setAttr('RingToe5.jointOrient', (0, 0, 0))

    #pm.move('Root', 0, -.8, 0, r=True)

def feathersFitSkeleton():
    # Primaries ================================================================
    primariesInfo= [[(-12.86360345, 18.53153049, 8.306063085), (-26.06981827, 18.53153049, 12.02674499), 'IndexFinger2'],\
                    [(-12.0106408, 18.53153049, 7.70310673), (-26.84924966, 18.53153049, 10.6590635), 'IndexFinger1'],\
                    [(-11.81945952, 18.53153049, 7.350156668), (-26.68748088, 18.53153049, 8.997256957), 'IndexFinger1'],\
                    [(-10.5547218, 18.53153049, 6.864850333), (-25.43744941, 18.53153049, 7.320744163), 'Wrist'],\
                    [(-10.01059045, 18.53153049, 6.526606523), (-23.76093662, 18.53153049, 5.5412876), 'Wrist'],\
                    [(-9.642934138, 18.53153049, 6.203068966), (-22.14324883, 18.53153049, 3.820656048), 'Wrist'],\
                    [(-9.378221591, 18.53153049, 6.011887683), (-20.45202978, 18.53153049, 2.482387063), 'Wrist'],\
                    [(-9.14292155, 18.53153049, 5.776587642), (-18.71669198, 18.53153049, 0.8794055321), 'Wrist'],\
                    [(-8.967984, 18.53153049, 5.539010509), (-17.095809, 18.53153049, -0.3849234914), 'Wrist']]
    priCtrl = pm.curve(p=[(-27.1491891127, 18.53153049, 13.0764591394),\
                    	(-27.4982296082, 18.53153049, 7.6532459788),\
                    	(-23.3200995313, 18.53153049, 1.71173650929),\
                    	(-17.2458531438, 18.53153049, -1.241109745)],\
                    	n='PrimariesCtrl')
    priJoints=[]
    for i in range(len(primariesInfo)):
        priJoints.append(createfeatherJoint('Primary_'+str(i),\
                                            primariesInfo[i][0],\
                                            primariesInfo[i][1],\
                                            primariesInfo[i][2], 3, 0.05, 25, priCtrl))

    # Secondaries ==============================================================
    secondariesInfo =  [[(-8.694386056, 18.53153049, 5.092613863), (-15.41586672, 18.53153049, -1.4838331), 'Elbow'],\
                        [(-8.486922066, 18.53153049, 4.750908469), (-14.69589146, 18.53153049, -2.115390347), 'Elbow'],\
                        [(-8.328273134, 18.53153049, 4.262757906), (-13.84960475, 18.53153049, -2.974308202), 'Elbow'],\
                        [(-8.084197852, 18.53153049, 3.725792286), (-13.05384262, 18.53153049, -3.643758883), 'Elbow'],\
                        [(-7.803511278, 18.53153049, 3.237641723), (-12.4854411, 18.53153049, -4.010062086), 'Elbow'],\
                        [(-7.583843525, 18.53153049, 2.810509981), (-11.87914614, 18.53153049, -4.313209564), 'Elbow'],\
                        [(-7.303156951, 18.53153049, 2.383378238), (-11.34863806, 18.53153049, -4.692143912), 'Elbow'],\
                        [(-6.998062849, 18.53153049, 1.992857788), (-10.67918738, 18.53153049, -5.159496274), 'Elbow'],\
                        [(-6.656357455, 18.53153049, 1.626744865), (-9.921318681, 18.53153049, -5.412119173), 'Elbow'],\
                        [(-6.387874646, 18.53153049, 1.321650763), (-9.27713029, 18.53153049, -5.588955202), 'Elbow'],\
                        [(-6.156003128, 18.53153049, 1.187409359), (-8.25400755, 18.53153049, -5.412119173), 'Elbow'],\
                        [(-5.960742903, 18.53153049, 1.016556662), (-7.281409391, 18.53153049, -5.083709405), 'Elbow']]
    secCtrl = pm.curve(p=[(-16.5246216252, 18.53153049, -1.62038791504),\
                    	(-14.9866453017, 18.53153049, -4.66487943424),\
                    	(-11.1286870108, 18.53153049, -6.76245024149),\
                    	(-7.29458769468, 18.53153049, -5.94298120383)],\
                    	n='SecondariesCtrl')
    secJoints=[]
    for i in range(len(secondariesInfo)):
        secJoints.append(createfeatherJoint('Secondary_'+str(i),\
                                            secondariesInfo[i][0],\
                                            secondariesInfo[i][1],\
                                            secondariesInfo[i][2], 3, 0.05, 25, secCtrl))

    # Tertiaris ================================================================
    tertiarisInfo= [[(-5.223763545, 18.53153049, 1.027956662), (-6.260171785, 18.53153049, -4.545627746), 'Shoulder'],\
                    [(-4.398227473, 18.53153049, 0.9751366524), (-5.326210969, 18.53153049, -3.986066628), 'Shoulder'],\
                    [(-3.428735181, 18.53153049, 0.9513619387), (-4.495570592, 18.53153049, -3.174867282), 'Shoulder'],\
                    [(-2.475140002, 18.53153049, 0.9275872249), (-3.79244802, 18.53153049, -2.385826872), 'Shoulder']]
    terCtrl = pm.curve(p=[(-3.50762228058, 18.53153049, -2.58540533101),\
                    	(-4.20619320952, 18.53153049, -3.64221776197),\
                    	(-5.33465394088, 18.53153049, -4.66320604273),\
                    	(-6.51685089755, 18.53153049, -5.36177697167)],\
                    	n='TertiarisCtrl')
    terJoints=[]
    for i in range(len(tertiarisInfo)):
        terJoints.append(createfeatherJoint('Tertiary_'+str(i),\
                                            tertiarisInfo[i][0],\
                                            tertiarisInfo[i][1],\
                                            tertiarisInfo[i][2], 3, 0.05, 25, terCtrl))

    # Primaries Coverts Top ====================================================
    priCovertsInfo=[[(-11.3947113, 18.83153049, 7.526788519), (-16.09678779, 18.83153049, 9.370112318), 'Wrist'],\
                    [(-11.15895683, 18.83153049, 7.370109178), (-16.65530952, 18.83153049, 8.738100886), 'Wrist'],\
                    [(-10.88160853, 18.83153049, 7.194329919), (-16.80228892, 18.83153049, 8.003203872), 'Wrist'],\
                    [(-10.60206759, 18.83153049, 7.045165817), (-16.49363217, 18.83153049, 6.944952171), 'Wrist'],\
                    [(-10.24289207, 18.83153049, 6.811982318), (-16.15535741, 18.83153049, 6.099265254), 'Wrist'],\
                    [(-9.866958792, 18.83153049, 6.599621044), (-15.40833396, 18.83153049, 5.070346172), 'Wrist'],\
                    [(-9.507849109, 18.83153049, 6.378404418), (-14.56264705, 18.83153049, 4.266943601), 'Wrist']]
    priCovertsJoints=[]
    for i in range(len(priCovertsInfo)):
        priCovertsJoints.append(createfeatherJoint('PrimaryCovert_'+str(i),\
                                                    priCovertsInfo[i][0],\
                                                    priCovertsInfo[i][1],\
                                                    priCovertsInfo[i][2], 2, 0.05, 10, priCtrl))

def createfeatherJoint(name, pos1, pos2, parent, sample, fat, endFatY, ctrlCurve):
    pm.select(cl=True)
    s=name+'_0'
    e=name+'_end'
    pm.joint(p=pos1, n=s); pm.refresh()
    pm.joint(p=pos2, n=e); pm.refresh()
    pm.joint(s, e=True, zso=True, oj='xyz', sao='zup')

    pm.addAttr(s, e, longName='fat', at='float', k=True, dv=fat)
    pm.addAttr(s, e, longName='fatY', at='float', k=True, dv=2)
    pm.addAttr(s, e, longName='fatZ', at='float', k=True, dv=1)
    pm.setAttr(e+'.fatY', endFatY)

    pm.addAttr(s, longName='curveGuide', at='enum', en=ctrlCurve+':', k=True, dv=0)
    pm.addAttr(s, longName='curveGuideMode', at='enum', en='point:aim', k=True, dv=1)

    pm.addAttr(s, longName='inbetweenJoints', at='byte', k=True, dv=sample)
    #pm.addAttr(s, longName='twistJoints', at='byte', k=True, dv=sample)
    #pm.addAttr(s, longName='bendyJoints', at='bool', k=True, dv=True)

    pm.setAttr(e+'.jointOrient', (0, 0, 0))
    pm.parent(s, parent)
    pm.refresh()
