from Cities_API import create_app

if __name__ == '__main__':
    create_app = create_app()
    create_app.run(debug=True)
else:
    server = create_app()
