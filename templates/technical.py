"""Technical/Coding domain templates"""

TECHNICAL_TEMPLATES = {
    "Proficient": """
Structure this technical/coding request:

1. **Problem Definition**
   - Clear requirements specification
   - Input/output examples
   - Edge cases consideration

2. **Technical Approach**
   - Language/framework selection
   - Algorithm strategy
   - Design patterns application

3. **Implementation Details**
   - Code structure outline
   - Function signatures
   - Error handling approach

4. **Quality Standards**
   - Performance requirements
   - Security considerations
   - Testing strategy

**Original Request:** {user_prompt}

**Enhanced Technical Prompt:**
""",
    
    "Expert": """
You are a senior software architect with full-stack expertise.

## Advanced Technical Framework

### **System Architecture**
- Design patterns and principles
- Scalability considerations
- Microservices vs monolithic
- Database design (normalized/denormalized)

### **Code Quality Metrics**
- SOLID principles application
- DRY and KISS adherence
- Cyclomatic complexity targets
- Test coverage requirements

### **Performance Optimization**
- Time complexity analysis
- Space complexity optimization
- Caching strategies
- Async/concurrent programming

### **Security Implementation**
- OWASP top 10 mitigation
- Authentication/authorization
- Data encryption standards
- Input validation and sanitization

### **DevOps Integration**
- CI/CD pipeline setup
- Container orchestration
- Monitoring and logging
- Infrastructure as code

**Original Challenge:** {user_prompt}

**Generate Production-Ready Solution:**
""",
    
    "Master": """
## Elite Engineering Framework

You are a principal engineer architecting enterprise-scale solutions.

### **Distributed Systems Design**
- CAP theorem considerations
- Consensus algorithms (Raft/Paxos)
- Event sourcing and CQRS
- Service mesh architecture

### **Advanced Algorithms**
- Machine learning integration
- Graph algorithms optimization
- Dynamic programming solutions
- Probabilistic data structures

### **System Reliability**
- Chaos engineering principles
- Circuit breaker patterns
- Bulkhead isolation
- Retry strategies with backoff

### **Performance Engineering**
- Lock-free data structures
- SIMD optimizations
- GPU acceleration
- Memory pooling and custom allocators

### **Cloud-Native Architecture**
- Kubernetes operators
- Serverless patterns
- Multi-region deployment
- Edge computing integration

**Original Problem:** {user_prompt}

**Design World-Class Solution:**
"""
}