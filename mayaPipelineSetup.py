import os, sys, shutil
import pymel.core as pm
import maya.mel as mel

def toNativePath(strFile):
	if pm.about(nt=True):
		strFile = pm.encodeString(strFile).replace("/","\\")
	return strFile;

pipset = None

class PipelineSetup(object):

    repositorySour=None
    repositoryDest=None
    repositoryName=None

    menus={}
    mainMenu=None

#------------------------------------------------------------------------------#
    def initial(self, source, installToVersionDir):
        self.repositorySour = os.path.join(source, 'Maya', 'Repository')
        # Set Repository Name
        self.repositoryName = [x for x in os.listdir(self.repositorySour) if os.path.isdir(os.path.join(self.repositorySour, x))][0]
        # Set Repository Source
        self.repositorySour = os.path.join(self.repositorySour, self.repositoryName)
        if installToVersionDir :
            self.repositoryDest = pm.internalVar(upd=True)[0:-7]
        else:
            self.repositoryDest = pm.internalVar(uad=True)
        # Set Destination
        self.repositoryDest = os.path.join(toNativePath(self.repositoryDest), 'scripts', self.repositoryName)

    def analyzeInfo(self, menufile):
        root, filename = os.path.split(menufile)
        menu, suffix = os.path.splitext(filename)

        info = {}
        if suffix in ['.inf', '.INF', '.py', '.PY', '.mel', '.MEL'] and not filename == '__init__.py':

            if suffix in ['.py', '.PY'] and not os.path.exists(os.path.join(root, menu+'.inf')):
                info['name'] = menu
                info['type'] = 'python'
                info['file'] = menufile
                info['c'] = menu+'.'+menu+'()'
                info['l'] = mel.eval('interToUI( "'+menu+'" )')

            elif suffix in ['.inf', '.INF']:
                pass

            else:
                pass
        else:
            info = None

        return info

    def installRepository(self):
        for root, dirs, files in os.walk(self.repositorySour):
            parent = os.path.split(root)[-1]
            # Make Repository Directory
            relativePath = root.partition(self.repositorySour)[-1]
            destPath = self.repositoryDest + relativePath
            if not os.path.exists(destPath):
                os.mkdir(destPath)

            for copyfile in files:
                filename = os.path.splitext(copyfile)
                suffix = filename[-1]
                menu = os.path.basename(filename[0])
                if suffix in ['.py', '.PY', '.inf', '.INF']:
                    # Copy Repository files
                    shutil.copy(os.path.join(root, copyfile),\
                                os.path.join(destPath, copyfile))

    def createMenu(self):
        for root, dirs, files in os.walk(self.repositoryDest):
            parent = os.path.split(root)[-1]

            for menu in dirs:
                label = mel.eval('interToUI( "'+menu+'" )')
                if pm.menu( menu, ex=True ):
                    pm.deleteUI( menu )
                if parent==self.repositoryName:
                    mayaMainWin = mel.eval('$tempMelVar=$gMainWindow')
                    self.menus[menu]={'object': pm.menu( menu, l=label, p=mayaMainWin, to=True )}
                    self.menus[menu]['type'] = 'menu'
                    if not self.mainMenu:
                        self.mainMenu = self.menus[menu]['object']
                else:
                    self.menus[menu]={'object': pm.menuItem( menu, sm=True, l=label, p=parent, to=True )}
                    self.menus[menu]['type'] = 'submenu'
                self.menus[menu]['dir'] = os.path.join(root, menu)

            if not parent==self.repositoryName:
                for menufile in files:
                    info = self.analyzeInfo( os.path.join(root, menufile) )
                    if info:
                        # Create MenuItem
                        if pm.menuItem( info['name'], ex=True ):
                            pm.deleteUI( info['name'] )
                        self.menus[info['name']]={'object': pm.menuItem( info['name'], l=info['l'], p=parent )}
                        self.menus[info['name']]['type'] = info['type']
                        self.menus[info['name']]['file'] = info['file']

                        if 'c' in info:
                            pm.menuItem( info['name'], e=True, c=info['c'] )

    def manageMenuItem(self):
        parent = self.mainMenu
        pm.menuItem(divider=True, p=parent)
        uninstallCmd = 'try:\n\t'+self.repositoryName+'_pipset.uninstall()\n'\
                     + 'except:\n\tmayaPipelineSetup.uninstall()'
        pm.menuItem('uninstall', l='Uninstall', c=uninstallCmd, p=parent)

    def pipelineStartup_py(self):
        startupCmd = 'import sys\n'

        syspathStr = ''
        importStr = '\nimport pymel.core as pm\n'

        for k, menu in self.menus.iteritems():
            if 'file' in menu:
                if menu['type']=='python':
                    importStr += ('import ' + k + '\n')
            else:
                syspathStr += ('if \'' + pm.encodeString(menu['dir']) + '\' not in sys.path:\n')
                syspathStr += ('\tsys.path.append(\'' + pm.encodeString(menu['dir']) + '\')\n')

        startupCmd += syspathStr
        startupCmd += importStr
        startupCmd += 'from ' + self.repositoryName + ' import mayaPipelineSetup\n\n'
        startupCmd += self.repositoryName+'_pipset = mayaPipelineSetup.PipelineSetup()\n\n'
        startupCmd += self.repositoryName+'_pipset.repositorySour = \'' + pm.encodeString(self.repositorySour) + '\'\n'
        startupCmd += self.repositoryName+'_pipset.repositoryDest = \'' + pm.encodeString(self.repositoryDest) + '\'\n'
        startupCmd += self.repositoryName+'_pipset.repositoryName = \'' + self.repositoryName + '\'\n\n'

        startupCmd += self.repositoryName+'_pipset.createMenu()\n'
        startupCmd += self.repositoryName+'_pipset.manageMenuItem()\n'

        pipStartup = open(os.path.join(self.repositoryDest, 'pipelineStartup.py'), 'w')
        pipStartup.write( startupCmd )
        pipStartup.close()

    def userSetup_mel(self, uninstall=False):
        filepath = os.path.join(os.path.split(self.repositoryDest)[0], 'userSetup.mel')
        flag = '//'+self.repositoryName+'_PIPELINESTARTUP'
        statupcmd = '\npython("from '+self.repositoryName+'.pipelineStartup import *" ); '+flag
        if not os.path.exists(filepath):
            if not uninstall:
                userSetup = open(filepath, 'w')
                userSetup.write(statupcmd)
                userSetup.close()
        else:
            userSetup = open(filepath, 'r')
            cmds=''
            for EachLine in userSetup:
                if not flag in EachLine and not EachLine == '\n':
                    cmds += EachLine
            userSetup.close()
            if not uninstall:
                cmds += statupcmd
            userSetup = open(filepath, 'w')
            userSetup.write(cmds)
            userSetup.close()

    def uninstall(self, uninstallFromVersionDir=True):
        # Delete Menus
        for k, menu in self.menus.iteritems():
            if pm.menu( menu['object'], ex=True ):
                pm.deleteUI( menu['object'] )
        # Delete Repository
        if os.path.exists(self.repositoryDest):
            shutil.rmtree(self.repositoryDest)
        # Cleaning userSetup
        self.userSetup_mel(uninstall=True)

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
    def install(self, source, installToVersionDir):

        # Initial
        self.initial(source, installToVersionDir)

        # Make Repository Directory
        if not os.path.exists(self.repositoryDest):
            os.mkdir(self.repositoryDest)

        # Copy Repository Files
        self.installRepository()

        # Copy mayaPipelineSetup.py to Repository
        shutil.copy(os.path.join(source, 'mayaPipelineSetup.py'),\
                    os.path.join(self.repositoryDest, 'mayaPipelineSetup.py'))

        # Create Menus
        self.createMenu()

        # Create manager menu items
        self.manageMenuItem()

        # Create pipelineStartup.py
        self.pipelineStartup_py()

        # Create userSetup
        self.userSetup_mel()

#------------------------------------------------------------------------------#

def install( source, installToVersionDir=True ):
    global pipset
    if pipset is None:
        pipset = PipelineSetup()
    pipset.install( source, installToVersionDir )

def uninstall( installToVersionDir=True ):
    global pipset
    if pipset is None:
        pipset = PipelineSetup()
    pipset.uninstall( installToVersionDir )
