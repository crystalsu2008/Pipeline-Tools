import pymel.core as pm

def HHAS_Character(name='HHAS_', exprCtrlname='HHExpr_'):
    FKSpinal = ['Main', 'RootX_M', 'FKRoot_M', 'FKSpine1_M', 'FKSpine2_M', 'FKChest_M',
                'FKNeck_M', 'FKHead_M', 'HipSwinger_M']
    IKSpinal = ['IKSpine1_M', 'IKSpine2_M']
    facial = ['FKEye_L', 'FKEye_R', 'AimEye_L', 'AimEye_R', 'AimEye_M', 'FKJaw_M']
    FKArm_L = ['FKScapula_L', 'FKShoulder_L', 'FKElbow_L', 'FKWrist_L']
    IKArm_L = ['PoleArm_L', 'IKArm_L']
    FKArm_R = ['FKScapula_R', 'FKShoulder_R', 'FKElbow_R', 'FKWrist_R']
    IKArm_R = ['IKArm_R', 'PoleArm_R']
    hand_L = ['FKThumbFinger3_L', 'FKThumbFinger2_L', 'FKThumbFinger1_L',
              'FKIndexFinger3_L', 'FKIndexFinger2_L', 'FKIndexFinger1_L',
              'FKMiddleFinger3_L', 'FKMiddleFinger2_L', 'FKMiddleFinger1_L',
              'FKRingFinger3_L', 'FKRingFinger2_L', 'FKRingFinger1_L',
              'FKPinkyFinger3_L', 'FKPinkyFinger2_L', 'FKPinkyFinger1_L', 'Fingers_L']
    hand_R = ['FKThumbFinger3_R', 'FKThumbFinger2_R', 'FKThumbFinger1_R',
              'FKIndexFinger3_R', 'FKIndexFinger2_R', 'FKIndexFinger1_R',
              'FKMiddleFinger3_R', 'FKMiddleFinger2_R', 'FKMiddleFinger1_R',
              'FKRingFinger3_R', 'FKRingFinger2_R', 'FKRingFinger1_R',
              'FKPinkyFinger3_R', 'FKPinkyFinger2_R', 'FKPinkyFinger1_R', 'Fingers_R']
    IKLeg_L = ['PoleLeg_L', 'IKLeg_L', 'RollToes_L', 'RollToesEnd_L', 'RollHeel_L']
    FKLeg_L = ['FKToes_L', 'FKAnkle_L', 'FKKnee_L', 'FKHip_L']
    IKLeg_R = ['IKLeg_R', 'PoleLeg_R', 'RollToes_R', 'RollToesEnd_R', 'RollHeel_R']
    FKLeg_R = ['FKToes_R', 'FKAnkle_R', 'FKKnee_R', 'FKHip_R']
    FKTongue = ['FKtongue1_M', 'FKtongue2_M', 'FKtongue3_M', 'FKtongue4_M', 'FKtongue5_M', 'FKtongue6_M', 'FKtongue7_M']
    IKTongue = ['IKSplineTongue1_M', 'IKSplineTongue2_M', 'IKSplineTongue3_M', 'IKSplineTongue4_M']
    FKIK = ['FKIKArm_R', 'FKIKArm_L', 'FKIKSpine_M', 'FKIKLeg_R', 'FKIKLeg_L', 'FKIKSplineTongue_M']

    pm.character(FKSpinal, IKSpinal, facial, FKArm_L, IKArm_L, FKArm_R, IKArm_R, hand_L, hand_R, IKLeg_L, FKLeg_L, IKLeg_R, FKLeg_R, FKIK,\
                 name=name+'BodySet', excludeVisibility=True, excludeScale=False)
    pm.select(cl=True)

    # ======================================================================== #

    Pronounciations = [exprCtrlname+'Sliderzcdnrstx.tx', exprCtrlname+'Slidera_e_i.tx', exprCtrlname+'Slideru_w.tx', exprCtrlname+'Sliderb_m_p.tx',
            exprCtrlname+'Sliderf_v.tx', exprCtrlname+'Slidero.tx', exprCtrlname+'Sliderkiss.tx', exprCtrlname+'Slideru_tongue.tx', exprCtrlname+'Slidertongue.tx']

    Expressions = [exprCtrlname+'Jaw.tx', exprCtrlname+'Jaw.ty', exprCtrlname+'Mouth_Smile_Depressed.ty', exprCtrlname+'Mouth_Corner_R.tx', exprCtrlname+'Mouth_Corner_R.ty',
                   exprCtrlname+'Mouth_Corner_L.tx', exprCtrlname+'Mouth_Corner_L.ty', exprCtrlname+'Mouth_Jeer_L.tx', exprCtrlname+'Mouth_Jeer_L.ty', exprCtrlname+'Mouth_Jeer_R.tx',
                   exprCtrlname+'Mouth_Jeer_R.ty', exprCtrlname+'Brow_Up_Down_Out_L.ty', exprCtrlname+'UpperEyelid_R.ty', exprCtrlname+'Brow_Up_Angry_In_R.ty', exprCtrlname+'Nose.tx',
                   exprCtrlname+'Nose.ty', exprCtrlname+'Nose_Up_L.ty', exprCtrlname+'Nose_Up_R.ty', exprCtrlname+'Nose_Enlarge.ty', exprCtrlname+'UpperEyelid_L.ty',
                   exprCtrlname+'Brow_Up_Down_Out_R.ty', exprCtrlname+'LowerEyelid_Half_R.ty', exprCtrlname+'LowerEyelid_Half_L.ty', exprCtrlname+'Brow_Up_Angry_In_L.ty']

    pronounciationSet = pm.character(em=True, name=name+'PronounciationSet')
    for pron in Pronounciations:
        if pm.objExists(pron):
            pm.character(pron, add=pronounciationSet)

    expressionSet = pm.character(em=True, name=name+'ExpressionSet')
    for expr in Expressions:
        if pm.objExists(expr):
            pm.character(expr, add=expressionSet)

    pm.character( pronounciationSet, expressionSet, n=name+'FaceSet' )
