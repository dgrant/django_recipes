-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: recipes_django
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipes_category`
--

DROP TABLE IF EXISTS `recipes_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `order_index` int(10) unsigned DEFAULT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_category`
--

LOCK TABLES `recipes_category` WRITE;
/*!40000 ALTER TABLE `recipes_category` DISABLE KEYS */;
INSERT INTO `recipes_category` VALUES (1,'Appetizers',NULL,'appetizers'),(2,'Desserts',NULL,'desserts'),(3,'Pies, Tarts, Pastries',NULL,'pies-tarts-pastries'),(4,'Cookies, Brownies, Cakes',NULL,'cookies-brownies-cakes'),(5,'Sauces, Spice Mixtures',NULL,'sauces-spice-mixtures'),(6,'Eggs, Breakfast, Brunch',NULL,'eggs-breakfast-brunch'),(7,'Beverages',NULL,'beverages'),(8,'Pork',NULL,'pork'),(9,'Beef',NULL,'beef'),(10,'Test',NULL,'test'),(11,'Fruits',NULL,'fruits'),(12,'Vegetables',NULL,'vegetables'),(13,'Soups',NULL,'soups'),(14,'Salads',NULL,'salads'),(15,'Pasta',NULL,'pasta'),(16,'Grains',NULL,'grains'),(17,'Breads',NULL,'breads'),(18,'Seafood',NULL,'seafood'),(19,'Poultry',NULL,'poultry'),(20,'Meat',NULL,'meat'),(21,'Beans',NULL,'beans'),(22,'Lamb',NULL,'lamb'),(23,'Mains',NULL,'mains'),(24,'Curries',NULL,'curries');
/*!40000 ALTER TABLE `recipes_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_direction`
--

DROP TABLE IF EXISTS `recipes_direction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_direction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `recipe_id` int(11) NOT NULL,
  `order` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_id_refs_id_4ca31660f2f22585` (`recipe_id`),
  CONSTRAINT `recipe_id_refs_id_4ca31660f2f22585` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=214 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_direction`
--

