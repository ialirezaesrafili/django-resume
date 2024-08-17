from django.shortcuts import render

portfolio_content2 = {
    "portfolio": {
        "projects_overview": [
            {"title": "Project 1", "thumbnail_alt": "A preview image of Project 1",
             "description": "A brief description of Project 1 highlighting key features or outcomes."},
            {"title": "Project 2", "thumbnail_alt": "A preview image of Project 2",
             "description": "A brief description of Project 2 highlighting key features or outcomes."},
            # Add more projects as needed
        ],
        "case_studies": [
            {
                "title": "Case Study: Project 1",
                "challenges": "The main challenge was [describe challenge].",
                "process": "To address this, I [describe process].",
                "outcome": "The result was [describe outcome], leading to [specific benefit]."
            },
            # Add more case studies as needed
        ],
        "skills": ["Skill 1", "Skill 2", "Skill 3"],  # List your key skills here
        "categories": ["Design", "Development", "Photography"]  # Adjust categories as needed
    },
    "resume": {
        "experience": [
            {
                "job_title": "Job Title 1",
                "company": "Company Name",
                "duration": "Start Date - End Date",
                "responsibilities": [
                    "Responsibility 1",
                    "Responsibility 2",
                    # Add more responsibilities as needed
                ]
            },
            # Add more job experiences as needed
        ],
        "education": [
            {
                "degree": "Degree Name",
                "institution": "Institution Name",
                "year": "Year of Graduation"
            },
            # Add more educational qualifications as needed
        ],
        "achievements_awards": [
            {"title": "Award/Recognition", "description": "Brief description of the award."},
            # Add more awards as needed
        ],
        "downloadable_resume": "Link to downloadable resume file"
    },
    "services": {
        "offerings": [
            {"service_name": "Service 1", "description": "Brief description of Service 1."},
            {"service_name": "Service 2", "description": "Brief description of Service 2."},
            # Add more services as needed
        ],
        "packages_pricing": [
            {"package_name": "Basic Package", "price": "$X", "details": "What's included in the Basic Package."},
            {"package_name": "Premium Package", "price": "$Y", "details": "What's included in the Premium Package."},
            # Add more packages as needed
        ],
        "testimonials": [
            {"client_name": "Client 1", "feedback": "What the client said about your service."},
            {"client_name": "Client 2", "feedback": "What the client said about your service."},
            # Add more testimonials as needed
        ]
    },
    "blog": {
        "posts": [
            {"title": "Blog Post 1", "summary": "Brief summary of Blog Post 1.", "link": "Link to full blog post."},
            {"title": "Blog Post 2", "summary": "Brief summary of Blog Post 2.", "link": "Link to full blog post."},
            # Add more blog posts as needed
        ],
        "categories": ["Category 1", "Category 2", "Category 3"],  # Adjust categories as needed
        "comments_engagement": "Allow visitors to comment and engage with posts"
    },
    "contact": {
        "contact_form": {
            "name_label": "Your Name",
            "email_label": "Your Email",
            "message_label": "Your Message",
            "submit_button": "Send Message"
        },
        "social_media_links": {
            "LinkedIn": "Your LinkedIn URL",
            "Twitter": "Your Twitter URL",
            "Instagram": "Your Instagram URL",
            # Add more social links as needed
        },
        "direct_contact": {
            "email": "your.email@example.com",
            "phone": "+1234567890"
        },
        "location_map": "Embed link to Google Maps if relevant"
    },
    "testimonials": {
        "client_feedback": [
            {"client_name": "Client 1", "testimonial": "Their feedback about your work."},
            {"client_name": "Client 2", "testimonial": "Their feedback about your work."},
            # Add more testimonials as needed
        ],
        "video_testimonials": [
            {"client_name": "Client 1", "video_link": "Link to video testimonial."},
            # Add more video testimonials as needed
        ],
        "ratings": "Include average ratings if applicable (e.g., 4.8/5 based on X reviews)"
    },
    "press_media": {
        "featured_in": [
            {"publication_name": "Publication 1", "link": "Link to article or feature."},
            {"publication_name": "Publication 2", "link": "Link to article or feature."},
            # Add more features as needed
        ],
        "interviews": [
            {"interviewer_name": "Interviewer 1", "link": "Link to interview or article."},
            # Add more interviews as needed
        ],
        "press_kit": "Link to downloadable press kit"
    },
    "gallery": {
        "images_videos": [
            {"title": "Image/Video 1", "description": "Brief description of the image/video."},
            {"title": "Image/Video 2", "description": "Brief description of the image/video."},
            # Add more images or videos as needed
        ],
        "before_after": [
            {"before_title": "Before Image", "after_title": "After Image",
             "description": "Transformation description."},
            # Add more before/after examples if relevant
        ],
        "exhibitions_shows": [
            {"event_name": "Exhibition/Show 1", "details": "Details about the event."},
            # Add more exhibitions or shows if applicable
        ]
    },
    "shop": {
        "products": [
            {"product_name": "Product 1", "description": "Brief description of Product 1.", "price": "$X"},
            {"product_name": "Product 2", "description": "Brief description of Product 2.", "price": "$Y"},
            # Add more products as needed
        ],
        "shopping_cart": "Include shopping cart functionality if applicable",
        "licensing": "Details on how to license your work if relevant"
    },
    "faq": {
        "common_questions": [
            {"question": "Question 1", "answer": "Answer to Question 1."},
            {"question": "Question 2", "answer": "Answer to Question 2."},
            # Add more questions and answers as needed
        ],
        "support": "Information on how clients can get support or more information"
    },


}


def home(request):
    return render(request, 'index.html', {'context': portfolio_content2})
