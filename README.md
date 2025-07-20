# Gold Code Transmission Simulator

This is an educational web application that simulates how **Gold codes** are used in digital communications. It demonstrates how data is encoded, transmitted (with simulated noise), and decoded using Gold codes. The purpose of this project is to help users understand the theory and practice behind error-resilient digital transmission.

---

## Features

- Interactive **form-based interface** to input transmission parameters  
- Simulation of **bit errors** during transmission  
- Generation of reports showing things like:
  - Generated Gold code
  - Used polynomials
  - Encoded/decoded sequences
- Dedicated **explanation page** describing:
  - What Gold codes are and how they work
  - How to use the simulator
  - Requirements for the input
  - How encoding and decoding is performed
- Backend-driven simulation with realistic noise behavior (done in software)

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML + Tailwind CSS, JavaScript

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/dexppy/goldCodeSimulator.git
cd goldCodeSimulator
```
### 2. Create and activate a virtual environment
#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### On Linux\macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the app
```bash
flask run
```
Then open your browser and navigate to:
http://localhost:5000

## Background
This project was developed as a university assignment focused on signal transmission and coding theory. The goal was to create an educational tool to help visualize the behavior of Gold codes and the effects of bit errors in noisy environments.

The simulator is fully self-contained, with no external services or network dependencies—transmission and noise are simulated programmatically.

## What Could Be Improved
<ul>
  <li>Adding functional documentation and inline code comments</li>
  <li>Implementing security features (e.g., form validation, error handling)</li>
  <li>Automated unit tests</li>
</ul>
This project was developed entirely by me, and due to time constraints, I focused on core functionality rather than robustness or production-readiness.
