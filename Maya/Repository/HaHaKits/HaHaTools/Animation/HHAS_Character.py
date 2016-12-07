import pymel.core as pm

def HHAS_Character():
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
    FKIK = ['FKIKArm_R', 'FKIKArm_L', 'FKIKSpine_M', 'FKIKLeg_R', 'FKIKLeg_L']

    pm.character(FKSpinal, IKSpinal, facial, FKArm_L, IKArm_L, FKArm_R, IKArm_R, hand_L, hand_R, IKLeg_L, FKLeg_L, IKLeg_R, FKLeg_R, FKIK,\
                 name='HHAS_BodySet', excludeVisibility=True, excludeScale=True)
    pm.select(cl=True)
