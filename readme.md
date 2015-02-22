#SDL site code

Working version of new SDL site.

## Markdown modifications

To add new content, edit the appropriate [markdown](https://help.github.com/articles/markdown-basics/) files in the `flask_app/content` folder.

I've added a couple of modifications to markdown to make our lives easier.

1. The `~~~` character, with newlines before and after, delimits one element. For instance, in `people.md`, separate different people with `~~~`. These different elements are then parsed into different elements on the site.
2. The `~path~` element. This specifies a path to a picture, and should be put on its own line.

See markdown files in `flask_app/content` for examples of both of these. Nobody needs to edit HTML, just these easy to read `.md` files, which are parsed and formatted properly on the site.

## Under the Hood

Made using [Bootstrap](http://twitter.github.io/bootstrap/) and [Flask](http://flask.pocoo.org/).

### Flask 

Flask does three things: 

1. Handles all incoming requests.

2. Sends parsed `.md` files to page templates.

3. Uses [Jinja2]() to render arbitrary numbers of elements on the page nicely.

### Bootstrap

Bootstrap makes life easier by easily allowing responsive design, scaling the page for phones/tablets/pcs. The column widths are specified in the `.html` template files in `flask_app/templates`. 

These aren't true `.html` files, but Jinja2 templates that Flask converts to proper `.html` files to serve when a request comes in. 

`base_template.html` contains the boilerplate: CSS and JS imports, the basic navbar design, and placement for child templates to insert items.

All other templates inherit from `base_template.html` and put their own content in the appropriate slots in the base template.
