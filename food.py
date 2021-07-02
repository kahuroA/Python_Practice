bronze_package = {'starch' : 'rice',
                  'stew' : 'chicken curry',
                  'vegetables' : 'cabbages', 
                  'desert' : 'melon'}
silver_package = {'starch' : 'rice and chapati',
                  'stew' : 'beef curry',
                  'vegetables' : 'spinach', 
                  'desert' : 'melon and bananas'}
gold_package = {'starch' : 'chapati and mukimo',
                  'stew' : 'beef curry',
                  'vegetables' : 'managu', 
                  'desert' : 'tart'}
food_packages = {'bronze_package' : bronze_package.values(),
                 'silver_package' : silver_package.values(),
                 'gold_package' : gold_package.values()}
print(food_packages)
