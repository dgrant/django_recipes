[![Build Status](https://travis-ci.org/dgrant/django_recipes.png)](https://travis-ci.org/dgrant/django_recipes) [![Coverage Status](https://coveralls.io/repos/dgrant/django_recipes/badge.png)](https://coveralls.io/r/dgrant/django_recipes)

This is a complete recipe system using Python + Django. A complete demonstration is live at [http://recipes.davidgrant.ca/cookbook/](http://recipes.davidgrant.ca/cookbook/).

Features
========

* Most important models, such as Recipe, Food, Ingredient, Direction, Category, and a few more.
* Very nice admin interface for creating recipes with inline ingredients and directions.
* Front-end: only a recipe_list and recipe_detail so far, but the recipe_detail has an experimental method of displaying recipes that is based on this LaTeX style: http://www.ctan.org/tex-archive/macros/latex/contrib/cooking/ (apparently based on style in a famous German cookbook by Dr. Oetker (Gromzik, J.; Reich, C.; Sander, C. (ed.): Dr. Oetker Schulkochbuch – Das Original. Ceres, Bielefeld, 1996.)
* Automatic conversion from imperial weights and volumes to grams
* Automatic nice formatting of imperial volumes.
* Uses South database migration system.

Competitors/related projects
============================

* KRecipes - KDE-based desktop recipes software.
* Ben Collins-Sussman's effrecipes - Simple, but it works. Not under active development.
* Recipes on Rails - Ruby on Rails recipes site. Not open source as far as I know. Embeds "Source: Recipes on Rails" on all photos and has google ads. Great site though. One thing it has that my site lacks is per-direction photos. This would be easy to do. I already have per-direction ingredients.

If you are aware of any other similar projects please let me know. I am especially interested in any other web-based and open-source cookbook projects.

Getting started
===============

Follow these steps to get the recipes site up and running.

1. Checkout the project from svn.
1. Edit settings.py and set your DATABASE_ENGINE, DATABASE_USER, DATABASE_NAME, and DATABASE_PASSWORD.
1. Run ./manage.py syncdb from the menu
1. Run ./manage.py runserver
1. Go to http://locahost:8000 in your browser
1. The admin interface is at http://localhost:8000/admin and there is a somewhat useful view at http://localhost:8000/recipes/recipes
