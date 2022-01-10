from Cities_API import create_app

if __name__ == '__main__':
    create_app = create_app()
    create_app.run()
else:
    server = create_app()
