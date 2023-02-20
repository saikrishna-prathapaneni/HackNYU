# Open AI key: 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
# print("Hello World")
"""
import openai
openai.api_key="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"

completion = openai.Completion.create(engine="davinci", prompt="Thank you for taking the time to talk to us about the Intern-Machine Learning We have made the decision to move forward with another candidate who best fits the needs of the Intern-Machine Learning at this time. If you have applied to another position at Symbotic the recruiting team will reach out to you on the status of your application. Please continue to check out our career page and follow as on LinkedIn as we continue to add new opportunities every day. This email box is not monitored. Please do not reply to this message.",max_tokens=100,temperature=0.5)
print(completion.choices[0]['text'])

# a7oFOY0DTi2c5glFzT3BlbkFJtW16IVSxRI9JQVJPFt59"
# print("Hello World")
import openai
openai.api_key="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"

#completion = openai.Completion.create(engine="davinci", prompt="Thank you for taking the time to talk to us about the Intern-Machine Learning We have made the decision to move forward with another candidate who best fits the needs of the Intern-Machine Learning at this time. If you have applied to another position at Symbotic the recruiting team will reach out to you on the status of your application. Please continue to check out our career page and follow as on LinkedIn as we continue to add new opportunities every day. This email box is not monitored. Please do not reply to this message.",max_tokens=100,temperature=0.5)
#print(completion.choices[0]['text'])


prompt = ( "For the following prompt \" Thank you for taking the time to talk to us about the Intern-Machine Learning "
           "We have made the decision to move forward with another candidate who best fits the needs of the "
           "Intern-Machine Learning at this time. If you have applied to another position at Symbotic the recruiting "
           "team will reach out to you on the status of your application. Please continue to check out our career page "
           "and follow as on LinkedIn as we continue to add new opportunities every day."
           "This email box is not monitored. Please do not reply to this message.\""
         )

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0.5,
  max_tokens=60,
  n=1,
  stop=None,
)

f"1st Prompt: Thank you for taking the time to talk to us about the Intern-Machine Learning. We have made the decision to move forward with another candidate who best fits the needs of the Intern-Machine Learning at this time. If you have applied to another position at Symbotic the recruiting team will reach out to you on the status of your application. Please continue to check out our career page and follow us on LinkedIn as we continue to add new opportunities every day.\n"

print(response.choices[0].text)

paragraph = "I am an AI language model and do not have the ability to confirm whether I am 18 or older. However, I can provide you with information and answer any questions you may have about the other topics listed in the email. Please let me know how I can assist you."
single_line = ' '.join(paragraph.split())
print(single_line)
"""

from get_mail import get_topN_mails
import re
import openai
import re

openai.api_key = "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"

# Define prompt
prompt_old = (f"Please extract the following information from the following 2 prompts:\n"
          f"1st Prompt: Thank you for taking the time to talk to us about the Intern-Machine Learning. "
          f"We have made the decision to move forward with another candidate who best fits the needs "
          f"of the Intern-Machine Learning at this time. If you have applied to another position at "
          f"Symbotic the recruiting team will reach out to you on the status of your application. "
          f"Please continue to check out our career page and follow us on LinkedIn as we continue to "
          f"add new opportunities every day.\n"
          f"2nd Prompt:  Hi Kaushik,Thanks for your interest in Google’s Software Engineering Internship opportunities in North America for Summer 2023. My name is Kathleen and I’m so excited to be working with you! Please read this entire email, share the requested info, and reach out to me if you have any questions.Before we continue, can you please confirm that you are currently 18 or older? If you're under 18, please let me know. There is a lot of information we’ll be discussing, so to make it simple, I’ve broken it down below: Scheduling Interviews - Please read carefully and provide all the information requested. Not doing so can delay your candidacy and interview process: You will be scheduled for two technical interviews via Google Meet. Please let me know if you prefer to have the interviews conducted over the phone.  Please send me your availability one week out from today. (Please be advised that Google will be closed on November 24-25 for Thanksgiving) Please note that we interview between the hours of 10AM - 4PM PT from Monday-Friday. For quickest scheduling, please share at least 5 different dates with at least 3 hour windows of availability. Please specify which coding language you’d like to be interviewed in: Java, Javascript, C++, C, Python.I’m also happy to speak with you over the phone/GVC - just let me know what are some good times for us to talk.\n"
          f"Extract the following information:\n"
          f"- Company Name:\n"
          f"- Job Position:\n"
          f"- Status:\n")

#p="Dear Kaushik Tummalapalli - Thank you for your interest in working at NVIDIA. We are reaching out to inform you that we are no longer recruiting for the Deep Learning Algorithm Engineering Intern role. We are always hiring and hope you’ll continue to explore opportunities with us as they become available. We appreciate your passion for NVIDIA and wish you the best in your job search. Best Regards, The NVIDIA Recruiting Team"

