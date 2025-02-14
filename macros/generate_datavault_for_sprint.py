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

#Below the type mapping for Snowflake, feel free to adapt it for your own databae techno
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

genpath =  modutils.createFile ( modutils.markFileNameDate ( str(modutils.getWorkspacePath().getAbsolutePath()) + "\\datavault_generated\\retail_Finance_Sprint1" ) )
genpath.mkdirs()
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Retail", "Sprint1") )
#You may add as many datamesh/dataproduct/sprints you want
#useCases.add ( modutils.createPair ( "Finance", "Sprint1") )
mas = cartomgr.getArtefactsForUseCases ( useCases )

print genpath

for c in mas.getClasses():
    sthubname = modutils.getStereotypeInstValueString ( c.cls, modutils.getProjectStereotype ( "HUB_NAME" ), "Name" )
    hubname = modutils.getUpperSqlNameFromJavaName ( c.cls.getName () )
    if modutils.isNullOrEmptyString ( sthubname ) == False: hubname = sthubname
    if ( c.attributes.size() == 0 ): 
        print "HUB not created, no attributes => " + hubname
    else:
        f = modutils.createFile ( genpath.getAbsolutePath () + "\\HUB_" + hubname + ".ddl" )
        sb = modutils.createStringBuilder ()
        sb.append ( "create or replace TABLE HUB_" + hubname + " (\n" )
        sb.append ( "	HUB_" + hubname + "_HK VARCHAR(32),\n" )
        sb.append ( "	HUB_" + hubname + "_BK VARCHAR(32),\n" )
        sb.append ( "	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',\n" )
        sb.append ( "	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',\n" )
        sb.append ( "   constraint PK_HUB_" + hubname + " primary key (HUB_" + hubname + "_HK)\n" )
        sb.append ( ")" )
        desc = modutils.getDescription ( c.cls )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT = '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ";\n" )
        modutils.writeTextFile ( f, sb );
        print "HUB => " + f.getAbsolutePath ()
    f = modutils.createFile ( genpath.getAbsolutePath () + "\\SAT_" + hubname + ".ddl" )
    sb = modutils.createStringBuilder ()
    sb.append ( "create or replace TABLE SAT_" + hubname + " (\n" )
    sb.append ( "   HUB_" + hubname + "_HK VARCHAR(32),\n" )
    sb.append ( "   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',\n" )
    sb.append ( "   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',\n" )
    sb.append ( "   SAT_HASH_DIFF VARCHAR(32) NOT NULL,\n" )
    for a in c.attributes:
        stcolname = modutils.getStereotypeInstValueString ( a, modutils.getProjectStereotype ( "COL_NAME" ), "Name" )
        colname = modutils.getUpperSqlNameFromJavaName ( a.getName () )
        if modutils.isNullOrEmptyString ( stcolname ) == False: colname = stcolname
        sb.append ( "   " + colname + " " + dbtypemapping.findValueOrNull ( a.getType().getName() ) ) 
        desc = modutils.getDescription ( a )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ",\n" )
    sb.append ( "   constraint PK_SAT_" + hubname + " primary key (HUB_" + hubname + "_HK, SAT_LOAD_DTS),\n" )
    sb.append ( "   constraint FK_SAT_" + hubname + " foreign key (HUB_" + hubname + "_HK) references HUB_" + hubname + "(HUB_" + hubname + "_HK)\n" )
    sb.append ( ");\n" )
    modutils.writeTextFile ( f, sb );
    print "SAT => " + f.getAbsolutePath ()
    for a in c.associations:
        linkname = c.cls.getName () .upper () + "_" + a.getTarget ().getName () .upper () + "_" + a.getName () .upper ()
        hubtargetname = modutils.getUpperSqlNameFromJavaName ( a.getTarget () .getName () )
        f = modutils.createFile ( genpath.getAbsolutePath () + "\\LINK_" + linkname + ".ddl" )
        sb = modutils.createStringBuilder ()
        sb.append ( "create or replace TABLE LINK_" + linkname + " (\n" )
        sb.append ( "	LINK_" + linkname + "_HK VARCHAR(32),\n" )
        sb.append ( "	LINK_" + linkname + "_BK VARCHAR(32),\n" )
        sb.append ( "	LINK_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',\n" )
        sb.append ( "	LINK_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',\n" )
        sb.append ( "	HUB_" + hubname + "_HK VARCHAR(32),\n" )
        sb.append ( "	HUB_" + hubtargetname + "_HK VARCHAR(32),\n" )
        sb.append ( "   constraint PK_LINK_" + linkname + " primary key (LINK_" + linkname + "_HK),\n" )
        sb.append ( "   constraint FK_LINK_" + linkname + "_HUB_" + hubname + " foreign key (HUB_" + hubname + "_HK) references HUB_" + hubname + "(HUB_" + hubname + "_HK),\n" )
        sb.append ( "   constraint FK_LINK_" + linkname + "_HUB_" + hubtargetname + " foreign key (HUB_" + hubtargetname + "_HK) references HUB_" + hubtargetname + "(HUB_" + hubtargetname + "_HK)\n" )
        sb.append ( "" )
        sb.append ( ")" )
        desc = modutils.getDescription ( a )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ";\n" )
        modutils.writeTextFile ( f, sb );
        print "LINK => " + f.getAbsolutePath ()
   


print "End generate DataVault objects"