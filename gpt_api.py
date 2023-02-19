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

p="Dear Kaushik Tummalapalli - Thank you for your interest in working at NVIDIA. We are reaching out to inform you that we are no longer recruiting for the Deep Learning Algorithm Engineering Intern role. We are always hiring and hope you’ll continue to explore opportunities with us as they become available. We appreciate your passion for NVIDIA and wish you the best in your job search. Best Regards, The NVIDIA Recruiting Team"


p1="Hi Sri, We would like to thank you for your interest in BETA Technologies. We appreciate you taking the time to participate in our video screening and for your continued interest in BETA. It has provided us with an opportunity to learn about your skills and accomplishments. After much consideration, we've determined we do not currently have an opening for an Internship that matches your interests and experience. That being said, we’d like to keep your resume on file for future internship opportunities or if our needs shift for this coming summer. We encourage you to stay connected as you expand your experience and knowledge throughout your studies and encourage you to reapply to future opportunities at BETA. We really appreciate you taking the time to get to know BETA. Best of luck, and please keep in touch! Sincerely"
#print(len(p1))
prompt = (f"Please extract the following information from the following prompt:\n"
          f"Prompt: {p1}\n"
          f"Extract the following information from the above prompt and return the following:, and for the Status choose the best appropriate between [Accepted, Rejected, Interview call, Online Assesment]\n"
          f"- Company Name:\n"
          f"- Job Position:\n"
          f"- Status:\n")
        
all_emails=get_topN_mails()
#print(max(all_emails, key=len))
#print(len(max(all_emails, key=len)))
#print(len(all_emails))

def is_job_application_status(prompt):
    job_keywords = ["rejected","job application", "job status", "job offer", "job interview","job","status","application","applied","applied for","applied to","applied for the","applied to the","applied for the position","applied to the position","applied for the role","applied to the role","applied for the job","applied to the job","applied for the internship","applied to the internship","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role","applied to the internship role","applied for the internship job","applied to the internship job","applied for the internship position","applied to the internship position","applied for the internship role"]
    internship_keywords = ["internship application", "internship status", "internship offer", "internship interview"]
    prompt_lower = prompt.lower()
    for keyword in job_keywords:
        if keyword in prompt_lower:
            return True
    for keyword in internship_keywords:
        if keyword in prompt_lower:
            return True
    return False

for prompt in all_emails:
    p1 = re.sub(r"[\r\n\t]+", " ", prompt)
    prompt = (f"Please extract the following information from the following prompt:\n"
          f"Prompt: {p1}\n"
          f"Extract the following information from the above prompt and return the following:, and for the Status choose the best appropriate between [Accepted, Rejected, Interview call, Online Assesment]\n"
          f"- Company Name:\n"
          f"- Job Position:\n"
          f"- Status:\n")

    #print(prompt)

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


# Extract the Company Name, Job Position, and Status from the response
#output = response.choices[0].text.strip()
#print(output)
"""
p1="Hi Sri, We would like to thank you for your interest in BETA Technologies. We appreciate you taking the time to participate in our video screening and for your continued interest in BETA. It has provided us with an opportunity to learn about your skills and accomplishments. After much consideration, we've determined we do not currently have an opening for an Internship that matches your interests and experience. That being said, we’d like to keep your resume on file for future internship opportunities or if our needs shift for this coming summer. We encourage you to stay connected as you expand your experience and knowledge throughout your studies and encourage you to reapply to future opportunities at BETA. We really appreciate you taking the time to get to know BETA. Best of luck, and please keep in touch! Sincerely"
#print(len(p1))
prompt = (f"Please extract the following information from the following prompt:\n"
          f"Prompt: {p1}\n"
          f"Extract the following information from the above prompt and return the following:, and for the Status choose the best appropriate between [Accepted, Rejected, Interview call, Online Assesment]\n"
          f"- Company Name:\n"
          f"- Job Position:\n"
          f"- Status:\n")


# Call OpenAI's GPT-3 API to generate the desired output
if(is_job_application_status(prompt)):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,)
    output = response.choices[0].text.strip()
    #print(output)
else:
    print("Not a job application status prompt")


# Regular Expressions to extract the Company Name, Job Position, and Status from the above prompt:
company_name = re.search(r"Company Name:(.*)Job Position:", output).group(1).strip()
job_position = re.search(r"Job Position:(.*)Status:", output).group(1).strip()
status = re.search(r"Status:(.*)", output).group(1).strip()

# Print the Company Name, Job Position, and Status
print(f"Company Name: {company_name}")
print(f"Job Position: {job_position}")
print(f"Status: {status}")
"""

"Thank You for your interest in BETA Technologies\r\nTo: <sp6904@nyu.edu>\r\n\r\n\r\nHi Sri,\r\n\r\nWe would like to thank you for your interest in BETA Technologies. We\r\nappreciate you taking the time to participate in our video screening and\r\nfor your continued interest in BETA. It has provided us with an opportunity\r\nto learn about your skills and accomplishments.\r\n\r\nAfter much consideration, we've determined we do not currently have an\r\nopening for an Internship that matches your interests and experience. That\r\nbeing said, we’d like to keep your resume on file for future internship\r\nopportunities or if our needs shift for this coming summer. We encourage\r\nyou to stay connected as you expand your experience and knowledge\r\nthroughout your studies and encourage you to reapply to future\r\nopportunities at BETA.\r\n\r\nWe really appreciate you taking the time to get to know BETA. Best of luck"
