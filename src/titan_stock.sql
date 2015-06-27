PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "titan_stock" ("seq" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "market" varchar(50) NOT NULL, "code" integer NOT NULL, "name" varchar(50) NOT NULL);
INSERT INTO "titan_stock" VALUES(1,'sh',600036,'招商银行');
INSERT INTO "titan_stock" VALUES(2,'sh',601288,'农业银行');
INSERT INTO "titan_stock" VALUES(3,'sh',601818,'光大银行');
INSERT INTO "titan_stock" VALUES(4,'sh',603169,'兰石重装');
INSERT INTO "titan_stock" VALUES(5,'sh',600221,'海南航空');
INSERT INTO "titan_stock" VALUES(7,'sh',600585,'海螺水泥');
INSERT INTO "titan_stock" VALUES(8,'sh',600363,'联创光电');
INSERT INTO "titan_stock" VALUES(9,'sh',601628,'中国人寿');
INSERT INTO "titan_stock" VALUES(11,'sh',601318,'中国平安');
INSERT INTO "titan_stock" VALUES(12,'sh',600600,'青岛啤酒');
INSERT INTO "titan_stock" VALUES(13,'sh',600439,'瑞贝卡');
INSERT INTO "titan_stock" VALUES(14,'sh',600547,'山东黄金');
INSERT INTO "titan_stock" VALUES(15,'sh',600030,'中信证券');
INSERT INTO "titan_stock" VALUES(16,'sh',601069,'西部黄金');
INSERT INTO "titan_stock" VALUES(17,'sh',600489,'中金黄金');
INSERT INTO "titan_stock" VALUES(18,'sh',600329,'中新药业');
INSERT INTO "titan_stock" VALUES(19,'sh',600089,'特变电工');
INSERT INTO "titan_stock" VALUES(20,'sh',600028,'中国石化');
INSERT INTO "titan_stock" VALUES(21,'sh',600705,'中航投资');
INSERT INTO "titan_stock" VALUES(22,'sh',600050,'中国联通');
INSERT INTO "titan_stock" VALUES(23,'sh',600578,'京能电力');
INSERT INTO "titan_stock" VALUES(24,'sz',300137,'先河环保');
INSERT INTO "titan_stock" VALUES(25,'sh',601989,'中国重工');
INSERT INTO "titan_stock" VALUES(26,'sh',600855,'航天长峰');
INSERT INTO "titan_stock" VALUES(27,'sh',600038,'中直股份');
INSERT INTO "titan_stock" VALUES(28,'sh',600845,'宝信软件');
INSERT INTO "titan_stock" VALUES(29,'sh',600690,'青岛海尔');
INSERT INTO "titan_stock" VALUES(30,'sh',600795,'国电电力');
INSERT INTO "titan_stock" VALUES(31,'sz',2,'万科A');
INSERT INTO "titan_stock" VALUES(32,'hk',700,'腾讯控股');
INSERT INTO "titan_stock" VALUES(33,'hk',5,'汇丰控股');
INSERT INTO "titan_stock" VALUES(34,'hk',154,'北京发展');
INSERT INTO "titan_stock" VALUES(35,'hk',392,'北京控股');
INSERT INTO "titan_stock" VALUES(36,'hk',1164,'中广核矿业');
INSERT INTO "titan_stock" VALUES(37,'hk',1299,'友邦保险');
INSERT INTO "titan_stock" VALUES(38,'hk',1330,'绿色动力环保');
INSERT INTO "titan_stock" VALUES(39,'hk',1613,'协同通信');
INSERT INTO "titan_stock" VALUES(41,'hk',6136,'康达环保');
INSERT INTO "titan_stock" VALUES(42,'hk',384,'中国燃气');
INSERT INTO "titan_stock" VALUES(43,'hk',439,'光启科学');
INSERT INTO "titan_stock" VALUES(44,'hk',85,'中国电子');
INSERT INTO "titan_stock" VALUES(45,'hk',241,'阿里健康');
INSERT INTO "titan_stock" VALUES(46,'hk',268,'金蝶国际');
INSERT INTO "titan_stock" VALUES(47,'hk',317,'广州广船国际股份');
INSERT INTO "titan_stock" VALUES(48,'hk',323,'马鞍山钢铁股份');
INSERT INTO "titan_stock" VALUES(49,'hk',338,'上海石油化工股份');
INSERT INTO "titan_stock" VALUES(50,'hk',354,'中国软件国际');
INSERT INTO "titan_stock" VALUES(51,'hk',368,'中外运航运');
INSERT INTO "titan_stock" VALUES(52,'hk',390,'中国中铁');
INSERT INTO "titan_stock" VALUES(53,'hk',400,'科通芯城');
INSERT INTO "titan_stock" VALUES(54,'hk',402,'天下图控股');
INSERT INTO "titan_stock" VALUES(55,'hk',434,'博雅互动');
INSERT INTO "titan_stock" VALUES(56,'hk',493,'国美电器');
INSERT INTO "titan_stock" VALUES(57,'hk',498,'保华集团');
INSERT INTO "titan_stock" VALUES(58,'sz',300405,'科隆精化');
INSERT INTO "titan_stock" VALUES(59,'hk',510,'时富金融服务集团');
INSERT INTO "titan_stock" VALUES(60,'hk',525,'广深铁路股份');
INSERT INTO "titan_stock" VALUES(61,'hk',543,'太平洋网络');
INSERT INTO "titan_stock" VALUES(62,'hk',546,'阜丰股份');
INSERT INTO "titan_stock" VALUES(63,'hk',560,'珠江船务');
INSERT INTO "titan_stock" VALUES(64,'hk',570,'中国中药');
INSERT INTO "titan_stock" VALUES(65,'hk',579,'京能清洁能源');
INSERT INTO "titan_stock" VALUES(66,'hk',587,'华瀚生物制药');
INSERT INTO "titan_stock" VALUES(67,'hk',656,'复星国际');
INSERT INTO "titan_stock" VALUES(68,'hk',665,'海通国际');
INSERT INTO "titan_stock" VALUES(69,'hk',694,'北京首都机场股份');
INSERT INTO "titan_stock" VALUES(70,'hk',696,'中国民航信息网络');
INSERT INTO "titan_stock" VALUES(71,'hk',699,'神州租车');
INSERT INTO "titan_stock" VALUES(72,'hk',750,'兴业太阳能');
INSERT INTO "titan_stock" VALUES(73,'hk',777,'网龙');
INSERT INTO "titan_stock" VALUES(74,'hk',816,'华电福新');
INSERT INTO "titan_stock" VALUES(75,'hk',818,'高阳科技');
INSERT INTO "titan_stock" VALUES(76,'hk',819,'天能动力');
INSERT INTO "titan_stock" VALUES(77,'hk',882,'天津发展');
INSERT INTO "titan_stock" VALUES(78,'hk',906,'中粮包装');
INSERT INTO "titan_stock" VALUES(79,'hk',963,'华熙生物科技');
INSERT INTO "titan_stock" VALUES(80,'hk',978,'招商局置地');
INSERT INTO "titan_stock" VALUES(81,'hk',1030,'新城发展控股');
INSERT INTO "titan_stock" VALUES(82,'hk',1035,'BBI生命科技');
INSERT INTO "titan_stock" VALUES(83,'hk',1052,'越秀交通基建');
INSERT INTO "titan_stock" VALUES(84,'hk',1055,'南方航空股份');
INSERT INTO "titan_stock" VALUES(85,'hk',1060,'阿里影业');
INSERT INTO "titan_stock" VALUES(86,'hk',1112,'合生元');
INSERT INTO "titan_stock" VALUES(87,'hk',1211,'比亚迪电子');
INSERT INTO "titan_stock" VALUES(88,'hk',1297,'中国擎天软件');
INSERT INTO "titan_stock" VALUES(89,'hk',1314,'翠华控股');
INSERT INTO "titan_stock" VALUES(90,'hk',1322,'CW GROUP HOLD');
INSERT INTO "titan_stock" VALUES(91,'hk',2369,'酷派集团');
INSERT INTO "titan_stock" VALUES(92,'hk',1345,'中国先锋医药');
INSERT INTO "titan_stock" VALUES(93,'hk',1349,'复旦张江');
INSERT INTO "titan_stock" VALUES(94,'hk',1358,'普华和顺');
INSERT INTO "titan_stock" VALUES(95,'hk',1363,'中滔环保');
INSERT INTO "titan_stock" VALUES(96,'hk',1371,'华彩控股');
INSERT INTO "titan_stock" VALUES(97,'hk',1385,'上海复旦');
INSERT INTO "titan_stock" VALUES(98,'hk',1515,'凤凰医疗');
INSERT INTO "titan_stock" VALUES(99,'hk',1639,'安捷利实业');
INSERT INTO "titan_stock" VALUES(100,'hk',1661,'智美集团');
INSERT INTO "titan_stock" VALUES(101,'hk',1666,'同仁堂科技');
INSERT INTO "titan_stock" VALUES(102,'hk',1668,'华南城');
INSERT INTO "titan_stock" VALUES(103,'hk',1766,'中国南车');
INSERT INTO "titan_stock" VALUES(104,'hk',1778,'彩生活');
INSERT INTO "titan_stock" VALUES(105,'hk',1788,'国泰君安');
INSERT INTO "titan_stock" VALUES(106,'hk',1816,'中广核电力');
INSERT INTO "titan_stock" VALUES(107,'hk',1818,'招金矿业');
INSERT INTO "titan_stock" VALUES(108,'hk',1833,'银泰商业');
INSERT INTO "titan_stock" VALUES(109,'hk',1886,'汇源果汁');
INSERT INTO "titan_stock" VALUES(110,'hk',1980,'天鸽互动');
INSERT INTO "titan_stock" VALUES(111,'hk',2009,'金隅股份');
INSERT INTO "titan_stock" VALUES(112,'hk',2018,'瑞声科技');
INSERT INTO "titan_stock" VALUES(113,'hk',2188,'泰坦能源技术');
INSERT INTO "titan_stock" VALUES(114,'hk',2196,'复星医药');
INSERT INTO "titan_stock" VALUES(115,'hk',2208,'金风科技');
INSERT INTO "titan_stock" VALUES(116,'hk',2211,'金天医药集团');
INSERT INTO "titan_stock" VALUES(117,'hk',2280,'慧聪网');
INSERT INTO "titan_stock" VALUES(118,'hk',2298,'都市丽人');
INSERT INTO "titan_stock" VALUES(119,'hk',2331,'李宁');
INSERT INTO "titan_stock" VALUES(120,'hk',2348,'东瑞制药');
INSERT INTO "titan_stock" VALUES(121,'hk',2357,'中航科工');
INSERT INTO "titan_stock" VALUES(122,'hk',2488,'元征科技');
INSERT INTO "titan_stock" VALUES(123,'hk',2727,'上海电气');
INSERT INTO "titan_stock" VALUES(124,'hk',2789,'远大中国');
INSERT INTO "titan_stock" VALUES(125,'hk',3315,'金邦达宝嘉');
INSERT INTO "titan_stock" VALUES(126,'hk',3337,'安东油田服务');
INSERT INTO "titan_stock" VALUES(127,'hk',3378,'厦门港务');
INSERT INTO "titan_stock" VALUES(128,'hk',3382,'天津港发展');
INSERT INTO "titan_stock" VALUES(129,'hk',3389,'亨得利');
INSERT INTO "titan_stock" VALUES(130,'hk',3393,'威胜集团');
INSERT INTO "titan_stock" VALUES(131,'hk',3888,'金山软件');
INSERT INTO "titan_stock" VALUES(132,'hk',3899,'中集安科瑞');
INSERT INTO "titan_stock" VALUES(133,'hk',3993,'洛阳钼业');
INSERT INTO "titan_stock" VALUES(134,'hk',8002,'IGG');
INSERT INTO "titan_stock" VALUES(135,'hk',8138,'同仁堂国药');
INSERT INTO "titan_stock" VALUES(136,'hk',8143,'华夏医疗');
INSERT INTO "titan_stock" VALUES(137,'hk',8207,'中国信贷');
INSERT INTO "titan_stock" VALUES(138,'hk',8267,'蓝港互动');
INSERT INTO "titan_stock" VALUES(140,'sz',725,'京东方A');
INSERT INTO "titan_stock" VALUES(145,'sh',601866,'中海集运');
INSERT INTO "titan_stock" VALUES(146,'sh',601727,'上海电气');
INSERT INTO "titan_stock" VALUES(147,'sz',410,'沈阳机床');
INSERT INTO "titan_stock" VALUES(148,'sz',538,'云南白药');
INSERT INTO "titan_stock" VALUES(149,'sz',875,'吉电股份');
INSERT INTO "titan_stock" VALUES(150,'sz',2128,'露天煤业');
INSERT INTO "titan_stock" VALUES(151,'hk',2380,'中国电力');
INSERT INTO "titan_stock" VALUES(152,'hk',735,'中国电力新能源');
INSERT INTO "titan_stock" VALUES(153,'sh',600021,'上海电力');
INSERT INTO "titan_stock" VALUES(154,'sz',958,'东方能源');
INSERT INTO "titan_stock" VALUES(155,'sz',767,'漳泽电力');
INSERT INTO "titan_stock" VALUES(156,'sh',600292,'中电远达');
INSERT INTO "titan_stock" VALUES(157,'sh',600401,'海润光伏');
INSERT INTO "titan_stock" VALUES(158,'sh',600619,'海立股份');
INSERT INTO "titan_stock" VALUES(159,'sz',682,'东方电子');
INSERT INTO "titan_stock" VALUES(160,'sz',2562,'兄弟科技');
INSERT INTO "titan_stock" VALUES(161,'sz',62,'深圳华强');
INSERT INTO "titan_stock" VALUES(162,'sz',1,'深发展A');
INSERT INTO "titan_stock" VALUES(163,'sz',21,'深科技A');
INSERT INTO "titan_stock" VALUES(164,'sz',22,'深赤湾A');
INSERT INTO "titan_stock" VALUES(165,'sz',27,'深能源A');
INSERT INTO "titan_stock" VALUES(166,'sz',39,'中集集团');
INSERT INTO "titan_stock" VALUES(167,'sz',63,'中兴通讯');
INSERT INTO "titan_stock" VALUES(168,'sz',69,'华侨城A');
INSERT INTO "titan_stock" VALUES(169,'sz',88,'盐田港A');
INSERT INTO "titan_stock" VALUES(170,'sz',89,'深圳机场');
INSERT INTO "titan_stock" VALUES(171,'sz',100,'TCL集团');
INSERT INTO "titan_stock" VALUES(172,'sz',402,'金融街');
INSERT INTO "titan_stock" VALUES(173,'sz',503,'海虹控股');
INSERT INTO "titan_stock" VALUES(174,'sz',539,'粤电力');
INSERT INTO "titan_stock" VALUES(175,'sz',625,'长安汽车');
INSERT INTO "titan_stock" VALUES(176,'sz',629,'新巩钒');
INSERT INTO "titan_stock" VALUES(177,'sz',651,'格力电器');
INSERT INTO "titan_stock" VALUES(178,'sz',709,'唐钢股份');
INSERT INTO "titan_stock" VALUES(179,'sz',729,'燕京啤酒');
INSERT INTO "titan_stock" VALUES(180,'sz',792,'盐湖钾肥');
INSERT INTO "titan_stock" VALUES(181,'sz',800,'一汽轿车');
INSERT INTO "titan_stock" VALUES(182,'sz',825,'太钢不锈');
INSERT INTO "titan_stock" VALUES(183,'sz',839,'中信国安');
INSERT INTO "titan_stock" VALUES(184,'sz',858,'五粮液');
INSERT INTO "titan_stock" VALUES(185,'sz',898,'鞍钢新轧');
INSERT INTO "titan_stock" VALUES(186,'sz',932,'华菱管线');
INSERT INTO "titan_stock" VALUES(187,'sz',959,'首钢股份');
INSERT INTO "titan_stock" VALUES(188,'sz',983,'西山煤电');
INSERT INTO "titan_stock" VALUES(189,'sz',2024,'苏宁电器');
INSERT INTO "titan_stock" VALUES(190,'sh',600000,'浦发银行');
INSERT INTO "titan_stock" VALUES(192,'sh',600004,'白云机场');
INSERT INTO "titan_stock" VALUES(193,'sh',600005,'武钢股份');
INSERT INTO "titan_stock" VALUES(194,'sh',600006,'东风汽车');
INSERT INTO "titan_stock" VALUES(195,'sh',600008,'首创股份');
INSERT INTO "titan_stock" VALUES(196,'sh',600009,'上海机场');
INSERT INTO "titan_stock" VALUES(197,'sh',600010,'包钢股份');
INSERT INTO "titan_stock" VALUES(198,'sh',600011,'华能国际');
INSERT INTO "titan_stock" VALUES(199,'sh',600012,'皖通高速');
INSERT INTO "titan_stock" VALUES(200,'sh',600015,'华夏银行');
INSERT INTO "titan_stock" VALUES(201,'sh',600016,'民生银行');
INSERT INTO "titan_stock" VALUES(202,'sh',600018,'上港集箱');
INSERT INTO "titan_stock" VALUES(203,'sh',600019,'宝钢股份');
INSERT INTO "titan_stock" VALUES(204,'sh',600020,'中原高速');
INSERT INTO "titan_stock" VALUES(205,'sh',600026,'中海发展');
INSERT INTO "titan_stock" VALUES(206,'sh',600027,'华电国际');
INSERT INTO "titan_stock" VALUES(207,'sh',600029,'南方航空');
INSERT INTO "titan_stock" VALUES(208,'sh',600033,'福建高速');
INSERT INTO "titan_stock" VALUES(209,'sh',600037,'歌华有线');
INSERT INTO "titan_stock" VALUES(210,'sh',600058,'五矿发展');
INSERT INTO "titan_stock" VALUES(211,'sh',600085,'同仁堂');
INSERT INTO "titan_stock" VALUES(212,'sh',600098,'广州控股');
INSERT INTO "titan_stock" VALUES(213,'sh',600100,'清华同方');
INSERT INTO "titan_stock" VALUES(214,'sh',600104,'上海汽车');
INSERT INTO "titan_stock" VALUES(215,'sh',600115,'东方航空');
INSERT INTO "titan_stock" VALUES(216,'sh',600117,'雅戈尔');
INSERT INTO "titan_stock" VALUES(217,'sh',600188,'兖州煤业');
INSERT INTO "titan_stock" VALUES(219,'sh',600236,'桂冠电力');
INSERT INTO "titan_stock" VALUES(220,'sh',600269,'赣粤高速');
INSERT INTO "titan_stock" VALUES(221,'sh',600270,'外运发展');
INSERT INTO "titan_stock" VALUES(222,'sh',600309,'烟台万华');
INSERT INTO "titan_stock" VALUES(223,'sh',600320,'振华港机');
INSERT INTO "titan_stock" VALUES(224,'sh',600348,'国阳新能');
INSERT INTO "titan_stock" VALUES(225,'sh',600350,'G鲁高速');
INSERT INTO "titan_stock" VALUES(226,'sh',600362,'江西铜业');
INSERT INTO "titan_stock" VALUES(227,'sh',600377,'宁沪高速');
INSERT INTO "titan_stock" VALUES(228,'sh',600428,'中远航运');
INSERT INTO "titan_stock" VALUES(229,'sh',600500,'中化国际');
INSERT INTO "titan_stock" VALUES(230,'sh',600519,'贵州茅台');
INSERT INTO "titan_stock" VALUES(231,'sh',600548,'深高速');
INSERT INTO "titan_stock" VALUES(232,'sh',600569,'安阳钢铁');
INSERT INTO "titan_stock" VALUES(233,'sh',600583,'海油工程');
INSERT INTO "titan_stock" VALUES(234,'sh',600597,'光明乳业');
INSERT INTO "titan_stock" VALUES(235,'sh',600598,'北大荒');
INSERT INTO "titan_stock" VALUES(236,'sh',600631,'百联股份');
INSERT INTO "titan_stock" VALUES(237,'sh',600642,'申能股份');
INSERT INTO "titan_stock" VALUES(238,'sh',600649,'原水股份');
INSERT INTO "titan_stock" VALUES(239,'sh',600660,'福耀玻璃');
INSERT INTO "titan_stock" VALUES(240,'sh',600663,'陆家嘴');
INSERT INTO "titan_stock" VALUES(241,'sh',600688,'上海石化');
INSERT INTO "titan_stock" VALUES(242,'sh',600717,'天津港');
INSERT INTO "titan_stock" VALUES(243,'sh',600808,'马钢股份');
INSERT INTO "titan_stock" VALUES(244,'sh',600333,'长春燃气');
INSERT INTO "titan_stock" VALUES(246,'sz',777,'中核科技');
INSERT INTO "titan_stock" VALUES(247,'sh',600170,'上海建工');
INSERT INTO "titan_stock" VALUES(248,'sh',600031,'三一重工');
INSERT INTO "titan_stock" VALUES(249,'sz',2049,'同方国芯');
INSERT INTO "titan_stock" VALUES(250,'sh',600875,'用友网络');
INSERT INTO "titan_stock" VALUES(251,'sz',2130,'沃尔核材');
INSERT INTO "titan_stock" VALUES(252,'sz',2385,'大北农');
INSERT INTO "titan_stock" VALUES(253,'sz',2588,'史丹利');
INSERT INTO "titan_stock" VALUES(254,'sz',2470,'金正大');
INSERT INTO "titan_stock" VALUES(255,'sz',2170,'芭田股份');
INSERT INTO "titan_stock" VALUES(256,'sh',600238,'海南椰岛');
INSERT INTO "titan_stock" VALUES(257,'sz',886,'海南高速');
INSERT INTO "titan_stock" VALUES(258,'sh',600209,'罗顿发展');
INSERT INTO "titan_stock" VALUES(259,'sh',600198,'大唐电信');
INSERT INTO "titan_stock" VALUES(260,'sz',997,'新大陆');
INSERT INTO "titan_stock" VALUES(261,'sz',2197,'证通电子');
INSERT INTO "titan_stock" VALUES(262,'sh',600299,'蓝星新材');
INSERT INTO "titan_stock" VALUES(263,'hk',806,'惠理集团');
INSERT INTO "titan_stock" VALUES(264,'hk',1000,'北青传媒');
INSERT INTO "titan_stock" VALUES(265,'hk',1478,'丘钛科技');
INSERT INTO "titan_stock" VALUES(266,'hk',2202,'万科企业');
INSERT INTO "titan_stock" VALUES(267,'hk',941,'中国移动');
INSERT INTO "titan_stock" VALUES(268,'hk',857,'中国石油');
INSERT INTO "titan_stock" VALUES(269,'hk',1088,'中国神华');
INSERT INTO "titan_stock" VALUES(270,'hk',386,'中国石化');
INSERT INTO "titan_stock" VALUES(271,'hk',1398,'工商银行');
INSERT INTO "titan_stock" VALUES(272,'hk',2318,'中国平安');
INSERT INTO "titan_stock" VALUES(273,'hk',1988,'民生银行');
INSERT INTO "titan_stock" VALUES(274,'hk',3988,'中国银行');
INSERT INTO "titan_stock" VALUES(275,'hk',1288,'农业银行');
INSERT INTO "titan_stock" VALUES(276,'hk',1157,'中联重科');
INSERT INTO "titan_stock" VALUES(277,'sh',600545,'新疆城建');
INSERT INTO "titan_stock" VALUES(278,'sz',2307,'北新路桥');
INSERT INTO "titan_stock" VALUES(279,'sz',2594,'比亚迪');
INSERT INTO "titan_stock" VALUES(280,'sh',600680,'上海普天');
INSERT INTO "titan_stock" VALUES(281,'sh',600372,'中航电子');
INSERT INTO "titan_stock" VALUES(282,'sh',600391,'成发科技');
INSERT INTO "titan_stock" VALUES(283,'sz',738,'中航动控');
INSERT INTO "titan_stock" VALUES(284,'sz',2179,'中航光电');
INSERT INTO "titan_stock" VALUES(285,'sz',2617,'露笑科技');
INSERT INTO "titan_stock" VALUES(286,'sz',2008,'大族激光');
INSERT INTO "titan_stock" VALUES(287,'sz',610,'西安旅游');
INSERT INTO "titan_stock" VALUES(288,'sh',600187,'国中水务');
INSERT INTO "titan_stock" VALUES(289,'sh',600111,'北方稀土');
INSERT INTO "titan_stock" VALUES(290,'sh',601179,'中国西电');
INSERT INTO "titan_stock" VALUES(291,'sh',600863,'内蒙华电');
INSERT INTO "titan_stock" VALUES(292,'sz',507,'珠海港');
INSERT INTO "titan_stock" VALUES(293,'sz',998,'隆平高科');
INSERT INTO "titan_stock" VALUES(294,'sz',504,'南华生物');
INSERT INTO "titan_stock" VALUES(295,'sh',600661,'新南洋');
INSERT INTO "titan_stock" VALUES(296,'sz',948,'南天信息');
INSERT INTO "titan_stock" VALUES(297,'sz',826,'桑德环境');
INSERT INTO "titan_stock" VALUES(298,'hk',8060,'国联通信');
INSERT INTO "titan_stock" VALUES(299,'hk',575,'励晶太平洋');
INSERT INTO "titan_stock" VALUES(300,'hk',1,'长和');
INSERT INTO "titan_stock" VALUES(301,'sh',1,'上证指数');
INSERT INTO "titan_stock" VALUES(302,'sh',601005,'重庆钢铁');
INSERT INTO "titan_stock" VALUES(303,'sh',600282,'南钢股份');
INSERT INTO "titan_stock" VALUES(304,'sh',600126,'杭钢股份');
INSERT INTO "titan_stock" VALUES(305,'sz',917,'电广传媒');
INSERT INTO "titan_stock" VALUES(306,'sh',600635,'大众公用');
INSERT INTO "titan_stock" VALUES(307,'sz',61,'农产品');
INSERT INTO "titan_stock" VALUES(308,'sz',60,'中金岭南');
INSERT INTO "titan_stock" VALUES(309,'sz',42,'中洲控股');
INSERT INTO "titan_stock" VALUES(310,'sh',600495,'晋西车轴');
INSERT INTO "titan_stock" VALUES(311,'sh',600528,'中铁二局');
INSERT INTO "titan_stock" VALUES(312,'hk',388,'香港交易所');
INSERT INTO "titan_stock" VALUES(313,'sz',2456,'欧菲光');
INSERT INTO "titan_stock" VALUES(314,'sh',600068,'葛洲坝');
INSERT INTO "titan_stock" VALUES(315,'sh',600106,'重庆路桥');
INSERT INTO "titan_stock" VALUES(316,'sh',600801,'华新水泥');
INSERT INTO "titan_stock" VALUES(317,'sz',2063,'远光软件');
INSERT INTO "titan_stock" VALUES(318,'sh',601169,'北京银行');
INSERT INTO "titan_stock" VALUES(319,'hk',2628,'中国人寿');
INSERT INTO "titan_stock" VALUES(320,'sh',600893,'航空动力');
INSERT INTO "titan_stock" VALUES(321,'hk',1203,'广南集团');
INSERT INTO "titan_stock" VALUES(322,'hk',270,'粤海投资');
INSERT INTO "titan_stock" VALUES(323,'hk',124,'粤海置地控股有限公司');
INSERT INTO "titan_stock" VALUES(324,'sz',399001,'深证成指');
INSERT INTO "titan_stock" VALUES(325,'sh',600343,'航天动力');
INSERT INTO "titan_stock" VALUES(326,'sz',2550,'千红制药');
INSERT INTO "titan_stock" VALUES(327,'sz',2230,'科大讯飞');
INSERT INTO "titan_stock" VALUES(328,'hk',6886,'华泰证券');
INSERT INTO "titan_stock" VALUES(329,'hk',1776,'广发证券');
INSERT INTO "titan_stock" VALUES(330,'hk',1138,'中海发展H');
INSERT INTO "titan_stock" VALUES(331,'hk',1230,'雅士利国际');
INSERT INTO "titan_stock" VALUES(332,'hk',1093,'石药集团');
INSERT INTO "titan_stock" VALUES(333,'hk',598,'中国外运');
INSERT INTO "titan_stock" VALUES(334,'hk',992,'联想集团');
INSERT INTO "titan_stock" VALUES(335,'hk',1308,'海丰国际');
INSERT INTO "titan_stock" VALUES(336,'hk',3369,'秦港股份');
INSERT INTO "titan_stock" VALUES(337,'hk',688,'中国海外发展');
INSERT INTO "titan_stock" VALUES(338,'hk',6869,'长飞光纤光缆');
INSERT INTO "titan_stock" VALUES(339,'sh',600638,'新黄浦');
INSERT INTO "titan_stock" VALUES(340,'hk',99999999,'HSI');
INSERT INTO "titan_stock" VALUES(341,'sz',2451,'摩恩电器');
INSERT INTO "titan_stock" VALUES(342,'sh',600593,'大连圣亚');
INSERT INTO "titan_stock" VALUES(343,'hk',848,'茂业国际');
INSERT INTO "titan_stock" VALUES(344,'hk',8271,'环球数码');
INSERT INTO "titan_stock" VALUES(345,'sh',601766,'中国中车');
INSERT INTO "titan_stock" VALUES(346,'hk',1766,'中国中车');
INSERT INTO "titan_stock" VALUES(347,'sh',600266,'北京城建');
INSERT INTO "titan_stock" VALUES(348,'hk',2878,'晶门科技');
INSERT INTO "titan_stock" VALUES(349,'sz',2673,'西部证券');
INSERT INTO "titan_stock" VALUES(350,'sh',600703,'三安光电');
INSERT INTO "titan_stock" VALUES(351,'hk',981,'中芯国际');
INSERT INTO "titan_stock" VALUES(352,'hk',90,'琥珀能源');
INSERT INTO "titan_stock" VALUES(353,'hk',109,'金威资源');
INSERT INTO "titan_stock" VALUES(354,'hk',260,'幸福控股');
INSERT INTO "titan_stock" VALUES(355,'hk',299,'中讯软件');
INSERT INTO "titan_stock" VALUES(356,'hk',376,'瑞东集团');
INSERT INTO "titan_stock" VALUES(357,'hk',686,'联合光伏');
INSERT INTO "titan_stock" VALUES(358,'hk',715,'中泛控股');
INSERT INTO "titan_stock" VALUES(359,'hk',934,'中石化冠德');
INSERT INTO "titan_stock" VALUES(360,'hk',1011,'泰凌医药');
INSERT INTO "titan_stock" VALUES(361,'hk',1036,'万科置业海外');
INSERT INTO "titan_stock" VALUES(362,'hk',1053,'重庆钢铁股份');
INSERT INTO "titan_stock" VALUES(363,'hk',1280,'汇银家电');
INSERT INTO "titan_stock" VALUES(364,'hk',1302,'先健科技');
INSERT INTO "titan_stock" VALUES(365,'hk',1530,'三生制药');
INSERT INTO "titan_stock" VALUES(366,'hk',2308,'研祥智能');
INSERT INTO "titan_stock" VALUES(367,'hk',2389,'正峰集团');
INSERT INTO "titan_stock" VALUES(368,'hk',3836,'和谐汽车');
INSERT INTO "titan_stock" VALUES(369,'hk',6839,'云南水务');
INSERT INTO "titan_stock" VALUES(370,'hk',6899,'联众');
INSERT INTO "titan_stock" VALUES(371,'hk',8068,'新宇国际');
INSERT INTO "titan_stock" VALUES(372,'hk',8083,'创新支付');
INSERT INTO "titan_stock" VALUES(373,'hk',8095,'北大青鸟');
INSERT INTO "titan_stock" VALUES(374,'hk',8356,'中国新华');
INSERT INTO "titan_stock" VALUES(375,'sz',2566,'益盛药业');
INSERT INTO "titan_stock" VALUES(376,'sz',938,'紫光股份');
INSERT INTO "titan_stock" VALUES(377,'sz',2302,'西部建设');
INSERT INTO "titan_stock" VALUES(378,'hk',8132,'中油港燃');
INSERT INTO "titan_stock" VALUES(379,'sh',601099,'太平洋');
COMMIT;
