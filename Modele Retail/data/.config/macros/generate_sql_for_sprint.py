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

dbtypemapping = modutils.createKeyedList ()
dbtypemapping.addValue( modutils.getUMLType ("boolean" ).getName(), "BOOLEAN" )
dbtypemapping.addValue( modutils.getUMLType ("byte" ).getName(), "TINYINT" )
dbtypemapping.addValue( modutils.getUMLType ("char" ).getName(), "CHAR" )
dbtypemapping.addValue( modutils.getUMLType ("date" ).getName(), "DATETIME" )
dbtypemapping.addValue( modutils.getUMLType ("double" ).getName(), "FLOAT8" )
dbtypemapping.addValue( modutils.getUMLType ("float" ).getName(), "FLOAT4" )
dbtypemapping.addValue( modutils.getUMLType ("integer" ).getName(), "INTEGER" )
dbtypemapping.addValue( modutils.getUMLType ("long" ).getName(), "INTEGER" )
dbtypemapping.addValue( modutils.getUMLType ("short" ).getName(), "SMALLINT" )
dbtypemapping.addValue( modutils.getUMLType ("string" ).getName(), "TEXT" )
	

print "Start generate DataVault objects"

genpath =  modutils.createFile ( modutils.markFileNameDate ( str(modutils.getWorkspacePath()) + "\\sql\\Integrated Margin Referentials" ) )
genpath.mkdirs()
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Integrated Margin", "Sprint1 Ref Canaux Distribution") )
afuc = cartomgr.getArtefactsForUseCases ( useCases )

print genpath

for c in afc.getClasses():
    sqltablename = modutils.getStereotypeInstValueString ( c.cls, modutils.getProjectStereotype ( "SQL" ), "TableName" )
    tablename = modutils.getUpperSqlNameFromJavaName ( c.cls.getName () )
    if modutils.isNullOrEmptyString ( sqltablename ) == False: tablename = sqltablename
    f = modutils.createFile ( genpath.getAbsolutePath () + "\\TABLE_" + tablename + ".ddl" )
    sb = modutils.createStringBuilder ()
    sb.append ( "create or replace TABLE " + tablename )
    desc = modutils.getDescription ( c.cls )
    if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT = '" + modutils.cleanForSqlComment ( desc ) + "' " )
    sb.append ( "(\r" )
    for a in c.attributes:
        colprefix = modutils.getStereotypeInstValueString ( a, modutils.getProjectStereotype ( "SatelliteColumn" ), "Prefix" )
        colname = modutils.getUpperSqlNameFromJavaName ( a.getName () )
        #if modutils.isNullOrEmptyString ( colprefix ) == False: colname = colprefix + "_" + colname
        sb.append ( "   " + colname + " " + dbtypemapping.findValueOrNull ( a.getType().getName() ) ) 
        desc = modutils.getDescription ( a )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ",\r" )
    for a in c.associations:
        colname = modutils.getUpperSqlNameFromJavaName ( a.getName () )
        sb.append ( "   " + colname + "_CODE " + dbtypemapping.findValueOrNull ( "string" ) ) 
        desc = modutils.getDescription ( a )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ",\r" )
    il = sb.lastIndexOf ( ",\r" )    
    if il != -1: sb.deleteCharAt ( il )
    sb.append ( ")\r" )
    modutils.writeTextFile ( f, sb );    
    print "TABLE => " + f.getAbsolutePath ()
    

