import os, sys, shutil
import pymel.core as pm
import maya.mel as mel

def toNativePath(strFile):
	if pm.about(nt=True):
		strFile = pm.encodeString(strFile).replace("/","\\")
	return strFile;

pipset = None

class PipelineSetup(object):

    source = None
    destination = None
    repositorySour = None
    repositoryDest = None
    repositoryName = None

    baseflags = ['name', 'l', 'c', 'type']
    extendflags = ['file']
    ext2Type = {'.py': 'python', '.PY': 'python', '.mel': 'mel', '.MEL': 'mel'}
    type2ext = {'python': '.py', 'mel': '.mel'}

    menus={}
    mainMenu = None

#------------------------------------------------------------------------------#
    def __init__(self, sour=None, dest=None, name=None):
        # Set Repository Name
        self.repositoryName = name
        # Set Repository Source
        self.repositorySour = sour
        # Set Destination
        self.repositoryDest = dest

    def installInitial(self, source, destination):
        self.source = source
        self.destination = destination
        reposDir = os.path.join(source, 'Maya', 'Repository')
        reposSubdirs = None
        if os.path.exists(reposDir):
            reposSubdirs = [x for x in os.listdir(reposDir) if os.path.isdir(os.path.join(reposDir, x))]
            # Set Repository Name
            if reposSubdirs:
                self.repositoryName = reposSubdirs[0]
                # Set Repository Source
                self.repositorySour = os.path.join(reposDir, self.repositoryName)
                # Set Destination
                self.repositoryDest = os.path.join(destination, self.repositoryName)
                return True
            else:
                print 'There is not any Repository exist in the "'+reposDir+'" directory!'
                return False
        else:
            print 'The Source directory "'+reposDir+'" does not exist!'
            return False

    def analyzeInfo(self, menufile):
        root, filename = os.path.split(menufile)
        menu, suffix = os.path.splitext(filename)

        info = {}
        if suffix in ['.inf', '.INF', '.py', '.PY', '.mel', '.MEL'] and not filename == '__init__.py':

            if suffix in ['.py', '.PY'] and not os.path.exists(os.path.join(root, menu+'.inf')) and not os.path.exists(os.path.join(root, menu+'.INF')):
                info['name'] = menu
                info['l'] = mel.eval('interToUI( "'+menu+'" )')
                info['c'] = menu+'.'+menu+'()'
                info['type'] = 'python'
                info['file'] = menufile

            elif suffix in ['.mel', '.MEL'] and not os.path.exists(os.path.join(root, menu+'.inf')) and not os.path.exists(os.path.join(root, menu+'.INF')):
                info['name'] = menu
                info['l'] = mel.eval('interToUI( "'+menu+'" )')
                info['c'] = menu+'()'
                info['type'] = 'mel'
                info['file'] = menufile

            elif suffix in ['.inf', '.INF']:
                info['name'] = menu

                # Analyz Info File
                inf = open(menufile, 'r')
                for eachLine in inf:
                    parts = eachLine.split(',')
                    for eachPart in parts:
                        flags = self.baseflags + self.extendflags
                        for flag in flags:
                            if (flag+':') in eachPart:
                                info[flag] = eachPart.partition(flag+':')[2].strip()
                inf.close()

                if 'l' not in info:
                    info['l'] = mel.eval('interToUI( "'+info['name']+'" )')

                if 'type' in info and 'file' not in info:
                    info['file'] = os.path.join(root, menu+type2ext[info['type']])

                if 'file' not in info:
                    info['file'] = os.path.join(root, menu+'.py')
                    if os.path.exists(info['file']):
                        info['type'] = 'python'
                    else:
                        info['file'] = os.path.join(root, menu+'.PY')
                        if os.path.exists(info['file']):
                            info['type'] = 'python'
                        else:
                            info['file'] = os.path.join(root, menu+'.mel')
                            if os.path.exists(info['file']):
                                info['type'] = 'mel'
                            else:
                                info['file'] = os.path.join(root, menu+'.MEL')
                                if os.path.exists(info['file']):
                                    info['type'] = 'mel'
                                else:
                                    print('There is no module '+menu+' exist. Menu "'+menu+'" will not be created!')
                                    info = None
                else:
                    baseFile = os.path.split(info['file'])[-1]
                    info['file'] =  os.path.join(root, baseFile)
                    if os.path.exists(info['file']):
                        module, filesuffix = os.path.splitext(baseFile)
                        info['type'] = self.ext2Type[filesuffix]
                        if 'c' not in info:
                            info['c'] = module+'.'+info['name']+'()'
                    else:
                        print('There is no file '+info['file']+' exist. Menu "'+menu+'" will not be created!')
                        info = None

                if info:
                    if 'c' not in info:
                        info['c'] = menu+'.'+info['name']+'()'
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

        refreshCmd = "import "+self.repositoryName+"\n" \
                 + "reload("+self.repositoryName+")\n" \
                 + "from "+self.repositoryName+".pipelineStartup import *\n" \
                 + "reload ("+self.repositoryName+".pipelineStartup)\n"
        pm.menuItem('refresh', l='Refresh', c=refreshCmd, p=parent)

        #uninstallCmd = 'try:\n\t'+self.repositoryName+'_pipset.uninstall()\n' +\
		#			   'except:\n\tmayaPipelineSetup.uninstall()'
        uninstallCmd = self.repositoryName+'_pipset.uninstall()'
        pm.menuItem('uninstall', l='Uninstall', c=uninstallCmd, p=parent)

    def setSource(self, source):
        self.source = source

    def setDestination(self, destination):
        self.destination = destination

    def setRepositoryName(self, name):
        self.repositoryName = name

    def setRepositorySour(self, sour):
        self.repositorySour = sour

    def setRepositoryDest(self, dest):
        self.repositoryDest = dest

    def pipelineStartup_py(self):
        startupCmd = 'import sys\n'

        syspathStr = ''
        importStr = '\nimport pymel.core as pm\n'

        for k, menu in self.menus.iteritems():
            if 'file' in menu:
                if menu['type']=='python':
                    module = os.path.split(os.path.splitext(menu['file'])[0])[-1]
                    importStr += ('import ' + module + ';reload(' + module + ')\n')
            else:
                syspathStr += ('if \'' + pm.encodeString(menu['dir']) + '\' not in sys.path:\n')
                syspathStr += ('\tsys.path.append(\'' + pm.encodeString(menu['dir']) + '\')\n')

        startupCmd += syspathStr
        startupCmd += importStr
        startupCmd += 'import ' + self.repositoryName + ';reload(' + self.repositoryName + ')\n\n'
        startupCmd += 'from ' + self.repositoryName + ' import mayaPipelineSetup;reload(mayaPipelineSetup)\n\n'

        startupCmd += self.repositoryName+'_pipset = mayaPipelineSetup.PipelineSetup()\n\n'

        startupCmd += self.repositoryName+'_pipset.setSource(\'' + pm.encodeString(self.source) + '\')\n'
        startupCmd += self.repositoryName+'_pipset.setDestination(\'' + pm.encodeString(self.destination) + '\')\n'
        startupCmd += self.repositoryName+'_pipset.setRepositoryName(\'' + pm.encodeString(self.repositoryName) + '\')\n'
        startupCmd += self.repositoryName+'_pipset.setRepositorySour(\'' + pm.encodeString(self.repositorySour) + '\')\n'
        startupCmd += self.repositoryName+'_pipset.setRepositoryDest(\'' + pm.encodeString(self.repositoryDest) + '\')\n'

        startupCmd += self.repositoryName+'_pipset.createMenu()\n'
        startupCmd += self.repositoryName+'_pipset.manageMenuItem()\n'

        pipStartup = open(os.path.join(self.repositoryDest, 'pipelineStartup.py'), 'w')
        pipStartup.write( startupCmd )
        pipStartup.close()

    def userSetup_mel(self, uninstall=False):
        mayaScriptPath = os.path.join(toNativePath(pm.internalVar(uad=True)), 'scripts', 'userSetup.mel')
        versionScriptPath = os.path.join(toNativePath(pm.internalVar(upd=True)[0:-7]), 'scripts', 'userSetup.mel')

        filepath = os.path.join(os.path.split(self.repositoryDest)[0], 'userSetup.mel')
        if not filepath == mayaScriptPath:
            filepath = versionScriptPath

        flag = '//'+self.repositoryName+'_PIPELINESTARTUP'
        statupcmd = '\npython("import '+self.repositoryName+';' \
                  + 'reload('+self.repositoryName+');' \
                  + 'from '+self.repositoryName+'.pipelineStartup import *;' \
                  + 'reload ('+self.repositoryName+'.pipelineStartup)" ); '+flag
        cmds=''
        if not os.path.exists(filepath):
            if not uninstall:
                userSetup = open(filepath, 'w')
                userSetup.write(statupcmd)
                userSetup.close()
        else:
            userSetup = open(filepath, 'r')
            for EachLine in userSetup:
                if not flag in EachLine and not EachLine == '\n':
                    cmds += EachLine
            userSetup.close()
            if not uninstall:
                cmds += statupcmd
            userSetup = open(filepath, 'w')
            userSetup.write(cmds)
            userSetup.close()
            if not cmds:
                os.remove(filepath)

    def confirmWindow(self):
        buttncmd = "import "+self.repositoryName+"\n" \
                 + "reload("+self.repositoryName+")\n" \
                 + "from "+self.repositoryName+".pipelineStartup import *\n" \
                 + "reload ("+self.repositoryName+".pipelineStartup)\n"

        if pm.window('PipelineConfirmWindow', ex=True ):
            pm.deleteUI('PipelineConfirmWindow')

        if int(pm.about(v=True)) < 2016:
            win = pm.window('PipelineConfirmWindow', w=350, h=100, s=0, mnb=0, mxb=0, t='Pipeline Tools Install')
        else:
            win = pm.window('PipelineConfirmWindow', w=350, h=100, s=0, mnb=0, mxb=0, t='Pipeline Tools Install', cc=buttncmd)

        form = pm.formLayout( numberOfDivisions=100)
        buttncmd+='pm.deleteUI(\''+win+'\')'
        buttn = pm.button(label='Click Here To Finish The Installation!', c=buttncmd)
        pm.formLayout(form, e=True, af=[(buttn,'top',30), (buttn,'bottom',30)], ap=[(buttn,'left',0,20), (buttn,'right',0,80)])
        pm.showWindow( win )

    def uninstall(self):
        # Delete Menus
        for k, menu in self.menus.iteritems():
            if pm.menu( menu['object'], ex=True ):
                pm.deleteUI( menu['object'] )
        # Delete Repository
        if os.path.exists(self.repositoryDest):
            shutil.rmtree(self.repositoryDest)
        # Cleaning userSetup
        self.userSetup_mel(uninstall=True)

    def install(self):
        # Make Repository Directory
        if not os.path.exists(self.repositoryDest):
            os.mkdir(self.repositoryDest)

        # Copy Repository Files
        self.installRepository()

        # Copy mayaPipelineSetup.py to Repository
        shutil.copy(os.path.join(self.source, 'mayaPipelineSetup.py'),\
                    os.path.join(self.repositoryDest, 'mayaPipelineSetup.py'))

        # Create Menus
        self.createMenu()

        # Create manager menu items
        self.manageMenuItem()

        # Create pipelineStartup.py
        self.pipelineStartup_py()

        # Create userSetup.mel
        self.userSetup_mel()

        # Finish The Installation Confirm.
        return self.repositoryName

