"""Research domain templates"""

RESEARCH_TEMPLATES = {
    "Proficient": """
Transform the following prompt into a structured research query:

## Research Framework Application

1. **Research Context & Scope**
   - Define the research domain and boundaries
   - Identify key variables and relationships
   - Establish the theoretical framework

2. **Methodology Requirements**
   - Specify data collection methods
   - Define analysis approach (qualitative/quantitative/mixed)
   - Outline validation criteria

3. **Literature Integration**
   - Reference relevant theories and models
   - Identify knowledge gaps
   - Position within existing research

4. **Output Specifications**
   - Format: [Academic paper/Report/Analysis]
   - Key sections to include
   - Evidence and citation requirements

5. **Quality Criteria**
   - Rigor and reproducibility standards
   - Bias mitigation strategies
   - Limitations acknowledgment

**Original Prompt:** {user_prompt}

**Enhanced Research Prompt:**
[Generate a comprehensive research-oriented version]
""",
    
    "Expert": """
You are a senior research scientist with expertise in systematic investigation and analysis.

## Advanced Research Framework
[Full template content here...]

**Original Prompt:** {user_prompt}

**Transform into Advanced Research Query:**
""",
    
    "Master": """
## Elite Research Synthesis Framework
[Full template content here...]

**Original Research Challenge:** {user_prompt}

**Generate Breakthrough Research Design:**
"""
}