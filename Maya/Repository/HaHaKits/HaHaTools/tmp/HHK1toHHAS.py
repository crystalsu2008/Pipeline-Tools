import pymel.core as pm

def HHK1toHHAS():
    sel = pm.ls(sl=True)[0]
    prefix, root = sel.split(':')

    pm.select(sel, hierarchy=True)
    tagJoints = pm.ls(sl=True)
    for joint in tagJoints:
        pm.setAttr(joint+'.r', 0, 0, 0)
    pm.select(cl=True)

    pm.setAttr(prefix+":HIP_CENTER.t", 0, 54.384, 7.815);
    pm.setAttr(prefix+":SHOULDER_LEFT.tx", 12.727);
    pm.setAttr(prefix+":SHOULDER_RIGHT.tx", 12.727);

    pos = pm.xform(prefix+':SPINE', q=True, t=True, ws=True)
    im_SPINE_L = pm.joint(p=pos)
    im_SPINE_R = pm.joint(p=pos)
    pos = pm.xform(prefix+':SHOULDER_LEFT', q=True, t=True, ws=True)
    im_SHOULDER_L = pm.joint(p=pos)
    pos = pm.xform(prefix+':SHOULDER_RIGHT', q=True, t=True, ws=True)
    im_SHOULDER_R = pm.joint(p=pos)

    pm.parent(im_SHOULDER_L, im_SPINE_L)
    pm.parent(im_SHOULDER_R, im_SPINE_R)
    pm.parent(im_SPINE_L, im_SPINE_R, prefix+':SPINE')

    FKScapula_L_ik = pm.ikHandle(sj=im_SPINE_L, ee=im_SHOULDER_L)
    FKScapula_R_ik = pm.ikHandle(sj=im_SPINE_R, ee=im_SHOULDER_R)
    pm.pointConstraint(FKScapula_L_ik[0], prefix+':SHOULDER_LEFT', mo=False)
    pm.pointConstraint(FKScapula_R_ik[0], prefix+':SHOULDER_RIGHT', mo=False)

    oConsMap = {'FKRoot_M': (['HIP_CENTER'],[1]),
                'FKSpine1_M': (['HIP_CENTER', 'SPINE'],[2,1]),
                'FKSpine2_M': (['HIP_CENTER', 'SPINE'],[1,2]),
                'FKChest_M': (['SPINE'],[1]),
                'FKNeck_M': (['SPINE', 'SHOULDER_CENTER'],[1,1]),
                'FKHead_M': (['SHOULDER_CENTER'],[1]),
                'FKShoulder_L': (['SHOULDER_LEFT'],[1]),
                'FKElbow_L': (['ELBOW_LEFT'],[1]),
                'FKWrist_L': (['WRIST_LEFT'],[1]),
                'FKShoulder_R': (['SHOULDER_RIGHT'],[1]),
                'FKElbow_R': (['ELBOW_RIGHT'],[1]),
                'FKWrist_R': (['WRIST_RIGHT'],[1]),
                'IKLeg_L': (['ANKLE_LEFT'],[1]),
                'IKLeg_R': (['ANKLE_RIGHT'],[1]),
                'FKToes_L': (['FOOT_LEFT'],[1]),
                'FKToes_R': (['FOOT_RIGHT'],[1]),
                'FKScapula_L': ([str(im_SPINE_L)],[1]),
                'FKScapula_R': ([str(im_SPINE_R)],[1])}
    pm.rename(im_SPINE_L, prefix+':'+im_SPINE_L)
    pm.rename(im_SPINE_R, prefix+':'+im_SPINE_R)

    for ctrl, tagsInfo in oConsMap.iteritems():
        tags=[]
        weights=[]
        for name in tagsInfo[0]:
            tags.append(prefix+':'+name)
        pm.orientConstraint(tags, ctrl, mo=True)

        for (name, weight) in zip(tags, tagsInfo[1]):
            pm.orientConstraint(name, ctrl, e=True, w=weight)



    pConsMap = {'RootX_M': ['HIP_CENTER'],
                'IKLeg_L': ['ANKLE_LEFT'],
                'IKLeg_R': ['ANKLE_RIGHT'],
                'PoleLeg_L': ['KNEE_LEFT'],
                'PoleLeg_R': ['KNEE_RIGHT']}

    for ctrl, tagsName in pConsMap.iteritems():
        tags=[]
        for name in tagsName:
            tags.append(prefix+':'+name)
        pm.pointConstraint(tags, ctrl, mo=True)

    #K1angle_r = prefix+':ANKLE_RIGHT'
    #IKLeg_R_Tran = pm.spaceLocator(n='IKLeg_R_tr')
