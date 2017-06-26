#Template for XML manifest taken from: https://medium.com/@HallgrimurTh/extending-adobe-cc-2014-apps-ba1d101e27da
# another example at: http://www.adobe.com/devnet/creativesuite/articles/a-short-guide-to-HTML5-extensions.html#fn-apps-supported

import os, time
from shutil import copyfile

class Folder:
	"""This class will will keep target paths for new folders"""
	def __init__(self, rootPath, folderName="."):		
		self.path = os.path.join(rootPath, folderName)
		os.mkdir(self.path)
		print("Created folder: " + self.path)

class CEPProject:
	"""This class will create an initial folder structure for your Adoobe application CEP extension. 
	It will copy common libraries (such as CSInterface.js) and create initial .js files to get you going quickly.
	"""

	def __init__(self):
		self.installerPath = os.path.dirname(__file__)
		self.extensionsFolder = os.path.join( self.installerPath, "..")
		self.AskQuestions()		
		self.foldersToCreateNames = ["js", "css", "host", "CSXS"]
		self.Folders = []		
		self.CreateFolders()
		self.CreateREADME()
		self.CopyInitialExtensionFiles()

	def AskQuestions(self):
		newExtensionName = input('Specify new extension name: ')
		if( newExtensionName == ""):
			print("Extension name must be specified")
			exit()
		else:
			self.newExtensionName = newExtensionName
			self.extensionRootFolder = os.path.join(self.extensionsFolder, self.newExtensionName)		

	def NewFolder(self, rootFolder, newFolderName ):
		self.Folders.append(Folder(rootFolder, newFolderName ))
		return self.Folders[-1]

	def CreateRootFolder(self):		
		self.extensionRootFolder = self.NewFolder( self.extensionsFolder, self.newExtensionName )

	def CreateFolders(self):
		print("\n\n")
		self.CreateRootFolder()
		for folder in self.foldersToCreateNames:
		 	self.NewFolder(self.extensionRootFolder.path, folder )
		print("\n\n")		

	def CreateREADME(self):
		ExtensionFolderStructureInfoFile = os.path.join( self.extensionRootFolder.path, self.newExtensionName+"_README.txt")
		f = open(ExtensionFolderStructureInfoFile, 'w')
		f.write("Extension folder structure created on: " + time.strftime("%Y %m %d %Hh%M")+ " by: "+ os.getlogin() )
		f.close()

	def CopyInitialExtensionFiles(self):		
		self.CopyFile( os.path.join(self.installerPath , "Resources", "manifest.xml"),  os.path.join(self.extensionRootFolder.path, "CSXS", "manifest.xml"))
		self.CopyFile( os.path.join(self.installerPath , "Resources", "index.html"),  os.path.join(self.extensionRootFolder.path, "index.html" ) )
		self.CopyFile( os.path.join(self.installerPath , "Resources", ".debug"),  os.path.join(self.extensionRootFolder.path, ".debug") )
		self.CopyFile( os.path.join(self.installerPath , "Resources", "CSInterface.js"),  os.path.join(self.extensionRootFolder.path, "js", "CSInterface.js"))
		self.CopyFile( os.path.join(self.installerPath , "Resources", "main.js"),  os.path.join(self.extensionRootFolder.path, "js", "main.js"))

	def CopyFile(self, src, dst):
		print("Copying file: " +src +"\n to " + dst+"\n\n")
		copyfile(src, dst)


a = CEPProject()