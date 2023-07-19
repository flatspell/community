# localinvestor.app
Repo for local investment network product, currently called lina: Local Investment Network Accelerator. 

In development and will be launching at localinvestor.app

## Heroku App
This app is managed via Heroku and can be accessed at https://flatspell.herokuapp.com

For local development, download the repo to your machine and setup a development branch. 

Setup a virtual environment so you have clean dependency management. Activate the virtual environment and download dependencies.
```
cd your/path/to/repos/community
python -m venv your_env_name
source your_env_name/bin/activate
pip install -r requirements.txt
```

From the top level directory you can boot up a local version of the app and test your changes in real-time.
```
git checkout -b yourname/yourtask
source .env
python manage.py run
```

You can exit the virtual enviroment by typing `deactivate` in your command line.
