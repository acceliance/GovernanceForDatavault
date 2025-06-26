create or replace TABLE SAT_PRODUCTBUYING (
   HUB_PRODUCTBUYING_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   IDLINE TEXT,   NUMBER INTEGER COMMENT 'Number of items purchased',   PRICEPURCHASE FLOAT8 COMMENT 'Purchase price which can be negotiated with respect to the catalog price (sales, promotions, etc.)',   AMOUNTLINE FLOAT8,   constraint PK_SAT_PRODUCTBUYING primary key (HUB_PRODUCTBUYING_HK, SAT_LOAD_DTS),
   constraint FK_SAT_PRODUCTBUYING foreign key (HUB_PRODUCTBUYING_HK) references HUB_PRODUCTBUYING(HUB_PRODUCTBUYING_HK)
);
