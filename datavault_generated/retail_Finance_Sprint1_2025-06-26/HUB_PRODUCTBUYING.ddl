create or replace TABLE HUB_PRODUCTBUYING (
	HUB_PRODUCTBUYING_HK VARCHAR(32),
	HUB_PRODUCTBUYING_BK VARCHAR(32),
	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   constraint PK_HUB_PRODUCTBUYING primary key (HUB_PRODUCTBUYING_HK)
) COMMENT = 'Contextualization of the act of purchasing the product by specifying the negotiated price and the quantity. This business object is used to manage profitability indicators.';
