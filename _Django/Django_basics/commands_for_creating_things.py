### Some guidance for getting a start with django project

#Using vitrual enviroments

    deactivate — Exit out of the current Python virtual environment
    workon — List available virtual environments
    workon name_of_environment — Activate the specified Python virtual environment
    rmvirtualenv name_of_environment — Remove the specified environment.

#Run server
python3 manage.py runserver 

#create new app
$ python3 manage.py startapp courses

#database migration
python3 manage.py   migrate

jango.db.models 
#has most of the model functionality you'll use to create models and their fields.

DateTimeField #holds datetime objects.
CharField #holds strings.
TextField #holds an unspecified amount of text.

#More Django model field types
python manage.py makemigrations [app] #will make the migrations for a specific app.
python manage.py migrate [app] #will run the pending migrations for a specific app. If you leave off the app name, any pending migrations for any apps will be run.

python manage.py shell # opens a Python shell with Django's configuration already loaded.

Model.save() #will save an in-memory instance of a model to the database.

Model.create() #will save an in-memory instance of a model to the database and return the newly-created object.

Model.filter(attribute=value) # will get a QuerySet of all instances of the Model that match the attribute values. You can change these values with other comparisons, too, like gte or in.



python manage.py createsuperuser #will create a new superuser, or a user that's allowed to log into the admin area with all permissions.

admin.site.register(Model) #will register a model with the default admin site, which allows you to edit instances of that model in the admin.





