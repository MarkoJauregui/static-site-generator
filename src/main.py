import os
import shutil
from textnode import TextNode, TextType


def copy_static():
    if os.path.exists("public"):
        shutil.rmtree("public")

    os.mkdir("public")

    copy_recursive("static", "public")


def copy_recursive(src_path, dest_path):
    for item in os.listdir(src_path):
        src_item_path = os.path.join(src_path, item)
        dest_item_path = os.path.join(dest_path, item)

        if os.path.isfile(src_item_path):
            print(f"Copying file: {src_item_path}")
            shutil.copy(src_item_path, dest_item_path)
        else:
            print(f"Processing directory: {src_item_path}")
            os.mkdir(dest_item_path)
            copy_recursive(src_item_path, dest_item_path)


def main():
    node = TextNode("Hello, world!", TextType.BOLD, "https://www.boot.dev")

    print(node)

    copy_static()


main()
