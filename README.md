# PromptLab Pro

![PromptLab Pro Logo](https://img.shields.io/badge/PromptLab%20Pro-AI%20Powered-4A9EFF?style=for-the-badge&logo=openai&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenRouter API](https://img.shields.io/badge/Powered%20by-OpenRouter-6C5B7B?style=for-the-badge)

PromptLab Pro is an advanced, AI-powered tool designed to transform your basic ideas into highly structured, detailed, and effective prompts for large language models (LLMs). Whether you're a researcher, a creative writer, a developer, or a business strategist, PromptLab Pro helps you craft superior prompts tailored to specific domains and desired complexity levels, ensuring better outputs from your AI interactions.

## 🌟 About the Project

PromptLab Pro acts as your personal prompt engineering assistant. It's built as a Streamlit web application, offering an intuitive interface to enhance your prompts.

**Key Features:**

*   **Domain-Specific Enhancement:** Choose from a variety of domains (e.g., Research & Analysis, Creative Writing, Technical/Coding, Business Strategy, Data Science, Education & Teaching, General Purpose) to guide the enhancement process.
*   **Complexity Levels:** Select a complexity level (Proficient, Expert, Master) to dictate the depth and sophistication of the generated prompt. Each level unlocks increasingly detailed and nuanced frameworks.
*   **Intuitive User Interface:** A clean and responsive Streamlit interface makes prompt enhancement quick and easy.
*   **OpenRouter Integration:** Leverages the OpenRouter API, providing flexibility to use various cutting-edge LLMs (configured by default with `deepseek/deepseek-chat-v3.1:free`) for robust prompt enhancement.
*   **Extensible Templates:** Easily add or modify domain-specific templates to customize the enhancement logic.

**Technologies Used:**

*   **Python:** The core programming language.
*   **Streamlit:** For creating the interactive web application.
*   **OpenRouter API:** The primary API for interacting with LLMs to perform prompt enhancement.
*   **python-dotenv:** For managing environment variables securely.
*   **requests:** For making HTTP requests to the OpenRouter API.
*   **Dev Containers:** Provides a ready-to-use development environment for VS Code users.

## 🚀 Getting Started

Follow these instructions to set up and run PromptLab Pro on your local machine.

### Prerequisites

*   Python 3.11 or higher
*   `pip` (Python package installer)
*   An OpenRouter API key

### 1. Clone the Repository

bash
git clone [https://github.com/your-username/promptlab-pro.git](https://github.com/Faizee-Asad/PromptLab-Pro)
cd promptlab-pro


### 2. Set Up Environment Variables

Create a file named `.env` in the root directory of the project. This file will store your API key and other configurations.

```
OPENROUTER_API_KEY="your_openrouter_api_key_here"
# Optional: Adjust model temperature (default: 0.7)
# TEMPERATURE="0.5"
# Optional: Adjust max tokens for API response (default: 50000)
# MAX_TOKENS="2000"
```
Replace `"your_openrouter_api_key_here"` with your actual API key obtained from [OpenRouter](https://openrouter.ai/).

### 3. Install Dependencies

Install the required Python packages:

bash
pip install -r requirements.txt


### 4. Run the Application

Start the Streamlit application:

bash
streamlit run app.py


After running, your web browser should automatically open to `http://localhost:8501`, where PromptLab Pro will be running.

### Using Dev Containers (Optional)

If you use VS Code and have the Dev Containers extension installed, you can open this project in a development container. This will automatically set up the Python environment, install dependencies, and even start the Streamlit app.

1.  Ensure you have Docker installed and running.
2.  Open the project in VS Code.
3.  Click the green "Open a remote window" button in the bottom left of the VS Code window or use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select `Dev Containers: Reopen in Container`.
4.  The container will build and configure the environment. Once ready, the Streamlit app will automatically launch and forward port `8501` to your local machine, opening a preview in VS Code or your browser.

## 💡 Usage

Once the application is running, follow these steps to enhance your prompts:

1.  **Enter your prompt:** In the main text area, type or paste your initial prompt. Be as specific as possible, even if it's brief, for the best enhancement.
2.  **Select Domain:** Choose the domain that best aligns with your prompt's context (e.g., "Business Strategy" for a marketing plan, "Data Science" for an analytical query).
3.  **Choose Complexity Level:**
    *   **Proficient:** Provides a solid, structured prompt with key considerations.
    *   **Expert:** Generates a highly detailed prompt, assuming advanced knowledge and incorporating more sophisticated frameworks.
    *   **Master:** Crafts a visionary, C-suite level prompt, integrating cutting-edge concepts and a broader strategic outlook.
4.  **Generate Enhanced Prompt:** Click the "🚀 Generate Enhanced Prompt" button.
5.  **Review Results:** The application will display your newly enhanced, structured prompt, ready for use with your preferred LLM.

Experiment with different domains and complexity levels to see how PromptLab Pro can refine your interactions with AI models!
