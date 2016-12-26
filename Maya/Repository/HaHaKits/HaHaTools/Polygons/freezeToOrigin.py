import pymel.core as pm

def freezeToOrigin(objects=None,cx='mid',cy='min',cz='mid'):
    if not objects:
        objects = pm.ls(sl=True, dag=True, typ="transform")
    for obj in objects:
        bbox = pm.exactWorldBoundingBox(obj)

        if cx=='min':
            x = bbox[0]
        elif cx=='mid':
            x = bbox[0] + (bbox[3]-bbox[0])/2
        else:
            x = bbox[3]

        if cy=='min':
            y = bbox[1]
        elif cy=='mid':
            y = bbox[1] + (bbox[4]-bbox[1])/2
        else:
            y = bbox[4]

        if  cz=='min':
            z = bbox[2]
        elif cz=='mid':
            z = bbox[2] + (bbox[5]-bbox[2])/2
        else:
            z = bbox[5]

        pm.move(x,y,z, obj+'.scalePivot', obj+'.rotatePivot', a=True, ws=True, rpr=True, spr=True)
        pm.move(-x,-y,-z, obj, r=True, ws=True)
        pm.makeIdentity( apply=True, t=True, r=True, s=True, n=False, pn=True )
