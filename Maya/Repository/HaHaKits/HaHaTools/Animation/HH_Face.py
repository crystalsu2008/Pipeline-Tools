import pymel.core as pm
import maya.mel as mel
#import freezeToOrigin

def HH_Face(name='HHExpr', textScale=10, font='Times New Roman|h-13|w400|c0'):

    p=0

    baseMesh = 'Head_Mesh'

    pronTargs = {'ZCDNRSTX': {'label': 'zcdnrstx', 'tar': 'Mouth_ZCDNRSTX'},
                 'A_E_I':    {'label': 'a_e_i',    'tar': 'Mouth_A_E_I'   },
                 'U_W':      {'label': 'u_w',      'tar': 'Mouth_U_W'     },
                 'B_M_P':    {'label': 'b_m_p',    'tar': 'Mouth_B_M_P'   },
                 'F_V':      {'label': 'f_v',      'tar': 'Mouth_F_V'     },
                 'O':        {'label': 'o',        'tar': 'Mouth_O'       },
                 'U_Tongue': {'label': 'u_tongue', 'tar': 'Mouth_UTongue' },
                 'Kiss':     {'label': 'kiss',     'tar': 'Mouth_Kiss'    }}

    pronTargsx = [{'label': 'zcdnrstx', 'tar': 'Mouth_ZCDNRSTX'},
                  {'label': 'a_e_i',    'tar': 'Mouth_A_E_I'   },
                  {'label': 'u_w',      'tar': 'Mouth_U_W'     },
                  {'label': 'b_m_p',    'tar': 'Mouth_B_M_P'   },
                  {'label': 'f_v',      'tar': 'Mouth_F_V'     },
                  {'label': 'o',        'tar': 'Mouth_O'       },
                  {'label': 'u_tongue', 'tar': 'Mouth_UTongue' },
                  {'label': 'kiss',     'tar': 'Mouth_Kiss'    }]

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
                       'd': 3, 'grp': 'Jaw_grp', 'grplocal': (0,-31.5,0), 'name':None,
                       'targs':['Jaw_UP', 'Jaw_Down', 'Jaw_Move_R', 'Jaw_Move_L'],
                       'lim': [(-7, 7), (-5, 5), (0, 0)],
                       'lock': ['tz','rx','ry','rz','sx','sy','sz','v']},
                'Jaw_Scope': {'points': [(-17.346979, 12, 0), (17.346979, 12, 0), (17.346979, -12, 0), (-17.346979, -12, 0), (-17.346979, 12, 0)],
                                'd': 1, 'decorate': True, 'local': (0,-31.5,0), 'name':None},
                'Mouth_Corner_R': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=3, d=3, ut=False, tol=0.01, s=8, ch=False)',
                                'grp': 'Mouth_Corner_R_grp', 'grplocal': (-20, -15, 0), 'name':None,
                                'targs':['Mouth_Shrink_R', 'Mouth_Extend_R', 'Mouth_Smile_R', 'Mouth_Depressed_R'],
                                'lim': [(-5, 5), (-5, 5), (0, 0)],
                                'lock': ['tz','rx','ry','rz','sx','sy','sz','v']},
                'Mouth_Corner_R_Scope': {'points': [(-8, 8, 0), (8, 8, 0), (8, -8, 0), (-8, -8, 0), (-8, 8, 0)],
                                'd': 1, 'decorate': True, 'local': (-20, -15, 0), 'name':None},
                'Mouth_Corner_L': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=3, d=3, ut=False, tol=0.01, s=8, ch=False)',
                                'grp': 'Mouth_Corner_L_grp', 'grplocal': (20, -15, 0), 'name':None,
                                'targs':['Mouth_Shrink_L', 'Mouth_Extend_L', 'Mouth_Smile_L', 'Mouth_Depressed_L'],
                                'lim': [(-5, 5), (-5, 5), (0, 0)],
                                'lock': ['tz','rx','ry','rz','sx','sy','sz','v']},
                'Mouth_Corner_L_Scope': {'points': [(-8, 8, 0), (8, 8, 0), (8, -8, 0), (-8, -8, 0), (-8, 8, 0)],
                                'd': 1, 'decorate': True, 'local': (20, -15, 0), 'name':None},
                'Mouth_Smile_Depressed': {'points': [(0, 1, 0), (12, 0, 0), (0, -1, 0), (-12, 0, 0), (0, 1, 0)],
                       'd': 1, 'grp': 'Mouth_Smile_Depressed_grp', 'grplocal': (0,-18,0), 'name':None,
                       'targs':['Mouth_Smile', 'Mouth_Depressed'],
                       'lim': [(0, 0), (-5, 5), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Brow_Up_Angry_In_R': {'points': [(-2.64187375, 1.5, 0), (-0.38591175, 1.5, 0), (2.42005555, 1.5, 0), (3.53625575, 1.5, 0),
                                            (3.53625575, -0.2001944, 0), (3.53625575, -1.5, 0), (2.29304305, -1.5, 0), (-1.37289515, -1.5, 0),
                                            (-3.53625575, -1.5, 0), (-3.52202905, 0.0411871, 0), (-3.48646255, 1.5, 0), (-2.68887295, 1.5, 0)],
                       'd': 3, 'grp': 'Brow_Up_Angry_In_R_grp', 'grplocal': (-9, 18, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (-5, 5), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Brow_Up_Angry_In_L': {'points': [(2.64187375, 1.5, 0), (0.38591175, 1.5, 0), (-2.42005555, 1.5, 0), (-3.53625575, 1.5, 0),
                                            (-3.53625575, -0.2001944, 0), (-3.53625575, -1.5, 0), (-2.29304305, -1.5, 0), (1.37289515, -1.5, 0),
                                            (3.53625575, -1.5, 0), (3.52202905, 0.0411871, 0), (3.48646255, 1.5, 0), (2.68887295, 1.5, 0)],
                       'd': 3, 'grp': 'Brow_Up_Angry_In_L_grp', 'grplocal': (9, 18, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (-5, 5), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Brow_Up_Down_Out_R': {'points': [(4.6214182, 2.12377205, 0), (4.7142892, 2.08065145, 0), (4.7242184, 0.04926635, 0), (4.7418461, -0.77373025, 0),
                                                (3.2437022, -0.77373025, 0), (0.510237, -0.77373025, 0), (-2.4830579, -1.42728325, 0), (-4.7418461, -2.22626975, 0),
                                                (-4.0198353, -1.19287575, 0), (-2.7139715, 0.10882665, 0), (-0.9053917, 1.52675825, 0), (2.3845528, 2.22626975, 0),
                                                (2.7161625, 2.22626975, 0), (4.6651644, 2.22626975, 0), (4.6214182, 2.12377205, 0)],
                       'd': 3, 'grp': 'Brow_Up_Down_Out_R_grp', 'grplocal': (-18, 17.25, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (-5, 5), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Brow_Up_Down_Out_L': {'points': [(-4.6214182, 2.12377205, 0), (-4.7142892, 2.08065145, 0), (-4.7242184, 0.04926635, 0), (-4.7418461, -0.77373025, 0),
                                                (-3.2437022, -0.77373025, 0), (-0.510237, -0.77373025, 0), (2.4830579, -1.42728325, 0), (4.7418461, -2.22626975, 0),
                                                (4.0198353, -1.19287575, 0), (2.7139715, 0.10882665, 0), (0.9053917, 1.52675825, 0), (-2.3845528, 2.22626975, 0),
                                                (-2.7161625, 2.22626975, 0), (-4.6651644, 2.22626975, 0), (-4.6214182, 2.12377205, 0)],
                       'd': 3, 'grp': 'Brow_Up_Down_Out_L_grp', 'grplocal': (18, 17.25, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (-5, 5), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'UpperEyelid_R': {'points': [(0, 1.6579173, 0), (-2.00430075, 1.6579173, 0), (-6.01290215, 0.3615243, 0), (-8.50352775, -1.6579173, 0),
                                            (-6.01290215, -1.0424714, 0), (0, 0.320564, 0), (6.01290215, -1.0424714, 0), (8.50352775, -1.6579173, 0),
                                            (6.01290215, 0.3615243, 0), (2.00430075, 1.6579173, 0), (0, 1.6579173, 0)],
                       'd': 3, 'grp': 'UpperEyelid_R_grp', 'grplocal': (-14, 8, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (-5, 0), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Eyeball_Scope_R': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=5, d=3, ut=False, tol=0.01, s=8, ch=False)',
                                'decorate': True, 'local': (-14, 3, 0), 'name':None},
                'UpperEyelid_L': {'points': [(0, 1.6579173, 0), (-2.00430075, 1.6579173, 0), (-6.01290215, 0.3615243, 0), (-8.50352775, -1.6579173, 0),
                                            (-6.01290215, -1.0424714, 0), (0, 0.320564, 0), (6.01290215, -1.0424714, 0), (8.50352775, -1.6579173, 0),
                                            (6.01290215, 0.3615243, 0), (2.00430075, 1.6579173, 0), (0, 1.6579173, 0)],
                       'd': 3, 'grp': 'UpperEyelid_L_grp', 'grplocal': (14, 8, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (-5, 0), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Eyeball_Scope_L': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=5, d=3, ut=False, tol=0.01, s=8, ch=False)',
                                'decorate': True, 'local': (14, 3, 0), 'name':None},
                'LowerEyelid_Half_R': {'points': [(0, -1.6579173, 0), (-2.00430075, -1.6579173, 0), (-6.01290215, -0.3615243, 0), (-8.50352775, 1.6579173, 0),
                                            (-6.01290215, 1.0424714, 0), (0, -0.320564, 0), (6.01290215, 1.0424714, 0), (8.50352775, 1.6579173, 0),
                                            (6.01290215, -0.3615243, 0), (2.00430075, -1.6579173, 0), (0, -1.6579173, 0)],
                       'd': 3, 'grp': 'LowerEyelid_Half_R_grp', 'grplocal': (-14, -2, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (0, 5), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'LowerEyelid_Half_L': {'points': [(0, -1.6579173, 0), (-2.00430075, -1.6579173, 0), (-6.01290215, -0.3615243, 0), (-8.50352775, 1.6579173, 0),
                                            (-6.01290215, 1.0424714, 0), (0, -0.320564, 0), (6.01290215, 1.0424714, 0), (8.50352775, 1.6579173, 0),
                                            (6.01290215, -0.3615243, 0), (2.00430075, -1.6579173, 0), (0, -1.6579173, 0)],
                       'd': 3, 'grp': 'LowerEyelid_Half_L_grp', 'grplocal': (14, -2, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 0), (0, 5), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Nose': {'points': [(0.0001465857859, -3.337852213, 0), (1.246356174, -3.289741011, 0), (3.527873904, -1.419334091, 0), (4.78994104, -0.1961448399, 0),
                                    (4.95457028, 0.4292957024, 0), (4.67518235, 0.921071964, 0), (3.21027754, 1.875868602, 0), (0, 3.180869549, 0),
                                    (-3.210277531, 1.875868602, 0), (-4.675182346, 0.9210719639, 0), (-4.954570278, 0.4292957023, 0), (-4.789941036, -0.1961448396, 0),
                                    (-3.527873892, -1.419334091, 0), (-1.246356135, -3.289741011, 0), (-0.0001465761081, -3.337852213, 0)],
                       'd': 3, 'grp': 'Nose_grp', 'grplocal': (0, -6, 0), 'name':None,
                       'targs':['Nose_Move_L', 'Nose_Move_R', 'Nose_Up', 'Nose_Down'],
                       'lim': [(-2, 2), (-3, 3), (0, 0)],
                       'lock': ['tz','rx','ry','rz','sx','sy','sz','v']},
                'Nose_Scope': {'points': [(0, -3.437671488, 0), (1.305939268, -3.437671488, 0), (3.917817803, -1.197674208, 0), (5.540631079, 0.373621081, 0),
                                        (3.917817803, 1.648674652, 0), (0, 3.437671488, 0), (-3.917817794, 1.648674652, 0), (-5.540631079, 0.373621081, 0),
                                        (-3.917817794, -1.197674208, 0), (-1.305939229, -3.437671488, 0), (0, -3.437671488, 0)],
                                'd': 3, 'decorate': True, 'local': (0, -6, 0), 'name':None, 'parent': 'Nose'},
                'Nose_Enlarge': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=1, d=3, ut=False, tol=0.01, s=8, ch=False)',
                       'd': 3, 'grp': 'Nose_Enlarge_grp', 'grplocal': (0, -3.25, 0), 'name':None, 'parent': 'Nose',
                       'targs':['Nose_Enlarge'],
                       'lim': [(0, 0), (0, 2), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Nose_Enlarge_Slot': {'points': [(0, 2.75, 0), (0, 4.75, 0)],
                                'd': 1, 'decorate': True, 'local': (0, -6, 0), 'name':None, 'parent': 'Nose'},
                'Nose_Up_R': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=1.5, d=3, ut=False, tol=0.01, s=8, ch=False)',
                       'd': 3, 'grp': 'Nose_Up_R_grp', 'grplocal': (-4, -8, 0), 'name':None, 'parent': 'Nose',
                       'targs':['Nose_Up_R'],
                       'lim': [(0, 0), (0, 2), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Nose_Up_L': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=1.5, d=3, ut=False, tol=0.01, s=8, ch=False)',
                       'd': 3, 'grp': 'Nose_Up_L_grp', 'grplocal': (4, -8, 0), 'name':None, 'parent': 'Nose',
                       'targs':['Nose_Up_L'],
                       'lim': [(0, 0), (0, 2), (0, 0)],
                       'lock': ['tx','tz','rx','ry','rz','sx','sy','sz','v']},
                'Jeer_ConstraintPlane_R': {'cmd': 'pm.listRelatives(pm.surface(du=1, dv=1, ku=(0,1), kv=(0,1), p=[(-5, 5, 0), (5, 0, 0), (-5, -5, 0), (5, 0, 0)]), p=True)',
                                'decorate': True, 'local': (-40, -15, 0), 'name':None},
                'Jeer_ConstraintPlane_L': {'cmd': 'pm.listRelatives(pm.surface(du=1, dv=1, ku=(0,1), kv=(0,1), p=[(-5, 0, 0), (5, 5, 0), (-5, 0, 0), (5, -5, 0)]), p=True)',
                                'decorate': True, 'local': (40, -15, 0), 'name':None},
                'Mouth_Jeer_R': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=3, d=3, ut=False, tol=0.01, s=8, ch=False)',
                       'd': 3, 'grp': 'Mouth_Jeer_R_grp', 'grplocal': (-35, -15, 0), 'name':None,
                       'targs':[],
                       'lim': [(-10, 0), (-5, 5), (0, 0)],
                       'lock': ['tz','rx','ry','rz','sx','sy','sz','v']},
                'Mouth_Jeer_L': {'cmd': 'pm.circle(c=(0,0,0), nr=(0,0,1), sw=360, r=3, d=3, ut=False, tol=0.01, s=8, ch=False)',
                       'd': 3, 'grp': 'Mouth_Jeer_L_grp', 'grplocal': (35, -15, 0), 'name':None,
                       'targs':[],
                       'lim': [(0, 10), (-5, 5), (0, 0)],
                       'lock': ['tz','rx','ry','rz','sx','sy','sz','v']}}

    handleRules = [{'Driver': 'Nose_Enlarge', 'Driven': 'Nose_Scope',
                    'Key': [('ty',0,'sx',1), ('ty',2,'sx',1.67), ('ty',0,'sy',1), ('ty',2,'sy',1.67), ('ty',0,'sz',1), ('ty',2,'sz',1.67)]}]

    targets =  {'Jaw_UP': {'Simple':True, 'label': 'jaw_up', 'tar': 'Jaw_UP', 'Driver': 'Jaw', 'Key': [('ty',0,0), ('ty',5,1)]},
                    'Jaw_Down': {'Simple':True, 'label': 'jaw_down', 'tar': 'Jaw_Down', 'Driver': 'Jaw', 'Key': [('ty',0,0), ('ty',-5,1)]},
                        'Jaw_Move_R': {'Simple':True, 'label': 'jaw_move_r', 'tar': 'Jaw_Move_R', 'Driver': 'Jaw', 'Key': [('tx',0,0), ('tx',-7,1)]},
                            'Jaw_Move_L': {'Simple':True, 'label': 'jaw_move_l', 'tar': 'Jaw_Move_L', 'Driver': 'Jaw', 'Key': [('tx',0,0), ('tx',7,1)]},
                'Mouth_Shrink_R': {'Simple':True, 'label': 'mouth_shrink_r', 'tar': 'Mouth_Shrink_R', 'Driver': 'Mouth_Corner_R', 'Key': [('tx',0,0), ('tx',5,1)]},
                    'Mouth_Extend_R': {'Simple':True, 'label': 'mouth_extend_r', 'tar': 'Mouth_Extend_R', 'Driver': 'Mouth_Corner_R', 'Key': [('tx',0,0), ('tx',-5,1)]},
                        'Mouth_Smile_R': {'Simple':True, 'label': 'mouth_smile_r', 'tar': 'Mouth_Smile_R', 'Driver': 'Mouth_Corner_R', 'Key': [('ty',0,0), ('ty',5,1)]},
                            'Mouth_Depressed_R': {'Simple':True, 'label': 'mouth_depressed_r', 'tar': 'Mouth_Depressed_R', 'Driver': 'Mouth_Corner_R', 'Key': [('ty',0,0), ('ty',-5,1)]},
                'Mouth_Shrink_L': {'Simple':True, 'label': 'mouth_shrink_l', 'tar': 'Mouth_Shrink_L', 'Driver': 'Mouth_Corner_L', 'Key': [('tx',0,0), ('tx',-5,1)]},
                    'Mouth_Extend_L': {'Simple':True, 'label': 'mouth_extend_l', 'tar': 'Mouth_Extend_L', 'Driver': 'Mouth_Corner_L', 'Key': [('tx',0,0), ('tx',5,1)]},
                        'Mouth_Smile_L': {'Simple':True, 'label': 'mouth_smile_l', 'tar': 'Mouth_Smile_L', 'Driver': 'Mouth_Corner_L', 'Key': [('ty',0,0), ('ty',5,1)]},
                            'Mouth_Depressed_L': {'Simple':True, 'label': 'mouth_depressed_l', 'tar': 'Mouth_Depressed_L', 'Driver': 'Mouth_Corner_L', 'Key': [('ty',0,0), ('ty',-5,1)]},
                'Mouth_Smile': {'Simple':True, 'label': 'mouth_smile', 'tar': 'Mouth_Smile', 'Driver': 'Mouth_Smile_Depressed', 'Key': [('ty',0,0), ('ty',5,1)]},
                    'Mouth_Depressed': {'Simple':True, 'label': 'mouth_depressed', 'tar': 'Mouth_Depressed', 'Driver': 'Mouth_Smile_Depressed', 'Key': [('ty',0,0), ('ty',-5,1)]},
                'UpperEyelid_Half_R': {'Simple':False, 'label': 'uppereyelid_half_r', 'tar': 'UpperEyelid_Half_R', 'Driver': 'Eye_R.rz', 'Key': []},
                    'UpperEyelid_R': {'Simple':False, 'label': 'uppereyelid_r', 'tar': 'UpperEyelid_R', 'Driver': 'Eye_R.rz', 'Key': []},
                        'UpperEyelid_Half_L': {'Simple':False, 'label': 'uppereyelid_half_l', 'tar': 'UpperEyelid_Half_L', 'Driver': 'Eye_L.rz', 'Key': []},
                            'UpperEyelid_L': {'Simple':False, 'label': 'uppereyelid_l', 'tar': 'UpperEyelid_L', 'Driver': 'Eye_L.rz', 'Key': []},
                                'LowerEyelid_Half_R': {'Simple':False, 'label': 'lowereyelid_half_r', 'tar': 'LowerEyelid_Half_R', 'Driver': 'Eye_R.rz', 'Key': []},
                                    'LowerEyelid_Half_L': {'Simple':False, 'label': 'lowereyelid_half_l', 'tar': 'LowerEyelid_Half_L', 'Driver': 'Eye_L.rz', 'Key': []},
                'Nose_Move_L': {'Simple':True, 'label': 'nose_move_l', 'tar': 'Nose_Move_L', 'Driver': 'Nose', 'Key': [('tx',0,0), ('tx',2,1)]},
                    'Nose_Move_R': {'Simple':True, 'label': 'nose_move_r', 'tar': 'Nose_Move_R', 'Driver': 'Nose', 'Key': [('tx',0,0), ('tx',-2,1)]},
                        'Nose_Up': {'Simple':True, 'label': 'nose_up', 'tar': 'Nose_Up', 'Driver': 'Nose', 'Key': [('ty',0,0), ('ty',3,1)]},
                            'Nose_Down': {'Simple':True, 'label': 'nose_down', 'tar': 'Nose_Down', 'Driver': 'Nose', 'Key': [('ty',0,0), ('ty',-3,1)]},
                                'Nose_Enlarge': {'Simple':True, 'label': 'nose_enlarge', 'tar': 'Nose_Enlarge', 'Driver': 'Nose_Enlarge', 'Key': [('ty',0,0), ('ty',2,1)]},
                                    'Nose_Up_R': {'Simple':True, 'label': 'nose_up_r', 'tar': 'Nose_Up_R', 'Driver': 'Nose_Up_R', 'Key': [('ty',0,0), ('ty',3,1)]},
                                        'Nose_Up_L': {'Simple':True, 'label': 'nose_up_l', 'tar': 'Nose_Up_L', 'Driver': 'Nose_Up_L', 'Key': [('ty',0,0), ('ty',3,1)]},
                'Mouth_Jeer_Down_R': {'Simple':False, 'label': 'mouth_jeer_down_r', 'tar': 'Mouth_Jeer_Down_R', 'Driver': '', 'Key': []},
                    'Mouth_Jeer_Down_L': {'Simple':False, 'label': 'mouth_jeer_down_l', 'tar': 'Mouth_Jeer_Down_L', 'Driver': '', 'Key': []},
                        'Mouth_Jeer_Up_R': {'Simple':False, 'label': 'mouth_jeer_up_r', 'tar': 'Mouth_Jeer_Up_R', 'Driver': '', 'Key': []},
                            'Mouth_Jeer_Up_L': {'Simple':False, 'label': 'mouth_jeer_up_l', 'tar': 'Mouth_Jeer_Up_L', 'Driver': '', 'Key': []},

                'Brow_Up_In_R': {'Simple':False, 'label': 'brow_up_in_r', 'tar': 'Brow_Up_In_R', 'Driver': 'Eye_R', 'Key': [('rz',0,0), ('ry',5,1)]},
                    'Brow_Angry_R': {'Simple':False, 'label': 'brow_angry_r', 'tar': 'Brow_Angry_R', 'Driver': 'Eye_R', 'Key': [('rz',0,0), ('ry',-5,1)]},
                        'Brow_Up_In_L': {'Simple':False, 'label': 'brow_up_in_l', 'tar': 'Brow_Up_In_L', 'Driver': 'Eye_L', 'Key': [('rz',0,0), ('ry',5,1)]},
                            'Brow_Angry_L': {'Simple':False, 'label': 'brow_angry_l', 'tar': 'Brow_Angry_L', 'Driver': 'Eye_L', 'Key': [('rz',0,0), ('ry',-5,1)]},
                'Brow_Up_Out_R': {'Simple':False, 'label': 'brow_up_out_r', 'tar': 'Brow_Up_Out_R', 'Driver': 'Eye_R', 'Key': [('rz',0,0), ('ry',5,1)]},
                    'Brow_Down_Out_R': {'Simple':False, 'label': 'brow_down_out_r', 'tar': 'Brow_Down_Out_R', 'Driver': 'Eye_R', 'Key': [('rz',0,0), ('ry',-5,1)]},
                        'Brow_Up_Out_L': {'Simple':False, 'label': 'brow_up_out_l', 'tar': 'Brow_Up_Out_L', 'Driver': 'Eye_L', 'Key': [('rz',0,0), ('ry',5,1)]},
                            'Brow_Down_Out_L': {'Simple':False, 'label': 'brow_down_out_l', 'tar': 'Brow_Down_Out_L', 'Driver': 'Eye_L', 'Key': [('rz',0,0), ('ry',-5,1)]}}


    otherTargets  =  {'Mouth_Jeer_Down': 'Mouth_Jeer_Down',
                        'Mouth_Jeer_Up': 'Mouth_Jeer_Up',
                            'LowerEyelid_Look_Up': 'LowerEyelid_Look_Up',
                                'UpperEyelid_Look_Down': 'UpperEyelid_Look_Down'}

    exprBlender = None
    if pm.objExists(baseMesh):
        exprBlender = pm.blendShape( 'Head_Mesh', foc=True )[0]
    else:
        pm.warning('The base mesh "'+targets['Base']['tar']+'" does not exists!!!')
        return

    expressionCtrl_rootGrp = pm.group( em=True, name=name+'_contrals' )

    # Create Pronounciation Controls
    #
    pronounciation_grp, p = pronExpression(p, name, exprBlender, baseMesh, textScale, font, pronTargs)
    pm.parent(pronounciation_grp, expressionCtrl_rootGrp)

    # Create Facial Handles
    #
    headGrp_curve, targets = facialHandles(name, handles, handleRules, targets)

    # Create Facial BlendShape Targets
    #
    p = facialBlender(p, name, exprBlender, baseMesh, targets)
    pm.parent(headGrp_curve, expressionCtrl_rootGrp)

    # Create Jeer Expressions
    #
    exprecmd_Mouth_Jeer_R = 'float $inst = 1.0 - linstep(-10, 0, ' + handles['Mouth_Jeer_R']['name'] + '.tx);\n' + \
        exprBlender +'.'+ targets['Mouth_Jeer_Up_R']['label'] + ' = linstep(-5, 5, ' + handles['Mouth_Jeer_R']['name'] + '.ty) * $inst;\n' + \
        exprBlender +'.'+ targets['Mouth_Jeer_Down_R']['label'] + ' = (1.0 - linstep(-5, 5, ' + handles['Mouth_Jeer_R']['name'] + '.ty)) * $inst;'
    pm.expression(s=exprecmd_Mouth_Jeer_R, n='expression' + handles['Mouth_Jeer_R']['name'])
    pm.geometryConstraint(handles['Jeer_ConstraintPlane_L']['name'], handles['Mouth_Jeer_L']['name'], weight=1)

    exprecmd_Mouth_Jeer_L = 'float $inst = linstep(0, 10, ' + handles['Mouth_Jeer_L']['name'] + '.tx);\n' + \
        exprBlender +'.'+ targets['Mouth_Jeer_Up_L']['label'] + ' = linstep(-5, 5, ' + handles['Mouth_Jeer_L']['name'] + '.ty) * $inst;\n' + \
        exprBlender +'.'+ targets['Mouth_Jeer_Down_L']['label'] + ' = (1.0 - linstep(-5, 5, ' + handles['Mouth_Jeer_L']['name'] + '.ty)) * $inst;'
    pm.expression(s=exprecmd_Mouth_Jeer_L, n='expression' + handles['Mouth_Jeer_L']['name'])
    pm.geometryConstraint(handles['Jeer_ConstraintPlane_R']['name'], handles['Mouth_Jeer_R']['name'], weight=1)

    # Make sure the Drivers exist.
    #
    for tarName, expr in targets.iteritems():
        if not pm.objExists(expr['Driver']) and not expr['Driver'] == '':
            print tarName
            print expr['Driver']


    # Create Eyelid Expressions
    #
    targ_UpperEyelid_R_Driver = targets['UpperEyelid_R']['Driver'] if pm.objExists(targets['UpperEyelid_R']['Driver']) else '0'
    exprecmd_Eyelid_R = 'float $eyeclose = 1.0-linstep(-5, 0, ' + handles['UpperEyelid_R']['name'] + '.ty);\n' + \
                        'float $eyelower = linstep(0, 5, ' + handles['LowerEyelid_Half_R']['name'] + '.ty);\n' + \
                        'float $lookup = 1.0-linstep(-25, 0, ' + targ_UpperEyelid_R_Driver + ');\n' + \
                        '$lookup = hermite(0,1,1,3,$lookup);\n' + \
                        'float $lookdown = linstep(0, 25, ' + targ_UpperEyelid_R_Driver + ');\n' + \
                        '$lookdown = hermite(0,1,1,3,$lookdown);\n' + \
                        '$lookup_lid = 1.0-$eyeclose;\n' + \
                        '$weight_upper_look = 0.5*($lookdown-$lookup)*$lookup_lid;\n' + \
                        '$weight_upper_close = linstep(.5, 1, $eyeclose);\n' + \
                        '$weight_upper_half = $weight_upper_look + linstep(0, .5, $eyeclose) - $weight_upper_close;\n' + \
                        '$weight_lower_look = 0.25*($lookup-$lookdown)*$lookup_lid;\n' + \
                        '$weight_lower_half = $weight_lower_look + linstep(0, 1, $eyelower);\n' + \
                        exprBlender +'.'+ targets['UpperEyelid_Half_R']['label'] + ' = $weight_upper_half;\n' + \
                        exprBlender +'.'+ targets['UpperEyelid_R']['label'] + ' = $weight_upper_close;\n' + \
                        exprBlender +'.'+ targets['LowerEyelid_Half_R']['label'] + ' = $weight_lower_half;'
    pm.expression(s=exprecmd_Eyelid_R, n='expression' + handles['UpperEyelid_R']['name'])

    targ_UpperEyelid_L_Driver = targets['UpperEyelid_L']['Driver'] if pm.objExists(targets['UpperEyelid_L']['Driver']) else '0'
    exprecmd_Eyelid_L = 'float $eyeclose = 1.0-linstep(-5, 0, ' + handles['UpperEyelid_L']['name'] + '.ty);\n' + \
                        'float $eyelower = linstep(0, 5, ' + handles['LowerEyelid_Half_L']['name'] + '.ty);\n' + \
                        'float $lookup = 1.0-linstep(-25, 0, ' + targ_UpperEyelid_L_Driver + ');\n' + \
                        '$lookup = hermite(0,1,1,3,$lookup);\n' + \
                        'float $lookdown = linstep(0, 25, ' + targ_UpperEyelid_L_Driver + ');\n' + \
                        '$lookdown = hermite(0,1,1,3,$lookdown);\n' + \
                        '$lookup_lid = 1.0-$eyeclose;\n' + \
                        '$weight_upper_look = 0.5*($lookdown-$lookup)*$lookup_lid;\n' + \
                        '$weight_upper_close = linstep(.5, 1, $eyeclose);\n' + \
                        '$weight_upper_half = $weight_upper_look + linstep(0, .5, $eyeclose) - $weight_upper_close;\n' + \
                        '$weight_lower_look = 0.25*($lookup-$lookdown)*$lookup_lid;\n' + \
                        '$weight_lower_half = $weight_lower_look + linstep(0, 1, $eyelower);\n' + \
                        exprBlender +'.'+ targets['UpperEyelid_Half_L']['label'] + ' = $weight_upper_half;\n' + \
                        exprBlender +'.'+ targets['UpperEyelid_L']['label'] + ' = $weight_upper_close;\n' + \
                        exprBlender +'.'+ targets['LowerEyelid_Half_L']['label'] + ' = $weight_lower_half;'
    pm.expression(s=exprecmd_Eyelid_L, n='expression' + handles['UpperEyelid_L']['name'])

    if pm.objExists(targets['Brow_Up_In_R']['Driver']):
        targets_Brow_Up_In_R_Driver_rz = targets['Brow_Up_In_R']['Driver'] + '.rz'
        targets_Brow_Up_In_R_Driver_ry = targets['Brow_Up_In_R']['Driver'] + '.ry'
    else:
        targets_Brow_Up_In_R_Driver_rz = '0'
        targets_Brow_Up_In_R_Driver_ry = '0'
    targets_Brow_Angry_R_Driver_rz = targets['Brow_Angry_R']['Driver']+'.rz' if pm.objExists(targets['Brow_Angry_R']['Driver']) else '0'
    targets_Brow_Up_Out_R_Driver_ry = targets['Brow_Up_Out_R']['Driver']+'.ry' if pm.objExists(targets['Brow_Up_Out_R']['Driver']) else '0'
    exprecmd_Brow_R = 'float $browinup = linstep(0, 5, ' + handles['Brow_Up_Angry_In_R']['name'] + '.ty);\n' + \
                      'float $browoutup = linstep(0, 5, ' + handles['Brow_Up_Down_Out_R']['name'] + '.ty);\n' + \
                      'float $browindown = 1.0-linstep(-5, 0, ' + handles['Brow_Up_Angry_In_R']['name'] + '.ty);\n' + \
                      'float $browoutdown = 1.0-linstep(-5, 0, ' + handles['Brow_Up_Down_Out_R']['name'] + '.ty);\n' + \
                      'float $lookup = 1.0-linstep(-25, 0, ' + targets_Brow_Up_In_R_Driver_rz + ');\n' + \
                      '$lookup = hermite(0,1,1,3,$lookup);\n' + \
                      'float $lookdown = linstep(0, 25, ' + targets_Brow_Angry_R_Driver_rz + ');\n' + \
                      '$lookdown = hermite(0,1,1,3,$lookdown);\n' + \
                      'float $lookright = linstep(-15, 0, ' + targets_Brow_Up_In_R_Driver_ry + ');\n' + \
                      'float $lookleft = 1.0-linstep(0, 15, ' + targets_Brow_Up_Out_R_Driver_ry + ');\n' + \
                      exprBlender +'.'+ targets['Brow_Up_In_R']['label'] + ' = $browinup + .25*$lookup * $lookleft;\n' + \
                      exprBlender +'.'+ targets['Brow_Up_Out_R']['label'] + ' = $browoutup + .25*$lookup * $lookright;\n' + \
                      exprBlender +'.'+ targets['Brow_Angry_R']['label'] + ' = $browindown + .05*$lookdown * $lookleft;\n' + \
                      exprBlender +'.'+ targets['Brow_Down_Out_R']['label'] + ' = $browoutdown + .05*$lookdown * $lookright;'
    pm.expression(s=exprecmd_Brow_R, n='expression' + handles['Brow_Up_Angry_In_R']['name'])

    if pm.objExists(targets['Brow_Up_In_L']['Driver']):
        targets_Brow_Up_In_L_Driver_rz = targets['Brow_Up_In_L']['Driver'] + '.rz'
        targets_Brow_Up_In_L_Driver_ry = targets['Brow_Up_In_L']['Driver'] + '.ry'
    else:
        targets_Brow_Up_In_L_Driver_rz = '0'
        targets_Brow_Up_In_L_Driver_ry = '0'
    targets_Brow_Angry_L_Driver_rz = targets['Brow_Angry_L']['Driver']+'.rz' if pm.objExists(targets['Brow_Angry_L']['Driver']) else '0'
    targets_Brow_Up_Out_L_Driver_ry = targets['Brow_Up_Out_L']['Driver']+'.ry' if pm.objExists(targets['Brow_Up_Out_L']['Driver']) else '0'
    exprecmd_Brow_L = 'float $browinup = linstep(0, 5, ' + handles['Brow_Up_Angry_In_L']['name'] + '.ty);\n' + \
                      'float $browoutup = linstep(0, 5, ' + handles['Brow_Up_Down_Out_L']['name'] + '.ty);\n' + \
                      'float $browindown = 1.0-linstep(-5, 0, ' + handles['Brow_Up_Angry_In_L']['name'] + '.ty);\n' + \
                      'float $browoutdown = 1.0-linstep(-5, 0, ' + handles['Brow_Up_Down_Out_L']['name'] + '.ty);\n' + \
                      'float $lookup = 1.0-linstep(-25, 0, ' + targets_Brow_Up_In_L_Driver_rz + ');\n' + \
                      '$lookup = hermite(0,1,1,3,$lookup);\n' + \
                      'float $lookdown = linstep(0, 25, ' + targets_Brow_Angry_L_Driver_rz + ');\n' + \
                      '$lookdown = hermite(0,1,1,3,$lookdown);\n' + \
                      'float $lookright = linstep(-15, 0, ' + targets_Brow_Up_In_L_Driver_ry + ');\n' + \
                      'float $lookleft = 1.0-linstep(0, 15, ' + targets_Brow_Up_Out_L_Driver_ry + ');\n' + \
                      exprBlender +'.'+ targets['Brow_Up_In_L']['label'] + ' = $browinup + .25*$lookup * $lookright;\n' + \
                      exprBlender +'.'+ targets['Brow_Up_Out_L']['label'] + ' = $browoutup + .25*$lookup * $lookleft;\n' + \
                      exprBlender +'.'+ targets['Brow_Angry_L']['label'] + ' = $browindown + .05*$lookdown * $lookright;\n' + \
                      exprBlender +'.'+ targets['Brow_Down_Out_L']['label'] + ' = $browoutdown + .05*$lookdown * $lookleft;'
    pm.expression(s=exprecmd_Brow_L, n='expression' + handles['Brow_Up_Angry_In_L']['name'])

    # Move Handels
    bbox = pm.exactWorldBoundingBox(baseMesh)
    hbox = pm.exactWorldBoundingBox(headGrp_curve)
    xpos = bbox[0] - hbox[3] - .2*(bbox[3]-bbox[0])
    ypos = bbox[1] - hbox[1]
    pm.setAttr((headGrp_curve+".t"), (xpos, ypos, 0))

    # Create Tongue Blender
    TongueBlender = pm.blendShape( 'Tongue_Expr', 'Tongue' )[0]

    UTongueBlender = pm.blendShape( 'Tongue_Mouth_UTongue', 'Tongue', foc=True )[0]
    pm.setDrivenKeyframe(UTongueBlender+".Tongue_Mouth_UTongue", cd='Slideru_tongue.tx', dv=0, v=0, itt='linear', ott='linear', )
    pm.setDrivenKeyframe(UTongueBlender+".Tongue_Mouth_UTongue", cd='Slideru_tongue.tx', dv=50, v=1, itt='linear', ott='linear', )

