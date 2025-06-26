create or replace TABLE HUB_TICKET (
	HUB_TICKET_HK VARCHAR(32),
	HUB_TICKET_BK VARCHAR(32),
	HUB_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
	HUB_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   constraint PK_HUB_TICKET primary key (HUB_TICKET_HK)
) COMMENT = 'The ticket or receipt represents the act of purchase in store or digitally. It can be attached to the physical person customer in the store if the latter presents his loyalty card.';
