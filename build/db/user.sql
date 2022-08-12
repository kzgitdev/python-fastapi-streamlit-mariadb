USE app;

DROP TABLE IF EXISTS actress;

CREATE TABLE actress(
  id int not null AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO actress(name)
VALUES (花岡エリカ), (川合勇), (澤田かおり), (藤森砂羽), (結城亮), (八木サダヲ), (吉崎竜也), (城咲俊介), (末永豊)
