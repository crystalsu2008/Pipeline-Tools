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

def referenceSymmetrical(across='YZ', posiToNega=False):
    objs = pm.ls(sl=True, fl=True)
    referenceMesh = objs[-1]
    try:
        refMeshShape = pm.listRelatives(referenceMesh, s=True)[0]
    except:
        print 'Error: The last selected object should be a referenceMesh.'
        return
    if not pm.objectType(refMeshShape, i='mesh'):
        print 'Error: The last selected object should be a referenceMesh.'
        return

    symId, symDir = symertricalOptions(across, posiToNega)

    matcher = pm.nodetypes.ClosestPointOnMesh()
    pm.connectAttr(referenceMesh+'.outMesh', matcher+'.inMesh')

    for vtx in objs[:-1]:
        vtxtype = pm.ls(vtx, showType=True)[1]
        if vtxtype == 'float3':
            meshvtx, vid = vtx.split('[')
            vid = vid[:-1]
            refvtx = referenceMesh+'.vtx['+vid+']'

            inpos = dt.Point(pm.pointPosition(refvtx, l=True))
            if inpos[symId]*symDir > 0:
                inpos[symId] *= -1
                pm.setAttr(matcher+'.inPosition', inpos)
                symvtxid = str( pm.getAttr(matcher+'.closestVertexIndex') )

                if not symvtxid == vid:
                    symvtx = meshvtx+'['+symvtxid+']'
                    pos = dt.Point(pm.pointPosition(symvtx, l=True))
                    pos[symId] *= -1
                    pm.xform(vtx, os=True, a=True, t=pos)

    pm.delete(matcher)
