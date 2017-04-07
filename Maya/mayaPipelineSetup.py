import os, sys, shutil
import pymel.core as pm
import maya.mel as mel
import filecmp

def toNativePath(strFile):
	if pm.about(nt=True):
		strFile = pm.encodeString(strFile).replace("/","\\")
	return strFile

pipset = None

class PipelineSetup(object):

    source = None
    destination = None
    repositorySour = None
    repositoryDest = None
    repositoryName = None

    ignore_filetype = ['.pyc']
    ignore_filename = ['__init__']
    menu_filetype = ['.py', '.PY', '.mel', '.MEL', '.div', '.DIV']

    #baseflags = ['name', 'l', 'c', 'type']
    #extendflags = ['file']
    #ext2Type = {'.py': 'python', '.PY': 'python', '.mel': 'mel', '.MEL': 'mel'}
    #type2ext = {'python': '.py', 'mel': '.mel'}

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
        reposDir = os.path.join(source, 'Repository')
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

    def copyRepository(self, force):
        copyOperation = 'Copy'

        # Confirm Dialog
        if not force and os.path.exists(self.repositoryDest):
            title = 'Overwrite Repository Dialog'
            message = 'There is a same Repository "'+self.repositoryName+'" exists in "' +self.source+ '" directory. ' +\
                'All the files and subdirectories under that directory will be deleted and overwrited. ' +\
                'Would you like to contiune Overwrite or Update?'
            copyOperation = pm.confirmDialog(title=title, message=message, button=['Overwrit','Update', 'Cnacel'],\
                defaultButton='Overwrit', cancelButton='Cnacel', dismissString='Cnacel' )

        # Copy Operation
        if copyOperation == 'Cancel':
            print 'Canceled Copy Repository.'
        else:
            if copyOperation == 'Update':
                # Update Rpository.
                self.updateRepository()
            else:
                if copyOperation == 'Overwrit':
                    # Delet Old Repository.
                    shutil.rmtree(self.repositoryDest)
                # Copy Repository.
                shutil.copytree(self.repositorySour, self.repositoryDest, True)
                print 'Copy "' + self.repositoryName + '".'
                # Copy mayaPipelineSetup.py to Repository
                sourceFile = os.path.join(self.source, 'mayaPipelineSetup.py')
                destinationFile = os.path.join(self.repositoryDest, 'mayaPipelineSetup.py')
                shutil.copy(sourceFile, destinationFile)
                print 'Copy "' + sourceFile + '"\n  to "' + destinationFile + '".'
        return copyOperation

    def updateRepository(self):
        # Copy and Update New files
        for root, dirs, files in os.walk(self.repositorySour):
            # Build Repository Directory
            relativePath = root.partition(self.repositorySour)[-1]
            destPath = self.repositoryDest + relativePath
            if not os.path.exists(destPath):
                os.mkdir(destPath)

            # Copy files
            for copyfile in files:
                sourceFile = os.path.join(root, copyfile)
                destinationFile = os.path.join(destPath, copyfile)

                if os.path.exists(destinationFile):
                    if filecmp.cmp(sourceFile, destinationFile):
                        continue

                shutil.copy(sourceFile, destinationFile)
                print "Copy '" + sourceFile + "'\n  to '" + destinationFile + "'."

        # Delete invalid directories & files
        for root, dirs, files in os.walk(self.repositoryDest):
            relativePath = root.partition(self.repositoryDest)[-1]
            sourPath = self.repositorySour + relativePath
            if not os.path.exists(sourPath):
                # Delete invalid directory
                shutil.rmtree(root)
                print "Remove '" + root + "'."
            elif not root == self.repositoryDest:
                # Delete invalid files
                for removefile in files:
                    destinationFile = os.path.join(root, removefile)
                    sourceFile = os.path.join(sourPath, removefile)

                    suffix = os.path.splitext(removefile)[-1]
                    is_update_type = suffix not in self.ignore_filetype

                    if is_update_type and not os.path.exists(sourceFile):
                        os.remove(destinationFile)
                        print "Remove '" + destinationFile + "'."

        # Copy mayaPipelineSetup.py to Repository
        sourceFile = os.path.join(self.source, 'mayaPipelineSetup.py')
        destinationFile = os.path.join(self.repositoryDest, 'mayaPipelineSetup.py')
        if not filecmp.cmp(sourceFile, destinationFile):
            shutil.copy(sourceFile, destinationFile)
            print "Copy '" + sourceFile + "'\n  to '" + destinationFile + "'."
