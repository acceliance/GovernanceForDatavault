create or replace TABLE SAT_STORE (
   HUB_STORE_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   CODE TEXT COMMENT 'Store code',
   LABEL TEXT COMMENT 'Store label',
   constraint PK_SAT_STORE primary key (HUB_STORE_HK, SAT_LOAD_DTS),
   constraint FK_SAT_STORE foreign key (HUB_STORE_HK) references HUB_STORE(HUB_STORE_HK)
);
