"""
PromptLab Pro - Advanced Prompt Enhancement Tool
With improved error handling and debugging
"""

import streamlit as st
import os
from config.settings import Config
from core.prompt_enhancer import PromptEnhancer
from ui.components import (
    render_header,
    render_domain_selector,
    render_complexity_selector,
    render_prompt_input,
    render_generate_button,
    render_results,
    render_footer,
    show_error,
    show_warning,
    show_info,
    show_spinner
)

# Page configuration
st.set_page_config(
    page_title=Config.APP_NAME,
    layout="wide",
    page_icon=Config.APP_ICON
)

# Debug mode (set to True to see more details)
DEBUG_MODE = False  # Change to True for debugging

def initialize_app():
    """Initialize the application with error handling"""
    try:
        if 'enhancer' not in st.session_state:
            st.session_state.enhancer = PromptEnhancer()
        return True
    except Exception as e:
        if DEBUG_MODE:
            st.error(f"Initialization Error: {str(e)}")
            st.code(f"""
Debug Information:
- API Type: {Config.API_TYPE}
- Model: {Config.MODEL_NAME}
- API Key Present: {bool(Config.API_KEY)}
- API Key Length: {len(Config.API_KEY) if Config.API_KEY else 0}
- API Key Start: {Config.API_KEY[:10] + '...' if Config.API_KEY and len(Config.API_KEY) > 10 else 'Not set'}
            """)
        return False

def main():
    """Main application logic"""
    
    # Render header
    render_header()
    
    # Initialize app
    if not initialize_app():
        show_error("Failed to initialize the application. Please check your configuration.")
        st.info("""
        **Troubleshooting Steps:**
        1. Verify your API key is correctly set in the .env file
        2. Check that you have the correct API type (groq or openai)
        3. Ensure your API key has sufficient credits/quota
        4. Verify your internet connection
        """)
        st.stop()
    
    # Create two columns for domain and complexity
    col1, col2 = st.columns([1, 1])
    
    with col1:
        domain = render_domain_selector()
    
    with col2:
        complexity = render_complexity_selector()
    
    # Prompt input
    user_prompt = render_prompt_input()
    
    # Add a debug section if enabled
    if DEBUG_MODE:
        with st.expander("🔧 Debug Information"):
            st.write("**Current Configuration:**")
            st.json({
                "API Type": Config.API_TYPE,
                "Model": Config.MODEL_NAME,
                "Domain": domain,
                "Complexity": complexity,
                "API Key Present": bool(Config.API_KEY)
            })
    
    # Generate button
    if render_generate_button():
        if not user_prompt.strip():
            show_warning("Please enter a prompt before generating")
        else:
            # Show processing spinner
            with show_spinner(f"Enhancing your prompt with {complexity}-level {domain} framework..."):
                try:
                    # Enhance the prompt
                    result = st.session_state.enhancer.enhance_prompt(
                        user_prompt=user_prompt,
                        domain=domain,
                        complexity=complexity
                    )
                    
                    # Display results
                    if result["success"]:
                        render_results(
                            enhanced_prompt=result["content"],
                            domain=domain,
                            complexity=complexity
                        )
                        show_info("✨ Prompt enhanced successfully!")
                    else:
                        show_error(result["error"])
                        
                        # Additional help for common errors
                        if "api" in result["error"].lower():
                            st.info("""
                            **API Configuration Help:**
                            - For Groq: Get your API key from [console.groq.com](https://console.groq.com)
                            - For OpenAI: Get your API key from [platform.openai.com](https://platform.openai.com)
                            - Make sure to add the key to your .env file
                            """)
                        
                except Exception as e:
                    error_message = f"An unexpected error occurred: {str(e)}"
                    show_error(error_message)
                    if DEBUG_MODE:
                        st.exception(e)
    
    # Render footer
    render_footer()

if __name__ == "__main__":
    # Check if API key is configured
    if not Config.API_KEY:
        st.error("⚠️ **Application not configured properly**")
        st.markdown("""
        ### Setup Instructions:
        
        1. **Create a `.env` file** in your project root directory
        
        2. **Add your OpenRouter API configuration:**
        ```
        OPENROUTER_API_KEY=your_openrouter_api_key_here
        DEFAULT_MODEL=deepseek/deepseek-chat-v3-free
        TEMPERATURE=0.7
        MAX_TOKENS=50000
        ```
        
        3. **Get your FREE OpenRouter API key:**
        - Visit [OpenRouter.ai](https://openrouter.ai)
        - Sign up for a free account
        - Go to [Keys](https://openrouter.ai/keys) section
        - Create a new API key
        - Copy and paste it into your .env file
        
        4. **Restart the application** after adding your API key
        
        **Note:** We're using DeepSeek V3 free model - completely free with no credit card required!
        """)
        st.stop()
    
    # Run main app
    try:
        main()
    except Exception as e:
        st.error(f"Application Error: {str(e)}")
        if DEBUG_MODE:
            st.exception(e)