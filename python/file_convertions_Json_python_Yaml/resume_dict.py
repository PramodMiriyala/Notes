"""python to json conversion"""
import json
import yaml

resume = {
    "personal_info": {
        "name": "John Doe",
        "address": "123 Main St, Anytown, USA",
        "phone": "(123) 456-7890",
        "email": "john.doe@example.com",
        "linkedin": "linkedin.com/in/johndoe"
    },
    "summary": "Results-driven software engineer with 5+ years of experience in developing scalable web applications and a passion for problem-solving.",
    "skills": [
        "Python",
        "JavaScript",
        "Django",
        "Flask",
        "React",
        "SQL",
        "Git",
        "RESTful APIs"
    ],
    "education": {
        "degree": "Bachelor of Science in Computer Science",
        "institution": "University of Anytown",
        "graduation_year": 2018
    },
    "certifications":
        {
            "certification_name": ["Certified Python Developer", "yaml", "json"],
            "issuing_organization": "Python Institute",
            "issue_date": "March 2020"
        }
}

# Python Dict --> Json
# with open("resume.json", "w", encoding="utf8") as file:
#     json.dump(resume, file, indent = 4)

# Python Dict --> Yaml
# with open("resume.yaml", 'w', encoding="utf8") as file:
#     yaml.dump(resume, file, indent= 4, default_flow_style=False)

# Json --> Python Dict 
# with open("user.json", "r", encoding="utf8") as json_file:
#     data = json.load(json_file)
#     print(data)

# yaml --> Python Dict
with open("details.yaml", "r", encoding="utf8") as yaml_file:
    details = yaml.load(yaml_file, Loader=yaml.FullLoader)
print(details)

