create or replace TABLE HUB_PRODUCT_BUYING (
	HUB_PRODUCT_BUYING_HK VARCHAR(32),
	HUB_PRODUCT_BUYING_BK VARCHAR(32),
	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   constraint PK_HUB_PRODUCT_BUYING primary key (HUB_PRODUCT_BUYING_HK)
) COMMENT = 'Contextualization of the act of purchasing the product by specifying the negotiated price and the quantity. This business object is used to manage profitability indicators.';
