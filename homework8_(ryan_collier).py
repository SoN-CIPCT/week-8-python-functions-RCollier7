##Homework Week 8 - Functions - Deadline 02Mar2026
##Issue accessing online workspace, had to save as homework8_(ryan_collier) without <> in filename due to error message.

sandwhich_ingredients_v1 = ['pickles', 'mayo', 'lettuce','tomato', 'sourdough bread']
sandwhich_ingredients_v2 = ['mustard', 'onions', 'olives','avocado','cheddar cheese', 'bacon', 'rye bread']

def sandwhich_generator(*ingredients):
    print ('You have ordered a sandwhich with the following ingredients:')
    for ingredient in ingredients:
        print (ingredient)

##Test the function with the two lists of ingredients provided above.
##Ingredients V1 should print 5 ingredients, and Ingredients V2 should print 7 ingredients.
sandwhich_generator(sandwhich_ingredients_v1)
sandwhich_generator(sandwhich_ingredients_v2)
