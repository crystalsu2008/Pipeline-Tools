import pymel.core as pm
import maya.mel as mel
import freezeToOrigin

def HH_Face(name='HHExpr', textScale=10, font='Times New Roman|h-13|w400|c0'):

    p=0

    baseMesh = 'Head_Mesh'

    pronTargs = {'ZCDNRSTX': {'label': 'zcdnrstx', 'tar': 'Mouth_ZCDNRSTX'},
                 'A_E_I':    {'label': 'a_e_i',    'tar': 'Mouth_A_E_I'   },
                 'U_W':      {'label': 'u_w',      'tar': 'Mouth_U_W'     },
                 'B_M_P':    {'label': 'b_m_p',    'tar': 'Mouth_B_M_P'   },
                 'F_V':      {'label': 'f_v',      'tar': 'Mouth_F_V'     },
                 'O':        {'label': 'o',        'tar': 'Mouth_O'       },
                 'Kiss':     {'label': 'kiss',     'tar': 'Mouth_Kiss'    }}

    handles = {'Jaw': {'points': [(0, -7, 0),
                                 (-0.794751475, -7, 0),
                                 (-3.830259775, -7, 0),
                                 (-7.293831375, -5.5388791, 0),
                                 (-9.719471875, -1.66854875, 0),
                                 (-10.33177008, 1.94991542, 0),
                                 (-10.33177008, 3.9580737, 0),
                                 (-10.33177008, 6, 0),
                                 (-10.33177008, 7, 0),
                                 (0, 7, 0),
                                 (10.33177007, 7, 0),
                                 (10.33177007, 6, 0),
                                 (10.33177007, 3.9580737, 0),
                                 (10.33177007, 1.94991542, 0),
                                 (9.719471915, -1.66854875, 0),
                                 (7.293831425, -5.5388791, 0),
                                 (3.830259825, -7, 0),
                                 (0.794751525, -7, 0),
                                 (0, -7, 0)],
                       'd': 3, 'grp': 'Jaw_grp', 'grplocal': (0,-31.5,0),
                       'targs':['Jaw_UP', 'Jaw_Down', 'Jaw_Move_R', 'Jaw_Move_L'],
                       'lim': [(-7, 7), (-5, 5), (0, 0)],
                       'lock':['tz','rx','ry','rz','sx','sy','sz','v']},
                'Jaw_Scope':{'points': [(-17.346979, 12, 0), (17.346979, 12, 0), (17.346979, -12, 0), (-17.346979, -12, 0), (-17.346979, 12, 0)],
                                'd': 1, 'decorate': True, 'local': (0,-31.5,0)}}

    targets =  {'Jaw_UP': {'label': 'jaw_up', 'tar': 'Jaw_UP', 'Driver': 'Jaw', 'Key': [('ty',0,0), ('ty',5,1)]},
                    'Jaw_Down': {'label': 'jaw_down', 'tar': 'Jaw_Down', 'Driver': 'Jaw', 'Key': [('ty',0,0), ('ty',-5,1)]},
                        'Jaw_Move_R': {'label': 'jaw_move_r', 'tar': 'Jaw_Move_R', 'Driver': 'Jaw', 'Key': [('tx',0,0), ('tx',-7,1)]},
                            'Jaw_Move_L': {'label': 'jaw_move_l', 'tar': 'Jaw_Move_L', 'Driver': 'Jaw', 'Key': [('tx',0,0), ('tx',7,1)]}}

    targetsx  =  {
                'Mouth_Shrink_R': 'Mouth_Shrink_R',
                    'Mouth_Shrink_L': 'Mouth_Shrink_L',
                        'Mouth_Extend_R': 'Mouth_Extend_R',
                            'Mouth_Extend_L': 'Mouth_Extend_L',
                'Mouth_Smile': 'Mouth_Smile',
                    'Mouth_Smile_R': 'Mouth_Smile_R',
                        'Mouth_Smile_L': 'Mouth_Smile_L',
                            'Mouth_Depressed': 'Mouth_Depressed',
                                'Mouth_Depressed_R': 'Mouth_Depressed_R',
                                    'Mouth_Depressed_L': 'Mouth_Depressed_L',
                'Mouth_Jeer_Down': 'Mouth_Jeer_Down',
                    'Mouth_Jeer_Down_R': 'Mouth_Jeer_Down_R',
                        'Mouth_Jeer_Down_L': 'Mouth_Jeer_Down_L',
                            'Mouth_Jeer_Up': 'Mouth_Jeer_Up',
                                'Mouth_Jeer_Up_R': 'Mouth_Jeer_Up_R',
                                    'Mouth_Jeer_Up_L': 'Mouth_Jeer_Up_L',
                'Brow_Up_In_R': 'Brow_Up_In_R',
                    'Brow_Up_In_L': 'Brow_Up_In_L',
                        'Brow_Up_Out_R': 'Brow_Up_Out_R',
                            'Brow_Up_Out_L': 'Brow_Up_Out_L',
                                'Brow_Down_Out_R': 'Brow_Down_Out_R',
                                    'Brow_Down_Out_L': 'Brow_Down_Out_L',
                                        'Brow_Angry_R': 'Brow_Angry_R',
                                            'Brow_Angry_L': 'Brow_Angry_L',
                'LowerEyelid_Half_R': 'LowerEyelid_Half_R',
                    'LowerEyelid_Half_L': 'LowerEyelid_Half_L',
                        'UpperEyelid_Half_R': 'UpperEyelid_Half_R',
                            'UpperEyelid_Half_L': 'UpperEyelid_Half_L',
                                'UpperEyelid_R': 'UpperEyelid_R',
                                    'UpperEyelid_L': 'UpperEyelid_L',
                                        'LowerEyelid_Look_Up': 'LowerEyelid_Look_Up',
                                            'UpperEyelid_Look_Down': 'UpperEyelid_Look_Down',
                'Nose_Enlarge': 'Nose_Enlarge',
                    'Nose_Down': 'Nose_Down',
                        'Nose_Up': 'Nose_Up',
                            'Nose_Up_R': 'Nose_Up_R',
                                'Nose_Up_L': 'Nose_Up_L',
                                    'Nose_Move_R': 'Nose_Move_R',
                                        'Nose_Move_L': 'Nose_Move_L'}

    exprBlender = None
    if pm.objExists(baseMesh):
        exprBlender = pm.blendShape( 'Head_Mesh' )[0]
    else:
        pm.warning('The base mesh "'+targets['Base']['tar']+'" does not exists!!!')
        return

    expressionCtrl_rootGrp = pm.group( em=True, name=name+'_contrals' )

    # Create Pronounciation Controls
    #
    pronounciation_grp, p = pronExpression(p, name, exprBlender, baseMesh, textScale, font, pronTargs)
    pm.parent(pronounciation_grp, expressionCtrl_rootGrp)

    # Create Pronounciation Controls
    #
    headGrp_curve, hbox, targets = facialHandles(name, handles, targets)

    # Create Facial BlendShape Targets
    #
    p = facialBlender(p, name, exprBlender, baseMesh, targets)
    pm.parent(headGrp_curve, expressionCtrl_rootGrp)

    bbox = pm.exactWorldBoundingBox(baseMesh)
    xpos = bbox[0] - hbox[3] - .2*(bbox[3]-bbox[0])
    ypos = bbox[1] - hbox[1]
    pm.setAttr((headGrp_curve+".t"), (xpos, ypos, 0))

