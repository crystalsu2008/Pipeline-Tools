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
    for node in fileNodes:
        textures[node] = os.path.split(pm.getAttr(node+'.fileTextureName'))[1]

    rootdir = pm.workspace(q=True, rd=True)
    for root, dirs, files in os.walk(rootdir):
        for fil in files:
            for node, imageName in textures.iteritems():
                if imageName == fil:
                    print imageName
