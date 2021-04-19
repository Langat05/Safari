from app import create_app
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
# Creating app instance


app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


if __name__ == '__main__':
    manager.run()