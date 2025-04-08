create or replace TABLE HUB_PRODUCT (
	HUB_PRODUCT_HK VARCHAR(32),
	HUB_PRODUCT_BK VARCHAR(32),
	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   constraint PK_HUB_PRODUCT primary key (HUB_PRODUCT_HK)
) COMMENT = 'The product offered for sale with its own characteristics as well as standard pricing (excluding promotion or other)';
