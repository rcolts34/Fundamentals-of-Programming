'''

#### Modules

    1.  Standard
        -  Built into the language itself
            → EX:  import random

    2.  External
        - Not part of the language itself
        - Have to install them before importing
            → EX:  pandas, numpy
                ∟ Most widely used in data science and machine  learning
        - Pandas is always aliased as 'pd'
            → import pandas as pd
        - You can specifically import functions from an external library
            ∟ Library may be very large, don't want to import things you don't need
            ∟ from find_index_module import find_index
        - Running export modules in the background can use resources.  Don't want to have them running if you dont need them. Adding print statements can inform that they are running.
            ∟ print('Running find index module: ', __name__)
        - Add if condition to stop module from running
            ∟ when file is run directly
            ∟ if __name__ == '__main__':
                ∟ stops imported code from running in the background
    3.  Custom
        - Built by developers for their specific use cases
        - Exists in a separate file, and is called, similar to a function

'''

## Standard module
import random

## External module
# import pandas as pd  →  need to be installed first

## Custom Module
# import find_index_module as fim
# req_idx = fim.find_index(['apple', 'oranges', 'kiwi', 'mango'], 'mango')
# print(req_idx)
# print(fim.test_var)

# To import only specific things
from find_index_module import find_index as fi
req_idx = fi(['apple', 'oranges', 'kiwi', 'mango'], 'mango')
print(req_idx)
print('Running modules intro: ', __name__)