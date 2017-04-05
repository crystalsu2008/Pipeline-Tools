import pymel.core as pm

def HH_ComplexBlender(poses=None,
                      characters=['HHAS_PronounciationSet','HHAS_ExpressionSet','HHAS_FaceSet'],
                      geometries=None):
    if not poses:
        clips = pm.ls(sl=True, type='animClip')
        if not clips:
            clips = pm.ls(type='animClip')
            if not clips:
                pm.warning( "No Pose Found!" )
                return
        poses = [clip for clip in clips if pm.getAttr(clip+'.pose')]
        if not poses:
            pm.warning( "No Pose Found!" )
            return

    if not characters:
        characters = pm.ls(sl=True, type='character')
        if not characters:
            characters = pm.ls(type='characters')
            if not characters:
                pm.warning( "No Character Found!" )
                return

    if not geometries:
        geometries = pm.ls(sl=True)
    meshs = filterMeshs(geometries)
    nurbses = filterNurbs(geometries)
    if not meshs and not nurbses:
        pm.warning( "Please at least selected one valid geometry!" )
        return

    #complexExprGrp = pm.group( em=True, name='Complex_Experssions' )
    expressions = {}
    if meshs:
        for mesh in meshs:
            expressions[str(mesh)] = {'geometry': mesh, 'type':'mesh', 'group': pm.group(em=True, name=mesh), 'poses': {}}
            expressions[str(mesh)]['blendShapes'] = searchNodes(mesh, 'blendShape')
            print expressions[str(mesh)]['blendShapes']
            # , ['joint','animCurveUU','animCurveTL','transform','animClip'], True)
    if nurbses:
        for nurbs in nurbses:
            expressions[str(nurbs)] = {'geometry': nurbs, 'type':'nurbs', 'group': pm.group(em=True, name=nurbs), 'poses': {}}
            expressions[str(nurbs)]['blendShapes'] = searchNodes(nurbs, 'blendShape')

    poseMove = 0
    for pose in poses:
        poseMoveAdd = 0
        poseGeos = []
        for char in characters:
            pm.pose(char, a=True, n=pose)
            pm.refresh()
        for geo, exprData in expressions.iteritems():
            if exprData['type'] == 'mesh':
                dupPose = copyMesh(exprData['geometry'], pose)
            elif exprData['type'] == 'nurbs':
                dupPose = copyNurbs(exprData['geometry'], pose)

            bbox = pm.exactWorldBoundingBox(dupPose)
            poseMoveAdd = bbox[3] if bbox[3] > poseMoveAdd else poseMoveAdd
            poseGeos.append(dupPose)

            pm.parent(dupPose, exprData['group'])
            exprData['poses'][pose] = dupPose

        poseMove += poseMoveAdd*2.1
        pm.move(poseMove, poseGeos, x=True)


def searchNodes(innode, searchNodeType, marked=[]):
    sourceNodes = pm.listConnections(innode, d=False, s=True, scn=True)
    sourceNodes = list(set(sourceNodes).difference(set(marked)))
    marked.extend(sourceNodes)
    nodes = []
    for node in sourceNodes:
        if pm.nodeType(node) == searchNodeType:
            nodes.append( node )
        nodes.extend( searchNodes(node, searchNodeType, marked) )
    return nodes

def copyMesh(mesh, poseName=''):
    cube = pm.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=0)[0]
    cubeShape = pm.listRelatives(cube, c=True, s=True)[0]
    pm.connectAttr(mesh+'.outMesh', cubeShape+'.inMesh', f=True)
    pm.delete(cube, ch=True)
    return pm.rename(cube, mesh+'_'+poseName)

def copyNurbs(nurbs, poseName=''):
    sphere = pm.sphere(r=10, ch=0)[0]
    sphereShape = pm.listRelatives(sphere, c=True, s=True)[0]
    pm.connectAttr(nurbs+'.worldSpace[0]', sphereShape+'.create', f=True)
    pm.delete(sphere, ch=True)
    return pm.rename(sphere, nurbs+'_'+poseName)


def filterMeshs(objs):
    meshs = pm.ls(objs, type='mesh')
    trans = pm.ls(objs, type='transform')
    if trans:
        validMeshs = [x for x in pm.listRelatives(trans, typ='mesh') if not pm.getAttr(x+'.intermediateObject')]
        meshs.extend(validMeshs)
    return meshs if meshs else None

def filterNurbs(objs):
    nurbses = pm.ls(objs, type='nurbsSurface')
    trans = pm.ls(objs, type='transform')
    if trans:
        validNurbses = [x for x in pm.listRelatives(trans, typ='nurbsSurface') if not pm.getAttr(x+'.intermediateObject')]
        nurbses.extend(validNurbses)
    return nurbses if nurbses else None