def facialHandles(name, handles, targs):
    # Create headGrp Curve
    hadpoints = [(0, 30.6789418, 0),
                (-2.14157775, 30.5893632, 0),
                (-6.08419185, 30.2882636, 0),
                (-10.36171435, 29.0775077, 0),
                (-11.77474445, 28.8891037, 0),
                (-12.81096655, 30.7731438, 0),
                (-15.07474155, 33.0928909, 0),
                (-17.21047495, 34.3204439, 0),
                (-21.35536325, 34.5088479, 0),
                (-25.52823765, 32.186174, 0),
                (-27.79201275, 27.9176342, 0),
                (-27.12967175, 23.4253872, 0),
                (-24.68041955, 19.6573069, 0),
                (-23.45500945, 18.3224915, 0),
                (-24.30361155, 16.0776306, 0),
                (-25.43403565, 13.25157029, 0),
                (-28.60336135, 4.842042695, 0),
                (-30.89775215, -4.081599205, 0),
                (-31.39195905, -14.0143463, 0),
                (-26.54455245, -22.63782682, 0),
                (-19.60636235, -27.0645372, 0),
                (-14.10910335, -32.61916612, 0),
                (0, -34.50884789, 0),
                (14.10910335, -32.61916612, 0),
                (19.60636235, -27.0645372, 0),
                (26.54455245, -22.63782682, 0),
                (31.39195905, -14.0143463, 0),
                (30.89775215, -4.081599205, 0),
                (28.60336135, 4.842042695, 0),
                (25.43403565, 13.25157029, 0),
                (24.30361155, 16.0776306, 0),
                (23.45500945, 18.3224915, 0),
                (24.68041955, 19.6573069, 0),
                (27.12967175, 23.4253872, 0),
                (27.79201265, 27.9176342, 0),
                (25.52823765, 32.186174, 0),
                (21.35536325, 34.5088479, 0),
                (17.21047495, 34.3204439, 0),
                (15.07474155, 33.0928909, 0),
                (12.81096655, 30.7731438, 0),
                (11.77474445, 28.8891037, 0),
                (10.36171425, 29.0775077, 0),
                (6.08419185, 30.2882636, 0),
                (2.14157775, 30.5893632, 0),
                (0, 30.6789418, 0)]
    headGrp_curve = pm.curve(n=name+'headGrp', d=3, p=hadpoints)
    hbox = pm.exactWorldBoundingBox(headGrp_curve)

    for handName, handle in handles.iteritems():
        handleName = name+'_'+handName
        points = handle['points']
        d = handle['d']
        handleCurve = pm.curve(n=handleName, d=d, p=points)

        if handle.has_key('decorate'):
            pm.setAttr(handleCurve+'.template', 1)
            pm.setAttr(handleCurve+'.t', handle['local'])
            pm.parent(handleCurve, headGrp_curve)
        else:
            for tar in handle['targs']:
                targs[tar]['Driver'] = handleCurve

            pm.transformLimits(handleCurve, tx=handle['lim'][0], etx=(1, 1), \
                                            ty=handle['lim'][1], ety=(1, 1), \
                                            tz=handle['lim'][2], etz=(1, 1))

            for attr in handle['lock']:
                pm.setAttr(handleCurve+'.'+attr, l=True, k=False, cb=False)

            handle_grp = pm.group(handleCurve, name=handleName+'grp')
            handle['grp'] = handle_grp
            pm.setAttr(handle_grp+'.t', handle['grplocal'])
            pm.parent(handle_grp, headGrp_curve)
    return headGrp_curve, hbox, targs