#------------------------------------------------------------------------------#

def install( source, installToVersionDir=True ):
    global pipset

    if installToVersionDir :
        destination = pm.internalVar(upd=True)[0:-7]
    else:
        destination = pm.internalVar(uad=True)
    destination = os.path.join(toNativePath(destination), 'scripts')

    # Initial
    if pipset in None:
        pipset = PipelineSetup()
        pipset.installInitial( source, destination )

    pipset.install()

    return pipset.repositoryName

def uiInstall():
    template = pm.uiTemplate( 'PipelineToolsInstallTemplate', force=True )
    template.define( pm.button, w=200, h=30, al='left' )
    template.define( pm.frameLayout, bv=True, lv=False, mh=5, mw=1 )

    if pm.window('PipelineToolsInstallWin', ex=True ):
        pm.deleteUI('PipelineConfirmWindow')

    with pm.window('PipelineToolsInstallWin', mb=False, mbv=False, t='Pipeline Tools Install') as win:
        # start the template block
        with template:
            with pm.columnLayout( rowSpacing=5 ):
                with pm.frameLayout():
                    with pm.columnLayout():
                        #sourField = pm.textFieldButtonGrp( l='Source Path:', fi=source, bl='   Browse   ', cw3=(65,265,70), w=400 )
                        destField = pm.textFieldButtonGrp( l='Install Path:', bl='   Browse   ', cw3=(65,265,70), w=400 )
                        destField.setFileName(pipset.destination)

                        browseCmd = "caption = 'Pick a Directory to install Repository'\n" \
                                  + "destination = pm.textFieldButtonGrp('"+destField+"', q=True, fi=True)\n" \
                                  + "pm.textFieldButtonGrp('"+destField+"', e=True, fi=pm.fileDialog2(cap=caption, fm=3, dir=destination)[0])"
                        destField.buttonCommand(browseCmd)
                with pm.horizontalLayout():
                    insButtnCmd = "source = mayaPipelineSetup.pipset.source\n" \
                                + "destination = mayaPipelineSetup.toNativePath( pm.textFieldButtonGrp('"+destField+"', q=True, fi=True) )\n" \
                                + "mayaPipelineSetup.pipset.installInitial(source, destination)\n" \
                                + "modul = mayaPipelineSetup.pipset.install()\n"
                    closeWinCmd = 'pm.deleteUI("'+win+'")\n'
                    confirmCmd = 'mayaPipelineSetup.pipset.confirmWindow()'

                    insButtn = pm.button( label='Install', c=insButtnCmd+closeWinCmd+confirmCmd )
                    canButtn = pm.button( label='Cancel', c=closeWinCmd )

def uninstall():
    global pipset
    if pipset:
        pipset.uninstall()
    else:
        print 'There is Nothing to Uninstall.'