LOCK TABLES `recipes_direction` WRITE;
/*!40000 ALTER TABLE `recipes_direction` DISABLE KEYS */;
INSERT INTO `recipes_direction` VALUES (1,'Cook bacon.',7,0),(2,'Grease a 1.5 L baking dish',1,0),(4,'Mix sugar and cocoa.',5,0),(5,'Cook butter and onion',6,0),(6,'Add all ingredients together in large mixing bowl except baking soda and water.',2,0),(7,'Mix dry ingredients in large bowl.',3,0),(8,'Mix all ingredients together and shake well.',7,1),(9,'Prepare apples, measure, and arrange in dish.',1,1),(11,'Add corn syrup, cream, and mix. Bring to boil. Simmer 3 minutes.',5,1),(12,'Add flour, stir and cook. Remove from heat.',6,1),(13,'Dissolve baking soda in hot water and add to mixture.',2,1),(14,'Mix wet ingredients in small bowl.',3,1),(15,'Combine lettuce, parmesean cheese, bacon, and dressing. Toss.',7,2),(16,'Sprinkle with granulated sugar',1,2),(17,'Stir in butter and vanilla.',5,2),(18,'Stir in seasonings and sour cream.',6,2),(19,'Bake in greased muffin pan at 350 degrees for 20-30 minutes until golden brown.',2,2),(20,'Dust blueberries with flour.',3,2),(21,'Combine lemon juice and water. Poor over apples.',1,3),(22,'Fold in beans.',6,3),(23,'Add all ingredients until dough just moistened. Bake in greased muffin tin at 350 degrees for 15-20 minutes until golden brown.',3,3),(24,'Cream butter and gradually add brown sugar.',1,4),(25,'Place in lightly greased 2L dish.',6,4),(26,'Blend in flour and oats. Spread over apples.',1,5),(27,'Cover with grated cheese and corn flake crumbs.',6,5),(28,'Bake at 375°F  until apples are tender, about 35 minutes.',1,6),(29,'Sprinkle with dots of butter.',6,6),(30,'Serve warm, plain, or with ice cream.',1,7),(31,'Bake for 30-45 minutes at 350 degrees.',6,7),(32,'Cut chicken breasts in to 5cm x 10 cm pieces and sprinkle with pepper. Cook chicken through.',8,0),(33,'Cook broccoli but not too much, it should still be crisp.',8,1),(34,'Mix together cream of chicken, mayonaise, curry powder, and lemon juice.',8,2),(35,'Put broccoli on bottom of a casserole dish, put chicken on top, then pour sauce over top and top with cheddar cheese.',8,3),(36,'Bake for 30 minutes at 375 degrees.',8,4),(46,'Heat oil in pan over medium-low heat. Add cumin seeds and cook until they start popping.',11,0),(48,'Add chopped onions, then add salt. Cook, stirring occasionally, for up to 30 minutes or until soft and golden.',11,1),(49,'When onions are translucent add garlic and ginger.',11,2),(50,'Stir in spices and bring out flavours. Add a bit of water if it sticks too much to pot.',11,3),(52,'Add salt to taste.',11,4),(53,'Add chili powder or cayenne to taste.',11,5),(54,'Stir in tomatoes and cook for about 10 minutes.',11,6),(55,'Rinse chick peas under cold water and add.',11,7),(57,'Add water just to cover. Bring to light boil and then simmer for at least 20-30 minutes.',11,8),(58,'Fold in cilantro (saving some for garnish) at last minute and serve.',11,10),(59,'Garnish with fresh cilantro.',11,11),(60,'Add lemon juice and simmer for a few more minutes.',11,9),(62,'Add all ingredients to bowl and mix with a spoon.',12,2),(63,'Bake at 375F for 15 minutes until golden brown.',12,4),(64,'Beat in order, adding ingredients one at a time',13,0),(65,'Sift together and add to liquid mixture',13,1),(66,'Fold in boiling water',13,2),(67,'Place mixture in two prepared, round 9” cake pans.',13,3),(68,'Sprinkle with ½ cup chocolate chips.',13,4),(69,'Bake for 25 minutes.',13,5),(70,'Beat egg in mixing bowl.',12,1),(72,'Fill tart shells with the mixture.',12,3),(73,'Thaw tart shells for 5-10 minutes.',12,0),(74,'Preheat oven to 350°.',14,0),(75,'Combine all ingredients in large bowl.',14,1),(76,'Shape into loaf in 13 x 9-inch baking or roasting pan.',14,3),(77,'Bake uncovered 1 hour at 350° or until meat reaches an internal temperature of 160°. Let stand 10 minutes before serving.',14,4),(79,'Glaze: mix all ingredients together and pour on top of meat loaf.',14,2),(80,'Brown ground beef and vegetables in large saucepan.',15,0),(81,'Add spices and garlic to pot.',15,2),(82,'Add tomato sauce, tomato paste, and diced tomatoes and bring to a boil.',15,3),(83,'Simmer (and still once in a while) or boil (and stir frequently) until the the chili becomes very thick.',15,4),(84,'Stir in kidney beans and corn and cook for a few minutes.',15,5),(85,'Combine cornmeal and milk and let sit for 10 minutes.',16,0),(86,'Combine flour, sugar, baking powder, and salt in a large bowl.',16,1),(87,'Beat egg and mix with oil. Add to cornmeal mixture and mix well. Add wet ingredients to dry ingredients and stir just until combined.',16,2),(88,'Fill greased muffin cups and bake at 400°F for 15-20 minutes until just golden.',16,3),(89,'Combine all ingredients to make coleslaw',17,0),(90,'Toast buns.',17,1),(91,'Mix BBQ sauce and pulled pork.',17,3),(93,'Apply mayonnaise to sandwiches and assemble sandwiches',17,2),(94,'Mix dry ingredients together in a bowl.',18,1),(95,'Beat eggs then mix wet ingredients together in another bowl. Slowly incorporate dry ingredients into the wet. Let batter sit for 5 minutes.',18,2),(96,'Pre-heat a non-stick or cast iron frying pan to medium to medium-high heat.',18,0),(97,'Add oil to pan as necessary and scoop 1/2 cup of pancake batter into the pan for each pancake and flip when you see bubbles break the surface.',18,3),(98,'Purée galic in food processor.',19,0),(99,'Add chickpeas, tahini, spices, lemon juice, salt, pepper. Pulse.',19,1),(100,'With the food processor slowly running, slowly add the olive oil until you reach the desired consistency.',19,2),(101,'Serve with some more olive oil drizzled on top or in a well in the centre and a bit of pepper and paprika.',19,3),(102,'Cook pasta al dente.',20,1),(103,'Melt butter in saucepan.',20,2),(104,'Slowly add milk, ensuring that the consistency stays thick.',20,4),(105,'Stir in onion, cheese, mustard, nutmeg, salt, and pepper.',20,5),(106,'Toss butter and bread crumbs together and then sprinkle bread crumbs on top.',20,9),(107,'Bake at 375F for 30 minutes or until golden on top.',20,9),(108,'Add flour, stirring together to make a roux.',20,3),(109,'Brown beef with onions in large saucepan.',21,0),(110,'Add tomato paste and cook another minute or so.',21,1),(111,'Add tomatoes, tomato sauce, bouillon cubes, and spices, and simmer to reduce liquid to desired consistency.',21,2),(112,'Preheat the oven to 325°F.',22,0),(113,'Melt butter and allow to cool to room temperature. Using a large bowl, cream together the butter, brown sugar and white sugar on high speed. Note: For cookies with a chewier texture, melt the butter and let cool slightly. For a less chewy texture, just use room temperature butter.',22,1),(114,'Next, add the vanilla extract, egg, and egg yolk and beat until smooth.',22,2),(115,'Sift the flour and baking soda together. Stir in the salt. Add the dry ingredients to the wet and mix on low until everything is incorporated.',22,3),(116,'Fold in the chocolate chips.',22,4),(117,'Line a baking tray with parchment paper or spray with non-stick spray. Form equal size rounds of dough and place on baking tray. Make sure to leave enough space between each cookie as they will spread out a bit as they bake. Refrigerate for fifteen minutes before baking. Bake the cookies for 13 to 15 minutes or until the edges turn a light golden colour. Once done, cool for a few minutes before transferring to a cooling rack. Allow to cool completely before serving.',22,5),(119,'Mix flour, coconut, and rolled oats.',23,0),(120,'Cream butter; gradually add brown sugar.',23,1),(121,'Dissolve soda in water. Gradually stir into creamed mixture.',23,2),(122,'Add vanilla to wet ingredients. Add flour mixture to wet ingredients, a part at a time.',23,3),(123,'Stir in chocolate chips.',23,4),(124,'Drop by spoonful on greased baking sheet. Press with fork. Bake at 375°F for 8-10 minutes.',23,5),(125,'Sprinkle cheese on top.',20,7),(126,'Combine sauce with pasta.',20,6),(127,'Preheat oven to 375°F',20,0),(128,'Combine the breadcrumbs and heavy cream in a small bowl, stirring with a fork until all the crumbs are moistened. Set aside.',24,0),(129,'Heat the oil in a small skillet over medium heat. Add the onion and sauté for about five minutes, until softened. Remove from heat.',24,1),(130,'In a large bowl, combine the ground beef, ground pork, onion, sugar and egg, salt, and pepper and mix well with your hands.',24,2),(131,'Add the breadcrumb-cream mixture and mix well. With wet hands (to keep the mixture from sticking), shape the mixture into meatballs the size of a golf ball, placing them on a plate lightly moistened with water. You should have about 24 meatballs.',24,3),(132,'Melt the butter in a large skillet over medium-high heat. Add the meatballs, in batches if necessary, and cook, turning frequently, for about 7 minutes until browned on all sides and cooked through. Transfer the meatballs to a plate and drain off all but 1 tablespoon of fat from the skillet.',24,4),(133,'The night before, combine all ingredients in a big bowl with a wooden spoon until the dough just comes together. It will be a shaggy, doughy mess. Cover with plastic wrap and let sit 12-20 hours on countertop.',25,0),(134,'The dough will now be wet, sticky and bubbly. Dump the dough on to a floured surface. Flour hands. Fold ends of dough over top few times with your hands until you have a smooth bottom and a top with seams. The seam side is the side that should be facing up while baking. Place a large sheet of parchment paper on counter. Plop your dough onto parchment paper seam side up, then lift parchment paper up with dough and place into a large bowl. Cover bowl with a towel. If you do not have parchment paper, plop dough seam side down onto a floured towel and cover with another towel.',25,1),(135,'Your dough should have doubled in size. Remove pot from oven. Grab the ends of the parchment paper and lift entire wobbly dough blob out of bowl and into pot (seam side up). Or, if on a towel, invert dough blob into pot (seam side up). Shake to even dough out if necessary. Cover and bake 30 minutes. Uncover, bake another 20 minutes or until the crust is beautifully golden. Remove and let cool on wired rack. If not eating right away, you can re-crisp crust in 350°F oven for 10 minutes.',25,3),(136,'Mix corn starch and cold water, then dump into pot and stir.',15,1),(137,'Fry meat, onion, and celery until meat is browned.',26,0),(138,'Add bean sprouts and cook 5 minutes more.',26,1),(139,'Add to cooked Catelli noodles.',26,2),(140,'Season with salt, pepper, and soy sauce to taste.',26,3),(141,'Place in 2 greased casserole dishes. Bake 1 hour at 300°F.',26,4),(142,'To prepare the leeks, cut off the root end and dark green parts. For the white and light green part, cut in half lengthwise and then cut across into fairly thin strips.',27,0),(143,'In a large pot or saucepan, add the butter and melt over medium heat. Once the butter has melted, add the onions and sweat for about 5 minutes until they start to soften. Next, add the garlic and cook for another minute or so. Add the leeks and salt and stir. Cover with a lid and let sweat over medium heat for about 8 minutes or until the leeks soften. Stir occasionally.',27,1),(144,'Peel, quarter the potatoes lengthwise and finely slice. Add the potatoes and stir to combine.',27,2),(145,'Add hot stock (more or less) to just to cover the ingredients. Bring the soup to a simmer. Cover and let cook over medium-low heat for about 10 minutes or just until the potatoes have just cooked through.',27,3),(146,'Take the soup off of the heat. Purée the soup on high for at least 1 minute, in batches if necessary. For velvety-smooth soup, strain the soup through a fine sieve, pressing out the solids, using the back of a ladle or spatula. Once done, transfer the soup back into a pot. If you need to thin the soup out, you can add a bit more hot stock and/or heavy cream, if desired. For a chunky soup, only purée half the soup.',27,4),(147,'Season to taste.',27,5),(148,'Garnish the soup with chives and a drizzle of heavy cream.',27,6),(149,'Add to large pot and cook on medium heat for about 15 minutes until carrots are soft but still holding their shape.',28,0),(150,'Pour in stock, tomatoes, and sugar. Bring to boil then reduce heat and simmer for 10 minutes.',28,1),(151,'Remove pot from heat and purée using a hand blender.',28,2),(152,'Add herbs and spices. Season to taste.',28,3),(153,'Put all ingredients in bread maker on dough cycle and press start.',29,0),(154,'On a lightly floured surface, roll into a 16x12 inch rectangle. Cut dough in half, creating two 8x12 inch rectangles. Roll up each half of dough tightly, beginning at 12 inch side, pounding out any air bubbles as you go. Tuck in ends if necessary and place 3 inches apart on a greased cookie sheet (or use parchment paper) seam-side down. Make deep diagonal slashes across loaves every 2 inches, or make one lengthwise slash on each loaf. Cover, and let rise in a warm place for 30 to 40 minutes, or until doubled in bulk.',29,1),(155,'Preheat oven to 375 degrees F (190 degrees C). Mix egg yolk with 1 tablespoon water; brush over tops of loaves.\r\nBake for 25 minutes in the preheated oven, or until golden brown.',29,2),(156,'Let it rest for 2 hours. When you\'ve got about a half hour left, slip your covered pot into the oven and preheat to 450F.',25,2),(157,'To make the béchamel, heat a saucepan over medium heat and melt the butter. Once melted, add the flour to create a roux and stir until smooth. Cook for about 6 to 7 minutes, stirring frequently, until it turns a light-golden brown.',30,0),(158,'Meanwhile, in a separate pot or in the microwave, heat the milk to just under a boil. ',30,1),(159,'Once the mixture has browned and the milk has heated, add the milk to the roux, about one cup at a time. Whisk constantly, until very smooth, bringing it back to a boil each time. Once all of the milk has been incorporated and the mixture has come back up to a gentle boil, turn the heat to low and let cook for about 10 minutes. Stir occasionally. The sauce should nicely coat the back of a spoon. ',30,2),(160,'Once done, remove from the heat and season with the salt and if using in an Italian dish, freshly-grated nutmeg.',30,3),(161,'Transfer to a bowl and place plastic wrap directly onto the surface, to prevent a skin from forming. Leave a bit of space around the edges for the steam to escape while it cools.',30,4),(162,'Pour lentils into a medium sauce pan. Add water and bring to boil. Reduce heat, cover and simmer for 10 minutes.',31,0),(163,'While the lentils are cooking, bring a pot of water to boil. Score the peel of the tomatoes with a sharp knife in the shape of an \"X\". Place the tomatoes in the boiling water and blanch for one minute. Remove the tomatoes, and once cool, peel the tomatoes and cut out and discard the tough stem end. Chop the tomatoes, and set aside.',31,1),(164,'After the lentils have cooked at least 5 minutes, start preparing the onions and spices. In a medium saucepan, heat the oil over medium heat. Add the chopped onions and cook until translucent, about 3 minutes. Add garlic and cook for 1 minute more, stirring continuously, making sure that the garlic does not burn. Add the Bengali five spice. Cook and stir for another 2-3 minutes. Add bay leaf and turmeric. Stir.',31,2),(165,'Add the cooked lentils to the onions and spices, along with the lentil cooking water. Add salt. Cook for 10 minutes. Add lime juice and tomatoes. Cook for 3-5 more minutes. Adjust salt if necessary. Stir in chopped cilantro and remove from heat. Garnish with more chopped cilantro.',31,3),(166,'Serve with basmati rice or naan bread.',31,4),(170,'Heat up a wok on high heat, add oil, and stir fry onions, peas, carrots. Add praws and stir until almost cooked through.',33,0),(171,'Move the onion, peas and carrots to the outside of the wok, and pour the beaten eggs into the centre. Scramble the eggs. Once cooked, mix the eggs with the vegetable mix.',33,1),(172,'Add the rice to the veggie and egg mixture. Pour the soy sauce on top. Stir and fry the rice and veggie mixture until heated through and combined. Add chopped green onions if desired.',33,2),(173,'Arrange potatoes in large microwave-safe bowl, top with 1 tablespoon butter, and cover tightly with plastic wrap. Microwave on high until edges of potatoes begin to soften, 5 to 7 minutes, shaking bowl (without removing plastic) to redistribute potatoes halfway through cooking.',34,0),(174,'Melt remaining 2 tablespoons butter in now-empty skillet over medium heat. Add potatoes and pack down with spatula. Cook, without moving, until underside of potatoes is brown, 5 to 7 minutes. Turn potatoes, pack down again, and continue to cook until well browned and crisp, 5 to 7 minutes. Reduce heat to medium-low and continue cooking, stirring potatoes every few minutes, until crusty and golden on all sides, 9 to 12 minutes.',34,2),(175,'Stir in onion, seasonings of your choice and salt and pepper to taste.',34,3),(176,'Melt 1 tablespoon butter in large cast iron skillet over medium heat. Add onion and cook until softened and golden brown, about 6 minutes. Transfer to a bowl.',34,1),(177,'Combine the soy sauce, sugar, sherry, vinegar, garlic, ginger and red pepper flakes and stir until the sugar dissolves. Transfer to a resealable plastic bag and add the chicken. Seal the bag and marinate the chicken in the refrigerator, turning once, for 1 hour. The chicken can be marinated for up to 4 hours.',35,0),(178,'Heat the broiler to high. Arrange the chicken on a broiler pan skin side down and broil until brown and crispy, 8 to 10 minutes.',35,1),(179,'Flip the chicken and broil until almost cooked through, about 8 minutes longer. Sprinkle with sesame seeds and cook until the seeds turn golden brown and the chicken is done, 1 to 2 minutes longer.',35,2),(180,'Whisk or shake all ingredients together.',36,0),(181,'Toss dressing with coleslaw mix.',36,1),(182,'Preheat oven to 375F degrees. Line two large cookie sheets with parchment paper or silicone baking mats. Set aside.',37,0),(183,'Toss sugar with cinnamon in a small bowl. Set aside.\r\n',37,1),(184,'In a large bowl using a hand-held mixer or stand mixer with paddle attachment, cream the softened butter for about 1 minute on medium speed. Get it nice and smooth, then add the sugar on medium speed until fluffy and light in color. Mix in egg and vanilla. Scrape down the sides as needed. Set aside.\r\n',37,2),(185,'In a medium size bowl, whisk together the flour, cream of tartar, baking soda, cinnamon, and salt. With the mixer running on low speed, slowly add the dry ingredients to the wet ingredients in 3 different parts. The dough is quite thick and you may have to stir the rest by hand.\r\n',37,3),(186,'Take 1.5 - 2 Tablespoons of dough and roll into a ball. Roll the dough balls into the reserved cinnamon-sugar topping. Sprinkle extra cinnamon-sugar on top if desired. Bake cookies for 11-12 minutes. The cookies will be very puffy and soft. When they are still very warm, lightly press down on them with the back of a spoon or fork to help flatten them out. Allow cookies to cool on the baking sheet for 10 minutes and transfer to a wire rack to cool completely. Cookies remain soft & fresh for 7 days in an airtight container at room temperature.',37,4),(187,'Preheat your oven to 400°F (200°C). Toss the tomatoes, onions, garlic, sausages, and olive oil together. Season to your taste with salt and pepper. Transfer to a roasting pan and place in the oven. Roast until the tomatoes, onion, and sausages are lightly brown and smell amazing, 30 to 45 minutes.',38,0),(188,'When the tomatoes are nearly done, bring a large pot of salted water to a full rolling boil. Dump in the penne and cook until al dente. Reserve some of the cooking liquid for later.',38,1),(189,'While the pasta is cooking, stack a tall pile of basil leaves, roll it into a tight cylinder, and slice as thinly as possible. Slice the green onions as well.',38,2),(190,'As the pasta finishes cooking, add a ladleful of the pasta water to the roasting pan. The moisture will dissolve any caramelized brown bits of flavour on the bottom of the pan. When the pasta is done, drain it and return it to the pot. Add the roasted sausages, onions, and tomatoes, scraping along every last bit of roasted flavour from the pan. Toss in the basil leaves and green onions and stir everything together.',38,3),(191,'Blah blah',39,0),(192,'Cook onion, carrot, celery, ground meats, beef stock, and bouillon cube on high heat in beef broth for about 30 minutes or until broth is reduced and the carrots, onions, and celery are soft.',40,0),(193,'When the stock has been reduced, add garlic and salt and cook for 10 minutes more. If using stock that contains salt, modify amount of added salt accordingly.',40,1),(194,'Add more beef broth, bring to boil, then reduce heat to simmer until most liquid is gone, about another 30 minutes or longer.',40,2),(195,'Turn off heat and add bread crumbs and stir which should soak up remaining liquid and fat.',40,4),(196,'Add spices and stir and cook another 5 minutes.',40,3),(197,'Preheat oven to 425 degrees F. Line a pie plate with pastry. Spoon in filling, spreading evenly. Cover with top crust. Cover edges of pie with strips of aluminum foil.',40,5),(198,'Slice chicken into thin slices and toss with ginger garlic paste, salt, and paprika (OR chilli powder), and shallow fry in oil and set aside.',41,0),(199,'To the leftover oil add, cumin, onion, ginger/garlic paste.',41,1),(200,'Add onion, tomatoes, cashews, and other spices and cook covered with a little water until everything is cooked through and soft.',41,2),(201,'Blend.',41,3),(202,'Melt butter in the pan, add blended ingredients and cook for a few minutes',41,4),(203,'Add chicken and cook for few more minutes. Add ketchup, stir in coriander leaves and serve.',41,5),(204,'Blend flour, sugar, and salt in processor.',42,0),(205,'Add butter and lard; using on/off turns, blend until mixture resembles coarse meal.',42,1),(206,'Transfer mixture to medium bowl. Add 5 tablespoons ice water and mix with fork until dough begins to clump together, adding more water by teaspoonfuls if dry.',42,2),(207,'Gather dough together. Divide dough in half; flatten each half into disk. Wrap each disk in plastic and refrigerate at least 1 hour. Keep refrigerated. If necessary, soften slightly at room temperature before rolling out.',42,3),(208,'Brush with beaten egg, if desired. Cut steam vent. Bake in preheated oven for 20 minutes; remove foil and return to oven. Bake for an additional 15 to 20 minutes, or until golden brown. Let cool 10 minutes before slicing.',40,6),(209,'Remove skin from underside of ribs.',43,0),(210,'Salt ribs, 1/2 tsp per side.',43,1),(211,'Apply rub, water first to wet them a bit, 2 Tbsp per side.',43,2),(212,'Cook ribs at 225',43,3),(213,'Apply BBQ sauce (1/3 cup per rack) and let caramelize on ribs for about 15 minutes.',43,4);
/*!40000 ALTER TABLE `recipes_direction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_food`
--

DROP TABLE IF EXISTS `recipes_food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_food` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `group_id` int(11) NOT NULL,
  `name_sorted` varchar(150) NOT NULL,
  `conversion_src_unit_id` int(11) DEFAULT NULL,
  `conversion_factor` double DEFAULT NULL,
  `name_plural` varchar(150) DEFAULT NULL,
  `detail` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `group_id_refs_id_47ae550f7b29cf1f` (`group_id`),
  KEY `recipes_food_6fa761cf` (`conversion_src_unit_id`),
  CONSTRAINT `conversion_src_unit_id_refs_id_3e0ebbff` FOREIGN KEY (`conversion_src_unit_id`) REFERENCES `recipes_unit` (`id`),
  CONSTRAINT `group_id_refs_id_47ae550f7b29cf1f` FOREIGN KEY (`group_id`) REFERENCES `recipes_foodgroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_food`
--

LOCK TABLES `recipes_food` WRITE;
/*!40000 ALTER TABLE `recipes_food` DISABLE KEYS */;
INSERT INTO `recipes_food` VALUES (2,'apples',4,'apples',NULL,NULL,NULL,''),(4,'baking powder',1,'baking powder',2,241,'',''),(5,'baking soda',1,'baking soda',2,305,'',''),(6,'mashed banana',4,'banana, mashed',2,247,'',''),(7,'Beau Monde seasoning',5,'seasoning, Beau Monde',NULL,NULL,'','Beau Monde is a Spice Islands brand seasoning. Substitute: 2 parts onion powder, 2 parts celery salt, 1 part superfine sugar'),(8,'blueberries',4,'blueberries',NULL,NULL,NULL,''),(9,'unsalted butter',3,'butter, unsalted',2,227,NULL,''),(10,'grated cheddar cheese',3,'cheese, cheddar, grated',NULL,NULL,'',''),(11,'grated parmesean cheese',3,'cheese, parmesean, grated',NULL,NULL,'',''),(12,'chicken stock (low-sodium)',12,'stock, chicken (low-sodium)',NULL,NULL,'',''),(13,'cocoa, packed',1,'cocoa, packed',2,128,'',''),(14,'corn Flake crumbs',1,'corn Flake crumbs',NULL,NULL,'',''),(15,'corn syrup',1,'corn syrup',2,330,'',''),(16,'12% cream',3,'cream, 12%',NULL,NULL,NULL,''),(17,'dijon mustard',2,'mustard, dijon',NULL,NULL,NULL,''),(18,'large egg',10,'egg, large',NULL,51,'large eggs',''),(19,'all-purpose flour',1,'flour, all-purpose',2,125,'','A combination of hard and soft wheat is milled to produce all-purpose flour. The resulting medium protein content (between 9% and 12%) offers just the right balance of strength and tenderness for the everyday baker to make chewy breads, delicate tarts and everything in between.'),(20,'clove garlic',13,'garlic, clove',NULL,4,'cloves garlic',''),(21,'canned green beans',13,'beans, green, canned',NULL,NULL,'',''),(22,'honey',2,'honey',NULL,NULL,NULL,''),(23,'lemon juice',6,'lemon juice',2,240,NULL,''),(24,'milk',3,'milk',2,237,NULL,''),(25,'MSG',5,'MSG',NULL,NULL,NULL,''),(26,'mustard powder',5,'mustard powder',NULL,NULL,NULL,''),(27,'rolled oats, large',1,'oats, rolled, large',2,NULL,'','Also knows as old-fashioned rolled oats, these are the thickest rolled oat, which retain their shape fairly well during cooking, as opposed to quick or instant oats which are pressed thinner and which lose their texture when cooked.'),(28,'vegetable oil',2,'oil, vegetable',2,208,NULL,''),(29,'onion',13,'onion',NULL,NULL,'onions',''),(30,'black pepper',5,'pepper, black',NULL,NULL,'',''),(31,'coarse ground pepper',5,'pepper, coarse ground',NULL,NULL,NULL,''),(32,'salt',1,'salt',10,18,'','Table salt. If substituting with kosher or seas salt and measuring in volume, use about 20% more.'),(33,'sour cream',3,'sour cream',2,240,NULL,''),(34,'white granulated sugar',1,'sugar, white granulated',2,200,'',''),(35,'packed brown sugar',1,'sugar, brown, packed',2,245,'',''),(36,'tabasco sauce',2,'tabasco sauce',NULL,NULL,NULL,''),(37,'vanilla extract',1,'vanilla, extract',10,15,'',''),(38,'apple cider vinegar',2,'vinegar, apple cider',2,240,'',''),(39,'white vinegar',2,'vinegar, white',NULL,NULL,'',''),(40,'water',17,'water',13,1,'',''),(41,'Worcestershire sauce',11,'Worchestershire sauce',10,16,'',''),(42,'chicken breasts',7,'chicken, breasts',NULL,NULL,NULL,''),(43,'broccoli',13,'broccoli',NULL,NULL,NULL,''),(44,'cream of chicken soup',12,'soup, cream of chicken',NULL,NULL,NULL,''),(45,'mayonnaise',2,'mayonnaise',2,227,NULL,''),(46,'curry powder',5,'curry powder',NULL,NULL,NULL,''),(47,'stewing beef',7,'beef, stewing',NULL,NULL,NULL,''),(48,'soft shortening',1,'shortening, soft',NULL,NULL,NULL,''),(49,'chopped walnuts',1,'walnuts, chopped',2,128,'',''),(50,'cumin seeds',5,'cumin, seeds',NULL,NULL,NULL,''),(51,'fresh ginger',13,'ginger, fresh',NULL,NULL,NULL,''),(52,'garam masala',5,'garam masala',NULL,NULL,NULL,''),(53,'coriander',5,'coriander',NULL,NULL,NULL,''),(54,'cumin',5,'cumin',NULL,NULL,NULL,''),(55,'turmeric',5,'turmeric',NULL,NULL,NULL,''),(56,'cardamom pods',5,'cardamom, pods',NULL,NULL,NULL,''),(57,'chili powder',5,'chili, powder',NULL,NULL,NULL,''),(58,'can stewed whole tomatoes',14,'tomatoes, stewed whole',NULL,NULL,'cans stewed whole tomatoes',''),(59,'chick peas',14,'chick peas',NULL,NULL,NULL,''),(60,'bay leaves',5,'bay leaves',NULL,NULL,NULL,''),(61,'tamarind juice',6,'tamarind, juice',NULL,NULL,NULL,''),(62,'plain 3% yogurt',3,'yogurt, plain 3%',NULL,NULL,NULL,''),(63,'dry mango powder',5,'mango powder, dry',NULL,NULL,NULL,''),(64,'cilantro',13,'cilantro',NULL,NULL,NULL,''),(65,'medium unsweetened coconut',1,'coconut, medium unsweetened',2,84,'',''),(66,'Chipits chocolate chips',1,'chocolate, chips (Chipits)',2,152,'',''),(67,'buttermilk',3,'buttermilk',NULL,NULL,NULL,''),(68,'3\" tart shells',15,'tart shells, 3\"',NULL,NULL,'',''),(70,'bread crumbs',16,'bread crumbs',2,124,'',''),(71,'ketchup',2,'ketchup',2,280,'',''),(72,'cornmeal',1,'cornmeal',2,150,'',''),(73,'lean ground beef',7,'beef, ground, lean',NULL,NULL,'',''),(74,'coarse black pepper',18,'black pepper, coarse',NULL,NULL,'',''),(75,'beef stock (low-sodium)',12,'stock, beef (low-sodium)',2,250,'',''),(76,'dried thyme',18,'thyme, dried',NULL,NULL,'',''),(77,'kosher salt',18,'salt, kosher',NULL,NULL,'',''),(78,'minced garlic',18,'garlic, minced',NULL,NULL,'',''),(79,'grainy Dijon mustard',2,'mustard, grainy Dijon',10,12,'',''),(80,'cayenne',18,'cayenne',NULL,NULL,'',''),(81,'diced canned tomatoes',14,'tomatoes, canned, diced',NULL,NULL,'',''),(82,'corn starch',1,'corn starch',NULL,NULL,'',''),(83,'oregano',18,'oregano',NULL,NULL,'',''),(84,'paprika',18,'paprika',NULL,NULL,'',''),(85,'28 fl. oz. can diced tomatoes',14,'tomatoes, diced, 28 fl. oz. can',NULL,NULL,'',''),(86,'tomato sauce',14,'tomato sauce',NULL,NULL,'',''),(87,'canned kidney beans',14,'beans, kidney, canned',NULL,NULL,'',''),(88,'shredded cabbage',13,'cabbage, shredded',2,60,'',''),(89,'olive oil',2,'oil, olive',NULL,NULL,'',''),(90,'pulled pork',7,'pork, pulled',NULL,NULL,'',''),(91,'BBQ sauce',2,'BBQ sauce',NULL,NULL,'',''),(92,'small hamburger buns',16,'buns, hamburger, small',NULL,NULL,'',''),(93,'19 floz. can chick peas',19,'chick peas, 19 floz. can',NULL,NULL,'',''),(94,'tahini',2,'tahini',NULL,NULL,'',''),(95,'macaroni',20,'pasta, macaroni',NULL,NULL,'',''),(96,'butter',3,'butter',2,227,'',''),(97,'can tomato sauce',14,'tomato, sauce, canned',NULL,NULL,'',''),(98,'chicken bouillon cube',12,'bouillon cube, chicken',NULL,NULL,'chicken bouillon cubes',''),(99,'Clubhouse brand Italian spice mix',18,'spice mix, Italian, Clubhouse brand',NULL,NULL,'',''),(100,'can tomato paste',14,'tomato, paste, canned',NULL,NULL,'cans tomato paste',''),(101,'large egg yolk',3,'egg, yolk, large',NULL,NULL,'',''),(102,'nutmeg',18,'nutmeg',NULL,NULL,'',''),(103,'ground pork',7,'pork, ground',NULL,NULL,'',''),(104,'red onion',13,'onion, red',NULL,NULL,'',''),(105,'slice of bacon',7,'bacon, slice',NULL,NULL,'slices of bacon',''),(106,'cinnamon',18,'cinammon',10,9,'',''),(108,'green bell pepper',13,'pepper, bell, green',NULL,NULL,'',''),(109,'stalk of celery',13,'celery, stalk',NULL,NULL,'stalks of celery',''),(110,'can of corn',14,'corn, canned',NULL,NULL,'',''),(111,'package Catelli fine thin noodles',20,'pasta, fine thin, Catelli',NULL,NULL,'packages Catelli fine thin noodles','Can be substituted with Vermicelli or any other type of thin wheat noodle.'),(112,'package bean sprouts',13,'sprouts, bean, package',NULL,300,'packages bean sprouts',''),(113,'soy sauce',11,'soy sauce',NULL,NULL,'',''),(114,'large leek',13,'leek, large',NULL,200,'large leeks',''),(115,'large russet potato',13,'potato, russet, large',NULL,200,'large russet potatoes',''),(116,'heavy cream',3,'cream, heavy (>36%)',NULL,NULL,'','Heavy cream is any cream with a fat content of 36% or more.'),(117,'chives',13,'chives',NULL,NULL,'',''),(118,'white pepper',18,'pepper, white',NULL,NULL,'',''),(119,'onion powder',18,'onion powder',NULL,NULL,'',''),(120,'celery salt',18,'celery salt',NULL,NULL,'',''),(121,'head green leaf lettuce',13,'lettuce, green leaf, head',NULL,NULL,'heads green leaf lettuce',''),(122,'carrot',13,'carrot',NULL,NULL,'carrots',''),(123,'large tomato',13,'tomato, large',NULL,NULL,'large tomatoes',''),(124,'fresh basil',5,'basil, fresh',NULL,NULL,'',''),(125,'basil',5,'basil',NULL,NULL,'basil',''),(126,'quick-rise instant dry yeast',1,'yeast, dry, quick-rise instant',NULL,NULL,'','For example: Fleischmann\'s® Quick-Rise Yeast'),(127,'Icing sugar',1,'sugar, icing',2,140,'',''),(128,'whole milk',3,'milk, whole',NULL,NULL,'',''),(129,'quick oats',1,'oats, rolled, quick',2,100,'','Also known as rolled oats, quick variety rolled oats are thinner than large flakes (though not as thin as \"minute\" style) and have good texture.'),(130,'split red lentils',21,'lentils, red, split',2,180,'','Split red lentils are made from splitting the whole red lentil. The skin is removed and the remaining reddish-orange seed is then split into two halves.'),(131,'plum tomato',13,'tomato, plum',NULL,NULL,'plum tomatoes',''),(132,'panch phoron',22,'panch phoron',NULL,NULL,'',''),(133,'lime',4,'lime',NULL,NULL,'limes',''),(134,'instant mashed potato flakes',13,'potatoes, instant mashed, flakes',2,70,'','Instant mashed potatoes are potatoes that have been through an industrial process of cooking, mashing and dehydrating to yield a packaged convenience food that can be reconstituted by adding hot water or milk, producing a close approximation of mashed potatoes.'),(135,'Wheat bran',1,'bran, wheat',2,59,'',''),(136,'basmati rice',23,'rice, basmati, white',2,186,'',''),(137,'Granny Smith apple',4,'apples, Granny Smith',NULL,NULL,'Granny Smith apples','Granny Smith apples have a hard, light green skin and a crisp, juicy flesh. They go from being yellow to turning completely green. The acidity mellows significantly, and it then takes on a balanced flavour. They are commonly used in pie baking.'),(138,'Sesame oil',17,'oil, sesame',NULL,NULL,'','Sesame oil is an edible vegetable oil derived from sesame seeds. Besides being used as a cooking oil in South India, it is often used as a flavor enhancer in Chinese, Japanese, Middle Eastern, Korean, and Southeast Asian cuisine.'),(139,'green peas',13,'peas, green',NULL,NULL,'',''),(140,'diced carrot',13,'carrot, diced',NULL,NULL,'diced carrots',''),(141,'cooked white rice',23,'rice, white, cooked',NULL,NULL,'',''),(142,'prawn',24,'prawn',NULL,NULL,'prawns',''),(143,'green onion',13,'onion, green',NULL,NULL,'green onions',''),(144,'whole black lentil',21,'lentil, black, whole',2,200,'whole black lentils','Vigna mungo, black gram, black lentil, is popular in India, largely used to make dal from the whole or split, dehusked seeds.'),(145,'dry kidney beans',21,'beans, kidney, dried',2,170,'','Red kidney beans are commonly used in chili con carne and are an integral part of the cuisine in northern regions of India and Pakistan.'),(146,'Yukon Gold potato',13,'potato, Yukon Gold',NULL,NULL,'Yukon Gold potatos','Yukon Gold is a large variety of potato most distinctly characterized by its thin, smooth eye free skin and yellow tinged flesh. Unlike some other potato varietals the Yukon Gold can stand up to both dry heat and wet heat cooking methods. Its waxy moist flesh and sweet flavour make it ideal for boiling, baking and frying but these potatoes will also withstand grilling, pan frying, and roasting.'),(147,'seasoning salt',22,'seasoning salt',NULL,NULL,'','Seasoned salt is a blend of table salt, herbs, spices, other flavourings, and sometimes monosodium glutamate (MSG). Common brands include Hy\'s and Lawry\'s.'),(148,'garlic powder',18,'garlic powder',NULL,NULL,'',''),(149,'Idahoan potato flakes',13,'potato, Idahoan flakes',2,70,'',''),(150,'roasted bell pepper and garlic seasoning',22,'seasoning, roasted bell pepper',NULL,NULL,'',''),(151,'dry sherry',25,'wine, sherry, dry',NULL,NULL,'',''),(152,'rice vinegar',2,'vinegar, rice',NULL,NULL,'',''),(153,'chili pepper flakes',18,'pepper, chili, flakes',NULL,NULL,'',''),(154,'chicken thighs (skinless)',7,'chicken, thighs, skinlesss',NULL,NULL,'',''),(155,'sesame seeds',26,'sesame, seeds',NULL,NULL,'',''),(156,'seasoned rice vinegar',2,'vinegar, rice, seasoned',NULL,NULL,'',''),(157,'prepared horseradish',2,'horseradish, prepared',NULL,NULL,'',''),(158,'coleslaw mix',13,'coleslaw mix',NULL,NULL,'',''),(159,'cream of tartar',1,'cream of tartar',NULL,NULL,'',''),(160,'cherry tomato',13,'tomato, cherry',NULL,NULL,'cherry tomatoes',''),(161,'Italian sausage',7,'sausages, Italian',NULL,NULL,'Italian sausages',''),(162,'penne pasta',20,'pasta, penne',NULL,NULL,'',''),(163,'batch spaghetti sauce',20,'Recipes, spaghetti sauce, 1 batch',NULL,NULL,'batches Spaghetti sauce',''),(164,'Lasagna noodles, express',20,'Express Lasagna noodles',NULL,NULL,'',''),(165,'mozarella cheese',3,'cheese, mozarelle',NULL,NULL,'',''),(166,'batch betchamel sauce',11,'Recipes, bechamel',NULL,NULL,'batches betchamel sauce',''),(167,'summer savoury',5,'savoury, summer',NULL,NULL,'',''),(168,'finely ground pepper',5,'pepper, finely ground',NULL,NULL,'',''),(169,'ground cloves',5,'cloves, ground',NULL,NULL,'',''),(170,'ground allspice',5,'allspice, ground',NULL,NULL,'',''),(171,'ground sage',5,'sage, ground',NULL,NULL,'',''),(172,'beef bouillon cube',12,'bouillon cube, beef',NULL,NULL,'',''),(173,'ginger/garlic paste',18,'ginger/garlic paste',NULL,NULL,'',''),(174,'ground chili',18,'chili, ground',NULL,NULL,'ground chillies','Pure ground chillies, not Mexican/Tex-Mex style chili powder.'),(175,'cashew nut',26,'nut, cashew',NULL,NULL,'cashew nuts',''),(176,'lard',1,'lard',NULL,NULL,'',''),(177,'saltless rib rub',5,'rub, saltless rib',NULL,NULL,'',''),(178,'baby back pork ribs',7,'pork, ribs, baby back',NULL,NULL,'','');
/*!40000 ALTER TABLE `recipes_food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_foodgroup`
--

DROP TABLE IF EXISTS `recipes_foodgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_foodgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_foodgroup`
--

LOCK TABLES `recipes_foodgroup` WRITE;
/*!40000 ALTER TABLE `recipes_foodgroup` DISABLE KEYS */;
INSERT INTO `recipes_foodgroup` VALUES (1,'Baking'),(2,'Condiments'),(3,'Dairy'),(4,'Fruit'),(5,'Herbs & Spices'),(6,'Juice'),(7,'Meat'),(10,'Poultry'),(11,'Sauces'),(12,'Soup'),(13,'Vegetable'),(14,'Canned'),(15,'Frozen Pastry'),(16,'Bread'),(17,'Misc'),(18,'spices'),(19,'Dip'),(20,'Pasta'),(21,'legumes'),(22,'spice mixes'),(23,'grains'),(24,'Seafood'),(25,'Alcohol'),(26,'Nuts');
/*!40000 ALTER TABLE `recipes_foodgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_ingredient`
--

DROP TABLE IF EXISTS `recipes_ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_ingredient` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` double DEFAULT NULL,
  `amountMax` double DEFAULT NULL,
  `unit_id` int(11) DEFAULT NULL,
  `recipe_id` int(11) NOT NULL,
  `food_id` int(11) NOT NULL,
  `prep_method_id` int(11) DEFAULT NULL,
  `order_index` int(10) unsigned DEFAULT NULL,
  `direction_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `unit_id_refs_id_36e06e969f141ae6` (`unit_id`),
  KEY `recipe_id_refs_id_1fad087d5e1489a0` (`recipe_id`),
  KEY `food_id_refs_id_6cfc5050cfec02fc` (`food_id`),
  KEY `direction_id_refs_id_1381270ec71efa6a` (`direction_id`),
  KEY `prep_method_id_refs_id_5f9eabd13618a9e8` (`prep_method_id`),
  CONSTRAINT `food_id_refs_id_6cfc5050cfec02fc` FOREIGN KEY (`food_id`) REFERENCES `recipes_food` (`id`),
  CONSTRAINT `prep_method_id_refs_id_5f9eabd13618a9e8` FOREIGN KEY (`prep_method_id`) REFERENCES `recipes_prepmethod` (`id`),
  CONSTRAINT `recipe_id_refs_id_1fad087d5e1489a0` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`),
  CONSTRAINT `recipes_in_direction_id_52d0f01cb1a7374f_fk_recipes_direction_id` FOREIGN KEY (`direction_id`) REFERENCES `recipes_direction` (`id`),
  CONSTRAINT `unit_id_refs_id_36e06e969f141ae6` FOREIGN KEY (`unit_id`) REFERENCES `recipes_unit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=426 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_ingredient`
--

LOCK TABLES `recipes_ingredient` WRITE;
/*!40000 ALTER TABLE `recipes_ingredient` DISABLE KEYS */;
INSERT INTO `recipes_ingredient` VALUES (1,4,NULL,NULL,7,105,3,0,1),(13,1,NULL,2,5,34,NULL,0,4),(14,0.5,NULL,2,5,13,NULL,1,4),(15,0.5,NULL,NULL,6,29,11,0,5),(16,3,NULL,10,6,9,NULL,1,5),(17,0.5,NULL,2,2,9,7,0,6),(18,0.5,NULL,2,2,34,NULL,1,6),(19,1,NULL,NULL,2,18,8,2,6),(20,1.5,NULL,2,2,19,NULL,3,6),(21,1,NULL,2,2,6,NULL,4,6),(22,0.5,NULL,11,2,37,NULL,5,6),(23,2,NULL,2,3,19,NULL,0,7),(24,1,NULL,2,3,34,NULL,1,7),(25,4,NULL,11,3,4,NULL,2,7),(26,0.125,NULL,11,3,32,NULL,3,7),(27,1,NULL,11,7,23,NULL,9,8),(28,1,NULL,11,7,32,NULL,0,8),(29,1.5,NULL,11,7,34,NULL,1,8),(31,1,NULL,11,7,26,NULL,2,8),(32,1,NULL,11,7,41,NULL,10,8),(33,1,NULL,11,7,31,NULL,4,8),(34,1,NULL,11,7,25,NULL,7,8),(35,1,NULL,NULL,7,20,NULL,8,8),(36,0.25,NULL,2,7,38,NULL,11,8),(37,0.75,NULL,2,7,28,NULL,11,8),(38,0.25,NULL,2,7,11,NULL,0,15),(39,4.5,NULL,2,1,137,5,0,9),(41,1,NULL,2,5,15,NULL,0,11),(42,0.5,NULL,2,5,16,NULL,1,11),(43,2,NULL,10,6,19,NULL,0,12),(44,1,NULL,11,2,5,NULL,0,13),(45,1,NULL,10,2,40,10,1,13),(46,0.5,NULL,2,3,24,NULL,0,14),(47,0.5,NULL,2,3,28,NULL,1,14),(48,2,NULL,NULL,3,18,NULL,2,14),(49,1,NULL,11,3,37,NULL,3,14),(50,1.5,NULL,2,3,8,NULL,4,20),(51,2,NULL,2,1,34,NULL,0,16),(52,4,NULL,10,5,9,NULL,0,17),(53,1,NULL,11,5,37,NULL,1,17),(54,1,NULL,11,6,30,NULL,0,18),(55,1,NULL,11,6,32,NULL,1,18),(57,1,NULL,2,6,33,NULL,2,18),(58,0.25,NULL,11,1,23,NULL,0,21),(59,0.333333333333,NULL,2,1,40,NULL,1,21),(60,24,NULL,6,6,21,NULL,0,22),(61,0.25,NULL,2,1,9,NULL,0,24),(62,0.5,NULL,2,1,35,NULL,1,24),(63,0.333333333333,NULL,2,1,19,NULL,0,26),(64,0.75,NULL,2,1,27,NULL,1,26),(65,1,NULL,2,6,10,NULL,0,27),(66,0.5,NULL,2,6,14,NULL,1,27),(67,2,NULL,10,6,9,NULL,0,29),(68,3,NULL,NULL,8,42,NULL,0,32),(69,1,NULL,11,8,30,NULL,1,32),(70,1,NULL,12,8,43,NULL,0,33),(71,540,NULL,13,8,44,NULL,0,34),(72,0.5,NULL,2,8,45,NULL,1,34),(73,1,NULL,11,8,46,NULL,2,34),(74,1,NULL,11,8,23,NULL,3,34),(75,1,NULL,2,8,10,NULL,0,35),(86,2,NULL,10,11,28,NULL,0,46),(88,2,NULL,NULL,11,29,1,0,48),(89,4,NULL,NULL,11,20,13,0,49),(90,1,NULL,10,11,51,6,1,49),(92,1,NULL,11,11,53,NULL,2,50),(94,0.5,NULL,11,11,55,NULL,1,50),(96,0.25,NULL,11,11,32,NULL,0,52),(97,0.5,NULL,11,11,80,NULL,0,53),(98,14,NULL,6,11,81,NULL,0,54),(99,38,NULL,6,11,59,NULL,0,55),(101,3,NULL,10,11,23,NULL,0,60),(105,0.5,NULL,2,11,64,NULL,0,58),(107,0.25,NULL,11,11,32,NULL,1,48),(108,0.5,NULL,2,11,40,NULL,0,57),(109,1,NULL,2,12,35,NULL,0,62),(110,0.25,NULL,2,12,9,14,1,62),(111,0.25,NULL,2,12,49,1,2,62),(112,0.25,NULL,2,12,65,NULL,3,62),(113,0.5,NULL,11,12,37,NULL,4,62),(114,1,NULL,NULL,12,18,NULL,0,70),(115,1,NULL,2,12,66,NULL,6,62),(116,2,NULL,NULL,13,18,NULL,0,64),(117,1,NULL,2,13,34,NULL,1,64),(118,2,NULL,10,13,9,14,2,64),(119,1,NULL,2,13,28,NULL,3,64),(120,0.5,NULL,2,13,13,NULL,4,64),(121,0.5,NULL,2,13,67,NULL,5,64),(122,1,NULL,11,13,37,NULL,6,64),(123,2.25,NULL,2,13,19,NULL,0,65),(124,1.5,NULL,11,13,5,NULL,1,65),(125,1.5,NULL,11,13,4,NULL,2,65),(126,1,NULL,2,13,40,15,0,66),(127,0.5,NULL,2,13,66,NULL,0,68),(128,12,NULL,NULL,12,68,NULL,0,73),(129,2,NULL,12,14,73,NULL,0,75),(130,2,NULL,NULL,14,18,8,2,75),(132,0.333333333333,NULL,2,14,71,NULL,4,75),(133,1,NULL,2,14,70,NULL,3,75),(134,1,NULL,11,14,41,NULL,9,75),(135,1,NULL,NULL,14,29,2,1,75),(136,1,NULL,11,14,74,NULL,8,75),(138,1,NULL,11,14,32,NULL,7,75),(139,1,NULL,11,14,78,NULL,10,75),(140,2,NULL,11,14,79,NULL,11,75),(141,4,NULL,10,14,71,NULL,0,79),(144,1,NULL,11,11,54,NULL,2,50),(145,2,NULL,12,15,73,NULL,0,80),(146,1,NULL,NULL,15,29,2,1,80),(147,2,NULL,NULL,15,20,NULL,0,81),(148,1,NULL,10,15,82,NULL,0,136),(149,1,NULL,10,15,83,NULL,1,81),(150,1,NULL,10,15,54,NULL,2,81),(151,1,NULL,11,15,32,NULL,3,81),(152,1,NULL,11,15,84,NULL,4,81),(153,0.5,NULL,11,15,80,NULL,5,81),(154,0.25,NULL,11,15,30,NULL,6,81),(155,796,NULL,13,15,81,NULL,1,82),(156,398,NULL,13,15,86,NULL,0,82),(157,540,NULL,13,15,87,NULL,0,84),(158,0.75,NULL,2,16,72,NULL,0,85),(159,1.25,NULL,2,16,24,NULL,1,85),(160,1,NULL,2,16,19,NULL,0,86),(161,0.333333333333,NULL,2,16,34,NULL,1,86),(162,1,NULL,10,16,4,NULL,2,86),(163,0.5,NULL,11,16,32,NULL,3,86),(164,1,NULL,NULL,16,18,NULL,0,87),(165,0.25,NULL,2,16,28,NULL,1,87),(166,3,NULL,2,17,88,NULL,0,89),(167,2,NULL,10,17,89,NULL,1,89),(168,2,NULL,10,17,38,NULL,2,89),(169,0.125,NULL,11,17,32,NULL,4,89),(170,0.125,NULL,11,17,30,NULL,3,89),(171,300,NULL,5,17,90,NULL,0,91),(172,100,NULL,5,17,91,NULL,1,91),(173,0.25,NULL,2,17,45,NULL,0,93),(174,5,NULL,NULL,17,92,NULL,0,90),(175,2,NULL,2,18,19,NULL,0,94),(176,2,NULL,10,18,34,NULL,1,94),(177,2,NULL,10,18,4,NULL,2,94),(178,0.25,NULL,11,18,32,NULL,3,94),(179,2,NULL,2,18,67,NULL,1,95),(180,2,NULL,NULL,18,18,NULL,0,95),(181,2,NULL,10,18,28,NULL,2,95),(182,4,NULL,10,18,28,NULL,0,97),(183,1,NULL,NULL,19,20,NULL,0,98),(184,1,NULL,NULL,19,93,NULL,0,99),(185,0.5,NULL,2,19,94,NULL,1,99),(186,0.5,NULL,11,19,54,NULL,3,99),(187,0.25,NULL,2,19,23,NULL,2,99),(188,0.5,NULL,11,19,32,NULL,4,99),(189,3,NULL,10,19,89,NULL,0,100),(190,0.25,NULL,11,19,31,NULL,5,99),(191,0.25,NULL,11,19,31,NULL,1,101),(192,3,NULL,10,19,89,NULL,0,101),(193,500,NULL,5,20,95,NULL,0,102),(194,1,NULL,NULL,20,29,16,0,105),(195,0.666666666666667,NULL,2,20,96,NULL,0,103),(196,0.666666666666667,NULL,2,20,19,NULL,0,108),(197,5,NULL,2,20,24,NULL,0,104),(198,600,NULL,5,20,10,NULL,2,105),(199,1,NULL,11,20,17,NULL,1,105),(201,0.75,NULL,2,20,70,NULL,0,106),(202,2,NULL,10,20,96,7,1,106),(203,2,NULL,NULL,21,58,NULL,0,111),(204,1,NULL,NULL,21,97,NULL,1,111),(205,1,NULL,NULL,21,29,NULL,0,109),(206,2,NULL,12,21,73,NULL,1,109),(207,2,NULL,NULL,21,98,NULL,2,111),(208,1,NULL,10,21,99,NULL,3,111),(209,1,NULL,NULL,21,100,NULL,0,110),(210,4,NULL,10,14,35,NULL,1,79),(211,0.75,NULL,2,22,9,NULL,0,113),(212,0.75,NULL,2,22,35,NULL,1,113),(213,0.5,NULL,2,22,34,NULL,2,113),(214,2,NULL,11,22,37,NULL,0,114),(215,1,NULL,NULL,22,18,NULL,1,114),(216,1,NULL,NULL,22,101,NULL,2,114),(217,2,NULL,2,22,19,NULL,0,115),(218,0.5,NULL,11,22,5,NULL,1,115),(219,0.5,NULL,11,22,32,NULL,2,115),(220,1,2,2,22,66,NULL,0,116),(221,1.75,NULL,2,23,19,NULL,0,119),(222,2,NULL,2,23,27,NULL,1,119),(223,0.5,NULL,2,23,65,NULL,2,119),(224,1,NULL,2,23,96,NULL,0,120),(225,1,NULL,2,23,35,NULL,1,120),(226,1,NULL,11,23,5,NULL,0,121),(227,0.25,NULL,2,23,40,15,1,121),(228,1,NULL,11,23,37,NULL,0,122),(229,1,NULL,2,23,66,NULL,0,123),(230,0.5,NULL,11,20,32,NULL,3,105),(231,0.25,NULL,11,20,30,NULL,4,105),(232,150,NULL,5,20,10,NULL,0,125),(233,0.125,NULL,11,20,102,NULL,5,105),(234,300,NULL,5,24,73,NULL,0,130),(235,300,NULL,5,24,103,NULL,1,130),(236,0.5,NULL,2,24,70,NULL,0,128),(237,0.25,NULL,2,24,16,NULL,1,128),(238,2,NULL,10,24,89,NULL,0,129),(239,1,NULL,NULL,24,104,11,1,129),(240,2,NULL,10,24,34,NULL,2,130),(241,1,NULL,NULL,24,18,NULL,3,130),(242,3,NULL,10,24,9,NULL,0,132),(243,1,NULL,11,24,32,NULL,4,130),(244,0.5,NULL,11,24,30,NULL,5,130),(245,3,NULL,2,25,19,NULL,0,133),(246,0.25,NULL,11,25,126,NULL,1,133),(247,1,NULL,11,25,32,NULL,2,133),(248,1.5,NULL,2,25,40,17,3,133),(249,1,NULL,NULL,15,108,NULL,2,80),(250,2,NULL,NULL,15,109,NULL,3,80),(251,1,NULL,NULL,15,100,NULL,2,82),(252,1,NULL,10,15,40,18,1,136),(253,1,NULL,NULL,15,110,NULL,1,84),(254,1,NULL,NULL,26,111,19,0,139),(255,2,NULL,NULL,26,112,NULL,0,138),(256,1,NULL,NULL,26,29,NULL,2,137),(257,2,NULL,NULL,26,109,NULL,2,137),(258,0.25,NULL,2,26,113,NULL,0,140),(259,1.25,NULL,12,26,73,NULL,0,137),(260,0.25,NULL,11,26,30,NULL,1,140),(261,1,NULL,NULL,27,29,20,1,143),(262,3,NULL,NULL,27,20,21,2,143),(263,5,NULL,NULL,27,114,NULL,0,142),(264,8,NULL,10,27,9,NULL,0,143),(265,1,NULL,11,27,32,NULL,3,143),(266,2,NULL,NULL,27,115,NULL,0,144),(267,3,4,2,27,12,10,0,145),(268,3,4,10,27,116,NULL,0,148),(269,NULL,NULL,10,27,117,11,1,148),(270,NULL,NULL,11,27,118,NULL,0,147),(271,NULL,NULL,NULL,27,32,NULL,1,147),(272,0.5,NULL,11,7,119,NULL,6,8),(273,0.5,NULL,11,7,120,NULL,5,8),(274,1,NULL,NULL,7,121,NULL,1,15),(275,2,NULL,NULL,28,122,22,1,149),(276,2,NULL,NULL,28,109,22,2,149),(277,2,NULL,NULL,28,29,22,3,149),(278,2,NULL,NULL,28,20,1,4,149),(279,1,NULL,10,28,89,NULL,0,149),(280,1500,NULL,13,28,12,NULL,0,150),(281,1,NULL,NULL,28,58,NULL,1,150),(282,6,NULL,NULL,28,123,NULL,2,150),(283,1,NULL,10,28,125,NULL,1,152),(284,3,NULL,11,28,32,NULL,2,152),(285,1,NULL,11,28,76,NULL,3,152),(286,2,NULL,11,28,34,NULL,3,150),(287,1,NULL,11,28,118,NULL,0,152),(288,1,NULL,2,29,40,NULL,0,153),(289,2.5,NULL,2,29,19,NULL,1,153),(290,1,NULL,10,29,34,NULL,2,153),(291,1,NULL,11,29,32,NULL,3,153),(292,1.5,NULL,11,29,126,NULL,4,153),(293,1,NULL,NULL,29,101,NULL,0,155),(294,1,NULL,10,29,40,NULL,1,155),(295,0.5,NULL,2,30,9,NULL,0,157),(296,0.5,NULL,2,30,19,NULL,1,157),(297,4,NULL,2,30,128,NULL,0,158),(298,1,NULL,11,30,32,NULL,0,160),(299,0.5,NULL,11,30,102,NULL,1,160),(300,1,NULL,2,31,130,24,0,162),(301,3,NULL,2,31,40,NULL,1,162),(302,3,NULL,NULL,31,131,NULL,0,163),(303,2,NULL,11,31,28,NULL,0,164),(304,0.5,NULL,NULL,31,29,NULL,1,164),(305,2,NULL,11,31,132,NULL,3,164),(306,1,NULL,11,31,55,NULL,5,164),(307,2,NULL,NULL,31,20,25,2,164),(308,1,NULL,NULL,31,60,NULL,4,164),(309,0.5,NULL,11,31,32,NULL,1,165),(310,1,NULL,NULL,31,133,NULL,0,165),(311,0.25,NULL,2,31,64,NULL,2,165),(312,0.5,NULL,11,11,52,NULL,3,50),(313,1,NULL,11,11,50,NULL,1,46),(314,2,NULL,10,33,138,NULL,0,170),(315,1,NULL,NULL,33,29,NULL,1,170),(316,0.5,NULL,2,33,139,NULL,2,170),(317,0.5,NULL,2,33,140,NULL,3,170),(318,12,NULL,NULL,33,142,NULL,4,170),(319,2,NULL,NULL,33,18,NULL,0,171),(320,3,NULL,2,33,141,18,0,172),(321,2,3,10,33,113,NULL,1,172),(322,2,NULL,10,33,143,NULL,2,172),(323,NULL,NULL,NULL,19,84,NULL,2,101),(324,700,NULL,5,34,146,NULL,0,173),(325,1,NULL,11,34,147,NULL,0,175),(326,0.5,NULL,11,34,148,NULL,2,175),(327,0.5,NULL,11,34,119,NULL,3,175),(328,0.5,NULL,11,34,84,NULL,4,175),(329,0.25,NULL,11,34,25,NULL,5,175),(330,0.25,NULL,11,34,76,NULL,6,175),(331,0.25,NULL,11,34,30,NULL,1,175),(332,1,NULL,NULL,34,29,NULL,0,176),(333,4,NULL,10,34,96,NULL,1,173),(334,0.5,NULL,11,34,150,NULL,7,175),(335,0.25,NULL,2,35,113,NULL,0,177),(336,2,NULL,10,35,35,NULL,1,177),(337,2,NULL,10,35,151,NULL,2,177),(338,2,NULL,10,35,152,NULL,3,177),(339,2,NULL,NULL,35,20,13,4,177),(340,1,NULL,11,35,51,6,5,177),(341,0.25,NULL,11,35,153,NULL,6,177),(342,2,NULL,12,35,154,NULL,7,177),(343,2,NULL,11,35,155,NULL,0,179),(344,1,NULL,2,36,45,NULL,0,180),(345,0.25,NULL,2,36,34,NULL,1,180),(346,2,NULL,10,36,156,NULL,2,180),(347,1.5,NULL,10,36,23,NULL,3,180),(348,1,NULL,10,36,157,NULL,4,180),(349,0.5,NULL,11,36,119,NULL,5,180),(350,0.5,NULL,11,36,26,NULL,6,180),(351,0.5,NULL,11,36,32,NULL,7,180),(352,0.5,NULL,11,36,120,NULL,8,180),(353,0.5,NULL,11,36,30,NULL,9,180),(354,800,NULL,5,36,158,NULL,0,181),(355,1,NULL,2,37,9,NULL,0,184),(356,1.33333,NULL,2,37,34,NULL,1,184),(357,1,NULL,NULL,37,18,NULL,2,184),(358,2,NULL,11,37,37,NULL,3,184),(359,3,NULL,2,37,19,NULL,0,185),(360,2,NULL,11,37,159,NULL,1,185),(361,1,NULL,11,37,5,NULL,2,185),(362,2.5,NULL,11,37,106,NULL,3,185),(363,0.5,NULL,11,37,32,NULL,4,185),(364,0.25,NULL,2,37,34,NULL,0,183),(365,1,NULL,11,37,106,NULL,1,183),(366,2,NULL,15,38,160,NULL,0,187),(367,1,NULL,NULL,38,29,26,1,187),(368,4,NULL,NULL,38,161,5,3,187),(369,4,NULL,NULL,38,20,NULL,2,187),(370,2,NULL,10,38,89,NULL,4,187),(371,0.5,NULL,11,38,32,NULL,5,187),(372,0.5,NULL,11,38,31,NULL,6,187),(373,375,NULL,5,38,162,NULL,0,188),(374,NULL,NULL,NULL,38,124,26,0,189),(375,4,NULL,NULL,38,143,5,1,189),(376,2,NULL,NULL,39,163,NULL,0,191),(377,20,NULL,NULL,39,164,NULL,1,191),(378,800,NULL,NULL,39,165,6,2,191),(379,1,NULL,NULL,39,166,NULL,3,191),(380,1,NULL,2,39,40,NULL,0,NULL),(381,1,NULL,NULL,40,122,16,2,192),(386,1,NULL,NULL,40,29,16,0,192),(387,1,NULL,2,40,75,NULL,5,192),(388,1,NULL,12,40,73,NULL,3,192),(389,1,NULL,12,40,103,NULL,4,192),(390,2,NULL,NULL,40,20,16,0,193),(391,1,NULL,2,40,75,NULL,0,194),(392,0.5,NULL,2,40,70,NULL,0,195),(393,0.25,NULL,11,40,76,NULL,0,196),(394,0.25,NULL,11,40,167,NULL,1,196),(395,0.25,NULL,11,40,168,NULL,2,196),(396,0.25,NULL,11,40,26,NULL,3,196),(397,0.125,NULL,11,40,169,NULL,4,196),(398,0.125,NULL,11,40,170,NULL,5,196),(399,0.125,NULL,11,40,106,NULL,6,196),(400,0.125,NULL,11,40,171,NULL,7,196),(401,0.5,NULL,11,40,32,NULL,1,193),(402,0.5,NULL,NULL,40,172,NULL,6,192),(403,1,NULL,NULL,40,109,16,1,192),(404,500,NULL,5,41,154,27,0,198),(405,1,NULL,11,41,173,NULL,1,198),(406,NULL,NULL,NULL,41,32,27,2,198),(407,2,NULL,10,41,28,NULL,3,198),(408,1,NULL,11,41,84,NULL,4,198),(409,1,NULL,11,41,174,NULL,5,198),(410,0.5,NULL,11,41,50,NULL,0,199),(411,1,NULL,NULL,41,29,NULL,1,199),(412,1,NULL,11,41,173,NULL,2,199),(413,4,NULL,NULL,41,175,NULL,3,199),(414,1,NULL,10,41,53,NULL,4,199),(415,2.5,NULL,2,42,19,NULL,0,204),(416,1.5,NULL,11,42,34,NULL,1,204),(417,1,NULL,11,42,32,NULL,2,204),(418,0.5,NULL,2,42,9,NULL,0,205),(419,0.5,NULL,2,42,176,NULL,1,205),(420,5,NULL,10,42,40,NULL,0,206),(421,1,NULL,NULL,40,18,NULL,0,208),(422,2,NULL,11,43,32,NULL,1,NULL),(423,4,NULL,10,43,177,NULL,2,NULL),(424,2,NULL,NULL,43,178,NULL,3,NULL),(425,0.66666666666,NULL,2,43,91,NULL,4,NULL);
/*!40000 ALTER TABLE `recipes_ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_photo`
--

DROP TABLE IF EXISTS `recipes_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(200) NOT NULL,
  `recipe_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `keep` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recipe_id_refs_id_4facdcca2c0f3c2e` (`recipe_id`),
  CONSTRAINT `recipe_id_refs_id_4facdcca2c0f3c2e` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_photo`
--

LOCK TABLES `recipes_photo` WRITE;
/*!40000 ALTER TABLE `recipes_photo` DISABLE KEYS */;
/*!40000 ALTER TABLE `recipes_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_prepmethod`
--

DROP TABLE IF EXISTS `recipes_prepmethod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_prepmethod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_prepmethod`
--

LOCK TABLES `recipes_prepmethod` WRITE;
/*!40000 ALTER TABLE `recipes_prepmethod` DISABLE KEYS */;
INSERT INTO `recipes_prepmethod` VALUES (1,'chopped'),(2,'diced'),(3,'crumbled'),(4,'peeled'),(5,'sliced'),(6,'grated'),(7,'melted'),(8,'beaten'),(9,'mashed'),(10,'hot'),(11,'finely chopped'),(12,'mashed'),(13,'crushed'),(14,'softened'),(15,'boiling'),(16,'finely diced'),(17,'warm'),(18,'cold'),(19,'cooked'),(20,'finely sliced'),(21,'émincé'),(22,'roughly chopped'),(23,'luke-warm'),(24,'rinsed'),(25,'pureed'),(26,'thinly sliced'),(27,'to taste'),(28,'ice');
/*!40000 ALTER TABLE `recipes_prepmethod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_recipe`
--

DROP TABLE IF EXISTS `recipes_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_recipe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `summary` varchar(500) NOT NULL,
  `description` longtext NOT NULL,
  `slug` varchar(50) NOT NULL,
  `prep_time` varchar(100) NOT NULL,
  `ctime` datetime NOT NULL,
  `mtime` datetime NOT NULL,
  `category_id` int(11) NOT NULL,
  `serving_string_id` int(11) DEFAULT NULL,
  `serving_value` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `category_id_refs_id_67c4d79161a1ac99` (`category_id`),
  KEY `recipes_recipe_fcf4ae32` (`serving_string_id`),
  CONSTRAINT `category_id_refs_id_67c4d79161a1ac99` FOREIGN KEY (`category_id`) REFERENCES `recipes_category` (`id`),
  CONSTRAINT `serving_string_id_refs_id_f689017a` FOREIGN KEY (`serving_string_id`) REFERENCES `recipes_servingstring` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_recipe`
--

LOCK TABLES `recipes_recipe` WRITE;
/*!40000 ALTER TABLE `recipes_recipe` DISABLE KEYS */;
INSERT INTO `recipes_recipe` VALUES (1,'Apple Crisp','Delicious easy-to-make dessert','This is my mom\'s recipe and she has probably made it about one hundred times now.','apple-crisp','','2008-07-02 01:03:29','2014-07-29 06:06:53',2,NULL,NULL),(2,'Banana Muffins','','Can substitute butter with margarine','banana-muffins','','2008-09-10 01:03:29','2014-01-07 21:09:07',4,NULL,NULL),(3,'Blueberry Muffins','Time-tested recipe for blueberry muffins','','blueberry-muffins','30 minutes','2008-09-10 01:03:29','2009-06-14 20:21:55',4,NULL,NULL),(5,'Chocolate Hot Fudge Sauce','','Just like you can get at Dairy Queen. No better way to combine ice cream and chocolate.','chocolate-syrup','','2008-07-24 01:03:29','2014-02-01 09:16:26',2,4,2),(6,'Green Bean Casserole','','','green-bean-casserole','','2008-08-04 01:03:29','2009-06-06 01:00:18',12,NULL,NULL),(7,'Marni\'s Salad','Delicious salad, great for potlucks','','marnis-salad','15 minutes','2008-07-01 01:03:29','2014-03-24 07:19:32',14,1,8),(8,'Chicken Diane','','','chicken-diane','','2009-06-04 22:08:06','2009-06-04 22:16:46',19,NULL,NULL),(11,'Chana masala','','','chana-masala','','2009-07-05 17:47:41','2014-06-18 06:55:11',21,NULL,NULL),(12,'Chocolate Tarts','','','chocolate-tarts','10','2013-12-24 08:13:20','2014-02-01 09:14:24',2,3,12),(13,'Double Fudge Chocolate Cake','','','double-fudge-chocolate-cake','','2013-12-24 19:24:38','2014-01-04 09:04:59',2,NULL,NULL),(14,'Meatloaf','','','meatloaf','','2014-01-04 06:22:01','2014-02-01 17:22:22',20,1,6),(15,'Chili','Deliciously simple chili','','chili','','2014-01-05 07:13:29','2014-02-28 20:14:15',20,NULL,NULL),(16,'Cornmeal muffins','Perfect accompaniment to chili or BBQ','Makes 12 muffins.','cornmeal-muffins','','2014-01-05 07:31:28','2014-01-05 07:40:12',17,NULL,NULL),(17,'Pulled Pork Sandwiches','','Makes 4-5 sandwiches','pulled-pork-sandwiches','','2014-01-06 07:36:27','2014-01-06 07:41:48',20,NULL,NULL),(18,'Pancakes','Perfect pancakes','','pancakes','','2014-01-07 07:46:25','2014-01-07 08:04:55',6,NULL,NULL),(19,'Hummus','Hummus with Tahini','','hummus','','2014-01-08 07:40:53','2014-11-07 08:16:45',1,1,6),(20,'Macaroni & Cheese','','','macaroni-cheese','','2014-01-14 08:02:34','2014-05-27 04:52:03',15,1,8),(21,'Maureen\'s Spaghetti Sauce','','','maureens-spaghetti-sauce','','2014-01-16 08:17:00','2014-01-16 08:18:22',15,NULL,NULL),(22,'Chocolate Chip Cookies','','Delicious, chewy chocolate chip cookies. Use a wooden spoon to mix the cookie dough together. A mixer incorporates more air into the dough, which will give the cookies a cake-like texture. Instead of using regular table salt, you can use a more flavourful salt like fleur de sel.','chocolate-chip-cookies','','2014-01-22 08:02:23','2014-02-01 09:11:51',2,2,24),(23,'Oatmeal Chocolate Chip Cookies','','I think this the recipe my mom and nana used to make growing up. I need to try making it to see. The original recipe said \"lightly packed brown sugar\".','oatmeal-chocolate-chip-cookies','','2014-01-22 08:34:30','2014-01-22 08:42:14',4,NULL,NULL),(24,'Swedish Meatballs','','From http://www.foodrepublic.com/2012/01/20/marcus-samuelssons-swedish-meatballs','swedish-meatballs','','2014-01-23 07:02:40','2014-02-18 07:07:22',20,1,4),(25,'No-knead Bread','','','no-knead-bread','','2014-02-11 23:08:09','2014-07-28 20:35:28',17,NULL,NULL),(26,'Hamburger Chow Mein','','','hamburger-chow-mein','','2014-03-04 05:39:53','2014-03-04 05:50:49',23,1,8),(27,'Potato Leek Soup','','','potato-leek-soup','','2014-03-04 06:04:30','2014-03-04 06:55:25',13,1,6),(28,'Tomato Soup','','','tomato-soup','','2014-03-24 07:25:33','2014-03-24 07:50:22',13,NULL,NULL),(29,'Baguettes','','','baguettes','','2014-04-19 16:42:06','2014-04-19 20:29:14',17,5,2),(30,'Béchamel Sauce','','Also known as white sauce, béchamel Sauce is one of the mother sauces of French cuisine.','bechamel-sauce','','2014-05-07 04:58:15','2014-07-29 06:42:24',5,NULL,NULL),(31,'Red Lentil Dal','','','red-lentil-dal','10','2014-06-17 17:53:36','2014-06-17 18:02:39',24,1,4),(33,'Fried Rice','Simple and delicious fried rice recipe','','fried-rice','','2014-09-04 18:05:57','2014-09-04 21:03:59',23,NULL,NULL),(34,'Home Fries','still in the experimental stage','','home-fries','','2015-03-12 07:27:52','2015-03-20 07:38:13',12,NULL,NULL),(35,'Teriyaki Chicken Thighs','In Development','','teriyaki-chicken-thighs','','2015-03-23 04:38:02','2015-03-23 04:50:53',20,NULL,NULL),(36,'Coleslaw','','','coleslaw','','2015-03-23 07:37:13','2015-03-23 07:42:00',14,NULL,NULL),(37,'Snickerdoodles','','','snickerdoodles','','2015-11-14 18:18:05','2015-11-15 04:03:11',4,NULL,NULL),(38,'Megan\'s Pasta','Irresistible rustic pasta sauce','Actually it\'s Chef Michael\'s Smith\'s pasta, but I call it Megan\'s pasta, after our friend Megan Turnbull. She made this the first night we arrived at her place in Jasper and I had three helpings plus leftovers the next day.','megans-pasta','60 minutes','2015-12-07 09:14:56','2015-12-07 09:31:42',15,1,4),(39,'Big Huge Lasagna','You need a big pan for this, and a big appetite','','big-huge-lasagna','','2015-12-20 05:24:35','2015-12-20 05:25:17',15,NULL,NULL),(40,'Tourtiere','','','tourtiere','','2015-12-24 08:21:57','2017-01-07 16:30:26',20,1,8),(41,'Butter chicken','','','butter-chicken','','2016-08-18 08:24:58','2016-08-18 08:57:50',23,NULL,NULL),(42,'Pie crust','','Can be made 3 days ahead.','pie-crust','','2016-12-24 18:49:32','2016-12-24 18:54:10',2,NULL,NULL),(43,'Baby back ribs','','','baby-back-ribs','','2017-07-16 20:42:26','2017-07-16 20:45:13',20,NULL,NULL);
/*!40000 ALTER TABLE `recipes_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_recipe_sources`
--

DROP TABLE IF EXISTS `recipes_recipe_sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_recipe_sources` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipe_id` int(11) NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `recipe_id` (`recipe_id`,`source_id`),
  KEY `source_id_refs_id_623c8e3a108f7393` (`source_id`),
  CONSTRAINT `recipe_id_refs_id_167d36c176eeeb1c` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`),
  CONSTRAINT `source_id_refs_id_623c8e3a108f7393` FOREIGN KEY (`source_id`) REFERENCES `recipes_source` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=194 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_recipe_sources`
--

LOCK TABLES `recipes_recipe_sources` WRITE;
/*!40000 ALTER TABLE `recipes_recipe_sources` DISABLE KEYS */;
INSERT INTO `recipes_recipe_sources` VALUES (171,1,1),(83,2,1),(21,3,1),(124,5,3),(15,6,1),(157,7,6),(13,8,1),(120,12,1),(65,13,9),(134,15,10),(77,17,10),(82,18,11),(87,21,12),(117,22,11),(114,23,2),(137,26,2),(153,27,11),(168,31,13),(178,33,10),(186,34,10),(191,35,14),(192,38,15),(193,42,16);
/*!40000 ALTER TABLE `recipes_recipe_sources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_servingstring`
--

DROP TABLE IF EXISTS `recipes_servingstring`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_servingstring` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_servingstring`
--

LOCK TABLES `recipes_servingstring` WRITE;
/*!40000 ALTER TABLE `recipes_servingstring` DISABLE KEYS */;
INSERT INTO `recipes_servingstring` VALUES (1,'Serves %s'),(2,'Makes %s cookies'),(3,'Makes %s tarts'),(4,'Makes %s cups'),(5,'Makes %s baguettes');
/*!40000 ALTER TABLE `recipes_servingstring` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_source`
--

DROP TABLE IF EXISTS `recipes_source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `url` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_source`
--

LOCK TABLES `recipes_source` WRITE;
/*!40000 ALTER TABLE `recipes_source` DISABLE KEYS */;
INSERT INTO `recipes_source` VALUES (1,'Cathy Grant',''),(2,'Helen Grant',''),(3,'Jennifer Wyatt',''),(4,'Jordan McCurrach',''),(5,'Joy of Cooking',''),(6,'Marni Maitland',''),(7,'Judie Anderson',''),(8,'Sunbeam mixer cookbook',''),(9,'Nuts About Chocolate by Susan Mendelson & Deborah Roitberg',''),(10,'David Grant',''),(11,'Rouxbe','http://rouxbe.com/recipes/1390'),(12,'Maureen Lazzari',''),(13,'Simply Recipes','http://www.simplyrecipes.com/'),(14,'Ellie Krieger','http://www.foodnetwork.com/recipes/ellie-krieger/teriyaki-chicken-thighs-recipe.html'),(15,'Chef Michael Smith\'s Kitchen: 100 Of My Favourite Easy Recipes',''),(16,'Jeanne Thiel Kelley - Epicurious','http://www.epicurious.com/recipes/food/views/best-ever-pie-crust-238816');
/*!40000 ALTER TABLE `recipes_source` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_unit`
--

DROP TABLE IF EXISTS `recipes_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_unit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `name_abbrev` varchar(60) NOT NULL,
  `plural_abbrev` varchar(60) NOT NULL,
  `type` int(11) NOT NULL,
  `system` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `recipes_unit_name_6a65aefa33bc11d6_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_unit`
--

LOCK TABLES `recipes_unit` WRITE;
/*!40000 ALTER TABLE `recipes_unit` DISABLE KEYS */;
INSERT INTO `recipes_unit` VALUES (2,'cup','c.','c.',2,1),(5,'gram','g','g',1,0),(6,'fluid_ounce','fl. oz.','fl. ozs.',2,1),(10,'tablespoon','Tbsp','Tbsp',2,1),(11,'teaspoon','tsp.','tsp.',2,1),(12,'pound','lb','lbs',1,1),(13,'millilitre','ml','ml',2,0),(14,'kilogram','kg','kg',1,0),(15,'litre','litre','litres',2,0);
/*!40000 ALTER TABLE `recipes_unit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-29  1:18:54
