from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

from app.models import User,Comment,Posts
#creating app instance
app=create_app('production')

#creating manager instance

manager=Manager(app)
manager.add_command('server',Server)

migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Comment=Comment,Posts=Posts)

if __name__=='__main__':
    manager.run()