"""Data Science domain templates"""

DATA_SCIENCE_TEMPLATES = {
    "Proficient": """
Structure for data science analysis:

1. **Problem Formulation**
   - Business question translation
   - Hypothesis definition
   - Success metrics

2. **Data Requirements**
   - Data sources identification
   - Feature engineering needs
   - Data quality considerations

3. **Analytical Approach**
   - Statistical methods
   - ML algorithm selection
   - Validation strategy

4. **Insights Delivery**
   - Visualization requirements
   - Stakeholder communication
   - Actionable recommendations

**Original Query:** {user_prompt}

**Enhanced Data Science Prompt:**
""",
    
    "Expert": """
You are a senior data scientist with ML engineering expertise.

## Advanced Analytics Framework

### **Data Pipeline Architecture**
- ETL/ELT design
- Data lake/warehouse strategy
- Stream processing requirements
- Data governance framework

### **Feature Engineering**
- Domain-specific features
- Dimensionality reduction
- Feature selection methods
- Embedding strategies

### **Model Development**
- Ensemble methods
- Deep learning architectures
- AutoML integration
- Hyperparameter optimization

### **MLOps Implementation**
- Model versioning
- A/B testing framework
- Monitoring and drift detection
- Continuous training pipeline

**Original Problem:** {user_prompt}

**Generate Advanced Analytics Solution:**
""",
    
    "Master": """
## Elite Data Science Framework

You are a chief data scientist and AI researcher.

### **Advanced ML Architecture**
- Transformer models adaptation
- Graph neural networks
- Reinforcement learning integration
- Federated learning systems

### **Causal Inference**
- Causal DAGs construction
- Instrumental variables
- Difference-in-differences
- Synthetic control methods

### **Explainable AI**
- SHAP/LIME integration
- Counterfactual explanations
- Model interpretability layers
- Fairness metrics

### **Production Systems**
- Real-time inference optimization
- Edge deployment strategies
- Model compression techniques
- Distributed training architecture

**Original Challenge:** {user_prompt}

**Design Cutting-Edge ML Solution:**
"""
}