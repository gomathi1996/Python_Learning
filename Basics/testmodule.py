# Method 1
import commonmodule
commonmodule.print_captain()
commonmodule.print_vice_captain()

# Method 2
from commonmodule import print_captain
print_captain()

# Method 3
from commonmodule import print_captain as pc
pc()