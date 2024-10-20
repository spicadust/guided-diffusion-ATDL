import os
from dotenv import load_dotenv, set_key

# Load existing .env file if it exists
load_dotenv()

# Get the current working directory (assuming the script is in assignment_2)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up one level to the repo root
repo_root = os.path.abspath(os.path.join(current_dir, '..'))
fastai_home = os.path.join(repo_root, '.fastai/')

# Set the FASTAI_HOME environment variable
os.environ['FASTAI_HOME'] = fastai_home

# Update or create .env file
dotenv_path = os.path.join(repo_root, '.env')
set_key(dotenv_path, 'FASTAI_HOME', fastai_home)

# Print the value to confirm
print(f"FASTAI_HOME is set to: {os.getenv('FASTAI_HOME')}")

# Optionally, you can list all environment variables
print("\nAll environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")
