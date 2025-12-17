from cms import create_app  # Import the function 'create_app'

app = create_app()          # Initialize the app using that function

if __name__ == '__main__':
    app.run(debug=True)