- WSGI : how python app and web server communicate

- Django blog
- python manage.py createsuperuser
- python manage.py makemigrations :

 => generates the SQL commands for preinstalled apps (which can be viewed in installed apps in settings.py) and your newly created apps' model which you add in installed apps

- python manage.py migrate : 

=> migrate executes those SQL commands in the database file.

- To show the SQL query which created the table :
`python manage.py sqlmigrate ModelName migrationNo`
- example :
`python manage.py sqlmigrate blog 0001`

- we can access the user data by : 

`user.ModelName_set.all()` example `user.Post_set.all()`

where user is object we created , `<User: hamza92>`

- we can create data for specific user : 

`user.ModelName_set.create(title="etc...")`


- `admin.site.register(ModelName)` # to give admin all access to the post model , add, update,delete
## create simplified API using django rest framework 

## steps:
1. django-admin startproject myproject 
2. pip install djangorestframework
3. add `'rest_framework'` in Setting.py in `INSTALLED_APPS`
4. create api folder , add __init__.py , views.py inside it.
5. inside views , import Response Class as `from rest_framework.response import Response`.

=> this response object take any python data or serialized data, and it will render it as json data.

6. import api_view , `from rest_framework.decorators import api_view` `

7. add the function and methods for endpoint 
```
@api.view(['GET'])
def getData(request):
    pass
    
```

8. add urls.py to add endpoint 
```
from . import view
urlpatterns=[
path( "" , views.getData),
path( "add/" , views.AddData),


]

```
include urls.py we've created on urls projects .


9. create an app to create a models for data we will serialize.
`python manage.py startapp myapp` 
- register  it in setting.py in installed Apps

10. add your models , for example:
```
class Item (models.Model):
    name= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)
```
11. run migrations

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py shell` (to add dumy data in models)

- to create data im model :
`ModelName.objects.create(fieldName="data etc...")`
- to get all data created  : 

`items = ModelName.objects.all()`

12. add serializer.py , 
- we need to create model serializer because the response object
cannot natively handle complex data types such as django instances. we need to serialize data before we handle it out.

13. in serializer.py import : 
`from rest_framework import serializer`

`from base.model import ModeName` , base is the app name.

- create a class serializer and pass the model and fields required:
``` 
class ModelNameSerializer(serialzers.ModelSerializer):
    class Meta:
        model=ModeName 
        fields='__all__'  # or select fields
```

14. in the views , import  models and serializers,
```
@api.view(['GET'])
def getData(request):
    items=ModelName.objects.all()
    serializer= ModelNameSerializer(items,many=True)
    return Response(serializer.data)
```
 
15. in post request:
```
@api.view(['POST'])
def AddData(request):
    serializer= ModelNameSerializer(data=request.data)
    if serializer.is_valid():  # to check data validity
        serializer.save()
    return Response(serializer.data)

```
### -------  end of create simplified API using django rest framework
