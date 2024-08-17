from django.shortcuts import render

developer_experiences = {
    "experience_1": {
        "title": "Full-Stack Web Development",
        "description": "Experience in building complete web applications, including frontend, backend, and database management using technologies like React, Node.js, and MongoDB."
    },
    "experience_2": {
        "title": "Mobile App Development",
        "description": "Proficient in developing cross-platform mobile applications using frameworks such as Flutter or React Native, with a focus on user-friendly interfaces and performance optimization."
    },
    "experience_3": {
        "title": "Cloud Computing",
        "description": "Expertise in deploying and managing scalable applications on cloud platforms like AWS, Azure, or Google Cloud, including experience with serverless architecture and cloud storage."
    },
    "experience_4": {
        "title": "DevOps & CI/CD",
        "description": "Skilled in implementing continuous integration and continuous deployment pipelines using tools like Jenkins, GitLab CI, or GitHub Actions, with a strong focus on automation and monitoring."
    },
    "experience_5": {
        "title": "Data Science & Machine Learning",
        "description": "Hands-on experience in data analysis, machine learning model development, and deployment using Python libraries like Pandas, Scikit-learn, and TensorFlow."
    }
}


def home(request):
    context = {'developer_experiences': developer_experiences}
    return render(request, 'index.html', context)
