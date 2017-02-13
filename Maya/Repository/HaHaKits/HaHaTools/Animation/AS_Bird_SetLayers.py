import pymel.core as pm
import maya.mel as mel

def AS_Bird_SetLayers():
    names = {'*Primary_*R':       {'type': 'joint',      'layerName': 'Primary_Joints_R'},
            '*Primary_*L':        {'type': 'joint',      'layerName': 'Primary_Joints_L'},
            '*Secondary_*R':      {'type': 'joint',      'layerName': 'Secondary_Joints_R'},
            '*Secondary_*L':      {'type': 'joint',      'layerName': 'Secondary_Joints_L'},
            '*Tertiary_*R':       {'type': 'joint',      'layerName': 'Tertiary_Joints_R'},
            '*Tertiary_*L':       {'type': 'joint',      'layerName': 'Tertiary_Joints_L'},
            '*PrimaryCovert_*R':  {'type': 'joint',      'layerName': 'PrimaryCovert_Joints_R'},
            '*PrimaryCovert_*L':  {'type': 'joint',      'layerName': 'PrimaryCovert_Joints_L'},
            'FKPrimary_*R':       {'type': 'transform', 'layerName': 'Primary_FK_R'},
            'FKPrimary_*L':       {'type': 'transform', 'layerName': 'Primary_FK_L'},
            'FKSecondary_*R':     {'type': 'transform', 'layerName': 'Secondary_FK_R'},
            'FKSecondary_*L':     {'type': 'transform', 'layerName': 'Secondary_FK_L'},
            'FKTertiary_*R':      {'type': 'transform', 'layerName': 'Tertiary_FK_R'},
            'FKTertiary_*L':      {'type': 'transform', 'layerName': 'Tertiary_FK_L'},
            'FKPrimaryCovert_*R': {'type': 'transform', 'layerName': 'PrimaryCovert_FK_R'},
            'FKPrimaryCovert_*L': {'type': 'transform', 'layerName': 'PrimaryCovert_FK_L'}}

    for match, info in names.iteritems():

        objs = pm.ls(match, type=info['type'])
        if pm.objExists(info['layerName']):
            pm.delete(info['layerName'])
        pm.createDisplayLayer(objs, noRecurse=True, name=info['layerName'])
        pm.setAttr(info['layerName']+'.visibility', 0)
