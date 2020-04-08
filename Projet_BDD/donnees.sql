-- A exécuter EN TANT QUE SCRIPT dans votre base
--
--
-- chevaux et jockeys

insert into chevaux(nom) values ('AGI DE CRENNES');
insert into chevaux(nom) values ('AGUERO DE JOUDES');
insert into chevaux(nom) values ('AMIE D''ANDY');
insert into chevaux(nom) values ('ARAGORN D''ALALIA');
insert into chevaux(nom) values ('ARCADIA');
insert into chevaux(nom) values ('ARCHANGEL AM');
insert into chevaux(nom) values ('ATOUT DU HAINAUT');
insert into chevaux(nom) values ('AURA NORMANDE');
insert into chevaux(nom) values ('BAGDAD CAFE');
insert into chevaux(nom) values ('BANDIT D''AINAY');
insert into chevaux(nom) values ('BAROJA');
insert into chevaux(nom) values ('BIALCO');
insert into chevaux(nom) values ('BLACK ATOUT');
insert into chevaux(nom) values ('BLACK NIGHT');
insert into chevaux(nom) values ('BLUE STORY');
insert into chevaux(nom) values ('BOCCACCIO');
insert into chevaux(nom) values ('C D''ARGENT');
insert into chevaux(nom) values ('DARASSO');
insert into chevaux(nom) values ('DARYASI');
insert into chevaux(nom) values ('DIAMOND CHARM');
insert into chevaux(nom) values ('DOGRA MAGRA');
insert into chevaux(nom) values ('DONUTS REYOR');
insert into chevaux(nom) values ('IT''S JENNIFER');
insert into chevaux(nom) values ('JANIKA');
insert into chevaux(nom) values ('MAX''S SPIRIT');
insert into chevaux(nom) values ('MEZIDON');
insert into chevaux(nom) values ('NICE TO SEE YOU');
insert into chevaux(nom) values ('OLYMPIC TORCH');
insert into chevaux(nom) values ('THE GOLDEN BOY');
insert into chevaux(nom) values ('VALFLEURY');
insert into chevaux(nom) values ('VARCOROSO');
insert into chevaux(nom) values ('VERTIGINOUS');
insert into chevaux(nom) values ('VIVIEN PEO');
insert into chevaux(nom) values ('VOCEAN DU JAAR');
insert into chevaux(nom) values ('YKAR');
insert into personnes(prenom,nom) values ('A.','BARRIER');
insert into personnes(prenom,nom) values ('A.','CRASTUS');
insert into personnes(prenom,nom) values ('A.','GASNIER');
insert into personnes(prenom,nom) values ('A.','HAMELIN');
insert into personnes(prenom,nom) values ('A.','LAURENT');
insert into personnes(prenom,nom) values ('ALXI.','ACKER');
insert into personnes(prenom,nom) values ('C.','DUVALDESTIN');
insert into personnes(prenom,nom) values ('D.','LOCQUENEUX');
insert into personnes(prenom,nom) values ('E.','CHAZELLE');
insert into personnes(prenom,nom) values ('E.','HARDOUIN');
insert into personnes(prenom,nom) values ('E.','LAMBERTZ');
insert into personnes(prenom,nom) values ('E.','RAFFIN');
insert into personnes(prenom,nom) values ('F.','NIVARD');
insert into personnes(prenom,nom) values ('G.','MASURE');
insert into personnes(prenom,nom) values ('J. M.','BAZIRE');
insert into personnes(prenom,nom) values ('J. P.','MAILLARD');
insert into personnes(prenom,nom) values ('J.','PLOUGANOU');
insert into personnes(prenom,nom) values ('J.','RICOU');
insert into personnes(prenom,nom) values ('JL.','BEAUNEZ');
insert into personnes(prenom,nom) values ('K.','NABET');
insert into personnes(prenom,nom) values ('M.','BARZALONA');
insert into personnes(prenom,nom) values ('M.','FARCINADE');
insert into personnes(prenom,nom) values ('M.','GUYON');
insert into personnes(prenom,nom) values ('M.','MOTTIER');
insert into personnes(prenom,nom) values ('P. Y.','VERVA');
insert into personnes(prenom,nom) values ('P.','CARBERRY');
insert into personnes(prenom,nom) values ('P.','LEVESQUE');
insert into personnes(prenom,nom) values ('PH.','DAUGEARD');
insert into personnes(prenom,nom) values ('R.','DERIEUX');
insert into personnes(prenom,nom) values ('R.','SCHMIDLIN');
insert into personnes(prenom,nom) values ('S.','COSSART');
insert into personnes(prenom,nom) values ('T.','BACHELOT');
insert into personnes(prenom,nom) values ('T.','PICCONE');
insert into personnes(prenom,nom) values ('T.','VIEL');

-- toutes les personnes sont des jockeys
insert into jockeys(id_personne) (select id_personne from personnes);

-- hippodromes
insert into hippodromes(localite,tel) values ('Auteuil', '01 40 71 47 47');
insert into hippodromes(localite,tel) values ('Enghien-Soisy', '01 34 17 87 00');
insert into hippodromes(localite,tel) values ('Saint-Cloud', '01 47 71 69 26');
insert into hippodromes(localite,tel) values ('Vincennes', '01 49 77 17 17');

