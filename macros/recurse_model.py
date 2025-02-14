

def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

#Starting point
modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")
mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )

def callbackpackage( element, namespace, packagename, description, userdata):
    return True

def callbackclass( element, namespace, clsname, description, userdata):
     return True
    
def callbackattribute (element, namespace, cls, clsname, attrname, typename, ismandatory, isarray, description, userdata):
    print clsname + "." + attrname
    return True



cartomgr.iterateModelAtRoot ( callbackpackage, callbackclass, callbackattribute, None, None, None )

