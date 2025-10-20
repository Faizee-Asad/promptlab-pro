"""Template modules initialization"""

from .research import RESEARCH_TEMPLATES
from .creative import CREATIVE_TEMPLATES
from .technical import TECHNICAL_TEMPLATES
from .business import BUSINESS_TEMPLATES
from .education import EDUCATION_TEMPLATES
from .data_science import DATA_SCIENCE_TEMPLATES
from .general import GENERAL_TEMPLATES

# Aggregate all templates
ALL_TEMPLATES = {
    "Research & Analysis": RESEARCH_TEMPLATES,
    "Creative Writing": CREATIVE_TEMPLATES,
    "Technical/Coding": TECHNICAL_TEMPLATES,
    "Business Strategy": BUSINESS_TEMPLATES,
    "Education & Teaching": EDUCATION_TEMPLATES,
    "Data Science": DATA_SCIENCE_TEMPLATES,
    "General Purpose": GENERAL_TEMPLATES
}