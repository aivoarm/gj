from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from bs4 import BeautifulSoup
import openai
 
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
import os



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'mysite/index.html', {'error_message': error_message})
    else:
        return render(request, 'mysite/login.html')

openai.api_key = os.getenv("OPENAI_API")

@login_required(login_url='login')

# Set up your OpenAI API credentials

def index(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        # Call OpenAI API to generate a response
        response = openai.Completion.create(
            engine='davinci',
            prompt=message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )

        generated_message = response.choices[0].text.strip()

        return render(request, 'mysite/index.html', {'generated_message': generated_message})
    else:
        return render(request, 'mysite/index.html', {'hide_content': True})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def aboutOLD():
   
 # Replace with code to extract information from LinkedIn profile
    name = "Arman Ayva"
    title = "Software Engineer"
    summary = "I am a software engineer with over 10 years of experience in developing web applications."
    experience = [
        {
            "company": "ABC Inc.",
            "position": "Senior Software Engineer",
            "start_date": "January 2018",
            "end_date": "Present",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
        {
            "company": "XYZ Corp.",
            "position": "Software Engineer",
            "start_date": "June 2014",
            "end_date": "December 2017",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
    ]

    context = {
        "name": name,
        "title": title,
        "summary": summary,
        "experience": experience
    }

    return render(request, "mysite/about.html", context)

#@login_required(login_url='login')
def download_linkedin_pdf(profile_url, save_path):
    response = requests.get(profile_url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            
        print('PDF downloaded successfully.')
    else:
        print('Failed to download PDF.')

from django.shortcuts import render

def about(request):
    pdf_path = "Profile.pdf"

    context = {
        "pdf_path": pdf_path
        
    }

    return render(request, "mysite/about.html", context)