#------------------------------------------------------------------------------#
    def analyzeInfo(self, menufilepath, isdir=False):
        info = {}
        namepath, suffix = os.path.splitext(menufilepath)
        parentpath, menu = os.path.split(namepath)
        rootpath, parent = os.path.split(parentpath)
        if isdir:
            info['name'] = menu
            info['l'] = mel.eval('interToUI( "'+menu+'" )')
            info['dir'] = namepath
            info['parent'] = parent
            info['sub'] = False
            info['hide'] = os.path.exists(os.path.join(namepath+'.hid'))
        else:
            if menu not in self.ignore_filename and suffix in self.menu_filetype:
                if suffix in ['.py', '.PY']:
                    info['type'] = 'python'
                    info['name'] = menu
                    info['l'] = mel.eval('interToUI( "'+menu+'" )')
                    info['c'] = menu+'.'+menu+'()'
                    info['file'] = menufilepath
                    info['parent'] = parent
                elif suffix in ['.mel', '.MEL']:
                    info['type'] = 'mel'
                    info['name'] = menu
                    info['l'] = mel.eval('interToUI( "'+menu+'" )')
                    info['c'] = 'mel.eval(\'' + menu + '\')'
                    info['file'] = menufilepath
                    info['parent'] = parent
                elif suffix in ['.div', '.DIV']:
                    info['type'] = 'divider'
                    info['name'] = menu
                    info['l'] = mel.eval('interToUI( "'+menu.split('_')[-1]+'" )')
                    info['file'] = menufilepath
                    info['parent'] = parent

                subfile = os.path.join(namepath+'.sub')
                if os.path.exists(subfile):
                    info['sub'] = True
                    info['subfile'] = subfile
                    info['name'] += 'sub'
                    info.pop('c')
                else:
                    info['sub'] = False
                info['hide'] = os.path.exists(os.path.join(namepath+'.hid'))
            else:
                info = None
        return info

    def readSubmenu(self, subfilepath):
        subfile = open(subfilepath, 'r')
        subinfo = []
        i=0
        for eachLine in subfile:
            if not eachLine == '':
                i += 1
        subfile.close()

        if i == 0:
            return None
        '''
            parts = eachLine.split(',')
            for eachPart in parts:
                subdate = eachPart.split(':')
                subinfo[i][subdate[0].strip()] = subdate[1].strip()

                flags = self.baseflags + self.extendflags
                for flag in flags:
                    if (flag+':') in eachPart:
                        info[flag] = eachPart.partition(flag+':')[2].strip()
        '''

    def analyzeSubmenu(self, parentInfo, menufilepath):
        namepath, suffix = os.path.splitext(menufilepath)
        parentpath, menu = os.path.split(namepath)
        rootpath, parent = os.path.split(parentpath)

        subinfo = []
        analyzfile = open(menufilepath, 'r')
        if suffix in ['.py', '.PY']:
            for eachLine in analyzfile:
                if eachLine[:4] == 'def ':
                    function = eachLine[4:].partition('(')[0].rstrip()
                    info = {}
                    info['name'] = function
                    info['l'] = mel.eval('interToUI( "'+function+'" )')
                    info['file'] = menufilepath
                    info['parent'] = parentInfo['name']
                    info['type'] = 'python'
                    info['c'] = menu+'.'+function+'()'
                    info['hide'] = False
                    subinfo.append(info)
        elif suffix in ['.mel', '.MEL']:
            for eachLine in analyzfile:
                if eachLine[:12] == 'global proc ':
                    function = eachLine[12:].partition('(')[0].rstrip()
                    info = {}
                    info['name'] = function
                    info['l'] = mel.eval('interToUI( "'+function+'" )')
                    info['file'] = menufilepath
                    info['parent'] = parentInfo['name']
                    info['type'] = 'mel'
                    info['c'] = 'mel.eval(\'' + function + '\')'
                    info['hide'] = False
                    subinfo.append(info)
        return subinfo

    def add_a_menu(self, info):
        menu = info['name']
        if pm.menu( menu, ex=True ):
            pm.deleteUI( menu )
        if info['parent']==self.repositoryName:
            mayaMainWin = mel.eval('$tempMelVar=$gMainWindow')
            self.menus[menu]={'object': pm.menu( menu, l=info['l'], p=mayaMainWin, to=True )}
            self.menus[menu]['sub'] = False
            self.menus[menu]['type'] = 'mainmenu'
            if not self.mainMenu:
                self.mainMenu = self.menus[menu]['object']
            self.menus[menu]['dir'] = info['dir']
        else:
            self.menus[menu]={'object': pm.menuItem( menu, sm=True, l=info['l'], p=info['parent'], to=True )}
            if info['sub']:
                self.menus[menu]['sub'] = True
                self.menus[menu]['type'] = info['type']
                self.menus[menu]['file'] = info['file']
            else:
                self.menus[menu]['sub'] = False
                self.menus[menu]['type'] = 'menu'
                self.menus[menu]['dir'] = info['dir']

    def add_a_menucmd(self, info):
        if pm.menuItem( info['name'], ex=True ):
            pm.deleteUI( info['name'] )
        if info['type'] == 'divider':
            self.menus[info['name']]={'object': pm.menuItem( info['name'], l=info['l'], divider=True, p=info['parent'] )}
        else:
            self.menus[info['name']]={'object': pm.menuItem( info['name'], l=info['l'], p=info['parent'] )}
        if 'c' in info:
            pm.menuItem( info['name'], e=True, c=info['c'] )
        self.menus[info['name']]['type'] = info['type']
        self.menus[info['name']]['file'] = info['file']
        if info['hide'] :
            pm.deleteUI( self.menus[info['name']]['object'] )

    # def updateMenu(self):
    #     for k, menu in self.menus.iteritems():
    #         filepath = menu['file'] if menu.has_key('file') else menu['dir']
    #         if not os.path.exists(filepath):
    #             pass

    def createMenu(self):
        self.menus.clear()
        for root, dirs, files in os.walk(self.repositoryDest):
            parent = os.path.split(root)[-1]

            # Create Menus
            for menu in dirs:
                menudirpath = os.path.join(root, menu)
                info = self.analyzeInfo(menudirpath, True)
                if info:
                    self.add_a_menu(info)

            if not parent==self.repositoryName:
                for menufile in files:
                    menufilepath = os.path.join(root, menufile)
                    info = self.analyzeInfo(menufilepath, False)

                    if info:
                        if info['sub']:
                            # Create Submenu
                            self.add_a_menu(info)

                            # Create Submenu Commands
                            subInfos = self.readSubmenu(info['subfile'])
                            if not subInfos:
                                subInfos = self.analyzeSubmenu(info, menufilepath)
                            for subInfo in subInfos:
                                self.add_a_menucmd(subInfo)

                        else:
                            # Create Menu Commands
                            self.add_a_menucmd(info)
