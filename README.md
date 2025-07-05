# Custom Quote Generator

A simple and elegant web app built with Flask that generates a quote based on how you're feeling. Enter your emotion (e.g., *happy*, *anxious*) and receive a personalized quote to match your mood.

## Features

* Accepts user input for emotions or feelings
* Displays a contextual quote based on the emotion entered
* Clean, responsive, and modern UI with:

  * Background image
  * Slight blur effect
  * Styled form and typography
* Easy to customize and expand with more quotes or themes

## Tech Stack

* **Backend:** Python + Flask
* **Frontend:** HTML, CSS (vanilla)
* **Templating:** Jinja2
* **Static Assets:** served via Flask's `static/` folder

## Project Structure

```
project/
   app.py
   static/
       images/
          background.jpg
   templates/
        index.html
   README.md
```

## Ideas for Improvement

* Add user authentication

* Store quotes in a database or API

* Add dark mode / accessibility options
