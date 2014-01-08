[![Build Status](https://travis-ci.org/dgrant/django_recipes.png)](https://travis-ci.org/dgrant/django_recipes) [![Coverage Status](https://coveralls.io/repos/dgrant/django_recipes/badge.png)](https://coveralls.io/r/dgrant/django_recipes)

I wanted to create a family cookbook, inspired by my mom who took my Nana's old recipes and put them into electronic form as a collection of Word documents. At first I thought about using LaTeX to separate the style from the content a bit, then I thought about using XML, then I settled on a database as being the most generic to store recipe data. I quickly decided on using Django to create this cookbook framework because Python is probably my strongest language and it makes creating custom websites really easy.

So far it includes:

Most important models, such as Recipe, Food, Ingredient, Direction, Category, and a few more.
Very nice admin interface for creating recipes with inline ingredients and directions.
Front-end: only a recipe_list and recipe_detail so far, but the recipe_detail has an experimental method of displaying recipes that is based on this LaTeX style: http://www.ctan.org/tex-archive/macros/latex/contrib/cooking/ (apparently based on style in a famous German cookbook by Dr. Oetker (Gromzik, J.; Reich, C.; Sander, C. (ed.): Dr. Oetker Schulkochbuch – Das Original. Ceres, Bielefeld, 1996.)

Competitors/related projects:

KRecipes - KDE-based desktop recipes software.
Ben Collins-Sussman's effrecipes - Simple, but it works. Not under active development.
Recipes on Rails - Ruby on Rails recipes site. Not open source as far as I know. Embeds "Source: Recipes on Rails" on all photos and has google ads. Great site though. One thing it has that my site lacks is per-direction photos. This would be easy to do. I already have per-direction ingredients.
If you are aware of any other similar projects please let me know. I am especially interested in any other web-based and open-source cookbook projects.
