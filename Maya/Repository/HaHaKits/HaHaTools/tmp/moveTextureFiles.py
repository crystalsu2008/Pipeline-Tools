import os, shutil
import pymel.core as pm

def moveTextureFiles(destDir = 'scenes'):
    destPath = pm.workspace.getPath()
    destPath = os.path.join(destPath, destDir)
    if not os.path.isdir(destPath):
        os.mkdir(destPath)

    fileNodes = pm.ls(type='file')
    for node in fileNodes:
        txfile = pm.getAttr(node+'.fileTextureName')
        if os.path.exists(txfile):
            root, filename = os.path.split(txfile)
            destFile = os.path.join(destPath, filename)
            shutil.move(txfile, destFile)
            pm.setAttr(node+'.fileTextureName', destFile)
        else:
            print "Texture doesn't exists: %s." % (txfile)
