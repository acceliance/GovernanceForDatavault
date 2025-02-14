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

genpath =  modutils.createFile ( modutils.markFileNameDate ( str(modutils.getWorkspacePath()) + "\\datavault_gen\\Integrated Margin Sprint1 Ref Canaux Distribution" ) )
genpath.mkdirs()
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Retail", "Sprint1") )
useCases.add ( modutils.createPair ( "Finance", "Sprint1") )
afuc = cartomgr.getArtefactsForUseCases ( useCases )

print genpath

for c in afc.getClasses():
    #hubname = modutils.getStereotypeInstValueString ( c, modutils.getProjectStereotype ( "HUB_NAME" ), "Name" )
    hubname = modutils.getUpperSqlNameFromJavaName ( c.getName () )
    if ( afuc.getAttributesFromClass ( c )  .getEntries().size() == 0 ):
        print "HUB not created, no attributes => " + hubname
    else:
        f = modutils.createFile ( genpath.getAbsolutePath () + "\\HUB_" + hubname + ".ddl" )
        sb = modutils.createStringBuilder ()
        sb.append ( "create or replace TABLE HUB_" + hubname + " (\r" )
        sb.append ( "	HUB_" + hubname + "_HK VARCHAR(32),\r" )
        sb.append ( "	HUB_" + hubname + "_BK VARCHAR(32),\r" )
        sb.append ( "	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',\r" )
        sb.append ( "	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',\r" )
        sb.append ( "	HUB_ETL_JOB VARCHAR(150) NOT NULL COMMENT 'ETL Source',\r" )
        sb.append ( "   constraint PK_HUB_" + hubname + " primary key (HUB_" + hubname + "_HK)\r" )
        sb.append ( ")" )
        desc = modutils.getDescription ( c )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT = '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ";\r" )
        modutils.writeTextFile ( f, sb );
        print "HUB => " + f.getAbsolutePath ()
    f = modutils.createFile ( genpath.getAbsolutePath () + "\\SAT_" + hubname + ".ddl" )
    sb = modutils.createStringBuilder ()
    sb.append ( "create or replace TABLE SAT_" + hubname + " (\r" )
    sb.append ( "   HUB_" + hubname + "_HK VARCHAR(32),\r" )
    sb.append ( "   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',\r" )
    sb.append ( "   SAT_LOAD_END_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time End',\r" )
    sb.append ( "   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',\r" )
    sb.append ( "   SAT_ETL_JOB VARCHAR(150) NOT NULL COMMENT 'ETL Source',\r" )
    sb.append ( "   SAT_HASH_DIFF VARCHAR(32) NOT NULL,\r" )
    for a in afuc.getAttributesFromClass ( c ).getValuesArray():
        #colname = modutils.getStereotypeInstValueString ( a, modutils.getProjectStereotype ( "COL_NAME" ), "Name" )
        colprefix = modutils.getStereotypeInstValueString ( a, modutils.getProjectStereotype ( "SatelliteColumn" ), "Prefix" )
        colname = modutils.getUpperSqlNameFromJavaName ( a.getName () )
        if modutils.isNullOrEmptyString ( colprefix ) == False: colname = colprefix + "_" + colname
        sb.append ( "   " + colname + " " + dbtypemapping.findValueOrNull ( a.getType().getName() ) ) 
        desc = modutils.getDescription ( a )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ",\r" )
    sb.append ( "   constraint PK_SAT_" + hubname + " primary key (HUB_" + hubname + "_HK, SAT_LOAD_DTS),\r" )
    sb.append ( "   constraint FK_SAT_" + hubname + " foreign key (HUB_" + hubname + "_HK) references HUB_" + hubname + "(HUB_" + hubname + "_HK)\r" )
    sb.append ( ");\r" )
    modutils.writeTextFile ( f, sb );
    print "SAT => " + f.getAbsolutePath ()
    for a in afuc.getAssociationEndsFromClass ( c ).getValuesArray():
        #linkname = modutils.getStereotypeInstValueString ( a, modutils.getProjectStereotype ( "LINK_NAME" ), "Name" )
        linkname = c.getName () .upper () + "_" + a.getTarget ().getName () .upper () + "_" + a.getName () .upper ()
        #hubtargetname = modutils.getStereotypeInstValueString ( a.getTarget(), modutils.getProjectStereotype ( "HUB_NAME" ), "Name" )
        hubtargetname = modutils.getUpperSqlNameFromJavaName ( a.getTarget () .getName () )
        f = modutils.createFile ( genpath.getAbsolutePath () + "\\LINK_" + linkname + ".ddl" )
        sb = modutils.createStringBuilder ()
        sb.append ( "create or replace TABLE LINK_" + linkname + " (\r" )
        sb.append ( "	LINK_" + linkname + "_HK VARCHAR(32),\r" )
        sb.append ( "	LINK_" + linkname + "_BK VARCHAR(32),\r" )
        sb.append ( "	LINK_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',\r" )
        sb.append ( "	LINK_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',\r" )
        sb.append ( "	LINK_ETL_JOB VARCHAR(150) NOT NULL COMMENT 'ETL Source',\r" )
        sb.append ( "	HUB_" + hubname + "_HK VARCHAR(32),\r" )
        sb.append ( "	HUB_" + hubtargetname + "_HK VARCHAR(32),\r" )
        sb.append ( "   constraint PK_LINK_" + linkname + " primary key (LINK_" + linkname + "_HK),\r" )
        sb.append ( "   constraint FK_LINK_" + linkname + "_HUB_" + hubname + " foreign key (HUB_" + hubname + "_HK) references HUB_" + hubname + "(HUB_" + hubname + "_HK),\r" )
        sb.append ( "   constraint FK_LINK_" + linkname + "_HUB_" + hubtargetname + " foreign key (HUB_" + hubtargetname + "_HK) references HUB_" + hubtargetname + "(HUB_" + hubtargetname + "_HK)\r" )
        sb.append ( "" )
        sb.append ( ")" )
        desc = modutils.getDescription ( a )
        if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ";\r" )
        modutils.writeTextFile ( f, sb );
        print "LINK => " + f.getAbsolutePath ()
   


