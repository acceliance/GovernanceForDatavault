create or replace TABLE SAT_CITY (
   HUB_CITY_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   CODE TEXT COMMENT 'City code',
   LABEL TEXT COMMENT 'City label',
   constraint PK_SAT_CITY primary key (HUB_CITY_HK, SAT_LOAD_DTS),
   constraint FK_SAT_CITY foreign key (HUB_CITY_HK) references HUB_CITY(HUB_CITY_HK)
);