#------------------------------------------------------------------------------#
    def manageMenuItem(self):
        parent = self.mainMenu
        pm.menuItem(divider=True, p=parent)

        # Update
        updateCmd = self.repositoryName+'_pipset.update()\n'
        updateCmd += 'refcmd = '+self.repositoryName+'_pipset.pipelineStartup_py(refresh=True)\n'
        updateCmd +=  "exec( refcmd )\n"
        updateCmd +=  "print 'Updated!'\n"
        pm.menuItem('update', l='Update', c=updateCmd, p=parent)

        # Refresh
        refreshCmd = 'refcmd = '+self.repositoryName+'_pipset.pipelineStartup_py(refresh=True)\n'
        refreshCmd +=  "exec( refcmd )\n"
        refreshCmd +=  "print 'Refreshed!'\n"
        pm.menuItem('refresh', l='Refresh', c=refreshCmd, p=parent)

        # Reinstall
        reinstallCmd = self.repositoryName+'_pipset.reinstall()\n'
        reinstallCmd += 'refcmd = '+self.repositoryName+'_pipset.pipelineStartup_py(refresh=True)\n'
        reinstallCmd +=  "exec( refcmd )\n"
        reinstallCmd +=  "print 'Reinstalled!'\n"
        pm.menuItem('reinstall', l='Reinstall', c=reinstallCmd, p=parent)

        # Uninstall
        uninstallCmd = self.repositoryName+'_pipset.uninstall()\n'
        pm.menuItem('uninstall', l='Uninstall', c=uninstallCmd, p=parent)
        pm.menuItem(divider=True, p=parent)

        # Update At Maya Startup
        checkbox = False
        updateIdentify = os.path.join(toNativePath(self.repositoryDest), 'updateAtStart')
        if os.path.exists(updateIdentify):
            checkbox = True
        updateAtStartupMenu = pm.menuItem('updateAtStart', l='Update At Maya Startup', cb=checkbox, p=parent)
        updateAtStartCmd = 'import sys, os, shutil\n'
        updateAtStartCmd += 'update = pm.menuItem("'+updateAtStartupMenu+'", q=True, cb=True)\n'
        updateAtStartCmd += "updateIdentify = os.path.join('"+toNativePath(self.repositoryDest)+"', 'updateAtStart')\n"
        updateAtStartCmd += 'if update:\n'
        updateAtStartCmd += "\tf = open(updateIdentify, 'w');f.close()\n"
        updateAtStartCmd += 'else:\n'
        updateAtStartCmd += '\tif os.path.exists(updateIdentify):\n'
        updateAtStartCmd += '\t\tos.remove(updateIdentify)\n'
        updateAtStartCmd += self.repositoryName+'_pipset.pipelineStartup_py()\n'
        pm.menuItem(updateAtStartupMenu, e=True, c=updateAtStartCmd)

    # def getRefreshCmd(self):
    #     refreshCmd = "import sys\n" \
    #             + "Dir = '" + self.destination + "'\n" \
    #             + "if Dir not in sys.path:\n" \
    #             + "\tsys.path.append(Dir)\n" \
    #             + "import "+self.repositoryName+"\n" \
    #             + "reload("+self.repositoryName+")\n" \
    #             + "from "+self.repositoryName+".pipelineStartup import *\n" \
    #             + "reload ("+self.repositoryName+".pipelineStartup)\n"
    #     return refreshCmd

    def pipelineStartup_py(self, refresh=False):
        startupCmd = 'import sys, os, shutil\n'

        syspathStr = ''
        importStr = '\nimport pymel.core as pm'
        importStr += '\nimport maya.mel as mel\n\n'

        for k, menu in self.menus.iteritems():
            if 'file' in menu:
                if menu['type']=='python':
                    module = os.path.split(os.path.splitext(menu['file'])[0])[-1]
                    importStr += ('import ' + module + ';reload(' + module + ')\n')
                elif menu['type']=='mel':
                    melfile = toNativePath(menu['file'])
                    importStr += ('mel.eval(\'source "' + pm.encodeString(melfile) + '"\')\n')
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

        if not refresh:
            startupCmd += "updateIdentify = os.path.join('"+toNativePath(self.repositoryDest)+"', 'updateAtStart')\n"
            startupCmd += 'if os.path.exists(updateIdentify):\n'
            startupCmd += '\t'+self.repositoryName+'_pipset.update()\n'
            startupCmd += 'else:\n'
            startupCmd += '\t'+self.repositoryName+'_pipset.createMenu()\n'
            startupCmd += '\t'+self.repositoryName+'_pipset.manageMenuItem()\n'

            pipStartup = open(os.path.join(self.repositoryDest, 'pipelineStartup.py'), 'w')
            pipStartup.write( startupCmd )
            pipStartup.close()
            return
        else:
            startupCmd += self.repositoryName+'_pipset.createMenu()\n'
            startupCmd += self.repositoryName+'_pipset.manageMenuItem()\n'
            return startupCmd

    def userSetup_mel(self, uninstall=False):
        mayaScriptPath = os.path.join(toNativePath(pm.internalVar(uad=True)), 'scripts', 'userSetup.mel')
        versionScriptPath = os.path.join(toNativePath(pm.internalVar(upd=True)[0:-7]), 'scripts', 'userSetup.mel')

        filepath = os.path.join(os.path.split(self.repositoryDest)[0], 'userSetup.mel')
        if not filepath == mayaScriptPath:
            filepath = versionScriptPath

        flag = '//'+self.repositoryName+'_PIPELINESTARTUP'

        statuppymel = "import sys\n" \
                + "Dir = '" + self.destination + "'\n" \
                + "if Dir not in sys.path:\n" \
                + "\tsys.path.append(Dir)\n" \
                + "import "+self.repositoryName+"\n" \
                + "reload("+self.repositoryName+")\n" \
                + "from "+self.repositoryName+".pipelineStartup import *\n" \
                + "reload ("+self.repositoryName+".pipelineStartup)\n"

        statupcmd = '\npython( "'+pm.encodeString(statuppymel)+'" ); '+flag

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

    def update(self, force=False):
        if not os.path.exists(self.repositorySour):
            print "There're no repository source path exists: '"+self.repositorySour+"'."
            return

        if not os.path.exists(self.repositoryDest):
            print "There're no repository destination path exists: '"+self.repositoryDest+"'."
            return

        # Reinstall Repository Files
        self.updateRepository()

        # Create Menus
        self.createMenu()

        # Create manager menu items
        self.manageMenuItem()

        # Rewrite pipelineStartup.py
        self.pipelineStartup_py()

        # Rewrite userSetup.mel
        self.userSetup_mel()

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
        print 'Ueinstalled!'

    def reinstall(self):
        if os.path.exists(self.source):
            self.install()
        else:
            print "There're no source path exists: '"+self.source+"'."

    def install(self, force=False):
        # Copy Repository Files
        operation = self.copyRepository(force)
        if operation == 'Cancel':
            return 'Canceled'

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

def install( source, destination ):
    global pipset

    # Initial
    if pipset is None:
        pipset = PipelineSetup()
        pipset.installInitial(source, destination)

    pipset.install()
    return pipset.repositoryName

def uninstall():
    global pipset
    if pipset:
        pipset.uninstall()
    else:
        print 'There is Nothing to Uninstall.'
