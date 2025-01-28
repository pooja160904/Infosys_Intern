# 🤖🤝 Project Title: AI-Enhanced Customer Support Ticket Resolution and Proactive Issue Prevention System

Welcome to the Customer Support Ticket Analysis and Prevention System!
This project is designed to revolutionize customer support operations. By harnessing the power of sentiment analysis, automated response generation, and issue escalation handling, this system aims to enhance efficiency and improve customer satisfaction.
Built using FastAPI for backend functionality and seamlessly integrated with Zapier, this application provides an end-to-end solution for analyzing support tickets, generating proactive responses, and minimizing recurring issues.

## Features

-  🤔Sentiment Analysis:** Automatically analyze the sentiment of incoming support tickets to prioritize and handle them effectively.
-  📈Issue Escalation:** Identify and escalate critical issues to the appropriate teams for faster resolution.
-  🤖Response Automation:** Generate intelligent and contextually relevant responses to common support queries.
-  📧Email Integration:** Streamlined email handling through Zapier, enabling automated email parsing, ticket creation, and notifications.
-  🖥️User-Friendly App Interface:** A FastAPI-powered application with an intuitive interface for managing tickets, viewing analytics, and handling escalations.

## Tech Stack

-  Programming Language: Python
-  Framework: FastAPI
-  Integration: Zapier for email handling
-  AI Tools: Sentiment analysis and predictive analytics libraries

---

## Project Structure

### Initial Data Analysis
The project begins with an exploratory **data analysis** conducted on two datasets
1. Understand the structure and quality of the data.
2. Identify patterns and trends that inform the subsequent machine learning models.

---

### Sentiment Analysis 
This module determines the sentiment of the user based on their ticket. By classifying tickets into positive, neutral, or negative sentiments, the system:
- Prioritizes tickets requiring immediate attention.
- Provides insights into the overall customer satisfaction levels.

Key steps:
1. Preprocessing ticket data.
2. Training and testing a sentiment classification model.

---

### Issue Escalation
This module identifies tickets requiring escalation based on specific keywords and patterns. If an issue is marked for escalation:
- The ticket is forwarded to a human agent for review.
- Automated responses are bypassed to ensure personalized handling.

Key steps:
1. Keyword-based filtering and rule-based classification.
2. Forwarding flagged tickets for manual intervention.

---

### Response Automation
This module generates automated responses for tickets using:

1. **Classical Machine Learning and Transformer-based Classification**:
   - Products are classified based on ticket content.
   - Predefined templates generate responses tailored to the classified product category.

---

### Integration with FastAPI and Zapier
The entire system is integrated using FastAPI to expose API endpoints for each module. These endpoints are connected through Zapier to:
- Automate workflows and email responses.
- Seamlessly handle escalations and response generation.

This integration ensures:
- Scalability of the system.
- A unified platform for executing all functionalities.

---

## Requirements
### Data
The `data` folder contains all datasets used in this project. Ensure to download the data for running the modules.

### Keys and Dependencies
To run the system, the following keys and dependencies are required:

1. **JSON Key for Google Sheets**
   - [Generate a Google Sheets API Key](https://developers.google.com/sheets/api/quickstart/python)

2. **Gemini API Key**
   - [Sign up for Gemini API Key](https://gemini.docs.api/)

3. **Pinecone API Key**
   - [Get a Pinecone API Key](https://www.pinecone.io/start/)

4. **Dataset**
   - Download from the `data` folder in this repository.

5. **FastAPI and Uvicorn**
   - Install using:
     ```bash
     pip install fastapi uvicorn
     ```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE.txt).

---
## Conclusion
The Customer Support Ticket Analysis and Prevention System offers a robust solution to modern customer support challenges. Leveraging sentiment analysis, issue escalation, and automated response generation, the system streamlines ticket management while ensuring superior customer satisfaction. With seamless integration through FastAPI and Zapier, it is designed to be both scalable and adaptable to a wide range of business requirements.
