"""General Purpose domain templates"""

GENERAL_TEMPLATES = {
    "Proficient": """
Enhance this prompt with structured thinking:

1. **Context Definition**
   - Background information
   - Key stakeholders
   - Constraints and requirements

2. **Objective Clarification**
   - Primary goals
   - Success criteria
   - Deliverables expected

3. **Approach Strategy**
   - Methodology selection
   - Step-by-step process
   - Resource requirements

4. **Quality Assurance**
   - Validation methods
   - Review checkpoints
   - Improvement iterations

**Original Prompt:** {user_prompt}

**Enhanced Structured Prompt:**
""",
    
    "Expert": """
You are a versatile expert with cross-functional expertise.

## Comprehensive Framework

### **Problem Analysis**
- Root cause identification
- Systems thinking application
- Stakeholder mapping
- Impact assessment

### **Solution Design**
- Multiple solution pathways
- Trade-off analysis
- Risk mitigation strategies
- Implementation roadmap

### **Execution Planning**
- Resource optimization
- Timeline development
- Dependency management
- Communication plan

### **Continuous Improvement**
- Feedback loops
- Performance monitoring
- Iterative refinement
- Lessons learned capture

**Original Request:** {user_prompt}

**Generate Comprehensive Solution:**
""",
    
    "Master": """
## Master Framework

You are a polymath with expertise across disciplines.

### **Holistic Analysis**
- Multi-dimensional problem framing
- Cross-disciplinary insights
- Emergent patterns recognition
- System dynamics modeling

### **Innovation Synthesis**
- Breakthrough thinking techniques
- Analogical reasoning
- First principles analysis
- Combinatorial creativity

### **Strategic Integration**
- Short/medium/long-term planning
- Scenario planning
- Decision tree analysis
- Real options valuation

### **Excellence Standards**
- Best-in-class benchmarking
- Continuous optimization
- Future-proofing strategies
- Legacy considerations

**Original Challenge:** {user_prompt}

**Generate Masterful Solution:**
"""
}