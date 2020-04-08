 ---------------------------------------------------------------
 --        Script Oracle.  
 ---------------------------------------------------------------


------------------------------------------------------------
-- Table: hippodromes
------------------------------------------------------------
CREATE TABLE hippodromes(
	localite  VARCHAR2 (60) NOT NULL  ,
	tel       VARCHAR2 (15)  ,
	CONSTRAINT hippodromes_PK PRIMARY KEY (localite)
);

------------------------------------------------------------
-- Table: courses
------------------------------------------------------------
CREATE TABLE courses(
	id_course  NUMBER NOT NULL ,
	libelle    VARCHAR2 (50) NOT NULL  ,
	quand      DATE  NOT NULL  ,
	terminee   NUMBER (1) NOT NULL  ,
	localite   VARCHAR2 (60) NOT NULL  ,
	CONSTRAINT courses_PK PRIMARY KEY (id_course),
	CONSTRAINT CHK_BOOLEAN_terminee CHECK (terminee IN (0,1))

	,CONSTRAINT courses_hippodromes_FK FOREIGN KEY (localite) REFERENCES hippodromes(localite)
);

------------------------------------------------------------
-- Table: personnes
------------------------------------------------------------
CREATE TABLE personnes(
	id_personne  NUMBER NOT NULL ,
	nom          VARCHAR2 (50) NOT NULL  ,
	prenom       VARCHAR2 (50) NOT NULL  ,
	passwd       VARCHAR2 (20)  ,
	ident        VARCHAR2 (15) UNIQUE ,
	CONSTRAINT personnes_PK PRIMARY KEY (id_personne)
);

------------------------------------------------------------
-- Table: chevaux
------------------------------------------------------------
CREATE TABLE chevaux(
	nom  VARCHAR2 (50) NOT NULL  ,
	CONSTRAINT chevaux_PK PRIMARY KEY (nom)
);

------------------------------------------------------------
-- Table: jockeys
------------------------------------------------------------
CREATE TABLE jockeys(
	id_personne  NUMBER(10,0)  NOT NULL  ,
	CONSTRAINT jockeys_PK PRIMARY KEY (id_personne)

	,CONSTRAINT jockeys_personnes_FK FOREIGN KEY (id_personne) REFERENCES personnes(id_personne)
);

------------------------------------------------------------
-- Table: tickets
------------------------------------------------------------
CREATE TABLE tickets(
	id_ticket    NUMBER NOT NULL ,
	nb_chevaux   NUMBER(10,0)  NOT NULL  ,
	desordre     NUMBER (1) NOT NULL  ,
	montant      NUMBER  NOT NULL  ,
	id_personne  NUMBER(10,0)  NOT NULL  ,
	CONSTRAINT tickets_PK PRIMARY KEY (id_ticket),
	CONSTRAINT CHK_BOOLEAN_desordre CHECK (desordre IN (0,1))

	,CONSTRAINT tickets_personnes_FK FOREIGN KEY (id_personne) REFERENCES personnes(id_personne)
);

------------------------------------------------------------
-- Table: dossards
------------------------------------------------------------
CREATE TABLE dossards(
	id_course    NUMBER(10,0)  NOT NULL  ,
	numero       NUMBER(10,0)  NOT NULL  ,
	arrivee      NUMBER(10,0)   ,
	nom          VARCHAR2 (50) NOT NULL  ,
	id_personne  NUMBER(10,0)  NOT NULL  ,
	CONSTRAINT dossards_PK PRIMARY KEY (id_course,numero)

	,CONSTRAINT dossards_courses_FK FOREIGN KEY (id_course) REFERENCES courses(id_course)
	,CONSTRAINT dossards_chevaux0_FK FOREIGN KEY (nom) REFERENCES chevaux(nom)
	,CONSTRAINT dossards_jockeys1_FK FOREIGN KEY (id_personne) REFERENCES jockeys(id_personne)
);

------------------------------------------------------------
-- Table: mise
------------------------------------------------------------
CREATE TABLE mise(
	id_course  NUMBER(10,0)  NOT NULL  ,
	numero     NUMBER(10,0)  NOT NULL  ,
	id_ticket  NUMBER(10,0)  NOT NULL  ,
	position   NUMBER(10,0)  NOT NULL  ,
	CONSTRAINT mise_PK PRIMARY KEY (id_course,numero,id_ticket)

	,CONSTRAINT mise_dossards_FK FOREIGN KEY (id_course,numero) REFERENCES dossards(id_course,numero)
	,CONSTRAINT mise_tickets0_FK FOREIGN KEY (id_ticket) REFERENCES tickets(id_ticket)
);


CREATE INDEX personnes_Idx ON personnes (ident);



CREATE SEQUENCE Seq_courses_id_course START WITH 1 INCREMENT BY 1 NOCYCLE;
CREATE SEQUENCE Seq_personnes_id_personne START WITH 1 INCREMENT BY 1 NOCYCLE;
CREATE SEQUENCE Seq_tickets_id_ticket START WITH 1 INCREMENT BY 1 NOCYCLE;


SET scan OFF;

CREATE OR REPLACE TRIGGER courses_id_course
	BEFORE INSERT ON courses 
  FOR EACH ROW 
	WHEN (NEW.id_course IS NULL) 
	BEGIN
		 select Seq_courses_id_course.NEXTVAL INTO :NEW.id_course from DUAL; 
	END;
/

CREATE OR REPLACE TRIGGER personnes_id_personne
	BEFORE INSERT ON personnes 
  FOR EACH ROW 
	WHEN (NEW.id_personne IS NULL) 
	BEGIN
		 select Seq_personnes_id_personne.NEXTVAL INTO :NEW.id_personne from DUAL; 
	END;
/

CREATE OR REPLACE TRIGGER tickets_id_ticket
	BEFORE INSERT ON tickets 
  FOR EACH ROW 
	WHEN (NEW.id_ticket IS NULL) 
	BEGIN
		 select Seq_tickets_id_ticket.NEXTVAL INTO :NEW.id_ticket from DUAL; 
	END;
/

COMMIT;
