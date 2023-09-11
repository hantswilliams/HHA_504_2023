
"""

first we 'load' our package called 'app' that we created, the package is defined by our __init__.py file

then we create an instance of our app using the create_app() function we defined in __init__.py

then we run the app, the __name__ variable is a special variable that gets as value the string "__main__", and the code within it
will only run if the script is executed directly, not imported

"""

from .app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
