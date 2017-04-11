import pymel.core as pm
import maya.mel as mel

def HH_ComplexBlender(poses=None,
                      characters=['HHAS_PronounciationSet','HHAS_ExpressionSet','HHAS_FaceSet'],
                      geometries=None):

    # Prepare Selected Objects
    #
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

    # Build Experssion Data
    #
    expressions = {}
    blendShapes = []
    if meshs:
        for mesh in meshs:
            expressions[str(mesh)] = {'geometry': mesh, 'type':'mesh', 'group': pm.group(em=True, name=mesh), 'poses': []}
            expressions[str(mesh)]['blendShapes'] = searchNodes(mesh, 'blendShape')
            blendShapes.extend(expressions[str(mesh)]['blendShapes'])
    if nurbses:
        for nurbs in nurbses:
            expressions[str(nurbs)] = {'geometry': nurbs, 'type':'nurbs', 'group': pm.group(em=True, name=nurbs), 'poses': []}
            expressions[str(nurbs)]['blendShapes'] = searchNodes(nurbs, 'blendShape')
            blendShapes.extend(expressions[str(nurbs)]['blendShapes'])

    # Duplicate Experssion Pose
    #
    poseMove = 0
    number = 0
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
            exprData['poses'].append({'pose': pose, 'id': number, 'geo': dupPose})
            number += 1

        poseMove += poseMoveAdd*2.1
        pm.move(poseMove, poseGeos, x=True)

    # Build Complex Expressions Blendshape
    pm.delete(blendShapes)

    prefix = 'ComplexExpr_'
    textScale=10
    ty = 0
    offset=-12
    font='Times New Roman|h-13|w400|c0'

    complexExpressionGrp = pm.group(em=True, name=prefix+'Contol_Grp')

    for expr, exprData in expressions.iteritems():
        exprData['complexBlender'] = pm.blendShape( exprData['geometry'], foc=True )[0]
        for pose in exprData['poses']:
            pm.blendShape(exprData['complexBlender'], e=True, t=(exprData['geometry'], pose['id'], pose['geo'], 1.0))
            aliasMel = 'blendShapeRenameTargetAlias '+exprData['complexBlender']+' '+str(pose['id'])+' '+pose['pose']+';'
            mel.eval(aliasMel)

            control = prefix+'Slider_'+pose['pose']
            if not pm.objExists(control):
                Slider_Dock = sliderDock_curve(prefix+'Slider_Dock_'+pose['pose'])
                titleCurve = sliderLabel_curve(prefix+'Title_'+pose['pose'], pose['pose'], textScale, font)
                SlideSlot = slideSlot_curve(prefix+'Slider_Slot_'+pose['pose'])
                Slider = slider_curve(control)

                pm.parent(Slider, Slider_Dock)
                pm.parent(SlideSlot, Slider_Dock)
                pm.parent(titleCurve, Slider_Dock)
                pm.parent(Slider_Dock, complexExpressionGrp)

                pm.transformLimits(Slider, tx=(0, 50), etx=(1, 1))
                pm.setAttr((Slider+'.ty'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.tz'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.rx'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.ry'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.rz'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.sx'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.sy'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.sz'), l=True, k=False, cb=False)
                pm.setAttr((Slider+'.v'), l=True, k=False, cb=False)

                pm.setAttr((Slider_Dock+".t"), (0, ty, 0))
                ty += offset

            pm.setDrivenKeyframe(exprData['complexBlender']+"."+pose['pose'], cd=control+'.tx', dv=0, v=0, itt='linear', ott='linear')
            pm.setDrivenKeyframe(exprData['complexBlender']+"."+pose['pose'], cd=control+'.tx', dv=50, v=1, itt='linear', ott='linear')
            print exprData['complexBlender']+"."+pose['pose'], control+'.tx'

    pm.select(cl=True)
    for geo, exprData in expressions.iteritems():
        pm.select(exprData['group'], tgl=True)

    targetsBox = pm.exactWorldBoundingBox()
    slidersBox = pm.exactWorldBoundingBox(complexExpressionGrp)
    xpos = targetsBox[0] + 50
    ypos = targetsBox[1] - 10
    pm.setAttr((complexExpressionGrp+".t"), (xpos, ypos, 0))
    pm.select(complexExpressionGrp, tgl=True)

def searchNodes(innode, searchNodeType, exceptType=['joint','animCurveUU','animCurveTL','transform','animClip','groupId','objectSet'], marked=[]):
    sourceNodes = pm.listConnections(innode, d=False, s=True, scn=True)
    sourceNodes = list(set(sourceNodes).difference(set(marked)))
    marked.extend(sourceNodes)
    nodes = []
    for node in sourceNodes:
        nodeType = pm.nodeType(node)
        if nodeType not in exceptType:
            if nodeType == searchNodeType:
                nodes.append( node )
            nodes.extend( searchNodes(node, searchNodeType, exceptType, marked) )
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

def slider_curve(name, l=5, h=7, d=0):
    return pm.curve( n=name, d=1, p=[(-0.5*l, 0.5*h, d), (0.5*l, 0.5*h, d), (0.5*l, -0.5*h, d), (-0.5*l, -0.5*h, d), (-0.5*l, 0.5*h, d)] )

def slideSlot_curve(name, l=50, h=1, d=0):
    curve = pm.curve( n=name, d=1, p=[(0, 0.5*h, d), (l, 0.5*h, d), (l, -0.5*h, d), (0, -0.5*h, d), (0, 0.5*h, d)] )
    pm.setAttr(curve+'.template', 1)
    return curve

def sliderDock_curve(name, lmn=-50, lmx=54, h=10, d=0):
    return pm.curve( n=name, d=1, p=[(lmn, 0.5*h, d), (lmx, 0.5*h, d), (lmx, -0.5*h, d), (lmn, -0.5*h, d), (lmn, 0.5*h, d)] )

def sliderLabel_curve(name, title, s, font='Times New Roman|h-13|w400|c0', t=(-28, 0, 0)):
    curve = pm.textCurves(n=name, ch=False, f=font, t=title)[0]
    pm.setAttr(curve+'.s', (s, s, s))
    freezeToOrigin(objects=[str(curve)],cx='mid',cy='mid',cz='mid')
    pm.setAttr(curve+'.t', t)
    pm.setAttr(curve+'.template', 1)
    return curve

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
