from java.lang import *
import os    
from org.eclipse.swt.graphics import Color, Image
from org.eclipse.swt.widgets import Display
reload(sys)
sys.setdefaultencoding('utf-8')

def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")
ormgen = Modelio.getInstance().getModuleService().getPeerModule("JavaOrmGenerator")
mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )


useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Extranet", "sprint1") )
afc = cartomgr.getArtefactsForUseCases ( useCases )
for c in afc.getClasses():
    print c.getName ()
    for a in c.attributes
        print c + "." + a

