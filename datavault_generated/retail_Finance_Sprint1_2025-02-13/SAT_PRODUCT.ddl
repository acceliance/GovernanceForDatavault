create or replace TABLE SAT_PRODUCT (
   HUB_PRODUCT_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   CODE TEXT COMMENT 'Product code',
   LABEL TEXT COMMENT 'Product label',
   CATALOG_PRICE FLOAT8 COMMENT 'List price of the product. This data is established by marketing',
   constraint PK_SAT_PRODUCT primary key (HUB_PRODUCT_HK, SAT_LOAD_DTS),
   constraint FK_SAT_PRODUCT foreign key (HUB_PRODUCT_HK) references HUB_PRODUCT(HUB_PRODUCT_HK)
);
