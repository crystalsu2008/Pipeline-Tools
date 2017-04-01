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
        meshs = pm.listRelatives(pm.ls(sl=True), typ='mesh')
        validMesh = [x for x in meshs if not pm.getAttr(x+'.intermediateObject')]
        nurbses = pm.listRelatives(pm.ls(sl=True), typ='nurbsSurface')
        validNurbs = [x for x in nurbses if not pm.getAttr(x+'.intermediateObject')]
        geometries = validMesh + validNurbs
        if not geometries:
            pm.warning( "Please at least selected one valid geometry!" )
            return

    #complexExprGrp = pm.group( em=True, name='Complex_Experssions' )
    print geometries
    expressions = {}
    for geo in geometries:
        expressions[str(geo)] = {'geometry': geo, 'group': pm.group(em=True, name=geo), 'poses': {}}

    for pose in poses:
        for char in characters:
            pm.pose(char, a=True, n=pose)
            pm.refresh()
#         for geo in geometries:
#             dupPose = pm.duplicate(geo, po=True)
#             pm.parent(dupPose, expressions[str(geo)]['group'])
#             expressions[str(geo)]['poses'][pose] = dupPose
#
#
# def copyMesh(mesh):
#     if not pm.nodeType(mesh) == mesh:
#         mesh = pm.listRelatives(mesh, typ='mesh')[0]
#
#     string $cube[] = `polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 0`;
#     pm.polyCube(w=1, h=1, d=1, sx=1, sy=1,)
