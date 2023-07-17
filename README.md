# H1 todo-app

# H3 description
A simple app to list your TODOs, with front written in svelte and back in fastAPI. One issue with is that after adding new tasks you need to refresh the page to see them because they need to be fetched from the database.

# H3 how to open the app
In order to open the app go to backend directory and in terminal run 'ucivorn main:app --reload' to open in development mode. It should run on host '127.0.0.1' and port '8000' (default settings). Then go to frontend directory and in terminal run 'npm run dev' to open the website in development mode. By default it should run on 'localhost:5173'