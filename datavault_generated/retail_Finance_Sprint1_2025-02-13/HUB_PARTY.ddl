create or replace TABLE HUB_PARTY (
	HUB_PARTY_HK VARCHAR(32),
	HUB_PARTY_BK VARCHAR(32),
	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   constraint PK_HUB_PARTY primary key (HUB_PARTY_HK)
) COMMENT = 'The person represents any third party in a commercial or business relationship';
