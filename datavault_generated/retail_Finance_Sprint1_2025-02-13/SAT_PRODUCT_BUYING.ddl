create or replace TABLE SAT_PRODUCT_BUYING (
   HUB_PRODUCT_BUYING_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   ID_LINE TEXT,
   NUMBER INTEGER COMMENT 'Number of items purchased',
   PRICE_PURCHASE FLOAT8 COMMENT 'Purchase price which can be negotiated with respect to the catalog price (sales, promotions, etc.)',
   AMOUNT_LINE FLOAT8,
   constraint PK_SAT_PRODUCT_BUYING primary key (HUB_PRODUCT_BUYING_HK, SAT_LOAD_DTS),
   constraint FK_SAT_PRODUCT_BUYING foreign key (HUB_PRODUCT_BUYING_HK) references HUB_PRODUCT_BUYING(HUB_PRODUCT_BUYING_HK)
);
