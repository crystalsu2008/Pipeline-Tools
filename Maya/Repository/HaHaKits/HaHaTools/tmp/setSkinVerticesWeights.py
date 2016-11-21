import pymel.core as pm

def setSkinVerticesWeights():
    vtxs = ['ShirtShape.vtx[27]', 'ShirtShape.vtx[37:50]', 'ShirtShape.vtx[72:87]', 'ShirtShape.vtx[93:95]', 'ShirtShape.vtx[97]', 'ShirtShape.vtx[102]', 'ShirtShape.vtx[123:142]', 'ShirtShape.vtx[190:193]', 'ShirtShape.vtx[227:229]', 'ShirtShape.vtx[235:239]', 'ShirtShape.vtx[241]', 'ShirtShape.vtx[243:249]', 'ShirtShape.vtx[251]', 'ShirtShape.vtx[255:258]', 'ShirtShape.vtx[260:275]', 'ShirtShape.vtx[325:358]', 'ShirtShape.vtx[369:372]', 'ShirtShape.vtx[374]', 'ShirtShape.vtx[403:436]', 'ShirtShape.vtx[487:495]', 'ShirtShape.vtx[509]', 'ShirtShape.vtx[512:513]', 'ShirtShape.vtx[515:518]', 'ShirtShape.vtx[520:530]', 'ShirtShape.vtx[554:570]', 'ShirtShape.vtx[578]', 'ShirtShape.vtx[584]', 'ShirtShape.vtx[607]', 'ShirtShape.vtx[610:627]', 'ShirtShape.vtx[647:654]']
    pm.skinPercent( 'skinCluster42', vtxs, tmw=('ShoulderPart1_L', 'Shoulder_L') )

def setSkinVerticesWeights1():
    vtxs = ['cat_bodyShape.vtx[416:419]', 'cat_bodyShape.vtx[442]', 'cat_bodyShape.vtx[445:447]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Scapula_L', 0.25), ('Shoulder_L', 0.5), ('ShoulderPart1_L', 0.25)] )
    vtxs = ['cat_bodyShape.vtx[422:424]', 'cat_bodyShape.vtx[427]', 'cat_bodyShape.vtx[429]', 'cat_bodyShape.vtx[431]', 'cat_bodyShape.vtx[444]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Shoulder_L', 0.5), ('ShoulderPart1_L', 0.5)] )
    vtxs = ['cat_bodyShape.vtx[530:536]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Shoulder_L', 0.3), ('ShoulderPart1_L', 0.6), ('Elbow_L', 0.1)] )
    vtxs = ['cat_bodyShape.vtx[523:529]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ShoulderPart1_L', 0.5), ('Elbow_L', 0.5)] )
    vtxs = ['cat_bodyShape.vtx[420:421]', 'cat_bodyShape.vtx[425:426]', 'cat_bodyShape.vtx[428]', 'cat_bodyShape.vtx[430]', 'cat_bodyShape.vtx[443]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ShoulderPart1_L', 0.1), ('Elbow_L', 0.6), ('ElbowPart1_L', 0.3)] )
    vtxs = ['cat_bodyShape.vtx[553:559]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Elbow_L', 0.5), ('ElbowPart1_L', 0.5)] )
    vtxs = ['cat_bodyShape.vtx[448:449]', 'cat_bodyShape.vtx[453:454]', 'cat_bodyShape.vtx[456]', 'cat_bodyShape.vtx[459:460]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Elbow_L', 0.3), ('ElbowPart1_L', 0.6), ('Wrist_L', 0.1)] )
    vtxs = ['cat_bodyShape.vtx[450:452]', 'cat_bodyShape.vtx[455]', 'cat_bodyShape.vtx[457:458]', 'cat_bodyShape.vtx[461]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ElbowPart1_L', 0.5), ('Wrist_L', 0.5)] )
    vtxs = ['cat_bodyShape.vtx[411]', 'cat_bodyShape.vtx[414]', 'cat_bodyShape.vtx[435]', 'cat_bodyShape.vtx[441]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ElbowPart1_L', 0.2), ('Wrist_L', 0.8)] )
    vtxs = ['cat_bodyShape.vtx[410]', 'cat_bodyShape.vtx[432]', 'cat_bodyShape.vtx[466]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ElbowPart1_L', 0.1), ('Wrist_L', 0.2), ('ThumbFinger1_L', 0.5), ('ThumbFinger2_L', 0.2)] )
    vtxs = ['cat_bodyShape.vtx[462:464]', 'cat_bodyShape.vtx[467]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ThumbFinger2_L', 0.5), ('ThumbFinger3_L', 0.5)] )
    vtxs = ['cat_bodyShape.vtx[433]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ThumbFinger2_L', 0.3), ('ThumbFinger3_L', 0.3), ('IndexFinger1_L', 0.4)] )
    vtxs = ['cat_bodyShape.vtx[500:504]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('ThumbFinger3_L', 1)] )
    vtxs = ['cat_bodyShape.vtx[413]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Wrist_L', 0.3), ('IndexFinger1_L', 0.3), ('IndexFinger2_L', 0.1), ('ThumbFinger2_L', 0.3)] )

    vtxs = ['cat_bodyShape.vtx[522]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Wrist_L', 0.45), ('IndexFinger1_L', 0.35), ('IndexFinger2_L', 0.1), ('ThumbFinger1_L', 0.1)] )
    vtxs = ['cat_bodyShape.vtx[412]', 'cat_bodyShape.vtx[434]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Wrist_L', 0.5), ('MiddleFinger1_L', 0.4), ('MiddleFinger2_L', 0.1)] )
    vtxs = ['cat_bodyShape.vtx[415]', 'cat_bodyShape.vtx[440]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('Wrist_L', 0.5), ('RingFinger1_L', 0.4), ('RingFinger2_L', 0.1)] )

    vtxs = ['cat_bodyShape.vtx[436:437]', 'cat_bodyShape.vtx[469]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('IndexFinger2_L', 0.7), ('IndexFinger3_L', 0.3)] )
    vtxs = ['cat_bodyShape.vtx[439]', 'cat_bodyShape.vtx[468]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('IndexFinger2_L', 0.35), ('IndexFinger3_L', 0.15), ('MiddleFinger2_L', 0.35), ('MiddleFinger3_L', 0.15)] )
    vtxs = ['cat_bodyShape.vtx[486:489]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('IndexFinger3_L', 1)] )

    vtxs = ['cat_bodyShape.vtx[498]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('MiddleFinger2_L', 0.35), ('MiddleFinger3_L', 0.15), ('RingFinger2_L', 0.35), ('RingFinger3_L', 0.15)] )
    vtxs = ['cat_bodyShape.vtx[438]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('MiddleFinger2_L', 0.5), ('MiddleFinger3_L', 0.2), ('RingFinger2_L', 0.2), ('RingFinger3_L', 0.1)] )
    vtxs = ['cat_bodyShape.vtx[494:497]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('MiddleFinger3_L', 1)] )

    vtxs = ['cat_bodyShape.vtx[499]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('RingFinger2_L', 0.5), ('RingFinger3_L', 0.2), ('MiddleFinger2_L', 0.2), ('MiddleFinger3_L', 0.1)] )
    vtxs = ['cat_bodyShape.vtx[470:471]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('RingFinger2_L', 0.7), ('RingFinger3_L', 0.3)] )
    vtxs = ['cat_bodyShape.vtx[490:493]']
    pm.skinPercent( 'skinCluster3', vtxs, tv=[('RingFinger3_L', 1)] )
