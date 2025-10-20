"""CSS styles for the application - Light Theme with visible logo"""

def get_custom_css():
    """Return custom CSS for the app with light theme and visible logo"""
    return """
    <style>
        /* ============ Color Variables - Light Theme ============ */
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --bg-card: #ffffff;
            --bg-hover: #f1f3f5;
            --text-primary: #1e1e1e;
            --text-secondary: #495057;
            --text-muted: #6c757d;
            --accent-primary: #4a9eff;
            --accent-secondary: #7b61ff;
            --accent-gradient: linear-gradient(135deg, #4a9eff 0%, #7b61ff 100%);
            --success: #28a745;
            --warning: #ffc107;
            --error: #dc3545;
            --border: #dee2e6;
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.08);
            --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.12);
        }
        
        /* ============ Global Styles ============ */
        .stApp {
            background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
            color: var(--text-primary);
        }
        
        /* ============ Header Styles - Fixed for Logo Visibility ============ */
        .main-header {
            font-size: 3.5em;
            font-weight: 800;
            text-align: center;
            margin-bottom: 10px;
            color: var(--text-primary) !important;
            animation: fadeIn 1s ease-out;
        }
        
        /* Logo emoji styling */
        .main-header .logo-emoji {
            display: inline-block;
            font-size: 1em;
            margin-right: 15px;
            animation: bounce 2s infinite;
        }
        
        /* App name with gradient */
        .main-header .app-name {
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: inline-block;
        }
        
        .subtitle {
            text-align: center;
            color: var(--text-secondary) !important;
            font-size: 1.2em;
            margin-bottom: 30px;
            font-weight: 400;
            letter-spacing: 0.5px;
            animation: fadeIn 1.2s ease-out;
        }
        
        .divider {
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--accent-primary), var(--accent-secondary), transparent);
            margin: 30px 0;
            opacity: 0.5;
            animation: shimmer 3s infinite;
        }
        
        /* ============ Input Components ============ */
        /* Text Area */
        .stTextArea > div > div > textarea {
            background-color: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border: 2px solid var(--border) !important;
            border-radius: 12px !important;
            padding: 15px !important;
            font-size: 16px !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            transition: all 0.3s ease !important;
            box-shadow: var(--shadow-sm) !important;
        }
        
        .stTextArea > div > div > textarea:focus {
            border-color: var(--accent-primary) !important;
            box-shadow: 0 0 0 3px rgba(74, 158, 255, 0.1), var(--shadow-md) !important;
            background-color: var(--bg-primary) !important;
        }
        
        .stTextArea > div > div > textarea::placeholder {
            color: var(--text-muted) !important;
        }
        
        /* Select Box */
        .stSelectbox > div > div > select {
            background-color: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border: 2px solid var(--border) !important;
            border-radius: 12px !important;
            padding: 10px 15px !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
            cursor: pointer !important;
            box-shadow: var(--shadow-sm) !important;
        }
        
        .stSelectbox > div > div > select:hover {
            border-color: var(--accent-primary) !important;
            background-color: var(--bg-hover) !important;
        }
        
        /* Radio Buttons */
        .stRadio > div {
            background-color: var(--bg-secondary);
            border-radius: 12px;
            padding: 12px;
            border: 2px solid var(--border);
            box-shadow: var(--shadow-sm);
        }
        
        /* ============ Buttons ============ */
        .stButton > button {
            background: var(--accent-gradient) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 14px 28px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            letter-spacing: 0.5px !important;
            transition: all 0.3s ease !important;
            box-shadow: var(--shadow-md) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(74, 158, 255, 0.3) !important;
        }
        
        /* Download Button */
        .stDownloadButton > button {
            background: linear-gradient(135deg, var(--success) 0%, #22c55e 100%) !important;
            color: white !important;
        }
        
        .stDownloadButton > button:hover {
            box-shadow: 0 6px 20px rgba(40, 167, 69, 0.3) !important;
            transform: translateY(-2px) !important;
        }
        
        /* ============ Results Section ============ */
        .enhanced-prompt-box {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border: 2px solid var(--accent-primary);
            border-left: 5px solid var(--accent-primary);
            border-radius: 16px;
            padding: 28px;
            color: var(--text-primary) !important;
            font-size: 16px;
            line-height: 1.8;
            box-shadow: 0 4px 20px rgba(74, 158, 255, 0.1);
            position: relative;
            overflow: hidden;
            animation: slideIn 0.5s ease-out;
            margin: 25px 0;
        }
        
        .enhanced-prompt-box::before {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            right: -100%;
            height: 3px;
            background: var(--accent-gradient);
            animation: shimmer 3s infinite;
        }
        
        /* Info Cards */
        .info-card {
            background: var(--bg-card);
            border-radius: 12px;
            padding: 18px 20px;
            border: 2px solid var(--border);
            border-left: 4px solid var(--accent-primary);
            box-shadow: var(--shadow-sm);
            transition: all 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
            border-color: var(--accent-primary);
        }
        
        /* ============ Footer ============ */
        .footer {
            text-align: center;
            padding: 40px 20px;
            margin-top: 60px;
            border-top: 2px solid var(--border);
            background: linear-gradient(180deg, transparent 0%, #f8f9fa 100%);
        }
        
        .footer p {
            color: var(--text-secondary) !important;
            margin: 8px 0;
            font-size: 14px;
        }
        
        .footer .app-name {
            color: var(--text-primary) !important;
            font-size: 20px;
            font-weight: 700;
        }
        
        .footer .creator {
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            font-size: 16px;
            margin: 20px 0 15px 0;
        }
        
        .footer .social-links a {
            color: var(--text-secondary) !important;
            text-decoration: none;
            margin: 0 15px;
            padding: 8px 16px;
            border-radius: 8px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            display: inline-block;
            transition: all 0.3s ease;
        }
        
        .footer .social-links a:hover {
            color: white !important;
            background: var(--accent-gradient);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
            border-color: transparent;
        }
        
        /* ============ Animations ============ */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        /* ============ Hide Streamlit Elements ============ */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display: none;}
    </style>
    """