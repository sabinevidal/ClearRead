# flask-boilerplate
 Flask + SQLAlchemy + SQLite + WTForms

 Recommend using yarn2 'berry' with pnp and no node_modules

For dev in 2 separate terminals run
`yarn run tailwind:watch`
`flask run`


https://dev.to/ffpaiki/flask-tailwindcss-flask-assets-51mo
https://yarnpkg.com/getting-started/install
https://github.com/cburmeister/flask-bones/blob/master/app/assets.py

https://www.section.io/engineering-education/integrate-tailwindcss-into-flask/

https://hackersandslackers.com/flask-assets/

https://testdriven.io/blog/flask-htmx-tailwind/

https://tailwindcomponents.com/cheatsheet/

# TODO: assets? compile scss
# TODO: basic styling
# TODO: image uploading?
# TODO: Auth setup
# TODO: errors
# TODO: tests https://flask.palletsprojects.com/en/2.0.x/tutorial/tests/
# TODO: README notes
# TODO: instructions for deployment


# * Accessibilty
# TODO: Check all html
# TODO: form html check best practices
# TODO: images check best practices
# TODO: colour guidelines

# * Forms
# TODO: specify input types and styles in _field.html
https://github.com/tailwindlabs/tailwindcss-forms/blob/master/index.html
```
<form method="POST" action="{{ request.url }}">
    {{ form.hidden_tag() }}
    <h3 class="form-heading">{{ form_heading }}</h3>
    <div>
        <fieldset>
            <legend>Information</legend>
            {{ render_field(form.name) }}
            {{ render_field(form.email) }}
        </fieldset>
        <fieldset>
            <legend>More Information</legend>
            {{ render_field(form.name2) }}
            {{ render_field(form.email2) }}
        </fieldset>
     </div>
    <input type="submit" role="button" name="submit" value="Submit" class="btn-grey">
</form>
```
http://web-accessibility.carnegiemuseums.org/code/forms/
https://adrianroselli.com/2016/01/links-buttons-submits-and-divs-oh-hell.html
https://css-tricks.com/a-complete-guide-to-links-and-buttons/
http://web-accessibility.carnegiemuseums.org/code/navigation/
