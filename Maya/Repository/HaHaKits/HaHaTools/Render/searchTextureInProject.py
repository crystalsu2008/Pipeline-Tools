import os, sys, shutil
import pymel.core as pm

def searchTextureInProject(fileNodes=[]):

    # Looking for file nodes.
    #
    if not fileNodes:
        fileNodes = pm.ls(sl=True, type='file')
        if not fileNodes:
            fileNodes = pm.ls(type='file')
            if not fileNodes:
                pm.warning( "No file nodes were found!" )
                return

    textures={}
    fileTextureName={}
    for node in fileNodes:
        fileTextureName[node] = pm.getAttr(node+'.fileTextureName')
        textures[node] = os.path.split(fileTextureName[node])[1]

    rootdir = pm.workspace(q=True, rd=True)
    for parent, dirs, files in os.walk(rootdir):
        for fil in files:
            popitems=[]
            for node, imageName in textures.iteritems():
                if imageName == fil:
                    relativePath = os.path.join(parent.partition(rootdir)[2], imageName)
                    pm.setAttr(node+'.fileTextureName', relativePath, type='string')
                    print('%s: \n\t%s --> %s') % (node+'.fileTextureName', fileTextureName[node], relativePath)
                    popitems.append(node)
            if popitems:
                for x in popitems:
                    textures.pop(x)
                    if not textures:
                        return
