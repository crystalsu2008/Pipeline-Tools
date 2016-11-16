import pymel.core as pm
import pymel.core.datatypes as dt

def symertricalOptions(across='YZ', posiToNega=True):
    if across=='XY':
        symId=2
    elif across=='YZ':
        symId=0
    elif across=='XZ':
        symId=1
    else:
        print 'Wrong symmetrical across argement "'+across+'".'
        symId=None

    symDir = -1 if posiToNega else 1

    return symId, symDir

def matchPoints(referenceMesh, across='YZ', posiToNega=True):
    symId, symDir = symertricalOptions(across='YZ', posiToNega=True)

    refTrans = pm.listRelatives(referenceMesh, p=True)[0]
    #piv = dt.Point(pm.xform(refTrans, q=True, ws=True, a=True, piv=True)[:3])

    matcher = pm.nodetypes.ClosestPointOnMesh()
    pm.connectAttr(referenceMesh+'.outMesh', matcher+'.inMesh')

    machMap={}
    vtxs = pm.ls(pm.polyListComponentConversion( referenceMesh, tv=True, internal=True ), fl=True)
    for vtx in vtxs:
        inpos = dt.Point(pm.pointPosition(vtx, l=True))
        if inpos[symId]*symDir > 0:
            inpos[symId] *= -1

            pm.setAttr(matcher+'.inPosition', inpos)
            symvid = str( pm.getAttr(matcher+'.closestVertexIndex') )

            vid = vtx.split('[')[1][:-1]
            if not vid == symvid:
                machMap[vid] = symvid
                #pm.select(referenceMesh+'.vtx['+vid+']', tgl=True)
    pm.delete(matcher)

    return machMap

def referenceSymmetrical(across='YZ', posiToNega=True):
    objs = pm.ls(sl=True, dag=True, type='mesh', fl=True)
    referenceMesh = objs[0]

    symId, symDir = symertricalOptions(across, posiToNega)
    machMap = matchPoints(referenceMesh, across, posiToNega)

    for mesh in objs[1:]:
        for vid, symvid in machMap.iteritems():
            vtx = mesh+'.vtx['+vid+']'
            symvtx = mesh+'.vtx['+symvid+']'
            pos = dt.Point(pm.pointPosition(symvtx, l=True))
            pos[symId] *= -1
            pm.xform(vtx, os=True, a=True, t=pos)
