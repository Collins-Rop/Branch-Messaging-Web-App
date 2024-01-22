# Branch Messaging Web App
 This is a simple messaging web app built using Django and Python.This Python-based web application demonstrates user/client communications, customer service agent responses. 
# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites
 Python 3.11
 Node.js and npm
 pip and pipenv (for managing Python dependencies)
 # Installing
1. Clone the repository:
git clone https://github.com/Collins-Rop/Branch-Messaging-Web-App
2. Create a virtual environment and activate it:
cd branch-messaging-web-app
python3 -m venv venv
source venv/bin/activate
3. Install Python dependencies
pip install virtualenv
 pip install django
 pip install django-crispy-forms==1.14.0
 pip install pandas
 pip install openpyxl pip
4. Compile the React app:
   cd branch messaging
   npm install
   npm run build

# Successfully Developed: 
 A web-based communications application designed to provide responses to inquiries submitted by clients. The system enables a group of agents to efficiently address incoming communications from many customers.
  Messages from customers may be transmitted and received via a simulated API endpoint implemented as a straightforward web form.
  Preserve communications from CSV files in a database.Individual messages are accessible via the agents' portal, where they are able to view and reply to them.
  Host my application locally on my system.
  Methods for surfacing messages that require immediate attention and are more essential were investigated.
  Search functionality has been implemented to enable agents to conduct searches on incoming messages and/or customers.
# Notable Accomplishments:
  Messages are sorted by key word matching, with high priority assigned to those that match, and normal priority assigned to the remaining messages.
