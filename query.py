"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

db.session.query(Brand).get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    mods = db.session.query(Model.name, Model.year, Model.brand_name, Brand.headquarters).join(Brand).all()

    if year == Model.year:
        for name, brand_name, headquarters in mods:
            print name, brand_name, headquarters

    # mods = db.session.query(Model, Brand).outerjoin(Brand).all()
    # So this is not working. I've been spending a good bit of time on it and I'm over it.

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     #For each brand in the brand table, print the brand and loop through models 
     #and print out all the models with that brand name.


    pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
    # The value returned would be the row "1 | Ford |    1903 | Dearborn, MI |  "
    #The data type is an object.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
    #An association table handles many to many relationships. The association table
    #contains only inofrmation that is contined in both tables in order to handle
    #the many many aspect.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):

    brands_from_string = Brand.query.filter(Brand.name.like('%\mystr%')).all()

    for brand in brands_from_string:
        print brand.name

    #This is not quite working, but I tried the query in interactive and it worked
    #not quite sure. :(


def get_models_between(start_year, end_year):
   
    models_between = Model.query.filter((Model.year>start_year) & (Model.year<end_year))

    for model in models_between:
        return model.name

    #I know that it said to return a list of objects, but I had a hard time seeing
    #if I was return the correct thing, so I did it this way. 


#My take away from this weeks skills assessment is that I need more practice and understanding
#around putting SQLAlchemy queries into functions!