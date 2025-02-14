

def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

def logModelio ():   
    ctx = modutils.getModelioContext()
    print("About Modelio")
    print(" version      = " + ctx.getVersion().toString())
    print(" language     = " + ctx.getLanguage())
    print(" workspace    = " + ctx.getWorkspacePath().toString())
    print(" project      = " + ctx.getProjectSpacePath().toString())
    print(" modelio path = " + ctx.getInstallPath().toString())

#Starting point
modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")
ormgen = Modelio.getInstance().getModuleService().getPeerModule("JavaOrmGenerator")
mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )
logModelio ()

oldpath=ormgen.getJavaGenerationPath  ()  
ormgen.cleanOrmInformationFromModel ()
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Retail", "Sprint1") )
useCases.add ( modutils.createPair ( "Finance", "Sprint1") )
ormgen.selectUmlArtefactsJavaFromUseCases  ( useCases )
newpath = modutils.getFullPathFromPrefixedPath( "$(Workspace)\\JavaApiSrv\\src\\main\\java" )
ormgen.setJavaGenerationPath  ( newpath )  
ormgen.deployApiInformationInModel ()
ormgen.executeJavaGeneration()
ormgen.setJavaGenerationPath  ( oldpath )  
ormgen.cleanOrmInformationFromModel ()
ormgen.selectAllUmlArtefactsJava ( False )
print "end api"