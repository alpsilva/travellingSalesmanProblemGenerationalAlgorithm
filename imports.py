import subprocess
import sys

# You can do this manually if you prefer
# Or just run this script once to install necessary libraries

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('matplotlib')
install('numpy')