# 7_2_assignment
This Flask application provides a simple API to count GET requests made to a specific endpoint and allows resetting the counter through a POST request.

## Features
**Count Requests:** Increments a counter with each GET request to `/count-requests`.

**Reset Counter:** Allows resetting the request counter to 0 with a POST request to `/reset-counter`.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- Flask

You can install Flask using pip:
``
pip install Flask
``

Run the Flask application:
``
python app.py
``

The Flask development server will start, and the application will be accessible at `http://localhost:5000`.

## Usage
- To increment the request counter, send a GET request to `/count-requests`. You can do this by visiting `http://localhost:5000/count-requests` in your web browser.

- To reset the request counter to 0, send a POST request to `/reset-counter`. This can be done using a tool like Postman or with the following curl command:

``
curl -X POST http://localhost:5000/reset-counter
``
## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.