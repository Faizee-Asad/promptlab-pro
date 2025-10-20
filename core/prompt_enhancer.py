"""Core logic for prompt enhancement using OpenRouter"""

from typing import Dict, Any
import traceback
from core.api_client import APIClient  # Changed this line

class PromptEnhancer:
    def __init__(self):
        """Initialize the prompt enhancer with OpenRouter client"""
        from config.settings import Config
        
        # Validate API configuration
        if not Config.API_KEY:
            raise ValueError("OpenRouter API key is not configured")
        
        # Initialize OpenRouter API client
        try:
            self.api_client = APIClient()
            print(f"✅ Initialized with model: {Config.DEFAULT_MODEL}")
        except Exception as e:
            print(f"❌ Error initializing API client: {str(e)}")
            raise
    
    def enhance_prompt(self, user_prompt: str, domain: str, complexity: str) -> Dict[str, Any]:
        """
        Enhance the user's prompt with better error handling
        """
        try:
            # Create the enhancement prompt
            enhancement_prompt = self._create_enhancement_prompt(user_prompt, domain, complexity)
            
            # Make API call using the API client
            result = self.api_client.generate(enhancement_prompt)
            
            if result["success"]:
                print(f"✅ Successfully enhanced prompt ({len(result['content'])} characters)")
            else:
                print(f"❌ Enhancement failed: {result.get('error', 'Unknown error')}")
            
            return result
                
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Enhancement error: {error_msg}")
            print(f"Traceback: {traceback.format_exc()}")
            
            # Provide more specific error messages
            if "api_key" in error_msg.lower() or "api key" in error_msg.lower():
                return {
                    "success": False,
                    "error": "API key is invalid or not configured properly. Please check your .env file."
                }
            elif "rate" in error_msg.lower() or "limit" in error_msg.lower():
                return {
                    "success": False,
                    "error": "Rate limit exceeded. Please wait a moment and try again."
                }
            elif "connection" in error_msg.lower() or "network" in error_msg.lower():
                return {
                    "success": False,
                    "error": "Connection error. Please check your internet connection and try again."
                }
            elif "timeout" in error_msg.lower():
                return {
                    "success": False,
                    "error": "Request timed out. The model might be busy. Please try again."
                }
            else:
                return {
                    "success": False,
                    "error": f"Error: {error_msg[:200]}"
                }
    
    def _create_enhancement_prompt(self, user_prompt: str, domain: str, complexity: str) -> str:
        """Create the prompt for enhancement based on parameters"""
        
        complexity_descriptions = {
            "Proficient": "comprehensive and well-structured with clear objectives and detailed guidance",
            "Expert": "highly detailed with advanced techniques, deep context, and sophisticated approaches",
            "Master": "exceptionally sophisticated with cutting-edge methodologies, nuanced understanding, and expert-level depth"
        }
        
        domain_contexts = {
            "Research & Analysis": "academic research, systematic investigation, data analysis, critical thinking, and evidence-based conclusions",
            "Creative Writing": "storytelling, narrative development, character creation, world-building, and creative expression",
            "Technical/Coding": "software development, programming best practices, system architecture, debugging, and technical implementation",
            "Business Strategy": "strategic planning, market analysis, competitive advantage, business development, and decision-making frameworks",
            "Education & Teaching": "pedagogical approaches, curriculum design, learning facilitation, assessment strategies, and educational effectiveness",
            "Data Science": "statistical analysis, machine learning, data visualization, predictive modeling, and data-driven insights",
            "General Purpose": "versatile application across multiple domains with balanced and adaptable approaches"
        }
        
        enhancement_instructions = f"""You are an expert prompt engineer specializing in {domain}.

**Your Task:** Transform the user's prompt into a highly effective, structured, and optimized prompt for AI systems.

**Complexity Level:** {complexity}
Create a {complexity_descriptions.get(complexity, 'comprehensive')} prompt.

**Domain Context:** {domain}
Focus on: {domain_contexts.get(domain, 'general use')}

**Enhancement Guidelines:**

1. **Clarify Objectives:** Define clear, specific goals and expected outcomes tailored to {domain}
2. **Add Context:** Include relevant background, constraints, and domain-specific requirements
3. **Structure Format:** Specify desired output format, style, and organizational structure
4. **Include Best Practices:** Integrate {domain} industry standards and methodologies
5. **Ensure Actionability:** Make it immediately usable with clear instructions
6. **Add Technical Details:** Include appropriate {complexity}-level technical depth and methodologies
7. **Define Success Criteria:** Specify how to measure or evaluate the output quality

**Important:** Output ONLY the enhanced prompt. Do not include:
- Explanations about what you changed
- Meta-commentary about the enhancement
- Introductory phrases like "Here's the enhanced prompt:"
- Any text outside the actual enhanced prompt itself

The enhanced prompt should be ready to copy and use immediately.

---

**Original User Prompt:**
"{user_prompt}"

**Enhanced Prompt:**"""

        return enhancement_instructions