-- courses
insert into courses(terminee,libelle,quand,localite) values (1,'PRIX GUILLAUME DE PRACOMTAL',to_date('03/10/17','DD/MM/YY'),'Auteuil');
insert into courses(terminee,libelle,quand,localite) values (1,'PRIX ANDRE ADELE TROU AUX BICHES BEACHCOMBER',to_date('08/10/17','DD/MM/YY'),'Auteuil');
insert into courses(terminee,libelle,quand,localite) values (1,'PRIX DES GOBELINS',to_date('16/10/17','DD/MM/YY'),'Enghien-Soisy');
insert into courses(terminee,libelle,quand,localite) values (0,'PRIX DES BOUCLES DE LA SEINE',to_date('15/11/17','DD/MM/YY'),'Saint-Cloud');
insert into courses(terminee,libelle,quand,localite) values (0,'PRIX BARBARA',to_date('18/11/17','DD/MM/YY'),'Vincennes');

-- résultats

insert into dossards (id_course,arrivee,numero,nom,id_personne) values (1,1,14,'DARASSO',(select id_personne from personnes where nom='COSSART'));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (1,2,16,'JANIKA',(select id_personne from personnes where nom='NABET' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (1,3,2,'DARYASI',(select id_personne from personnes where nom='SCHMIDLIN' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (1,4,4,'MAX''S SPIRIT',(select id_personne from personnes where nom='PLOUGANOU' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (1,5,8,'OLYMPIC TORCH',(select id_personne from personnes where nom='BEAUNEZ' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (1,6,10,'DOGRA MAGRA',(select id_personne from personnes where nom='FARCINADE' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (1,7,6,'THE GOLDEN BOY',(select id_personne from personnes where nom='RICOU' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (2,1,14,'BANDIT D''AINAY',(select id_personne from personnes where nom='ACKER' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (2,2,12,'YKAR',(select id_personne from personnes where nom='VIEL' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (2,3,13,'DIAMOND CHARM',(select id_personne from personnes where nom='CHAZELLE' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (2,4,11,'IT''S JENNIFER',(select id_personne from personnes where nom='CARBERRY' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (2,5,8,'ARAGORN D''ALALIA',(select id_personne from personnes where nom='MASURE' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (2,6,2,'BAGDAD CAFE',(select id_personne from personnes where nom='PLOUGANOU' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (2,7,1,'BIALCO',(select id_personne from personnes where nom='GASNIER' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (3,1,1,'BLACK ATOUT',(select id_personne from personnes where nom='MOTTIER' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (3,2,2,'BLUE STORY',(select id_personne from personnes where nom='LEVESQUE' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (3,3,14,'VIVIEN PEO',(select id_personne from personnes where nom='BARRIER' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (3,4,3,'BOCCACCIO',(select id_personne from personnes where nom='NIVARD' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (3,5,6,'ARCHANGEL AM',(select id_personne from personnes where nom='LOCQUENEUX' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (3,6,9,'VERTIGINOUS',(select id_personne from personnes where nom='DAUGEARD' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (3,7,8,'AMIE D''ANDY',(select id_personne from personnes where nom='VERVA' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (4,1,13,'BLACK NIGHT',(select id_personne from personnes where nom='PICCONE' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (4,2,11,'BAROJA',(select id_personne from personnes where nom='BARZALONA' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (4,3,1,'NICE TO SEE YOU',(select id_personne from personnes where nom='HAMELIN' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (4,4,15,'MEZIDON',(select id_personne from personnes where nom='HARDOUIN' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (4,5,14,'C D''ARGENT',(select id_personne from personnes where nom='CRASTUS' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (4,6,16,'ARCADIA',(select id_personne from personnes where nom='BACHELOT' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (4,7,5,'DONUTS REYOR',(select id_personne from personnes where nom='GUYON' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (5,1,6,'AGI DE CRENNES',(select id_personne from personnes where nom='MAILLARD' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (5,2,1,'ATOUT DU HAINAUT',(select id_personne from personnes where nom='RAFFIN' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (5,3,3,'AGUERO DE JOUDES',(select id_personne from personnes where nom='LAURENT' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (5,4,8,'AURA NORMANDE',(select id_personne from personnes where nom='LAMBERTZ' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (5,5,14,'VALFLEURY',(select id_personne from personnes where nom='DUVALDESTIN' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (5,6,11,'VARCOROSO',(select id_personne from personnes where nom='DERIEUX' ));
insert into dossards (id_course,arrivee,numero,nom,id_personne) values (5,7,7,'VOCEAN DU JAAR',(select id_personne from personnes where nom='BAZIRE' ));

CREATE PROCEDURE inscrire(
    xnom VARCHAR(20) NOT NULL,
    xprenom VARCHAR(20) NOT NULL,
    xident VARCHAR(20),
    xpwd VARCHAR(15) NOT NULL
    );
BEGIN 
    insert into personnes(nom,prenom,ident,passwd) values (xnom,xprenom,xident,xpwd);
    COMMIT;
END