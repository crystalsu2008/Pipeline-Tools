import pymel.core as pm
import maya.mel as mel
import freezeToOrigin

def HH_Face(name='expression_control', textScale=10, font='Times New Roman|h-13|w400|c0'):

    pronTargs = {'ZCDNRSTX': {'label': 'zcdnrstx', 'tar': 'Mouth_ZCDNRSTX'},
                 'A_E_I':    {'label': 'a_e_i',    'tar': 'Mouth_A_E_I'   },
                 'U_W':      {'label': 'u_w',      'tar': 'Mouth_U_W'     },
                 'B_M_P':    {'label': 'b_m_p',    'tar': 'Mouth_B_M_P'   },
                 'F_V':      {'label': 'f_v',      'tar': 'Mouth_F_V'     },
                 'O':        {'label': 'o',        'tar': 'Mouth_O'       },
                 'Kiss':     {'label': 'kiss',     'tar': 'Mouth_Kiss'    }}

    targets  =  {'base': {'label': 'base', 'tar': 'Head_Mesh'},
                'Jaw_UP': 'Jaw_UP',
                    'Jaw_Down': 'Jaw_Down',
                        'Jaw_Move_R': 'Jaw_Move_R',
                            'Jaw_Move_L': 'Jaw_Move_L',
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
    baseMesh = targets['base']['tar']
    if pm.objExists(baseMesh):
        exprBlender = pm.blendShape( 'Head_Mesh' )[0]
    else:
        pm.warning('The base mesh "'+targets['base']['tar']+'" does not exists!!!')
        return

    # Create Pronounciation Controls
    pronExpression(name, exprBlender, baseMesh, textScale, font, pronTargs)


def pronExpression(name, blender, baseMesh, textScale, font, targs, offset=-12):
    pronounciationGrp = pm.group(em=True, name=name+'_pronGrp')
    idx = pm.blendShape(blender, q=True, gi=True)[-1]
    ty = 0
    for pron, expr in targs.iteritems():
        if pm.objExists(expr['tar']):
            idx += 1
            pm.blendShape(blender, e=True, t=(baseMesh, idx, expr['tar'], 1.0))
            aliasMel = 'blendShapeRenameTargetAlias '+blender+' '+str(idx)+' '+expr['label']+';'
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

            pm.setAttr((Slider_Dock+".t"), (90, ty, 0))
            ty += offset
        else:
            pm.warning('The target mesh "'+expr['tar']+'" does not exists! Skiped.')

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