def facialBlender(p, name, blender, baseMesh, targs):
    for tarName, expr in targs.iteritems():
        if pm.objExists(expr['tar']):
            pm.blendShape(blender, e=True, t=(baseMesh, p, expr['tar'], 1.0))
            aliasMel = 'blendShapeRenameTargetAlias '+blender+' '+str(p)+' '+expr['label']+';'
            mel.eval(aliasMel)
            for i in range(len(expr['Key'])):
                driven = blender+"."+expr['label']
                driver = expr['Driver']+'.'+expr['Key'][i][0]
                driverValue = expr['Key'][i][1]
                value = expr['Key'][i][2]
                pm.setDrivenKeyframe(driven, cd=driver, dv=driverValue, v=value, itt='linear', ott='linear', )
            p += 1
        else:
            pm.warning('The target mesh "'+expr['tar']+'" does not exists! Skiped.')
    return p

def pronExpression(p, name, blender, baseMesh, textScale, font, targs, offset=-12):
    pronounciationGrp = pm.group(em=True, name=name+'_pronGrp')
    ty = 0
    for pronName, expr in targs.iteritems():
        if pm.objExists(expr['tar']):
            pm.blendShape(blender, e=True, t=(baseMesh, p, expr['tar'], 1.0))
            aliasMel = 'blendShapeRenameTargetAlias '+blender+' '+str(p)+' '+expr['label']+';'
            mel.eval(aliasMel)
            #pm.aliasAttr(expr['label'], blender+'.w['+str(idx)+']')

            Slider_Dock = sliderDock_curve('Slider_Dock'+expr['label'])
            titleCurve = sliderLabel_curve(expr['label'], (-20.25, 0, 0), textScale, font)
            SlideSlot = slideSlot_curve('Slider_Slot'+expr['label'])
            Slider = slider_curve('Slider'+expr['label'])

            pm.parent(Slider, Slider_Dock)
            pm.parent(SlideSlot, Slider_Dock)
            pm.parent(titleCurve, Slider_Dock)
            pm.parent(Slider_Dock, pronounciationGrp)

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

            pm.setDrivenKeyframe(blender+"."+expr['label'], cd=Slider+'.tx', dv=0, v=0, itt='linear', ott='linear', )
            pm.setDrivenKeyframe(blender+"."+expr['label'], cd=Slider+'.tx', dv=50, v=1, itt='linear', ott='linear', )

            pm.setAttr((Slider_Dock+".t"), (0, ty, 0))
            ty += offset
            p += 1
        else:
            pm.warning('The target mesh "'+expr['tar']+'" does not exists! Skiped.')

    bbox = pm.exactWorldBoundingBox(baseMesh)
    hbox = pm.exactWorldBoundingBox(pronounciationGrp)
    xpos = bbox[3] - hbox[0] + .2*(bbox[3]-bbox[0])
    ypos = bbox[1] - hbox[1]
    pm.setAttr((pronounciationGrp+".t"), (xpos, ypos, 0))
    return pronounciationGrp, p

def slider_curve(name):
    return pm.curve( n=name, d=1, p=[(-2.5, 3.5, 0), (2.5, 3.5, 0), (2.5, -3.5, 0), (-2.5, -3.5, 0), (-2.5, 3.5, 0)] )

def slideSlot_curve(name):
    curve = pm.curve( n=name, d=1, p=[(0, 0.5, 0), (50, 0.5, 0), (50, -0.5, 0), (0, -0.5, 0), (0, 0.5, 0)] )
    pm.setAttr(curve+'.template', 1)
    return curve

def sliderDock_curve(name):
    return pm.curve( n=name, d=1, p=[(-39, 5, 0), (54, 5, 0), (54, -5, 0), (-39, -5, 0), (-39, 5, 0)] )

def sliderLabel_curve(label, t, s, font='Times New Roman|h-13|w400|c0'):
    curve = pm.textCurves(n=label, ch=False, f=font, t=label)[0]
    pm.setAttr(curve+'.s', (s, s, s))
    freezeToOrigin.freezeToOrigin(objects=[str(curve)],cx='mid',cy='mid',cz='mid')
    pm.setAttr(curve+'.t', t)
    pm.setAttr(curve+'.template', 1)
    return curve
