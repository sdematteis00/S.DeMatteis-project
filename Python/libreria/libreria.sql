CREATE database mydata;
use mydata;
CREATE TABLE library_member (
  membertype VARCHAR(255) NOT NULL,
  prnno VARCHAR(255) NOT NULL PRIMARY KEY,
  ID VARCHAR(255),
  firstname VARCHAR(255),
  lastname VARCHAR(255) ,
  address1 VARCHAR(255) ,
  address2 VARCHAR(255),
  postcode VARCHAR(255),
  mobile VARCHAR(255),
  bookid VARCHAR(255),
  booktitle VARCHAR(255),
  author VARCHAR(255),
  borrowdate VARCHAR(255),
  duedate VARCHAR(255),
  loanperiod VARCHAR(255),
  latereturnfine VARCHAR(255),
  overduedate VARCHAR(255),
  actualprice VARCHAR(255)
);
