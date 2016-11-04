import pymel.core as pm

def freezeToOrigin():
    for obj in pm.ls(sl=True, dag=True, typ="transform"):
        bbox = pm.exactWorldBoundingBox(obj)
        x = bbox[0] + (bbox[3]-bbox[0])/2
        y = bbox[1]
        z = bbox[2] + (bbox[5]-bbox[2])/2
        pm.move(x,y,z, obj+'.scalePivot', obj+'.rotatePivot', a=True, ws=True, rpr=True, spr=True)
        pm.move(-x,-y,-z, obj, r=True, ws=True)
        pm.makeIdentity( apply=True, t=True, r=True, s=True, n=False, pn=True )
