create or replace TABLE SAT_TICKET (
   HUB_TICKET_HK VARCHAR(32),
   SAT_LOAD_DTS TIMESTAMP_NTZ(9) NOT NULL COMMENT 'Load Time',
   SAT_REC_SRC VARCHAR(50) NOT NULL COMMENT 'Application Source',
   SAT_HASH_DIFF VARCHAR(32) NOT NULL,
   TICKET_ID TEXT,
   DATE_TICKET TEXT COMMENT 'Ticket date',
   TOTAL_AMOUNT FLOAT8 COMMENT 'Total amount of the ticket including tax',
   constraint PK_SAT_TICKET primary key (HUB_TICKET_HK, SAT_LOAD_DTS),
   constraint FK_SAT_TICKET foreign key (HUB_TICKET_HK) references HUB_TICKET(HUB_TICKET_HK)
);
