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

......
IntegerField #is a field that holds integers, or whole numbers.

An inline #is a smaller form inside of a larger form. The smaller form represents a related record in the database.

StackedInline #is an inline where each field takes up the full width of the form. Fields are stacked.

TabularInline #is an inline where each field is part of a single row for the form.



{% url 'path.to.view' %} to link to a view who's URL doesn't have a name.

Note: This has been removed in Django 1.10 and beyond. If you want to use this feature, be sure to install Django 1.9 or below. You can do that with pip install django<1.10. Better yet, name all of your URLs as shown below.

url(r'pattern', views.view, name='list') to name an URL

{% url 'list' %} to link to a named URL

include('courses.urls', namespace='course') to namespace a group of URLs

{% url 'courses:list' %} to link to a named and namespaced URL




