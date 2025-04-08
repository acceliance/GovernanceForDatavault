create or replace TABLE SAT_PARTY_EXTENSIONS (
   HUB_PARTY_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   BIRTH_DATE TEXT COMMENT 'Date of birth of the person, used for promotional and statistical purposes',   constraint PK_SAT_PARTY_EXTENSIONS primary key (HUB_PARTY_HK, SAT_LOAD_DTS),
   constraint FK_SAT_PARTY_EXTENSIONS foreign key (HUB_PARTY_HK) references HUB_PARTY(HUB_PARTY_HK)
);
