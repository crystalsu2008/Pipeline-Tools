import pymel.core as pm

def HHK1toHHAS():
    sel = pm.ls(sl=True)[0]
    prefix, root = sel.split(':')
    print prefix, root

    K1angle_r = prefix+':ANKLE_RIGHT'
    IKLeg_R_Tran = pm.spaceLocator(n='IKLeg_R_tr')

    pm.pointConstraint( K1angle_r, IKLeg_R_Tran )
