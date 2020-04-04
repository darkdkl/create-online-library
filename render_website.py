from livereload import Server, shell
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import time


def rendering(num_page,books_info):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])    )

    template = env.get_template('template.html')           
    rendered_page = template.render(books_info=books_info)
    with open(f'index{num_page}.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

def main():
    books_in_page= 20
    with open('books/books_info.json', 'r', encoding='utf-8') as json_file:
        books_info = json.load(json_file)    
    books_info_split_in_pages = [books_info[index:index+books_in_page] 
                           for index in range(0, len(books_info), books_in_page)]
    for num_page,info_in_page in enumerate(books_info_split_in_pages):
        rendering(num_page,info_in_page)
    
    # server = Server()
    # server.watch('template.html', rendering)
    # server.serve(root='.')

if __name__ == "__main__":
    main()