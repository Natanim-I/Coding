# Django Todo App

A beautiful and modern todo application built with Django that allows you to create, edit, delete todos, assign due dates, and mark them as resolved.

## Features

- ✅ Create new todos with title, description, and due date
- ✏️ Edit existing todos
- 🗑️ Delete todos with confirmation
- 📅 Assign due dates to todos
- ✓ Mark todos as resolved/unresolved
- 🔍 Filter todos by status (All, Active, Completed, Overdue)
- 🎨 Modern and responsive UI with beautiful gradients
- ⚠️ Visual indicators for overdue todos

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd OASIS-Todo
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000/
   ```

## Usage

### Creating a Todo
1. Click the "Create New Todo" button on the main page
2. Fill in the title (required)
3. Optionally add a description
4. Optionally set a due date and time
5. Click "Save Todo"

### Editing a Todo
1. Click the "Edit" button on any todo item
2. Modify the fields as needed
3. Click "Save Todo"

### Marking as Resolved
- Click the "Mark Resolved" button on any active todo
- Or toggle the checkbox when editing a todo
- Click "Reopen" to mark a resolved todo as active again

### Deleting a Todo
1. Click the "Delete" button on any todo
2. Confirm the deletion in the confirmation page

### Filtering Todos
Use the filter buttons at the top:
- **All**: Show all todos
- **Active**: Show only unresolved todos
- **Completed**: Show only resolved todos
- **Overdue**: Show todos that are past their due date and not resolved

## Project Structure

```
OASIS-Todo/
├── manage.py
├── requirements.txt
├── README.md
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── todos/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    └── templates/
        └── todos/
            ├── base.html
            ├── todo_list.html
            ├── todo_form.html
            └── todo_confirm_delete.html
```

## Admin Panel

Access the Django admin panel at:
```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created to log in and manage todos from the admin interface.

## Technologies Used

- **Django 4.2+**: Web framework
- **SQLite**: Database (default, can be changed in settings.py)
- **HTML/CSS**: Frontend with modern, responsive design

## Customization

You can customize the app by:
- Modifying the `Todo` model in `todos/models.py` to add more fields
- Updating the templates in `todos/templates/todos/` to change the UI
- Adjusting the styling in the base template
- Changing the database in `todo_project/settings.py`

## License

This project is open source and available for personal and commercial use.

