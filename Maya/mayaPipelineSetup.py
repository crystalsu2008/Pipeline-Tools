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
    updateWhenStartup = True

    ignore_filetype = ['.pyc']
    ignore_filename = ['__init__']
    menu_filetype = ['.py', '.PY', '.mel', '.MEL']

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
    def setUpdateWhenStartup(self, update):
        self.updateWhenStartup = update

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

        print 'Updated!'

    def analyzeInfo(self, root, menu, suffix):
        #root, filename = os.path.split(menufile)
        #menu, suffix = os.path.splitext(filename)
        menufile = os.path.join(root, (menu+suffix))

        info = {}

        if os.path.exists(os.path.join(root, menu+'.sub')):
            info['type'] = 'submenu'
            info['name'] = menu
            info['l'] = mel.eval('interToUI( "'+menu+'" )')
            info['file'] = menufile

            subInfo = self.analyzeSubmenu(os.path.join(root, menu+'.sub'))
            if not subInfo:
                subInfo = self.analyzeSubmenu(menufile)

        else:
            if suffix in ['.py', '.PY']:
                info['type'] = 'python'
                info['name'] = menu
                info['l'] = mel.eval('interToUI( "'+menu+'" )')
                info['c'] = menu+'.'+menu+'()'
                info['file'] = menufile
            elif suffix in ['.mel', '.MEL']:
                info['type'] = 'mel'
                info['name'] = menu
                info['l'] = mel.eval('interToUI( "'+menu+'" )')
                info['c'] = 'mel.eval(\'' + menu + '\')'
                info['file'] = menufile

            # Analyz Info File
            # inf = open(menufile, 'r')
            # for eachLine in inf:
            #     parts = eachLine.split(',')
            #     for eachPart in parts:
            #         flags = self.baseflags + self.extendflags
            #         for flag in flags:
            #             if (flag+':') in eachPart:
            #                 info[flag] = eachPart.partition(flag+':')[2].strip()
            # inf.close()
            #
            # if 'l' not in info:
            #     info['l'] = mel.eval('interToUI( "'+info['name']+'" )')
            #
            # if 'type' in info and 'file' not in info:
            #     info['file'] = os.path.join(root, menu+type2ext[info['type']])
            #
            # if 'file' not in info:
            #     info['file'] = os.path.join(root, menu+'.py')
            #     if os.path.exists(info['file']):
            #         info['type'] = 'python'
            #     else:
            #         info['file'] = os.path.join(root, menu+'.PY')
            #         if os.path.exists(info['file']):
            #             info['type'] = 'python'
            #         else:
            #             info['file'] = os.path.join(root, menu+'.mel')
            #             if os.path.exists(info['file']):
            #                 info['type'] = 'mel'
            #             else:
            #                 info['file'] = os.path.join(root, menu+'.MEL')
            #                 if os.path.exists(info['file']):
            #                     info['type'] = 'mel'
            #                 else:
            #                     print('There is no module '+menu+' exist. Menu "'+menu+'" will not be created!')
            #                     info = None
            # else:
            #     baseFile = os.path.split(info['file'])[-1]
            #     info['file'] =  os.path.join(root, baseFile)
            #     if os.path.exists(info['file']):
            #         module, filesuffix = os.path.splitext(baseFile)
            #         info['type'] = self.ext2Type[filesuffix]
            #         if 'c' not in info:
            #             info['c'] = module+'.'+info['name']+'()'
            #     else:
            #         print('There is no file '+info['file']+' exist. Menu "'+menu+'" will not be created!')
            #         info = None
            #
            # if info:
            #     if 'c' not in info:
            #         info['c'] = menu+'.'+info['name']+'()'

        return info

    def analyzeSubmenu(self, subfilename):
        subfile = open(subfilename, 'r')
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

    def analyzeSubmenuFile(self, submenufilename):
        pass

    def createMenu(self):
        self.menus.clear()
        for root, dirs, files in os.walk(self.repositoryDest):
            parent = os.path.split(root)[-1]

            for menu in dirs:
                label = mel.eval('interToUI( "'+menu+'" )')
                if pm.menu( menu, ex=True ):
                    pm.deleteUI( menu )
                if parent==self.repositoryName:
                    mayaMainWin = mel.eval('$tempMelVar=$gMainWindow')
                    self.menus[menu]={'object': pm.menu( menu, l=label, p=mayaMainWin, to=True )}
                    self.menus[menu]['type'] = 'mainmenu'
                    if not self.mainMenu:
                        self.mainMenu = self.menus[menu]['object']
                else:
                    self.menus[menu]={'object': pm.menuItem( menu, sm=True, l=label, p=parent, to=True )}
                    self.menus[menu]['type'] = 'menu'
                self.menus[menu]['dir'] = os.path.join(root, menu)

            if not parent==self.repositoryName:
                for menufile in files:
                    menu, suffix = os.path.splitext(menufile)
                    if menu not in self.ignore_filename and suffix in self.menu_filetype:

                        #info = self.analyzeInfo( os.path.join(root, menufile) )
                        info = self.analyzeInfo(root, menu, suffix)

                        if info:
                            if info['type'] == 'submenu':
                                pass
                            else:
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

        # Update
        updateCmd = self.repositoryName+'_pipset.update()\n'
        updateCmd += self.pipelineStartup_py(refresh=True)
        #updateCmd += self.pipelineStartup_py(refresh=True)
        pm.menuItem('update', l='Update', c=updateCmd, p=parent)

        # Refresh
        refreshCmd = self.pipelineStartup_py(refresh=True)
        #refreshCmd += self.pipelineStartup_py(refresh=True)
        refreshCmd +=  "print 'Refreshed!'"
        pm.menuItem('refresh', l='Refresh', c=refreshCmd, p=parent)

        # Reinstall
        reinstallCmd = self.repositoryName+'_pipset.reinstall()\n'
        reinstallCmd += self.pipelineStartup_py(refresh=True)
        #reinstallCmd += self.pipelineStartup_py(refresh=True)
        pm.menuItem('reinstall', l='Reinstall', c=reinstallCmd, p=parent)

        # Uninstall
        uninstallCmd = self.repositoryName+'_pipset.uninstall()\n'
        pm.menuItem('uninstall', l='Uninstall', c=uninstallCmd, p=parent)
        pm.menuItem(divider=True, p=parent)

        # Update When Maya Startup
        updateWhenStartupMenu = pm.menuItem('updateWhenStart', l='Update When Maya Startup', cb=self.updateWhenStartup, p=parent)
        updateWhenStartCmd = 'update = pm.menuItem("'+updateWhenStartupMenu+'", q=True, cb=True)\n'
        updateWhenStartCmd += self.repositoryName+'_pipset.setUpdateWhenStartup(update)\n'
        updateWhenStartCmd += self.repositoryName+'_pipset.pipelineStartup_py()\n'
        pm.menuItem(updateWhenStartupMenu, e=True, c=updateWhenStartCmd)

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

    # def install3rd(self):
    #     the3rdSour = os.path.join(self.source, '3rd')
    #     the3rdDest = os.path.join(self.destination, '3rd')
    #     if not os.path.exists(the3rdDest):
    #         os.mkdir(the3rdDest)
    #
    #     for root, dirs, files in os.walk(the3rdSour):
    #         for the3rdfile in files:
    #             suffix = os.path.splitext(the3rdfile)[-1]
    #             if suffix in ['.py', '.PY', '.inf', '.INF', '.mel', '.MEL']:
    #                 shutil.copy(os.path.join(root, the3rdfile),\
    #                             os.path.join(the3rdDest, the3rdfile))

    def pipelineStartup_py(self, refresh=False):
        startupCmd = 'import sys\n'

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
        startupCmd += self.repositoryName+'_pipset.setUpdateWhenStartup(' + pm.encodeString(self.updateWhenStartup) + ')\n'

        if not refresh:
            if self.updateWhenStartup:
                startupCmd += self.repositoryName+'_pipset.update()\n'
            else:
                startupCmd += self.repositoryName+'_pipset.createMenu()\n'
                startupCmd += self.repositoryName+'_pipset.manageMenuItem()\n'

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
