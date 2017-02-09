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
