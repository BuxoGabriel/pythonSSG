import os
import shutil
from os.path import exists, isdir, isfile

from markdown import extract_title, markdown_to_html_node

def main():
    if exists("./public"):
        shutil.rmtree("./public")
    copy_dir_recursive("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

def copy_dir_recursive(path: str, dest: str):
    contents = os.listdir(path);
    if not exists(dest):
        os.mkdir(dest)
    for content_path in contents:
        copy_path = os.path.join(dest, content_path)
        content_path = os.path.join(path, content_path)
        if isfile(content_path):
            shutil.copy(content_path, copy_path)
        elif isdir(content_path):
            copy_dir_recursive(content_path, copy_path)

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    template_file = open(template_path)
    markdown = from_file.read()
    template = template_file.read()
    from_file.close()
    template_file.close()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    dest_file = open(dest_path, "w+")
    dest_file.write(template)
    dest_file.close()

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    paths = os.listdir(dir_path_content)
    if not exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for path in paths:
        content_path = os.path.join(dir_path_content, path)
        dest_path = os.path.join(dest_dir_path, path)
        if os.path.isfile(content_path) and path.endswith(".md"):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(content_path, template_path, dest_path)
        elif os.path.isdir(content_path):
            generate_pages_recursive(content_path, template_path, dest_path)


if __name__ == "__main__":
    main()
