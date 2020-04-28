create sequence seq_user
start with 1
increment 1;

select nextval('seq_user');

CREATE TABLE public."user" (
	id varchar primary key DEFAULT nextval('seq_user'::regclass),
	nom varchar NULL,
	prenom varchar NULL,
	email varchar NULL,
	mdp varchar NULL
)
WITH (
	OIDS=FALSE
) ;

create sequence seq_ecriture
start with 1
increment 1;

CREATE TABLE public.ecriture (
	id int8 primary key  DEFAULT nextval('seq_ecriture'::regclass),
	libelle varchar NULL,
	creele timestamp NULL,
	idjournal int8 NULL
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE public.userroles (
	username varchar NULL,
	rolename varchar NULL
)
WITH (
	OIDS=FALSE
) ;

create sequence seq_ligneecriture
start with 1
increment 1;

CREATE TABLE public.ligneecriture (
	id int8 primary key ,
	idEcriture int8 NULL,
	numeroCompte varchar NULL,
	montantDebit int8 NULL,
	montantCredit int8 NULL
)
WITH (
	OIDS=FALSE
) ;

CREATE TABLE public.typejournal (
	id int8 primary key ,
	libelle varchar NULL
)
WITH (
	OIDS=FALSE
) ;

create sequence seq_journal
start with 1
increment 1;

CREATE TABLE public.journal (
	id int8 primary key  DEFAULT nextval('seq_journal'::regclass),
	libelle varchar NULL,
	idTypeJournal int8 NULL
)
WITH (
	OIDS=FALSE
) ;

ALTER TABLE public."user" ADD datenaissance date NULL ;

CREATE TABLE public.compte (
	numero varchar primary key ,
	libelle varchar NULL,
	parent varchar NULL
)
WITH (
	OIDS=FALSE
) ;

insert into journal(libelle,idtypejournal) values ('Achat Janvier 2018',1);
insert into journal(libelle,idtypejournal) values ('Journal de banque Janvier 2018',2);

insert into compte(numero,libelle,parent) values ('1','COMPTES DE CAPITAUX','');
insert into compte(numero,libelle,parent) values ('10','Capital et réserves','1');
insert into compte(numero,libelle,parent) values ('101','Capital','10');
insert into compte(numero,libelle,parent) values ('104','Primes liées au capital social','10');
insert into compte(numero,libelle,parent) values ('105','Ecarts de réévaluation ','10');
insert into compte(numero,libelle,parent) values ('106','Réserves','10');
insert into compte(numero,libelle,parent) values ('107','Ecart d''équivalence','10');
insert into compte(numero,libelle,parent) values ('108','Compte de l''exploitant','10');
insert into compte(numero,libelle,parent) values ('109','Actionnaires : capital souscrit - non appelé ','10');
insert into compte(numero,libelle,parent) values ('11','Report à nouveau (solde créditeur ou débiteur) ','1');
insert into compte(numero,libelle,parent) values ('110','Report à nouveau (solde créditeur) ','11');
insert into compte(numero,libelle,parent) values ('119','Report à nouveau (solde débiteur) ','11');
insert into compte(numero,libelle,parent) values ('12','Résultat de l''exercice (bénéfice ou perte) ','1');
insert into compte(numero,libelle,parent) values ('120','Résultat de l''exercice (bénéfice) ','12');
insert into compte(numero,libelle,parent) values ('129','Résultat de l''exercice (perte) ','12');
insert into compte(numero,libelle,parent) values ('13','Subventions d''investissement','1');
insert into compte(numero,libelle,parent) values ('131','Subventions d''équipement','13');
insert into compte(numero,libelle,parent) values ('138','Autres subventions d''investissement (même ventilation que celle du compte 131) ','13');
insert into compte(numero,libelle,parent) values ('139','Subventions d''investissement inscrites au compte de résultat ','13');
insert into compte(numero,libelle,parent) values ('14','Provisions réglementées','1');
insert into compte(numero,libelle,parent) values ('142','Provisions réglementées relatives aux immobilisations ','14');
insert into compte(numero,libelle,parent) values ('143','Provisions réglementées relatives aux stocks ','14');
insert into compte(numero,libelle,parent) values ('144','Provisions réglementées relatives aux autres éléments de l''actif ','14');
insert into compte(numero,libelle,parent) values ('145','Amortissements dérogatoires','14');
insert into compte(numero,libelle,parent) values ('146','Provision spéciale de réévaluation ','14');
insert into compte(numero,libelle,parent) values ('147','Plus-values réinvesties ','14');
insert into compte(numero,libelle,parent) values ('148','Autres provisions réglementées ','14');
insert into compte(numero,libelle,parent) values ('15','Provisions pour risques et charges ','1');
insert into compte(numero,libelle,parent) values ('151','Provisions pour risques','15');
insert into compte(numero,libelle,parent) values ('153','Provisions pour pensions et obligations similaires ','15');
insert into compte(numero,libelle,parent) values ('154','Provisions pour restructurations ','15');
insert into compte(numero,libelle,parent) values ('155','Provisions pour impôts','15');
insert into compte(numero,libelle,parent) values ('156','Provisions pour renouvellement des immobilisations (entreprises concessionnaires) ','15');
insert into compte(numero,libelle,parent) values ('157','Provisions pour charges à répartir sur plusieurs exercices ','15');
insert into compte(numero,libelle,parent) values ('158','Autres provisions pour charges','15');
insert into compte(numero,libelle,parent) values ('16','Emprunts et dettes assimilées','1');
insert into compte(numero,libelle,parent) values ('161','Emprunts obligataires convertibles','16');
insert into compte(numero,libelle,parent) values ('163','Autres emprunts obligataires','16');
insert into compte(numero,libelle,parent) values ('164','Emprunts auprès des établissements de crédit ','16');
insert into compte(numero,libelle,parent) values ('165','Dépôts et cautionnements reçus ','16');
insert into compte(numero,libelle,parent) values ('166','Participation des salariés aux résultats ','16');
insert into compte(numero,libelle,parent) values ('167','Emprunts et dettes assortis de conditions particulières ','16');
insert into compte(numero,libelle,parent) values ('168','Autres emprunts et dettes assimilées ','16');
insert into compte(numero,libelle,parent) values ('169','Primes de remboursement des obligations ','16');
insert into compte(numero,libelle,parent) values ('17','Dettes rattachées à des participations ','1');
insert into compte(numero,libelle,parent) values ('171','Dettes rattachées à des participations (groupe) ','17');
insert into compte(numero,libelle,parent) values ('174','Dettes rattachées à des participations (hors groupe) ','17');
insert into compte(numero,libelle,parent) values ('178','Dettes rattachées à des sociétés en participation ','17');
insert into compte(numero,libelle,parent) values ('18','Comptes de liaison des établissements et sociétés en participation ','1');
insert into compte(numero,libelle,parent) values ('181','Comptes de liaison des établissements ','18');
insert into compte(numero,libelle,parent) values ('186','Biens et prestations de services échangés entre établissements (charges) ','18');
insert into compte(numero,libelle,parent) values ('187','Biens et prestations de services échangés entre établissements (produits) ','18');
insert into compte(numero,libelle,parent) values ('188','Comptes de liaison des sociétés en participation ','18');
insert into compte(numero,libelle,parent) values ('2','COMPTES D''IMMOBILISATIONS','');;
insert into compte(numero,libelle,parent) values ('20','Immobilisations incorporelles','2');
insert into compte(numero,libelle,parent) values ('201','Frais d''établissement','20');
insert into compte(numero,libelle,parent) values ('203','Frais de recherche et de développement ','20');
insert into compte(numero,libelle,parent) values ('205','Concessions et droits similaires, brevets, licences, marques, procédés, logiciels, droits et val','20');
insert into compte(numero,libelle,parent) values ('206','Droit au bail','20');
insert into compte(numero,libelle,parent) values ('207','Fonds commercial','20');
insert into compte(numero,libelle,parent) values ('208','Autres immobilisations incorporelles ','20');
insert into compte(numero,libelle,parent) values ('21','Immobilisations corporelles','2');
insert into compte(numero,libelle,parent) values ('211','Terrains ','21');
insert into compte(numero,libelle,parent) values ('212','Agencements et aménagements de terrains (même ventilation que celle du compte 211) ','21');
insert into compte(numero,libelle,parent) values ('213','Constructions','21');
insert into compte(numero,libelle,parent) values ('214','Constructions sur sol d''autrui (même ventilation que celle du compte 213) ','21');
insert into compte(numero,libelle,parent) values ('215','Installations techniques, matériels et outillage industriels ','21');
insert into compte(numero,libelle,parent) values ('218','Autres immobilisations corporelles','21');
insert into compte(numero,libelle,parent) values ('22','Immobilisations mises en concession','2');
insert into compte(numero,libelle,parent) values ('23','Immobilisations en cours','2');
insert into compte(numero,libelle,parent) values ('231','Immobilisations corporelles en cours','23');
insert into compte(numero,libelle,parent) values ('232','Immobilisations incorporelles en cours ','23');
insert into compte(numero,libelle,parent) values ('237','Avances et acomptes versés sur immobilisations incorporelles ','23');
insert into compte(numero,libelle,parent) values ('238','Avances et acomptes versés sur commandes d''immobilisations corporelles ','23');
insert into compte(numero,libelle,parent) values ('25','Parts dans des entreprises liées et créances sur des entreprises liées ','2');
insert into compte(numero,libelle,parent) values ('26','Participations et créances rattachées à des participations ','2');
insert into compte(numero,libelle,parent) values ('261','Titres de participation','26');
insert into compte(numero,libelle,parent) values ('266','Autres formes de participation ','26');
insert into compte(numero,libelle,parent) values ('267','Créances rattachées à des participations ','26');
insert into compte(numero,libelle,parent) values ('268','Créances rattachées à des sociétés en participation ','26');
insert into compte(numero,libelle,parent) values ('269','Versements restant à effectuer sur titres de participation non libérés ','26');
insert into compte(numero,libelle,parent) values ('27','Autres immobilisations financières ','2');
insert into compte(numero,libelle,parent) values ('271','Titres immobilisés autres que les titres immobilisés de l''activité de portefeuille (droit de pro','27');
insert into compte(numero,libelle,parent) values ('272','Titres immobilisés (droit de créance) ','27');
insert into compte(numero,libelle,parent) values ('273','Titres immobilisés de l''activité de portefeuille ','27');
insert into compte(numero,libelle,parent) values ('274','Prêts','27');
insert into compte(numero,libelle,parent) values ('275','Dépôts et cautionnements versés ','27');
insert into compte(numero,libelle,parent) values ('276','Autres créances immobilisées ','27');
insert into compte(numero,libelle,parent) values ('277','(Actions propres ou parts propres)','27');
insert into compte(numero,libelle,parent) values ('279','Versements restant à effectuer sur titres immobilisés non libérés ','27');
insert into compte(numero,libelle,parent) values ('28','Amortissements des immobilisations','2');
insert into compte(numero,libelle,parent) values ('280','Amortissements des immobilisations incorporelles ','28');
insert into compte(numero,libelle,parent) values ('281','Amortissements des immobilisations corporelles ','28');
insert into compte(numero,libelle,parent) values ('282','Amortissements des immobilisations mises en concession ','28');
insert into compte(numero,libelle,parent) values ('29','Dépréciations des immobilisations ','2');
insert into compte(numero,libelle,parent) values ('290','Dépréciations des immobilisations incorporelles ','29');
insert into compte(numero,libelle,parent) values ('291','Dépréciations des immobilisations corporelles (même ventilation que celle du compte 21) ','29');
insert into compte(numero,libelle,parent) values ('292','Dépréciations des immobilisations mises en concession ','29');
insert into compte(numero,libelle,parent) values ('293','Dépréciations des immobilisations en cours ','29');
insert into compte(numero,libelle,parent) values ('296','Provisions pour dépréciation des participations et créances rattachées à des participations ','29');
insert into compte(numero,libelle,parent) values ('297','Provisions pour dépréciation des autres immobilisations financières ','29');
insert into compte(numero,libelle,parent) values ('3','COMPTES DE STOCKS ET EN-COURS ','');;
insert into compte(numero,libelle,parent) values ('31','Matières premières (et fournitures) ','3');
insert into compte(numero,libelle,parent) values ('311','Matières (ou groupe) A','31');
insert into compte(numero,libelle,parent) values ('312','Matières (ou groupe) B','31');
insert into compte(numero,libelle,parent) values ('317','Fournitures A, B, C,','31');
insert into compte(numero,libelle,parent) values ('32','Autres approvisionnements','3');
insert into compte(numero,libelle,parent) values ('321','Matières consommables','32');
insert into compte(numero,libelle,parent) values ('322','Fournitures consommables','32');
insert into compte(numero,libelle,parent) values ('326','Emballages','32');
insert into compte(numero,libelle,parent) values ('33','En-cours de production de biens ','3');
insert into compte(numero,libelle,parent) values ('331','Produits en cours','33');
insert into compte(numero,libelle,parent) values ('335','Travaux en cours','33');
insert into compte(numero,libelle,parent) values ('34','En-cours de production de services ','3');
insert into compte(numero,libelle,parent) values ('341','Etudes en cours','34');
insert into compte(numero,libelle,parent) values ('345','Prestations de services en cours','34');
insert into compte(numero,libelle,parent) values ('35','Stocks de produits','3');
insert into compte(numero,libelle,parent) values ('351','Produits intermédiaires','35');
insert into compte(numero,libelle,parent) values ('355','Produits finis','35');
insert into compte(numero,libelle,parent) values ('358','Produits résiduels (ou matières de récupération) ','35');
insert into compte(numero,libelle,parent) values ('36','Compte à ouvrir, le cas échéant, sous l''intitulé  \"stocks provenant d''immobilisations\"','3');
insert into compte(numero,libelle,parent) values ('37','Stocks de marchandises','3');
insert into compte(numero,libelle,parent) values ('371','Marchandises (ou groupe) A','37');
insert into compte(numero,libelle,parent) values ('372','Marchandises (ou groupe) B','37');
insert into compte(numero,libelle,parent) values ('38','Lorsque l''entité tient un inventaire permanent en comptabilité générale, le compte 38 peut être ','3');
insert into compte(numero,libelle,parent) values ('39','Provisions pour dépréciation des stocks et en-cours ','3');
insert into compte(numero,libelle,parent) values ('391','Provisions pour dépréciation des matières premières (et fournitures) ','39');
insert into compte(numero,libelle,parent) values ('392','Provisions pour dépréciation des autres approvisionnements ','39');
insert into compte(numero,libelle,parent) values ('393','Provisions pour dépréciation des en-cours de production de biens ','39');
insert into compte(numero,libelle,parent) values ('394','Provisions pour dépréciation des en-cours de production de services ','39');
insert into compte(numero,libelle,parent) values ('395','Provisions pour dépréciation des stocks de produits ','39');
insert into compte(numero,libelle,parent) values ('397','Provisions pour dépréciation des stocks de marchandises ','39');
insert into compte(numero,libelle,parent) values ('4','COMPTES DE TIERS ','');;
insert into compte(numero,libelle,parent) values ('40','Fournisseurs et comptes rattachés','4');
insert into compte(numero,libelle,parent) values ('400','Fournisseurs et Comptes rattachés ','40');
insert into compte(numero,libelle,parent) values ('401','Fournisseurs','40');
insert into compte(numero,libelle,parent) values ('403','Fournisseurs - Effets à payer','40');
insert into compte(numero,libelle,parent) values ('404','Fournisseurs d''immobilisations','40');
insert into compte(numero,libelle,parent) values ('405','Fournisseurs d''immobilisations - Effets à payer ','40');
insert into compte(numero,libelle,parent) values ('408','Fournisseurs - Factures non parvenues ','40');
insert into compte(numero,libelle,parent) values ('409','Fournisseurs débiteurs','40');
insert into compte(numero,libelle,parent) values ('41','Clients et comptes rattachés','4');
insert into compte(numero,libelle,parent) values ('410','Clients et comptes rattachés ','41');
insert into compte(numero,libelle,parent) values ('411','Clients','41');
insert into compte(numero,libelle,parent) values ('413','Clients - Effets à recevoir','41');
insert into compte(numero,libelle,parent) values ('416','Clients douteux ou litigieux','41');
insert into compte(numero,libelle,parent) values ('418','Clients - Produits non encore facturés ','41');
insert into compte(numero,libelle,parent) values ('419','Clients créditeurs','41');
insert into compte(numero,libelle,parent) values ('42','Personnel et comptes rattachés','4');
insert into compte(numero,libelle,parent) values ('421','Personnel - Rémunérations dues ','42');
insert into compte(numero,libelle,parent) values ('422','Comités d''entreprises, d''établissement, ;;;','42');
insert into compte(numero,libelle,parent) values ('424','Participation des salariés aux résultats ','42');
insert into compte(numero,libelle,parent) values ('425','Personnel - Avances et acomptes','42');
insert into compte(numero,libelle,parent) values ('426','Personnel - Dépôts','42');
insert into compte(numero,libelle,parent) values ('427','Personnel - Oppositions','42');
insert into compte(numero,libelle,parent) values ('428','Personnel - Charges à payer et produits à recevoir ','42');
insert into compte(numero,libelle,parent) values ('43','Sécurité sociale et autres organismes sociaux ','4');
insert into compte(numero,libelle,parent) values ('431','Sécurité sociale','43');
insert into compte(numero,libelle,parent) values ('437','Autres organismes sociaux','43');
insert into compte(numero,libelle,parent) values ('438','Organismes sociaux - Charges à payer et produits à recevoir ','43');
insert into compte(numero,libelle,parent) values ('44','État et autres collectivités publiques ','4');
insert into compte(numero,libelle,parent) values ('441','État - Subventions à recevoir','44');
insert into compte(numero,libelle,parent) values ('442','Etat - Impôts et taxes recouvrables sur des tiers ','44');
insert into compte(numero,libelle,parent) values ('443','Opérations particulières avec l''Etat, les collectivités publiques, les organismes internationaux','44');
insert into compte(numero,libelle,parent) values ('444','Etat - Impôts sur les bénéfices ','44');
insert into compte(numero,libelle,parent) values ('445','Etat - Taxes sur le chiffre d''affaires ','44');
insert into compte(numero,libelle,parent) values ('446','Obligations cautionnées','44');
insert into compte(numero,libelle,parent) values ('447','Autres impôts, taxes et versements assimilés ','44');
insert into compte(numero,libelle,parent) values ('448','Etat - Charges à payer et produits à recevoir ','44');
insert into compte(numero,libelle,parent) values ('449','Quotas d''émission à restituer à l''Etat ','44');
insert into compte(numero,libelle,parent) values ('45','Groupe et associés ','4');
insert into compte(numero,libelle,parent) values ('451','Groupe','45');
insert into compte(numero,libelle,parent) values ('455','Associés - Comptes courants ','45');
insert into compte(numero,libelle,parent) values ('456','Associés - Opérations sur le capital ','45');
insert into compte(numero,libelle,parent) values ('457','Associés - Dividendes à payer ','45');
insert into compte(numero,libelle,parent) values ('458','Associés - Opérations faites en commun et en G;I;E; ','45');
insert into compte(numero,libelle,parent) values ('46','Débiteurs divers et créditeurs divers ','4');
insert into compte(numero,libelle,parent) values ('462','Créances sur cessions d''immobilisations ','46');
insert into compte(numero,libelle,parent) values ('464','Dettes sur acquisitions de valeurs mobilières de placement ','46');
insert into compte(numero,libelle,parent) values ('465','Créances sur cessions de valeurs mobilières de placement ','46');
insert into compte(numero,libelle,parent) values ('467','Autres comptes débiteurs ou créditeurs ','46');
insert into compte(numero,libelle,parent) values ('468','Divers - Charges à payer et produits à recevoir ','46');
insert into compte(numero,libelle,parent) values ('47','Comptes transitoires ou d''attente ','4');
insert into compte(numero,libelle,parent) values ('471 à 475','Comptes d''attente','471 à 47');
insert into compte(numero,libelle,parent) values ('476','Différence de conversion - Actif ','47');
insert into compte(numero,libelle,parent) values ('477','Différences de conversion - Passif ','47');
insert into compte(numero,libelle,parent) values ('478','Autres comptes transitoires','47');
insert into compte(numero,libelle,parent) values ('48','Comptes de régularisation','4');
insert into compte(numero,libelle,parent) values ('481','Charges à répartir sur plusieurs exercices ','48');
insert into compte(numero,libelle,parent) values ('486','Charges constatées d''avance ','48');
insert into compte(numero,libelle,parent) values ('487','Produits constatés d''avance ','48');
insert into compte(numero,libelle,parent) values ('488','Comptes de répartition périodique des charges et des produits ','48');
insert into compte(numero,libelle,parent) values ('489','Quotas d''émission alloués par l''Etat ','48');
insert into compte(numero,libelle,parent) values ('49','Provisions pour dépréciation des comptes de tiers ','4');
insert into compte(numero,libelle,parent) values ('491','Provisions pour dépréciation des comptes de clients ','49');
insert into compte(numero,libelle,parent) values ('495','Provisions pour dépréciation des comptes du groupe et des associés ','49');
insert into compte(numero,libelle,parent) values ('496','Provisions pour dépréciation des comptes de débiteurs divers ','49');
insert into compte(numero,libelle,parent) values ('5','COMPTES FINANCIERS','');;
insert into compte(numero,libelle,parent) values ('50','Valeurs mobilières de placement ','5');
insert into compte(numero,libelle,parent) values ('501','Parts dans des entreprises liées ','50');
insert into compte(numero,libelle,parent) values ('502','Actions propres','50');
insert into compte(numero,libelle,parent) values ('503','Actions','50');
insert into compte(numero,libelle,parent) values ('504','Autres titres conférant un droit de propriété ','50');
insert into compte(numero,libelle,parent) values ('505','Obligations et bons émis par la société et rachetés par elle ','50');
insert into compte(numero,libelle,parent) values ('506','Obligations','50');
insert into compte(numero,libelle,parent) values ('507','Bons du Trésor et bons de caisse à court terme','50');
insert into compte(numero,libelle,parent) values ('508','Autres valeurs mobilières de placement et autres créances assimilées ','50');
insert into compte(numero,libelle,parent) values ('509','Versements restant à effectuer sur valeurs mobilières de placement non libérées ','50');
insert into compte(numero,libelle,parent) values ('51','Banques, établissements financiers et assimilés','5');
insert into compte(numero,libelle,parent) values ('511','Valeurs à l''encaissement','51');
insert into compte(numero,libelle,parent) values ('512','Banques ','51');
insert into compte(numero,libelle,parent) values ('514','Chèques postaux','51');
insert into compte(numero,libelle,parent) values ('515','Caisses du Trésor et des établissements publics','51');
insert into compte(numero,libelle,parent) values ('516','Sociétés de bourse','51');
insert into compte(numero,libelle,parent) values ('517','Autres organismes financiers','51');
insert into compte(numero,libelle,parent) values ('518','Intérêts courus','51');
insert into compte(numero,libelle,parent) values ('519','Concours bancaires courants','51');
insert into compte(numero,libelle,parent) values ('52','Instruments de trésorerie','5');
insert into compte(numero,libelle,parent) values ('53','Caisse','5');
insert into compte(numero,libelle,parent) values ('531','Caisse siège social','53');
insert into compte(numero,libelle,parent) values ('532','Caisse succursale (ou usine) A ','53');
insert into compte(numero,libelle,parent) values ('533','Caisse succursale (ou usine) B ','53');
insert into compte(numero,libelle,parent) values ('54','Régies d''avance et accréditifs','5');
insert into compte(numero,libelle,parent) values ('58','Virements internes','5');
insert into compte(numero,libelle,parent) values ('59','Provisions pour dépréciation des comptes financiers ','5');
insert into compte(numero,libelle,parent) values ('590','Provisions pour dépréciation des valeurs mobilières de placement ','59');
insert into compte(numero,libelle,parent) values ('6','COMPTES DE CHARGES','');;
insert into compte(numero,libelle,parent) values ('60','Achats (sauf 603) ','6');
insert into compte(numero,libelle,parent) values ('601','Achats stockés - Matières premières (et fournitures) ','60');
insert into compte(numero,libelle,parent) values ('602','Achats stockés - Autres approvisionnements ','60');
insert into compte(numero,libelle,parent) values ('603','Variations des stocks (approvisionnements et marchandises) ','60');
insert into compte(numero,libelle,parent) values ('604','Achats d''études et prestations de services ','60');
insert into compte(numero,libelle,parent) values ('605',' Achats de matériel, équipements et travaux ','60');
insert into compte(numero,libelle,parent) values ('606','Achats non stockés de matière et fournitures ','60');
insert into compte(numero,libelle,parent) values ('607','Achats de marchandises','60');
insert into compte(numero,libelle,parent) values ('608','(Compte réservé, le cas échéant, à la récapitulation des frais accessoires incorporés aux achats','60');
insert into compte(numero,libelle,parent) values ('609','Rabais, remises et ristournes obtenus sur achats ','60');
insert into compte(numero,libelle,parent) values ('61','Services extérieurs','6');
insert into compte(numero,libelle,parent) values ('61/62','Autres services extérieurs ','61/6');
insert into compte(numero,libelle,parent) values ('611','Sous-traitance générale ','61');
insert into compte(numero,libelle,parent) values ('612','Redevances de crédit-bail','61');
insert into compte(numero,libelle,parent) values ('613','Locations ','61');
insert into compte(numero,libelle,parent) values ('614','Charges locatives et de copropriété ','61');
insert into compte(numero,libelle,parent) values ('615','Entretien et réparations','61');
insert into compte(numero,libelle,parent) values ('616','Primes d''assurances','61');
insert into compte(numero,libelle,parent) values ('617','Etudes et recherches','61');
insert into compte(numero,libelle,parent) values ('618','Divers','61');
insert into compte(numero,libelle,parent) values ('619','Rabais, remises et ristournes obtenus sur services extérieurs ','61');
insert into compte(numero,libelle,parent) values ('621','Personnel extérieur à l''entreprise ','62');
insert into compte(numero,libelle,parent) values ('622','Rémunérations d''intermédiaires et honoraires ','62');
insert into compte(numero,libelle,parent) values ('623','Publicité, publications, relations publiques ','62');
insert into compte(numero,libelle,parent) values ('624','Transports de biens et transports collectifs du personnel ','62');
insert into compte(numero,libelle,parent) values ('625','Déplacements, missions et réceptions ','62');
insert into compte(numero,libelle,parent) values ('626','Frais postaux et de télécommunications ','62');
insert into compte(numero,libelle,parent) values ('627','Services bancaires et assimilés ','62');
insert into compte(numero,libelle,parent) values ('628','Divers','62');
insert into compte(numero,libelle,parent) values ('629','Rabais, remises et ristournes obtenus sur autres services extérieurs ','62');
insert into compte(numero,libelle,parent) values ('63','Impôts, taxes et versements assimilés ','6');
insert into compte(numero,libelle,parent) values ('631','Impôts, taxes et versements assimilés sur rémunérations (administrations des impôts) ','63');
insert into compte(numero,libelle,parent) values ('633','Impôts, taxes et versements assimilés sur rémunérations (autres organismes) ','63');
insert into compte(numero,libelle,parent) values ('635','Autres impôts, taxes et versements assimilés (administrations des impôts) ','63');
insert into compte(numero,libelle,parent) values ('637','Autres impôts, taxes et versements assimilés (autres organismes) ','63');
insert into compte(numero,libelle,parent) values ('64','Charges de personnel','6');
insert into compte(numero,libelle,parent) values ('641','Rémunérations du personnel ','64');
insert into compte(numero,libelle,parent) values ('644','Rémunération du travail de l''exploitant ','64');
insert into compte(numero,libelle,parent) values ('645','Charges de sécurité sociale et de prévoyance ','64');
insert into compte(numero,libelle,parent) values ('646','Cotisations sociales personnelles de l''exploitant ','64');
insert into compte(numero,libelle,parent) values ('647','Autres charges sociales','64');
insert into compte(numero,libelle,parent) values ('648','Autres charges de personnel','64');
insert into compte(numero,libelle,parent) values ('65','Autres charges de gestion courante ','6');
insert into compte(numero,libelle,parent) values ('651','Redevances pour concessions, brevets, licences, marques, procédés, logiciels, droits et valeurs ','65');
insert into compte(numero,libelle,parent) values ('653','Jetons de présence','65');
insert into compte(numero,libelle,parent) values ('654','Pertes sur créances irrécouvrables ','65');
insert into compte(numero,libelle,parent) values ('655','Quote-part de résultat sur opérations faites en commun ','65');
insert into compte(numero,libelle,parent) values ('658','Charges diverses de gestion courante','65');
insert into compte(numero,libelle,parent) values ('66','Charges financières','6');
insert into compte(numero,libelle,parent) values ('661','Charges d''intérêts','66');
insert into compte(numero,libelle,parent) values ('664','Pertes sur créances liées à des participations ','66');
insert into compte(numero,libelle,parent) values ('665',' Escomptes accordés','66');
insert into compte(numero,libelle,parent) values ('666','Pertes de change','66');
insert into compte(numero,libelle,parent) values ('667','Charges nettes sur cessions de valeurs mobilières de placement ','66');
insert into compte(numero,libelle,parent) values ('668','Autres charges financières','66');
insert into compte(numero,libelle,parent) values ('67','Charges exceptionnelles','6');
insert into compte(numero,libelle,parent) values ('671','Charges exceptionnelles sur opérations de gestion ','67');
insert into compte(numero,libelle,parent) values ('672','(Compte à la disposition des entités pour enregistrer, en cours d''exercice, les charges sur exer','67');
insert into compte(numero,libelle,parent) values ('675','Valeurs comptables des éléments d''actif cédés ','67');
insert into compte(numero,libelle,parent) values ('678','Autres charges exceptionnelles','67');
insert into compte(numero,libelle,parent) values ('68','Dotations aux amortissements et aux provisions ','6');
insert into compte(numero,libelle,parent) values ('681','Dotations aux amortissements et aux provisions - Charges d''exploitation ','68');
insert into compte(numero,libelle,parent) values ('686','Dotations aux amortissements et aux provisions - Charges financières ','68');
insert into compte(numero,libelle,parent) values ('687','Dotations aux amortissements et aux provisions - Charges exceptionnelles ','68');
insert into compte(numero,libelle,parent) values ('69','Participation des salariés - impôts sur les bénéfices et assimiles ','6');
insert into compte(numero,libelle,parent) values ('691','Participation des salariés aux résultats ','69');
insert into compte(numero,libelle,parent) values ('695','Impôts sur les bénéfices ','69');
insert into compte(numero,libelle,parent) values ('696','Suppléments d''impôt sur les sociétés liés aux distributions ','69');
insert into compte(numero,libelle,parent) values ('697','Imposition forfaitaire annuelle des sociétés ','69');
insert into compte(numero,libelle,parent) values ('698','Intégration fiscale','69');
insert into compte(numero,libelle,parent) values ('699','Produits - Reports en arrière des déficits ','69');
insert into compte(numero,libelle,parent) values ('7','COMPTES DE PRODUITS','');;
insert into compte(numero,libelle,parent) values ('70','Ventes de produits fabriqués, prestations de services, marchandises','7');
insert into compte(numero,libelle,parent) values ('701','Ventes de produits finis','70');
insert into compte(numero,libelle,parent) values ('702','Ventes de produits intermédiaires ','70');
insert into compte(numero,libelle,parent) values ('703','Ventes de produits résiduels','70');
insert into compte(numero,libelle,parent) values ('704','Travaux','70');
insert into compte(numero,libelle,parent) values ('705','Etudes','70');
insert into compte(numero,libelle,parent) values ('706','Prestations de services','70');
insert into compte(numero,libelle,parent) values ('707','Ventes de marchandises','70');
insert into compte(numero,libelle,parent) values ('708','Produits des activités annexes ','70');
insert into compte(numero,libelle,parent) values ('709','Rabais, remises et ristournes accordés par l''entreprise ','70');
insert into compte(numero,libelle,parent) values ('71','Production stockée (ou déstockage)','7');
insert into compte(numero,libelle,parent) values ('713','Variation des stocks (en-cours de production, produits) ','71');
insert into compte(numero,libelle,parent) values ('72','Production immobilisée','7');
insert into compte(numero,libelle,parent) values ('721','Immobilisations incorporelles','72');
insert into compte(numero,libelle,parent) values ('722','Immobilisations corporelles','72');
insert into compte(numero,libelle,parent) values ('74','Subventions d''exploitation','7');
insert into compte(numero,libelle,parent) values ('75','Autres produits de gestion courante ','7');
insert into compte(numero,libelle,parent) values ('751','Redevances pour concessions, brevets, licences, marques, procédés, logiciels, droits et valeurs ','75');
insert into compte(numero,libelle,parent) values ('752','Revenus des immeubles non affectés à des activités professionnelles ','75');
insert into compte(numero,libelle,parent) values ('753','Jetons de présence et rémunérations d''administrateurs, gérants,;;; ','75');
insert into compte(numero,libelle,parent) values ('754','Ristournes perçues des coopératives (provenant des excédents) ','75');
insert into compte(numero,libelle,parent) values ('755','Quotes-parts de résultat sur opérations faites en commun ','75');
insert into compte(numero,libelle,parent) values ('758','Produits divers de gestion courante','75');
insert into compte(numero,libelle,parent) values ('76','Produits financiers','7');
insert into compte(numero,libelle,parent) values ('761','Produits de participations','76');
insert into compte(numero,libelle,parent) values ('762','Produits des autres immobilisations financières ','76');
insert into compte(numero,libelle,parent) values ('763','Revenus des autres créances','76');
insert into compte(numero,libelle,parent) values ('764','Revenus des valeurs mobilières de placement ','76');
insert into compte(numero,libelle,parent) values ('765','Escomptes obtenus','76');
insert into compte(numero,libelle,parent) values ('766','Gains de change','76');
insert into compte(numero,libelle,parent) values ('767','Produits nets sur cessions de valeurs mobilières de placement ','76');
insert into compte(numero,libelle,parent) values ('768','Autres produits financiers','76');
insert into compte(numero,libelle,parent) values ('77','Produits exceptionnels','7');
insert into compte(numero,libelle,parent) values ('771','Produits exceptionnels sur opérations de gestion ','77');
insert into compte(numero,libelle,parent) values ('772','(Compte à la disposition des entités pour enregistrer, en cours d''exercice, les produits sur exe','77');
insert into compte(numero,libelle,parent) values ('775','Produits des cessions d''éléments d''actif ','77');
insert into compte(numero,libelle,parent) values ('777','Quote-part des subventions d''investissement virée au résultat de l''exercice ','77');
insert into compte(numero,libelle,parent) values ('778','Autres produits exceptionnels ','77');
insert into compte(numero,libelle,parent) values ('78','Reprises sur amortissements et provisions ','7');
insert into compte(numero,libelle,parent) values ('781','Reprises sur amortissements et provisions (à inscrire dans les produits d''exploitation) ','78');
insert into compte(numero,libelle,parent) values ('786','Reprises sur provisions pour risques (à inscrire dans les produits financiers) ','78');
insert into compte(numero,libelle,parent) values ('787','Reprises sur provisions (à inscrire dans les produits exceptionnels) ','78');
insert into compte(numero,libelle,parent) values ('79','Transferts de charges','7');
insert into compte(numero,libelle,parent) values ('791','Transferts de charges d''exploitation ','79');
insert into compte(numero,libelle,parent) values ('796','Transferts de charges financières ','79');
insert into compte(numero,libelle,parent) values ('797','Transferts de charges exceptionnelles ','79');
insert into compte(numero,libelle,parent) values ('8','COMPTES SPECIAUX*','');;
insert into compte(numero,libelle,parent) values ('80','Engagements*','8');
insert into compte(numero,libelle,parent) values ('801','Engagements donnés par l''entité*','80');
insert into compte(numero,libelle,parent) values ('8011','Avals, cautions, garanties*','801');
insert into compte(numero,libelle,parent) values ('8014','Effets circulant sous l''endos de l''entité*','801');
insert into compte(numero,libelle,parent) values ('8016','Redevances crédit-bail restant à courir*','801');
insert into compte(numero,libelle,parent) values ('80161','Crédit-bail mobilier*','8016');
insert into compte(numero,libelle,parent) values ('80165','Crédit-bail immobilier*','8016');
insert into compte(numero,libelle,parent) values ('8018','Autres engagements donnés*','801');
insert into compte(numero,libelle,parent) values ('802','Engagements recus par l''entité*','80');
insert into compte(numero,libelle,parent) values ('8021','Avals, cautions, garanties*','802');
insert into compte(numero,libelle,parent) values ('8024','Créances escomptées non échues*','802');
insert into compte(numero,libelle,parent) values ('8026','Engagements reçus pour utilisation en crédit-bail*','802');
insert into compte(numero,libelle,parent) values ('80261','Crédit-bail mobilier*','8026');
insert into compte(numero,libelle,parent) values ('80265','Crédit-bail immobilier*','8026');
insert into compte(numero,libelle,parent) values ('8028','Autres engagements reçus*','802');
insert into compte(numero,libelle,parent) values ('809','Contrepartie des engagements*','80');
insert into compte(numero,libelle,parent) values ('8091','Contrepartie 801*','809');
insert into compte(numero,libelle,parent) values ('8092','Contrepartie 802*','809');
insert into compte(numero,libelle,parent) values ('88','Résultat en instance d''affectation*','8');
insert into compte(numero,libelle,parent) values ('89','Bilan*','8');

insert into ecriture (id,libelle,creele,idjournal) values (nextval('seq_ecriture'),'Facture Mac Book Air',now(),1);

insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'512',120000,0);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'600',0,100000);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'455',0,20000);

insert into ecriture (id,libelle,creele,idjournal) values (nextval('seq_ecriture'),'Facture Chaise bureau',now(),1);

insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'512',60000,0);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'600',0,50000);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'455',0,10000);

insert into ecriture (id,libelle,creele,idjournal) values (nextval('seq_ecriture'),'Petite cuiller',now(),1);

insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'512',1200,0);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'600',0,1000);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'455',0,200);

insert into ecriture (id,libelle,creele,idjournal) values (nextval('seq_ecriture'),'Fourchette en bois',now(),1);

insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'512',600,0);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'600',0,500);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'455',0,100);

insert into ecriture (id,libelle,creele,idjournal) values (nextval('seq_ecriture'),'Raspberry',now(),1);

insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'512',3840,0);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'600',0,3200);
insert into ligneecriture (id,idEcriture,numeroCompte,montantDebit,montantCredit) values (nextval('seq_ligneecriture'),currval('seq_ecriture'),'455',0,6400);


