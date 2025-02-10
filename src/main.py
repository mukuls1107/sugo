from textnode import TextNode, TextType
from htmlnode import LeafNode
from copy_static import copy_files_recursive
from generate_content import generate_pages_recursive
import os
import shutil



dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_pages_recursive
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)





  
main()