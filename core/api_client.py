"""API client for OpenRouter - Hidden from users"""

import requests
from typing import Optional, Dict, Any
from config.settings import Config

class APIClient:
    """API client for generating enhanced prompts via OpenRouter"""
    
    def __init__(self):
        """Initialize API client with hidden configuration"""
        self.api_key = Config.API_KEY
        self.base_url = Config.API_BASE_URL
        self.model = Config.DEFAULT_MODEL
        
        if not self.api_key:
            raise ValueError("OpenRouter API key is not configured")
        
    def generate(self, prompt: str) -> Dict[str, Any]:
        """
        Generate enhanced prompt using OpenRouter API
        All API details are hidden from the user
        """
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://your-app-url.com",  # Optional: Add your app URL
            "X-Title": "PromptLab Pro"  # Optional: Your app name
        }
        
        data = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert prompt engineer specializing in creating detailed, structured, and highly effective prompts for AI systems."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": Config.TEMPERATURE,
            "max_tokens": Config.MAX_TOKENS
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=data,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                return {
                    "success": True,
                    "content": content
                }
            elif response.status_code == 401:
                return {
                    "success": False,
                    "error": "Invalid API key. Please check your OpenRouter API key configuration."
                }
            elif response.status_code == 429:
                return {
                    "success": False,
                    "error": "Rate limit exceeded. Please wait a moment and try again."
                }
            elif response.status_code == 402:
                return {
                    "success": False,
                    "error": "Insufficient credits. Please check your OpenRouter account."
                }
            else:
                error_detail = response.json().get('error', {}).get('message', 'Unknown error')
                return {
                    "success": False,
                    "error": f"API Error: {error_detail}"
                }
                
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timed out. Please try again."
            }
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Connection error. Please check your internet connection."
            }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": f"Network error: {str(e)}"
            }
        except KeyError as e:
            return {
                "success": False,
                "error": "Unexpected response format from API."
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"An unexpected error occurred: {str(e)}"
            }