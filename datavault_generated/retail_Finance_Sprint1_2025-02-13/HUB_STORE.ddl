create or replace TABLE HUB_STORE (
	HUB_STORE_HK VARCHAR(32),
	HUB_STORE_BK VARCHAR(32),
	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   constraint PK_HUB_STORE primary key (HUB_STORE_HK)
) COMMENT = 'The physical store welcoming physical person customers';
