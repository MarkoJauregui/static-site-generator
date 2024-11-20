import os
import shutil

from copy_static import copy_files_recursive
from generate_content import generate_pages_recursive


dir_path_static = os.path.abspath("./static")
dir_path_public = os.path.abspath("./public")
dir_path_content = os.path.abspath("./content")
template_path = os.path.abspath("./template.html")

def main():
    print("Checking paths...")
    print(f"Content directory exists: {os.path.exists(dir_path_content)}")
    print(f"Template exists: {os.path.exists(template_path)}")
    print(f"Current directory: {os.getcwd()}")

       # Already existing print statements for path checks...

    # Debug: Show directory content
    print("Content directory files:", os.listdir(dir_path_content))
    print("Static directory files:", os.listdir(dir_path_static))

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    try:
        copy_files_recursive(dir_path_static, dir_path_public)
    except Exception as e:
        print(f"Error during copying: {e}")

    print("Generating content...")
    try:
        generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    except Exception as e:
        print(f"Error during content generation: {e}")


main()
