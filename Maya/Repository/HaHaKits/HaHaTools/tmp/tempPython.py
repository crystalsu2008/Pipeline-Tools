import pymel.core as pm
import maya.mel as mel

def tempPython():
    objs = pm.ls(sl=True)
    curves = pm.listRelatives(objs, s=True, type='nurbsCurve')
    for curve in curves:
        spans=pm.getAttr(curve+'.spans')
        degree=pm.getAttr(curve+'.degree')
        cvnumber=spans+degree

        pymelscript =  'pm.curve(p=['
        for i in range(cvnumber):
            cv = pm.getAttr(curve+'.controlPoints['+str(i)+']')
            pymelscript += '('+str(cv[0])+', '+str(cv[1])+', '+str(cv[2])+'),\\\n\t'
        pymelscript += "], n='PrimariesCtrl')"

        print pymelscript

def AnalyseUE4Error():
    # Analyse a UE4 error log file to find all problem vertexs
    f=open('E:/Jobs/Asset/HEYHA_ZOO/kangaroo/scenes/log.txt')
    allnums=[]
    vtxs=[]
    for eachLine in f:
        line=eachLine.replace('.',' ')
        for word in line.split(' '):
            if word.isdigit() and not allnums.count(word):
                allnums.append(word)
                vtxs.append('kangaroo_model.vtx['+word+']')
    f.close()
    select(cl=True)
    select (vtxs)


    # clear all namespace
    name_space=namespaceInfo(':',lon=True)
    name_space.remove('UI')
    name_space.remove('shared')

    namespace(f=True,mv=('lion_rig', ':'))
    namespace(rm='lion_rig')

    cmds.dagPose(restore=True, bindPose=True)

    cmds.dagPose(query=True, bindPose=True)
