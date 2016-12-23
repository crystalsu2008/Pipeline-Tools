import pymel.core as pm

def HH_Face(name='expression_control', textScale=10, font='Times New Roman|h-13|w400|c0'):

    pronTargs = {'ZCDNRSTX': {'name': 'zcdnrstx', 'tar': 'Mouth_ZCDNRSTX'},
                 'A_E_I':    {'name': 'a_e_i',    'tar': 'Mouth_A_E_I'   },
                 'U_W':      {'name': 'u_w',      'tar': 'Mouth_U_W'     },
                 'B_M_P':    {'name': 'b_m_p',    'tar': 'Mouth_B_M_P'   },
                 'F_V':      {'name': 'f_v',      'tar': 'Mouth_F_V'     },
                 'O':        {'name': 'o',        'tar': 'Mouth_O'       },
                 'Kiss':     {'name': 'kiss',     'tar': 'Mouth_Kiss'    }}

    targets  =  {'Head_Mesh': 'Head_Mesh',
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

    # Pronounciation Control zcdnrstx
    pronExpression(name, textScale, font, pronTargs)




def pronExpression(name, textScale, font, targs, offset=-12):
    pronounciationGrp = pm.group(em=True, name=name+'_pronGrp')

    ty = 0
    for pron, expr in targs.iteritems():
        Slider_Dock = sliderDock_curve('Slider_Dock'+expr['name'])
        titleCurve = sliderLabel_curve(expr['name'], (-35, -2.3, 0), textScale, font)
        SlideSlot = slideSlot_curve('Slider_Slot'+expr['name'])
        Slider = slider_curve('Slider'+expr['name'])

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

        pm.setAttr((Slider_Dock+".t"), (90, ty, 0))
        ty += offset
    return pronounciationGrp

def slider_curve(name):
    return pm.curve( n=name, d=1, p=[(-2.5, 3.5, 0), (2.5, 3.5, 0), (2.5, -3.5, 0), (-2.5, -3.5, 0), (-2.5, 3.5, 0)] )

def slideSlot_curve(name):
    curve = pm.curve( n=name, d=1, p=[(0, 0.5, 0), (50, 0.5, 0), (50, -0.5, 0), (0, -0.5, 0), (0, 0.5, 0)] )
    pm.setAttr(curve+'.template', 1)
    return curve

def sliderDock_curve(name):
    return pm.curve( n=name, d=1, p=[(-37, 5, 0), (54, 5, 0), (54, -5, 0), (-37, -5, 0), (-37, 5, 0)] )

def sliderLabel_curve(name, t, s, font='Times New Roman|h-13|w400|c0'):
    curve = pm.textCurves(n=name, ch=False, f=font, t=name)[0]
    pm.setAttr(curve+'.s', (s, s, s))
    pm.setAttr(curve+'.t', t)
    pm.setAttr(curve+'.template', 1)
    return curve
