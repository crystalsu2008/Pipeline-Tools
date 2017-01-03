'''
import sys
Dir = 'C:/Users/Administrator/Documents/DEV/MayaMiscTools/my_pipe'
if Dir not in sys.path:
    sys.path.append(Dir)

import advancedToKinect;reload(advancedToKinect)

advancedToKinect.createKinect2()
'''

import pymel.core as pm
import maya.mel as mel

a2k = None

class Advanced2Kinect(object):

    # Advanced to Avatar Map
    avamap = {'SPINEBASE': ('Root_M', None, 'SPINEMID', (1,0,0), (0,1,0)),
             'SPINEMID': ('Spine1_M', 'SPINEBASE', 'SPINESHOULDER', (1,0,0), (0,1,0)),
              'SPINESHOULDER': ('Chest_M', 'SPINEMID', 'NECK', (1,0,0), (0,1,0)),
               'NECK': ('Neck_M', 'SPINESHOULDER', 'HEAD', (1,0,0), (0,1,0)),
                'HEAD': ('HeadEnd_M', 'NECK', None, (1,0,0), (0,1,0)),
            'SHOULDERLEFT': ('Shoulder_L', 'SPINESHOULDER', 'ELBOWLEFT', (1,0,0), (0,0,-1)),
             'ELBOWLEFT': ('Elbow_L', 'SHOULDERLEFT', 'WRISTLEFT', (1,0,0), (0,0,-1)),
              'WRISTLEFT': ('Wrist_L', 'ELBOWLEFT', 'HANDLEFT', (1,0,0), (0,0,-1)),
               'HANDLEFT': ('MiddleFinger1_L', 'WRISTLEFT', 'HANDTIPLEFT', (1,0,0), (0,0,-1)),
                'HANDTIPLEFT': ('MiddleFinger4_L', 'HANDLEFT', None, (1,0,0), (0,0,-1)),
                 'THUMBLEFT': ('ThumbFinger4_L', 'WRISTLEFT', None, (1,0,0), (0,0,-1)),
            'SHOULDERRIGHT': ('Shoulder_R', 'SPINESHOULDER', 'ELBOWRIGHT', (1,0,0), (0,0,-1)),
             'ELBOWRIGHT': ('Elbow_R', 'SHOULDERRIGHT', 'WRISTRIGHT', (1,0,0), (0,0,-1)),
              'WRISTRIGHT': ('Wrist_R', 'ELBOWRIGHT', 'HANDRIGHT', (1,0,0), (0,0,-1)),
               'HANDRIGHT': ('MiddleFinger1_R', 'WRISTRIGHT', 'HANDTIPRIGHT', (1,0,0), (0,0,-1)),
                'HANDTIPRIGHT': ('MiddleFinger4_R', 'HANDRIGHT', None, (1,0,0), (0,0,-1)),
                 'THUMBRIGHT': ('ThumbFinger4_R', 'WRISTRIGHT', None, (1,0,0), (0,0,-1)),
            'HIPLEFT': ('Hip_L', 'SPINEBASE', 'KNEELEFT', (1,0,0), (0,-1,0)),
             'KNEELEFT': ('Knee_L', 'HIPLEFT', 'ANKLELEFT', (1,0,0), (0,-1,0)),
              'ANKLELEFT': ('Ankle_L', 'KNEELEFT', 'FOOTLEFT', (1,0,0), (0,-1,0)),
               'FOOTLEFT': ('ToesEnd_L', 'ANKLELEFT', None, (1,0,0), (0,-1,0)),
            'HIPRIGHT': ('Hip_R', 'SPINEBASE', 'KNEERIGHT', (1,0,0), (0,1,0)),
             'KNEERIGHT': ('Knee_R', 'HIPRIGHT', 'ANKLERIGHT', (1,0,0), (0,1,0)),
              'ANKLERIGHT': ('Ankle_R', 'KNEERIGHT', 'FOOTRIGHT', (1,0,0), (0,1,0)),
               'FOOTRIGHT': ('ToesEnd_R', 'ANKLERIGHT', None, (1,0,0), (0,1,0))}

    # Advanced to Kinect2 Map
    k2map = {'SPINEBASE': ('Root_M', None, 'SPINEMID', (1,0,0), (0,1,0)),
             'SPINEMID': ('Spine1_M', 'SPINEBASE', 'SPINESHOULDER', (1,0,0), (0,1,0)),
              'SPINESHOULDER': ('Chest_M', 'SPINEMID', 'NECK', (1,0,0), (0,1,0)),
               'NECK': ('Neck_M', 'SPINESHOULDER', 'HEAD', (1,0,0), (0,1,0)),
                'HEAD': ('HeadEnd_M', 'NECK', None, (1,0,0), (0,1,0)),
            'SHOULDERLEFT': ('Shoulder_L', 'SPINESHOULDER', 'ELBOWLEFT', (1,0,0), (0,0,-1)),
             'ELBOWLEFT': ('Elbow_L', 'SHOULDERLEFT', 'WRISTLEFT', (1,0,0), (0,0,-1)),
              'WRISTLEFT': ('Wrist_L', 'ELBOWLEFT', 'HANDLEFT', (1,0,0), (0,0,-1)),
               'HANDLEFT': ('MiddleFinger1_L', 'WRISTLEFT', 'HANDTIPLEFT', (1,0,0), (0,0,-1)),
                'HANDTIPLEFT': ('MiddleFinger4_L', 'HANDLEFT', None, (1,0,0), (0,0,-1)),
                 'THUMBLEFT': ('ThumbFinger4_L', 'WRISTLEFT', None, (1,0,0), (0,0,-1)),
            'SHOULDERRIGHT': ('Shoulder_R', 'SPINESHOULDER', 'ELBOWRIGHT', (1,0,0), (0,0,-1)),
             'ELBOWRIGHT': ('Elbow_R', 'SHOULDERRIGHT', 'WRISTRIGHT', (1,0,0), (0,0,-1)),
              'WRISTRIGHT': ('Wrist_R', 'ELBOWRIGHT', 'HANDRIGHT', (1,0,0), (0,0,-1)),
               'HANDRIGHT': ('MiddleFinger1_R', 'WRISTRIGHT', 'HANDTIPRIGHT', (1,0,0), (0,0,-1)),
                'HANDTIPRIGHT': ('MiddleFinger4_R', 'HANDRIGHT', None, (1,0,0), (0,0,-1)),
                 'THUMBRIGHT': ('ThumbFinger4_R', 'WRISTRIGHT', None, (1,0,0), (0,0,-1)),
            'HIPLEFT': ('Hip_L', 'SPINEBASE', 'KNEELEFT', (1,0,0), (0,-1,0)),
             'KNEELEFT': ('Knee_L', 'HIPLEFT', 'ANKLELEFT', (1,0,0), (0,-1,0)),
              'ANKLELEFT': ('Ankle_L', 'KNEELEFT', 'FOOTLEFT', (1,0,0), (0,-1,0)),
               'FOOTLEFT': ('ToesEnd_L', 'ANKLELEFT', None, (1,0,0), (0,-1,0)),
            'HIPRIGHT': ('Hip_R', 'SPINEBASE', 'KNEERIGHT', (1,0,0), (0,1,0)),
             'KNEERIGHT': ('Knee_R', 'HIPRIGHT', 'ANKLERIGHT', (1,0,0), (0,1,0)),
              'ANKLERIGHT': ('Ankle_R', 'KNEERIGHT', 'FOOTRIGHT', (1,0,0), (0,1,0)),
               'FOOTRIGHT': ('ToesEnd_R', 'ANKLERIGHT', None, (1,0,0), (0,1,0))}

    k2wmap= {'SPINEBASE': ['Root_M'],
             'SPINEMID': ['Spine1_M'],
              'SPINESHOULDER': ['Chest_M', 'Scapula_L', 'Scapula_R'],
               'NECK': ['Neck_M', 'Head_M', 'HeadEnd_M',
                        'Eye_R', 'EyeEnd_R', 'Eye_L', 'EyeEnd_L',
                        'Jaw_M', 'JawEnd_M'],
                'HEAD': None,
            'SHOULDERLEFT': ['Shoulder_L'],
             'ELBOWLEFT': ['Elbow_L'],
              'WRISTLEFT': ['Wrist_L', 'Cup_L', 'ThumbFinger1_L'],
               'HANDLEFT': ['MiddleFinger1_L', 'MiddleFinger2_L', 'MiddleFinger3_L', 'MiddleFinger4_L',
                            'IndexFinger1_L', 'IndexFinger2_L', 'IndexFinger3_L', 'IndexFinger4_L',
                            'RingFinger1_L', 'RingFinger2_L', 'RingFinger3_L', 'RingFinger4_L',
                            'PinkyFinger1_L', 'PinkyFinger2_L', 'PinkyFinger3_L', 'PinkyFinger4_L'],
                'HANDTIPLEFT': None,
                 'THUMBLEFT': ['ThumbFinger2_L', 'ThumbFinger3_L', 'ThumbFinger4_L'],
            'SHOULDERRIGHT': ['Shoulder_R'],
             'ELBOWRIGHT': ['Elbow_R'],
              'WRISTRIGHT': ['Wrist_R', 'Cup_R', 'ThumbFinger1_R'],
               'HANDRIGHT': ['MiddleFinger1_R', 'MiddleFinger2_R', 'MiddleFinger3_R', 'MiddleFinger4_R',
                            'IndexFinger1_R', 'IndexFinger2_R', 'IndexFinger3_R', 'IndexFinger4_R',
                            'RingFinger1_R', 'RingFinger2_R', 'RingFinger3_R', 'RingFinger4_R',
                            'PinkyFinger1_R', 'PinkyFinger2_R', 'PinkyFinger3_R', 'PinkyFinger4_R'],
                'HANDTIPRIGHT': None,
                 'THUMBRIGHT': ['ThumbFinger2_R', 'ThumbFinger3_R', 'ThumbFinger4_R'],
            'HIPLEFT': ['Hip_L'],
             'KNEELEFT': ['Knee_L'],
              'ANKLELEFT': ['Ankle_L', 'Toes_L'],
               'FOOTLEFT': None,
            'HIPRIGHT': ['Hip_R'],
             'KNEERIGHT': ['Knee_R'],
              'ANKLERIGHT': ['Ankle_R', 'Toes_R'],
               'FOOTRIGHT': None}

    noneKeepKeywords =  ['Root', 'Spine', 'Chest', 'Neck', 'Head', 'Eye', 'Jaw',
                                 'Scapula', 'Shoulder', 'Elbow', 'Wrist', 'Cup',
      'MiddleFinger', 'ThumbFinger', 'IndexFinger', 'PinkyFinger', 'RingFinger',
                                                 'Hip', 'Knee', 'Ankle', 'Toes']

    asSkins, k2Skins = [None], [None]

    def convertSkeleton(self, toType='Kinect2'):
        if toType=='Kinect2':
            mapdict = self.k2map
        elif toType=='Avatar':
            mapdict = self.avamap
        #
        # Create Kinect2 Joints
        #
        for kjot in mapdict:
            tag = mapdict[kjot][0]
            aimid = mapdict[kjot][2]
            aim = None if aimid is None else mapdict[aimid][0]
            aimv = mapdict[kjot][3]

            t = pm.xform( tag, q=True, ws=True, t=True )
            pm.select( cl=True )
            interJoint = pm.joint( p=t, n=(kjot+'intermediate') )

            if not aim is None:
                aimer = pm.aimConstraint( aim, interJoint, aim=aimv, wuo=aim,\
                                   wut='objectrotation', u=mapdict[kjot][4], wu=(0,1,0) )
                pm.delete( aimer )
            pm.duplicate( interJoint, n=kjot )

        #
        # Make Joints Hierarchy
        #
        for kjot in mapdict:
            parent = mapdict[kjot][1]
            aimid = mapdict[kjot][2]
            if not parent is None:
                pm.parent( (kjot+'intermediate'), (parent+'intermediate') )
                pm.parent( kjot, parent )
                if aimid is None:
                    pm.setAttr( kjot+'intermediate'+'.jointOrient', (0,0,0) )

            # Freeze Transformations
            if int(pm.about(v=True)[0:4]) >= 2016:
                pm.makeIdentity( (kjot+'intermediate'), a=True, jo=False, t=False,\
                                 r=True, s=False, n=0, pn=True )
            else:
                pm.makeIdentity( (kjot+'intermediate'), a=True, jo=False, t=False,\
                                 r=True, s=False, n=0 )
        #
        # Make Constraint
        #
        for kjot in mapdict:
            parent = mapdict[kjot][1]
            tag = mapdict[kjot][0]
            aimid = mapdict[kjot][2]
            aim = None if aimid is None else mapdict[aimid][0]
            aimv = mapdict[kjot][3]

            # Point Constraint
            pm.pointConstraint( tag, (kjot+'intermediate') )

            # Aim Constraint
            if not aim is None:
                pm.aimConstraint( aim, (kjot+'intermediate'), aim=aimv, wuo=aim,\
                          wut='objectrotation', u=mapdict[kjot][4], wu=(0,1,0) )

            pm.setAttr( (kjot+'.jointOrient'), pm.getAttr(kjot+'intermediate.jointOrient') )
            pm.connectAttr( (kjot+'intermediate.r'), (kjot+'.r') )
            pm.connectAttr( (kjot+'intermediate.t'), (kjot+'.t') )

        #
        # Create None Kinect2 Joints
        #
        # Get (AdvancedSkeleton: Kinect2) joint dict.
        as_map_k2={}
        for k2jo, asjos in self.k2wmap.iteritems():
            if asjos:
                for asjo in asjos:
                    as_map_k2[asjo]=k2jo

        # Finding the keepJoints.
        keepJoints = {}
        for joint in pm.listRelatives('DeformationSystem', ad=True, typ='joint'):
            keepJoint=True
            for keyword in self.noneKeepKeywords:
                if keyword in str(joint):
                    keepJoint=False
                    break

            if keepJoint:
                jointParent = pm.listRelatives(joint, p=True, typ='joint')[0]
                keepJoints[joint] = jointParent

        # Create None Kinect2 joints and intermediate joints.
        interJoints={}
        k2keepJoints={}
        for kepJot, kepJotParent in keepJoints.iteritems():
            t = pm.xform( kepJot, q=True, ws=True, t=True )
            pm.select( cl=True )
            intJot = pm.joint( p=t, n=('k2'+kepJot+'intermediate') )
            k2kepJot=pm.duplicate( intJot, n=('k2'+kepJot) )[0]
            # Get the correct parent.
            if as_map_k2.has_key(str(kepJotParent)):
                interJoints[intJot] = (as_map_k2[str(kepJotParent)]+'intermediate', kepJot)
                k2keepJoints[k2kepJot] = (as_map_k2[str(kepJotParent)], intJot)
            else:
                interJoints[intJot] = ('k2'+kepJotParent+'intermediate', kepJot)
                k2keepJoints[k2kepJot] = ('k2'+kepJotParent, intJot)

        #
        # Make Joints Hierarchy
        #
        for intJot, intJotInfo in interJoints.iteritems():
            pm.parent( intJot, intJotInfo[0] )
            pm.parentConstraint( intJotInfo[1], intJot )
        for k2kepJot, k2kepJotInfo in k2keepJoints.iteritems():
            pm.parent( k2kepJot, k2kepJotInfo[0] )
            pm.setAttr( (k2kepJot+'.jointOrient'), pm.getAttr(k2kepJotInfo[1]+'.jointOrient') )
            pm.connectAttr( (k2kepJotInfo[1]+'.r'), (k2kepJot+'.r') )
            pm.connectAttr( (k2kepJotInfo[1]+'.t'), (k2kepJot+'.t') )

        #
        # Create 'Kinect2' joint root curve handle.
        #
        xpos, ypos, zpos = self.getHandlePos()
        textCurveGrp = pm.textCurves( f='Courier', t=toType, ch=False)
        bbox = pm.exactWorldBoundingBox(textCurveGrp)
        pm.xform(textCurveGrp, t=(xpos, ypos, zpos), ro=(0,0,-90),\
                      s=(ypos/3/bbox[3],ypos/3/bbox[3],ypos/3/bbox[3]))
        rootCurvesShape = pm.listRelatives(textCurveGrp, ad=True, s=True)
        rootCurves = pm.parent(rootCurvesShape, w=True)
        pm.makeIdentity(rootCurves, apply=True, t=1, r=1, s=1, n=0)

        # Create 'Kinect2' joint root.
        rootGrp = pm.group( 'SPINEBASE', n='K2_Skeleton', w=True, em=True)
        pm.parent( rootCurvesShape, rootGrp, s=True, add=True)
        pm.delete( textCurveGrp, rootCurves )
        pm.parent( 'SPINEBASE', rootGrp )

        # Move intermediate joint to Advanced Skeleton Group.
        asGroup = pm.listRelatives(pm.listRelatives(pm.ls('MainShape', typ='nurbsCurve'), p=True), p=True)[0]
        pm.parent( 'SPINEBASEintermediate', asGroup)
        pm.setAttr( 'SPINEBASEintermediate.visibility', False )
        return

    def getHandlePos(self):
        x = y = z = 0
        for jot in pm.listRelatives('SPINEBASE', ad=True, typ='joint'):
            x1, y1, z1 = pm.xform(jot, q=True, t=True, ws=True)
            x = x1 if x1 > x else x
            y = y1 if y1 > y else y
            z = z1 if z1 > z else z
        return x, y, z

    def copySkinWeights(self):
        if not self.asSkins[0] or not self.k2Skins[0]:
            pm.error("At least given a source skinned object and a destination object.")
        else:
            for fromSkin, toSkin in zip(self.asSkins, self.k2Skins):
                pm.select(fromSkin, toSkin, replace=True)
                pm.copySkinWeights(nm=True, sa='closestPoint', ia='closestJoint', nr=True)

    def duplicateSkinObjects(self):
        fromClusters=[]
        for joint in pm.listRelatives('DeformationSystem', ad=True, typ='joint'):
            clusters = pm.listConnections(joint+'.worldMatrix', type='skinCluster')
            for cluster in clusters:
                if not cluster in fromClusters:
                    fromClusters.append(cluster)
        formSkins=[]
        for cluster in fromClusters:
            skinobjs = pm.listConnections(cluster+'.outputGeometry', type='mesh')
            formSkins.extend(skinobjs)
        toSkins=[]
        for obj in formSkins:
            toSkins.extend(pm.duplicate( obj, n='k2'+obj, rr=True ))
            self.removeInvalidIntermediate(obj)
            # Bind kinect2 skins
            pm.skinCluster('SPINEBASE', toSkins[-1], nw=1, mi=3, dr=4.0)

        geogrp = pm.group( n='K2_Geometry', em=True, w=True )
        pm.parent(toSkins, geogrp)

        self.asSkins=formSkins
        self.k2Skins=toSkins

    def removeInvalidIntermediate(self, objs):
        allShapes=pm.listRelatives(objs, c=True, s=True)
        notIntermediateShapes=pm.listRelatives(objs,c=True, s=True, ni=True)
        intermediateShapes=list(set(allShapes)-set(notIntermediateShapes))
        for x in intermediateShapes:
            if not len(pm.listConnections(x)):
                pm.delete(x)

def createAvatar():
    global a2k
    if a2k is None:
        a2k = Advanced2Kinect()
    a2k.convertSkeleton(toType='Avatar')
    a2k.duplicateSkinObjects()
    a2k.copySkinWeights()

def createKinect2():
    global a2k
    if a2k is None:
        a2k = Advanced2Kinect()
    a2k.convertSkeleton()
    a2k.duplicateSkinObjects()
    a2k.copySkinWeights()

def copySkinWeights():
    global a2k
    if a2k is None:
        a2k = Advanced2Kinect()
    a2k.copySkinWeights()
