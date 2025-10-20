"""UI components for the application"""

import streamlit as st
from config.settings import Config
from ui.styles import get_custom_css

def render_header():
    """Render application header with visible logo"""
    # Apply CSS only once here
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Render header with separated logo and text for better visibility
    st.markdown(
        f'''<h1 class="main-header">
            <span class="logo-emoji">{Config.APP_ICON}</span>
            <span class="app-name">{Config.APP_NAME}</span>
        </h1>''',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="subtitle">✨ Transform your prompts into powerful, structured queries</p>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Rest of your components.py functions remain the same...
def render_domain_selector():
    """Render domain selection dropdown"""
    return st.selectbox(
        "🎯 **Select Domain**",
        Config.DOMAINS,
        help="Choose the domain that best fits your prompt"
    )

def render_complexity_selector():
    """Render complexity level selector"""
    return st.radio(
        "📊 **Complexity Level**",
        Config.COMPLEXITY_LEVELS,
        horizontal=True,
        help="Choose the depth and sophistication of enhancement"
    )

def render_prompt_input():
    """Render prompt input area"""
    return st.text_area(
        '✍️ **Enter your prompt:**',
        height=150,
        placeholder="Describe what you want to accomplish... Be as specific as possible for better results.",
        help="💡 Tip: The more detailed your input, the better the enhanced output!"
    )

def render_generate_button():
    """Render generate button"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        return st.button(
            "🚀 Generate Enhanced Prompt",
            use_container_width=True,
            type="primary"
        )

def render_results(enhanced_prompt, domain, complexity):
    """Render the results section"""
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown("### ✨ **Enhanced Prompt Result**")
    
    # Metrics cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class="info-card">
                <strong>🎯 DOMAIN</strong><br/>
                <span style="font-size: 18px; font-weight: 600; color: #1e1e1e;">{domain}</span>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="info-card">
                <strong>📊 COMPLEXITY</strong><br/>
                <span style="font-size: 18px; font-weight: 600; color: #1e1e1e;">{complexity}</span>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="info-card">
                <strong>📝 CHARACTERS</strong><br/>
                <span style="font-size: 18px; font-weight: 600; color: #1e1e1e;">{len(enhanced_prompt):,}</span>
            </div>
        """, unsafe_allow_html=True)
    
    # Enhanced prompt display
    st.markdown("")
    st.markdown(
        f'<div class="enhanced-prompt-box">{enhanced_prompt}</div>',
        unsafe_allow_html=True
    )
    
    # Action buttons
    st.markdown("")
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📋 **Copy Prompt**"):
            st.code(enhanced_prompt, language=None)
            st.caption("Select all text above and copy (Ctrl+A, Ctrl+C)")
    
    with col2:
        st.download_button(
            label="📥 Download Enhanced Prompt",
            data=enhanced_prompt,
            file_name=f"enhanced_prompt_{domain.lower().replace(' ', '_')}_{complexity.lower()}.txt",
            mime="text/plain",
            use_container_width=True
        )

def render_footer():
    """Render application footer"""
    st.markdown(f"""
        <div class="footer">
            <p class="app-name">{Config.APP_NAME} v{Config.APP_VERSION}</p>
            <p>Transform your ideas into powerful, structured prompts</p>
            <p class="creator">Created with ❤️ by Asad Faizee</p>
            <div class="social-links">
                <a href="https://github.com/Faizee-Asad" target="_blank">🔗 GitHub</a>
                <a href="https://www.linkedin.com/in/asad-faizee-566341200" target="_blank">💼 LinkedIn</a>
                <a href="https://x.com/faizee_asad" target="_blank">🐦 Twitter</a>
            </div>
            <p style="margin-top: 20px; font-size: 12px; color: #6c757d;">
                © 2025 All rights reserved | Built with Streamlit
            </p>
        </div>
    """, unsafe_allow_html=True)

def show_error(message):
    """Display error message"""
    st.error(f"❌ **Error:** {message}")

def show_warning(message):
    """Display warning message"""
    st.warning(f"⚠️ **Warning:** {message}")

def show_success(message):
    """Display success message"""
    st.success(f"✅ **Success:** {message}")

def show_info(message):
    """Display info message"""
    st.info(f"ℹ️ **Info:** {message}")

def show_spinner(message):
    """Return spinner context"""
    return st.spinner(f"⏳ {message}")