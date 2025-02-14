

def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

#Starting point
modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")
ormgen = Modelio.getInstance().getModuleService().getPeerModule("JavaOrmGenerator")
dvbgen = Modelio.getInstance().getModuleService().getPeerModule("DatavaultBuilderGenerator")
mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )

def callbackattribute (element, namespace, clsname, attrname, typename, ismandatory, isarray, description, userdata):
    if ( str(type(element)) != "<type 'org.modelio.metamodel.impl.uml.statik.AttributeImpl'>" ): return True # dont process if association (link)
    si = dvbgen.getSatelliteInformation ( element )
    sprint = modutils.getStereotypeInstValueString ( element, cartomgr.getStereotypeCartographieUsage (), "Extranet" ) #get extranet usage
    if ( si != None and sprint != None ):
#        si.satelliteName = "Extranet_" + sprint #set satellite name
#        dvbgen.setSatelliteInformation ( element, si )
        print "Set satellite name => " + clsname + "." + attrname + " = " "Extranet_" + sprint
    return True

tr = modutils.createTransaction ( "gendvb" )
#clean the model from any DVB information
dvbgen.removeAllUmlArtefactsDVB ()
#deploy DVB selection information from 
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Extranet", "sprint1") )
dvbgen.selectUmlArtefactsDVBFromUseCases ( useCases )
#now deploy sprint names into the stallite names so that the incremental DVB config will happen smoothly
#so this will support federal enterprise model down to the DVB instance or data mesh (per usage) instances
#cartomgr.iterateModelAtRoot ( None, None, callbackattribute, None, None, None )
#set the target path
oldpath=dvbgen.getConfigDatavaultBuilderPath  ()  
newpath = modutils.getFullPathFromPrefixedPath( "$(Workspace)\\DatavaultBuilder\\ModelRetail" )
dvbgen.setConfigDatavaultBuilderPath  ( newpath )  
#generate the DVB json files on disk
dvbgen.deployDVBConfiguration ()
#reset the path
dvbgen.setConfigDatavaultBuilderPath  ( oldpath )  
#dont memorize the selection
modutils.rollbackTransaction ( tr )
#modutils.closeTransaction ( tr )
