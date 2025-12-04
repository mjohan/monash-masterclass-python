# Monash App Sprint - Django Sign Up Demo

This project is a small Django web application for a Monash University Indonesia masterclass.

The goal of this project is to:

- Show how a real web application sign up form works  
- Demonstrate how Python and Django can validate each field in the form  
- Allow you to start from a version without validation, then add rules together during the session  

The main pages are:

- A landing page with a short introduction and a button to the sign up form  
- A sign up page with several fields such as username, full name, age, phone number, email, password, and confirm password  
- A simple success page that appears after a successful form submission  

All validation rules are designed to live in `accounts/services/validators.py`.  
The Django form in `accounts/forms/signup_form.py` calls those validator functions.

## Requirements

You need the following tools installed on your system:

- Python 3.12  
- Git  
- Conda or another virtual environment tool  
- Django 6.x (it will be installed inside the environment)  

## Setup

You can follow these steps to set up the project.

### 1. Clone the repository

```bash
git clone https://github.com/mjohan/monash-masterclass-python.git monash-masterclass
cd monash-masterclass
```

### 2. Create and activate a conda environment

```bash
conda create -n monash_signup python=3.12
conda activate monash_signup
```

If you do not want to use conda, you can use another environment tool instead. The important part is that you have an isolated environment with Python 3.12.

### 3. Install Django

Inside the activated environment, run:

```bash
python -m pip install "Django>=6.0,<7.0"
```

You can pin a specific Django version if you prefer, for example:

```bash
python -m pip install "Django==6.0.1"
```

### 4. Run database migrations

Even though the demo does not create custom models for the sign up form, Django still needs its default tables.

```bash
python manage.py migrate
```

## Run the development server

Start the Django development server with:

```bash
python manage.py runserver
```

Then open your browser and visit:

- Landing page: `http://127.0.0.1:8000/`  
- Sign up page: `http://127.0.0.1:8000/accounts/signup/`  

On the sign up page you should see the form. In the starter version, the form accepts any values and always goes to the success page. During the masterclass you can open `accounts/services/validators.py` and add real validation rules together with the students.

## Switch between versions with and without validation

You can use Git tags to move between different versions of the project.

The following tag names are only examples. You can adjust them to match the tags you actually create.

- `v1.0-signup-validation`  
  Version where validation logic is fully implemented  

- `v1.1-signup-starter`  
  Version where validators are only stubs and do not enforce rules yet  

### List available tags

```bash
git tag
```

This shows all tags in the repository.

### Check out the version with validation

```bash
git checkout v1.0-signup-validation
```

Then run:

```bash
conda activate monash_signup # if needed
python manage.py migrate
python manage.py runserver
```

In this version, the validators in `accounts/services/validators.py` contain real checks and use `raise ValidationError("message")` when a rule fails.

### Check out the starter version without validation

```bash
git checkout v1.1-signup-starter
```

Then run:

```bash
conda activate monash_signup   # if needed
python manage.py migrate
python manage.py runserver
```

In this version:

- Form fields are defined with `required=False`  
- The `validators.py` functions only return their input values  
- Each function has a small `# TODO` comment that reminds you to use `raise ValidationError("message")` when you implement rules  

This is the recommended version to use at the start of the masterclass, because you can add each rule step by step in front of the students.

## Where to add or change validation rules

During the session, the main file you will edit is:

`accounts/services/validators.py`

Example functions in that file:

- `validate_username(username)`  
- `validate_full_name(full_name)`  
- `validate_age(age)`  
- `validate_phone_number(phone_number)`  
- `validate_email_address(email)`  
- `validate_password(password)`  
- `validate_confirm_password(password, confirm_password)`  
- `validate_agree_to_terms(agree_to_terms)`  

The `SignupForm` in `accounts/forms/signup_form.py` already calls these functions in:

- `clean_username`, `clean_full_name`, `clean_age`, and other `clean_<field>` methods  
- The `clean` method for checks that involve more than one field  

This means you can focus on `validators.py` during the live coding without changing the form or the views.

## Questions and contributions

If you want to make a pull request or ask a question about this project, please contact:

**Muhammad Johan Alibasa**  
Email: johan.alibasa@monash.edu

---