emails=["Thank you for applying at Cisco! We think it's a great place to work and we're excited that you're interested in joining us as a Product Management Intern (MBA) - Summer FY23 Internship (Meraki), Job ID 1388255 here, please upload your resume to your Cisco Careers profile if you haven't done so already, we'll use the information you provided and assess your background based on the role requirements, if there's a potential match for the position, we will contact you to discuss next steps, we may also use this information to consider you for future openings that match your skills and experience, in which case we would contact you directly, to update your profile, view application status, or search for other exciting opportunities, please visit our Cisco Careers, meanwhile, keep checking for other roles that might match your interests, and even set up job alerts to notify you of any new openings, thank you again for your interest in Cisco, best regards, Cisco Recruiting.","Hi Kaushik, thank you for applying for our Strategic Student Program: Software Developer Intern (Summer 2023) (348636) position, you're now one step closer to joining the world's smartest minds who make real what matters – from smart grids that power whole cities to manufacturing systems that use lightweight robotics, we'll review your application and contact you to let you know the next steps, you can also follow your progress within your Siemens account.",
"Hello Kaushik, thank you for wanting to join this adventure with us, we have received your application for our Software Engineering Intern - Software Systems (Summer 2023) role and will review it shortly, our recruiting team will contact you should the opportunity and your experience align, to learn more about Rivian, please visit our Careers site, our LinkedIn page, and our YouTube channel to see how we are bringing our work to life, thanks again for considering us, regards, the Rivian Talent Acquisition Team.","Dear Kaushik Tummalapalli, thank you for your application for the Artificial Intelligence / Machine Learning: Human Assisted AI & Data-Centric AI - Intern - 384 Santa Trinita Ave, Sunnyvale, CA 94085, USA position, your online application was successfully received, we will carefully compare your experience and qualifications to the specific position for which you applied, we will then get back to you accordingly, please click on the button below to register and access your application in future, you will then be able to check the current status of your application, if you have any questions please don't hesitate to contact us by replying to this email, yours sincerely, Bosch Group Talent Acquisition Team, Bosch privacy policy, SmartRecruiters terms of use and privacy policy, https://www.bosch.com/careers/."]

p1="Hi Sri, We would like to thank you for your interest in BETA Technologies. We appreciate you taking the time to participate in our video screening and for your continued interest in BETA. It has provided us with an opportunity to learn about your skills and accomplishments. After much consideration, we've determined we do not currently have an opening for an Internship that matches your interests and experience. That being said, we’d like to keep your resume on file for future internship opportunities or if our needs shift for this coming summer. We encourage you to stay connected as you expand your experience and knowledge throughout your studies and encourage you to reapply to future opportunities at BETA. We really appreciate you taking the time to get to know BETA. Best of luck, and please keep in touch! Sincerely"
#print(len(p1))
prompt_old = (f"Please extract the following information from the following prompt:\n"
          f"Prompt: {p1}\n"
          f"Extract the following information from the above prompt and return the following:, and for the Status choose the best appropriate between [Accepted, Rejected, Interview call, Online Assesment]\n"
          f"- Company Name:\n"
          f"- Job Position:\n"
          f"- Status:\n")

def is_job_application_status(prompt):
    job_keywords = ["rejected","job application", "job status", "job offer", "job interview","applied","apply"]
    internship_keywords = ["internship application", "internship status", "internship offer", "internship interview"]
    prompt_lower = prompt.lower()
    wrong_keywords = ["github","git","groww","digest", "article", "headline", "story", "report", "journalism", "news", "newspaper", "magazine", "press", "press release", "press conference"]
    for keyword in job_keywords:
        if keyword in wrong_keywords:
            return False
        if keyword in prompt_lower:
            return True
    for keyword in internship_keywords:
        if keyword in prompt_lower:
            return True
    return False
"""
all_emails=get_topN_mails()
email_top= all_emails
#print(email_top)
#print(max(all_emails, key=len))
#print(len(max(all_emails, key=len)))
#print(len(all_emails))
p1 = re.sub(r"[\r\n\t]+", " ", email_top)
prompt = (f"Please extract the following information from the following prompt:\n"
          f"Prompt: {p1}\n"
          f"Extract the following information from the above prompt and return the following:, and for the Status choose the best appropriate between [Accepted, Rejected, Interview call, Online Assesment]\n"
          f"- Company Name:\n"
          f"- Job Position:\n"
          f"- Status:\n")

if(is_job_application_status(prompt)):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,)
    output = response.choices[0].text.strip()
    print(output)
else:
    print("Not a job application status prompt")    
"""

def gpt_api():
    all_emails=get_topN_mails()
    email_top= all_emails
    p1 = re.sub(r"[\r\n\t]+", " ", email_top)
    prompt = (f"Please extract the following information from the following prompt:\n"
          f"Prompt: {p1}\n"
          f"Extract the following information from the above prompt and return the following:, and for the Status choose the best appropriate between [Accepted, Rejected, Interview call, Online Assesment]\n"
          f"- Company Name:\n"
          f"- Job Position:\n"
          f"- Status:\n")
    if(is_job_application_status(prompt)):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,)
        output = response.choices[0].text.strip()
        li=output.split("\n")
        return {"Company":li[0],"Job Position":li[1],"Status":li[2],"mail":email_top}
        #print(output)
    else:
        return "Not a job application status prompt"

# print(gpt_api())


