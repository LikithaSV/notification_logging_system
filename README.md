## Setup

#### Please follow the following steps to setup the sample app:

```
git clone git@bitbucket.org:tata1mg/torpedo_boilerplate.git
cd torpedo_boilerplate
pyenv virtualenv 3.8.15 torpedo_boilerplate
touch config.json
```
* copy config from config_template.json.
* add database credentials(postgres needs to run locally or you can to a remote database)
* Activate virtualenv if not activated automatically
```
   pip install -r requirements/base.txt
   python3 -m app.service
   ```
   
* Happy coding!



#### How to run sample handlers
1. hello world
```
curl --request GET \
  --url http://0.0.0.0:6561/v4/hello/<name>
```

2. get user
```
curl --location --request GET 'http://localhost:6561/v4/users?username=<username>'
```

#### Sample response structure

```
{
    "data": {}
} 
```