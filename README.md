# Django Appointment Booking with Google Calendar Integration

This project is a Django-based appointment booking system with integration to Google Calendar. Users can book appointments with doctors, and events are automatically created in Google Calendar.

---

## Features

1. **User Registration and Authentication**:
   - Users can register, log in, and log out.
   - Staff and non-staff roles are supported.

2. **Appointment Booking**:
   - Patients can book appointments with doctors.
   - Appointment duration is set to 45 minutes by default.

3. **Google Calendar Integration**:
   - Automatically creates calendar events for booked appointments.
   - Uses OAuth 2.0 for authentication.

4. **Doctor Management**:
   - View a doctor's profile.
   - Restricts staff access to specific functionalities.

---

## Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS
- **Database**: SQLite (default, configurable)
- **Integration**: Google Calendar API
- **Authentication**: Django Authentication Framework

---

## Installation

### Prerequisites

1. Python 3.12 or later.
2. Django 4.x.
3. Google Cloud project with Calendar API enabled.

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Configure Google Calendar API:

Download your credentials.json file from Google Cloud.
Place it in the credentials directory of the project.

Run database migrations:

python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Usage
Navigate to the app in your browser at http://127.0.0.1:8000.
Register or log in as a user.
Book an appointment with a doctor.
Check your Google Calendar for the created event.


Google Calendar Integration Details
Authentication:

The create_google_calendar_event function manages the authentication and event creation.
Token files are stored locally to avoid repeated authentication.
Scopes:

The project uses the https://www.googleapis.com/auth/calendar.events scope.
Error Handling:

Handles token expiration and refresh automatically.
Known Issues
Event timezones default to UTC. Update the timeZone field in the create_google_calendar_event function if required.
Ensure that the token.json file is not exposed in production.
