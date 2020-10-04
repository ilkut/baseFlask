# baseFlask
Blueprinted flask scaffolding including homepage and user profile for future clones.

Based on : [Miguel Grinberg's guide.](courses.miguelgrinberg.com)

### Following clone into a new directory with no packages:
0. rmdir /migrations
1. virtualenv venv && source venv/Scripts/activate && pip install -r requirements.txt
2. flask db init
3. flask db migrate -m 'users & posts table' && flask db upgrade
4. play


### To Do
+ password recovery
