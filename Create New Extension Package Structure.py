import os, time

NewExtensionName = input('Specify new extension name: ')

AllExtensionsRootFolder = os.path.dirname(__file__)

NewExtensionRootPath = os.path.join(AllExtensionsRootFolder, NewExtensionName )
os.mkdir( NewExtensionRootPath )

CSXSFolderPath = os.path.join(NewExtensionRootPath, "CSXS")
JSPath = os.path.join(NewExtensionRootPath, "JS")
os.mkdir(CSXSFolderPath)
os.mkdir(JSPath)

ExtensionFolderStructureInfoFile = os.path.join(NewExtensionRootPath, NewExtensionName+"_Info.txt")
f = open(ExtensionFolderStructureInfoFile, 'w')
f.write("Extension folder structure created on: " + time.strftime("%Y %m %d %Hh%M")+ " by: "+ os.getlogin() )
f.close()


#Template for XML manifest taken from: https://medium.com/@HallgrimurTh/extending-adobe-cc-2014-apps-ba1d101e27da
# another example at: http://www.adobe.com/devnet/creativesuite/articles/a-short-guide-to-HTML5-extensions.html#fn-apps-supported

ManifestFileContent = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<ExtensionManifest ExtensionBundleId="com.example.helloworld" ExtensionBundleName="Hello world" ExtensionBundleVersion="1.0" Version="4.0">
	<ExtensionList>
		<Extension Id="com.example.helloworld.extension" Version="1.0"/>
	</ExtensionList>
	<ExecutionEnvironment>
		<HostList>			
			<Host Name="IDSN" Version="[10.0,20.0]"/>
		</HostList>
		<LocaleList>
			<Locale Code="All"/>
		</LocaleList>
		<RequiredRuntimeList>
			<RequiredRuntime Name="CSXS" Version="7.0"/>
		</RequiredRuntimeList>
	</ExecutionEnvironment>
	<DispatchInfoList>
		<Extension Id="com.example.helloworld.extension">
			<DispatchInfo>
				<Resources>
					<MainPath>./index.html</MainPath>
				</Resources>
				<UI>
					<Type>Panel</Type>
					<Menu>Hello world</Menu>
					<Geometry>
						<Size>
							<Height>400</Height>
							<Width>400</Width>
						</Size>
					</Geometry>
				</UI>
			</DispatchInfo>
		</Extension>
	</DispatchInfoList>
</ExtensionManifest>"""

ManifestFilePath = os.path.join(CSXSFolderPath, "Manifest.xml")
f = open(ManifestFilePath, 'w')
f.write(ManifestFileContent)
f.close()

htmlFileContent = """<!doctype html>
<html>
<body>
<div>This little div is sooo coool!</div>
	<button id="btn">Click me!</button>
</body>
</html>
"""


IndexFilePath = os.path.join(NewExtensionRootPath, "Index.html")
f = open(IndexFilePath, 'w')
f.write(htmlFileContent)
f.close()

debugFileContent = """<?xml version="1.0" encoding="UTF-8"?> 
<ExtensionList>
    <Extension Id="com.example.helloworld.extension">
        <HostList>
           <Host Name="IDSN" Port="8069"/> 
        </HostList>
    </Extension>
</ExtensionList>"""


DebugPortSpecifyFile = os.path.join(NewExtensionRootPath, ".debug")
f = open(DebugPortSpecifyFile, 'w')
f.write(debugFileContent)
f.close()
