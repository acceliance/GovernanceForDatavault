create or replace TABLE SAT_PARTY (
   HUB_PARTY_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   PARTYID TEXT COMMENT 'Unique party identifier',   constraint PK_SAT_PARTY primary key (HUB_PARTY_HK, SAT_LOAD_DTS),
   constraint FK_SAT_PARTY foreign key (HUB_PARTY_HK) references HUB_PARTY(HUB_PARTY_HK)
);
