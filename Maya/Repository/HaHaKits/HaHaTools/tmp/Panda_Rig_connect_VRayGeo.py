import pymel.core as pm
import maya.mel as mel

def Panda_Rig_connect_VRayGeo():
    nspaceA = 'Panda_Rig:'
    nspaceB = ''

    pm.blendShape( nspaceA+'panda_body', nspaceB+'panda_bodyWrap_mesh', w=[(0, 1)])
    pm.blendShape( nspaceA+'Head_MeshShape', nspaceB+'Head_MeshShape', w=[(0, 1)])
    pm.blendShape( nspaceA+'Tongue_MeshShape', nspaceB+'Tongue_MeshShape', w=[(0, 1)])
    pm.blendShape( nspaceA+'Teeth_Upper_MeshShape', nspaceB+'Teeth_Upper_MeshShape', w=[(0, 1)])
    pm.blendShape( nspaceA+'Teeth_Lower_Mesh', nspaceB+'Teeth_Lower_Mesh', w=[(0, 1)])

    pm.select(cl=True)
    pm.select(nspaceB+'nose', nspaceA+'Head_Mesh', r=True)
    mel.eval('CreateWrap;')

    pm.select(cl=True)
    pm.select(nspaceB+'panda_pants', nspaceA+'panda_body', r=True)
    mel.eval('CreateWrap;')

    pm.select(cl=True)
    pm.select(nspaceB+'panda_shoe_l', nspaceA+'panda_shoe_L', r=True)
    mel.eval('CreateWrap;')

    pm.select(cl=True)
    pm.select(nspaceB+'panda_shoe_r', nspaceA+'panda_shoe_R', r=True)
    mel.eval('CreateWrap;')

    pm.select(cl=True)
    pm.select(nspaceB+'panda_pants.f[5473]',\
              nspaceB+'panda_pants.f[5327]',\
              nspaceB+'panda_pants.f[6182]',\
              nspaceB+'panda_pants.f[6051]',\
              r=True)
    mel.eval('createHair 8 8 10 0 0 0 0 5 0 2 2 2;')

    fol = pm.ls(type='follicle')

    pm.setAttr( fol[0]+'.parameterU', 0.5113)
    pm.setAttr( fol[0]+'.parameterV', 0.9675)
    parent = pm.listRelatives(fol[0], p=True)[0]
    pm.parentConstraint( parent, nspaceB+'botton1_grp' )

    pm.setAttr( fol[1]+'.parameterU', 0.5017)
    pm.setAttr( fol[1]+'.parameterV', 0.4965)
    parent = pm.listRelatives(fol[1], p=True)[0]
    pm.parentConstraint( parent, nspaceB+'botton2_grp' )

    pm.setAttr( fol[2]+'.parameterU', 0.9097)
    pm.setAttr( fol[2]+'.parameterV', 0.5351)
    parent = pm.listRelatives(fol[2], p=True)[0]
    pm.parentConstraint( parent, nspaceB+'botton3_grp' )

    pm.setAttr( fol[3]+'.parameterU', 0.9145)
    pm.setAttr( fol[3]+'.parameterV', 0.4267)
    parent = pm.listRelatives(fol[3], p=True)[0]
    pm.parentConstraint( parent, nspaceB+'botton4_grp' )

    #locator_eye = pm.spaceLocator( p=(0, 0, 0), n='locator_eye' )
    locator_eye='locator_eye'
    pm.parentConstraint( nspaceA+'Head_M', locator_eye, mo=True )
    #pm.parent(nspaceB+'locator_eye_R', nspaceB+'locator_eye_L', locator_eye)
    pm.orientConstraint( nspaceA+'Eye_R', 'locator_eye_R_tar', offset=(0,0,0), weight=1)
    pm.orientConstraint( nspaceA+'Eye_L', 'locator_eye_L_tar', offset=(0,0,0), weight=1)

    pm.parentConstraint( 'locator_eye_R_tar', nspaceB+'locator_eye_R')
    pm.parentConstraint( 'locator_eye_L_tar', nspaceB+'locator_eye_L')
