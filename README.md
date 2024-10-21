## ML-Enhanced Web Application Firewall (WAF)
# Overview
Introducing my ML-Enhanced Web Application Firewall (WAF), a smarter way to protect your digital presence and resources. Unlike regular firewalls, my WAF uses machine learning, which helps it to learn and adapt to new threats as they emerge, to detect and respond to the potential attacks to our system.

# Features
- Machine Learning-Powered: Uses K-means clustering (unsupervised learning algorithms) to analyze and detect potential threats with high accuracy.
- Real-Time Threat Detection: Learns from incoming traffic patterns and adapts to evolving cyberattacks.
- Custom Dataset: Created using tools like Acunetix and Burp Suite to simulate a wide range of web vulnerabilities and attack vectors.
- Scalable Protection: Suitable for any web application regardless of size, able to handle increasing traffic and threats dynamically.
- In-Progress Frontend: Intuitive and easy-to-use frontend interface for monitoring and managing detected threats (under development).

# How It Works
- Data Collection:
Security tools like Acunetix and Burp Suite were used to gather data on various web application vulnerabilities and attack types (SQL injections).
- Preprocessing:
The collected dataset is preprocessed to remove noise, normalize values, and ensure it is ready for training.
- Machine Learning Model:
A K-means clustering algorithm is used for unsupervised training. The algorithm identifies normal behavior patterns in the network traffic and flags anomalies that could indicate malicious activity.
- Real-Time Analysis:
As traffic flows into the web application, the WAF evaluates it against known patterns and detects any potential security threats. New threats are continuously learned by the model to enhance future detection capabilities.

# Tools and Technologies
- Acunetix: Used for vulnerability scanning and dataset collection.
- Burp Suite: Another dataset collection tool.
- K-means Clustering: The machine learning algorithm used for unsupervised classification of normal and malicious traffic.
- Python & PyCaret: Used to develop and train the machine learning model.
- Flask/FastAPI (In Progress): To create an API for model communication with the frontend.
- React.js/Material UI (In Progress): Frontend in development to offer a real-time dashboard for monitoring attacks and managing the firewall.

# Workflow Diagram
[Workflow](README.md) ![Workflow](<Screenshot 2024-09-04 095634.png>)

# Model Training Results
[Results](README.md) ![Results](<Screenshot 2024-10-21 223034.png>)

# Installation
- Clone the repository:
git clone https://github.com/Nidhi-Satyapriya/ML-Enhanced-WebApp-Firewall/
 
   cd ML-WAF

- Install dependencies:
pip install -r requirements.txt

- Run the model (when available):
python run_model.py

- Start the web dashboard (when available):
cd frontend
npm install
npm start

# Usage
- Run the Model: Ensure that the server is running and the machine learning model is active for traffic analysis.
python run_model.py
- Enter a Website URL: Once the frontend is ready, users will be able to enter the URL of any website on the dashboard.

- Prediction:
   - The WAF will analyze the URL's traffic behavior and compare it to known threat patterns.
   - The result will indicate whether the website is Safe or Not Safe based on the model’s predictions.

- Threat Details (when available): The dashboard will provide detailed insights on why the URL was classified as unsafe, including any anomalies detected in the traffic.
- When the frontend is complete, you'll be able to access detailed reports, logs, and threat mitigation options through the dashboard.

# Future Enhancements
- Frontend Completion: A user-friendly interface to monitor the firewall's status, view threats, and configure rules.
- Model Optimization: Further fine-tuning the machine learning model to improve performance with large datasets.
- Threat Reporting: Automated alerting and real-time notifications when a threat is detected.

# Contribution
We welcome contributions from the community! Feel free to submit issues, feature requests, or pull requests.

# How to contribute
 - Fork the repository.
 - Create a feature branch.
 - Commit your changes.
 - Open a pull request.

# License
This project is licensed under the MIT License.

# Contact
For more information, please contact:

Nidhi

B.Tech in Computer Science Engineering

IIIT Bhagalpur

Email: nidhi.2201186cs@iiitbh.ac.in
