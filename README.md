# Restaurant Name Generator

This project is a restaurant name and menu generator web app, created using LangChain and Streamlit. The app suggests restaurant names based on the cuisine type and generates a menu for the named restaurant.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Restaurant Name Generator uses the LangChain library to create chains of prompts that generate a restaurant name based on a given cuisine and then create a menu for the restaurant. The web app is built and hosted using Streamlit.

### Features

- Generate a fancy restaurant name based on the type of cuisine.
- Generate a menu for the restaurant.
- Display the restaurant name and menu on a web app.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit

### Clone the Repository

git clone https://github.com/yourusername/restaurant-name-generator.git
cd restaurant-name-generator

### Install Dependencies

pip install -r requirements.txt

Usage
Running the App

    Set your OpenAI API key in a .env file:

    plaintext

OPENAI_API_KEY=your_openai_api_key

Run the Streamlit app:

streamlit run restaurant_generator.py

    Open your browser and go to http://localhost:8501.

### Project Structure

    restaurant_generator.py: The Streamlit app code.
    langchain_helper.py: Contains the functions and chains for generating restaurant names and menus.
    requirements.txt: Lists the Python dependencies.
    .env: Contains the OpenAI API key (not included in the repository).

### Resources

- LangChain Documentation: https://python.langchain.com/v0.1/docs/get_started/introduction
- LangChain Chains: https://python.langchain.com/v0.1/docs/expression_language/cookbook/multiple_chains/
- LangChain Fundamentals Video: https://www.youtube.com/watch?v=yF9kGESAi3M&t=3811s
- Restaurant Creator App Tutorial: https://www.youtube.com/watch?v=nAmC7SoVLd8&t=1614s
- Streamlit Documentation: https://streamlit.io/

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
License

This project is licensed under the MIT License. See the LICENSE file for details.

```

```