def facialHandles(name, handles, handleRules, targs):
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
        if handle.has_key('points'):
            points = handle['points']
            d = handle['d']
            handleCurve = pm.curve(n=handleName, d=d, p=points)
        else:
            handleCurve = pm.python(handle['cmd'])[0]
            handleCurve = pm.rename(handleCurve, handleName)
        handle['name'] = handleCurve

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

            handle_grp = pm.group(handleCurve, name=handleName+'_grp')
            handle['grp'] = handle_grp
            pm.setAttr(handle_grp+'.t', handle['grplocal'])
            pm.parent(handle_grp, headGrp_curve)

    for handName, handle in handles.iteritems():
        if handle.has_key('parent'):
            parent = handles[handle['parent']]['name']
            if not parent is None:
                if handle.has_key('grp'):
                    pm.parent(handle['grp'], parent)
                else:
                    pm.parent(handle['name'], parent)

    for rule in handleRules:
        for key in rule['Key']:
            driver = handles[rule['Driver']]['name']+"."+key[0]
            driven = handles[rule['Driven']]['name']+"."+key[2]
            pm.setDrivenKeyframe(driven, cd=driver, dv=key[1], v=key[3], itt='linear', ott='linear')

    return headGrp_curve, targs

def facialBlender(p, name, blender, baseMesh, targs):
    for tarName, expr in targs.iteritems():
        if pm.objExists(expr['tar']):
            pm.blendShape(blender, e=True, t=(baseMesh, p, expr['tar'], 1.0))
            aliasMel = 'blendShapeRenameTargetAlias '+blender+' '+str(p)+' '+expr['label']+';'
            mel.eval(aliasMel)
            if expr['Simple']:
                for i in range(len(expr['Key'])):
                    driven = blender+"."+expr['label']
                    driver = expr['Driver']+'.'+expr['Key'][i][0]
                    driverValue = expr['Key'][i][1]
                    value = expr['Key'][i][2]
                    pm.setDrivenKeyframe(driven, cd=driver, dv=driverValue, v=value, itt='linear', ott='linear')
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
