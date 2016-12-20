import pymel.core as pm
import pymel.core.datatypes as dt

def referenceMirror(across='YZ', refresh=True, duplicate=True, unoverlap=True):
    objs = pm.ls(sl=True)
    meshs = pm.listRelatives(objs, s=True, type='mesh')
    allVtxs=[]
    dupMeshs={}
    for obj in objs:
        objtype = pm.ls(obj, showType=True)[1]
        if objtype == 'float3':
            if duplicate:
                meshvtx, vid = obj.split('[')
                mesh = meshvtx.split('.')[0]
                vid = vid[:-1]
                if not mesh in dupMeshs:
                    dupMeshs[mesh] = pm.duplicate(mesh, rr=True)[0]
                    if unoverlap:
                        abox = pm.exactWorldBoundingBox(dupMeshs.keys(), meshs)
                        bbox = pm.exactWorldBoundingBox(dupMeshs[mesh])
                        pm.move(abox[3]-bbox[0], 0, 0, dupMeshs[mesh], r=True)
                obj = dupMeshs[mesh]+'.vtx['+vid+']'
            allVtxs.extend(pm.ls(obj, fl=True))

    if len(meshs)==0 or (len(meshs)==1 and len(allVtxs)==0):
        print 'Error: At least select two meshs, or some mesh vertexs and one mesh, the last mesh should be a reference mesh.'
        return

    referenceMesh = meshs[-1]

    for mesh in meshs[:-1]:
        if duplicate:
            if not mesh in dupMeshs:
                dupMeshs[mesh] = pm.duplicate(mesh, rr=True)
                mesh = dupMeshs[mesh]
                if unoverlap:
                    abox = pm.exactWorldBoundingBox(dupMeshs.keys(), meshs)
                    bbox = pm.exactWorldBoundingBox(mesh)
                    pm.move(abox[3]-bbox[0], 0, 0, mesh, r=True)
        vtxs =  pm.ls( pm.polyListComponentConversion(mesh, tv=True), fl=True )
        allVtxs.extend(vtxs)

    mirId=0
    if across=='XY':
        mirId=2
    elif across=='YZ':
        mirId=0
    elif across=='XZ':
        mirId=1
    else:
        print 'Wrong symmetrical across argement "'+across+'".'
        return

    matcher = pm.nodetypes.ClosestPointOnMesh()
    pm.connectAttr(referenceMesh+'.outMesh', matcher+'.inMesh')

    mirPos = {}
    machid = {}

    print 'Scanning...'
    pm.select(cl=True)
    for vtx in allVtxs:
        meshvtx, vid = vtx.split('[')
        vid = vid[:-1]

        if not vid in machid:
            refvtx = referenceMesh+'.vtx['+vid+']'
            inpos = dt.Point(pm.pointPosition(refvtx, l=True))
            inpos[mirId] *= -1
            pm.setAttr(matcher+'.inPosition', inpos)
            mirvtxid = str( pm.getAttr(matcher+'.closestVertexIndex') )
            machid[vid] = mirvtxid

        #if not machid[vid] == vid:
        mirvtx = meshvtx+'['+machid[vid]+']'
        pos = dt.Point(pm.pointPosition(mirvtx, l=True))
        pos[mirId] *= -1
        thisPos = dt.Point(pm.pointPosition(vtx, l=True))
        mirPos[vtx] = pos
        if refresh:
            pm.select(vtx, tgl=True)
            pm.refresh()

    print 'Mirroring...'
    if refresh:
        for vtx in mirPos:
            pm.xform(vtx, os=True, a=True, t=mirPos[vtx])
            pm.select(vtx, tgl=True)
            pm.refresh()
        pm.select(cl=True)
    else:
        for vtx in mirPos:
            pm.xform(vtx, os=True, a=True, t=mirPos[vtx])

    print 'Done!'
    pm.delete(matcher)
