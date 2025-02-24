import app
application = app.create_app()

if __name__ == '__main__':
    application.run(port=8080, debug=True)
