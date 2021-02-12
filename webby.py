#importing libraries

from tkinter import *
import requests
from bs4 import BeautifulSoup
import webbrowser



root = Tk()
root.title('WebbyJob')


# size configurations

root.geometry('1280x650+1+0')
root.minsize(200, 100)
root.maxsize(1500, 700)

#functions
def callback(link):
    webbrowser.open_new(link)
def search():
    
    domain = domain_value.get()
    location = location_value.get()
    #print(domain)
    #print(location)
    if domain == 'None' or location == 'None':
        Label(root, text="Please select one field from both domains and locations!!", font='times 20 bold', fg='red').place(x=280, y=450)
    else:
        root1 = Tk()
        URL = 'https://www.monster.com/jobs/search/?q='+domain+'&where='+location
        #print(URL)
        #Label(root, text=URL, font='times 20 bold', fg='red').place(x=10, y=500)
        scrollbar = Scrollbar(root1)
        scrollbar.pack(side=RIGHT, fill=Y)
        box = Listbox(root1, height=300, width=1250, bg='white', yscrollcommand=scrollbar.set)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='ResultsContainer')
        job_elems = results.find_all('section', class_='card-content')
        for job_elem in job_elems:
            title_elem = job_elem.find('h2', class_='title')
            company_elem = job_elem.find('div', class_='company')
            location_elem = job_elem.find('div', class_='location')
            if None in (title_elem, company_elem, location_elem):
                continue
        first_domain = domain.split('-')
        #print(first_domain)
        python_jobs = results.find_all('h2', string=lambda text: first_domain[0].lower() in text.lower())
        for p_job in python_jobs:
            link = p_job.find('a')['href']
            #print(p_job.text.strip())
            box.insert(END, p_job.text.strip())
            #print(f"Apply here: {link}\n")
            box.insert(END, "Click on the link to apply-  {}\n\n\n\n".format(link))
            box.bind("<Button-1>", lambda e: callback(link))
            box.insert(END, "        ".format(link))
            
        box.pack(side=BOTTOM)
        scrollbar.config(command=box.yview)
        root1.mainloop()

            
#****************************widgets******************************

#heading
Label(root, text = 'WebbyJob', bg='black', fg='white', font='Elephant 30 bold', borderwidth=3, padx=5, pady=5, relief=SUNKEN).pack(fill=BOTH)
#caption
Label(root, text="You choose, we provide!!", bg='silver',fg='black', font='Elephant 15 bold').pack(fill=BOTH)
#About
Label(root, text="This application will provide you all the jobs that you are searching for. I hope this will help you and you get placements in\
 your ream job. Thank you and Best of luck!!" , font='times 10 bold').pack(pady=5)


#************************Options************************************



#Domains

choose_label = Label(root, text="Chosse your preferences here:", font = 'times 15')

domain_label = Label(root, text="Domains:", fg='black', font='times 17 bold').place(x=400,y=220)


domain_value = StringVar()
domain_value.set("None") # if initial value is not set then all the radio buttons will be selected by default

software_cb = Radiobutton(root, text="Software-Developer", variable=domain_value, value="Software-Developer")
python_cb = Radiobutton(root, text="Python-Developer", variable=domain_value, value="Python-Developer")
web_cb = Radiobutton(root, text="Web-Developer", variable = domain_value, value="Web-Developer")
android_cb = Radiobutton(root, text="Android-Developer", variable=domain_value, value="Android-Developer")

search_button = Button(root, text = 'Search', borderwidth=2, relief=SUNKEN, height=1, width=5, command=search)

#Locations
location_label = Label(root, text="Locations:", fg='black', font='times 17 bold').place(x=750,y=220)
location_value = StringVar()
location_value.set("None")  # if initial value is not set then all the radio buttons will be selected by default
sunny_cb = Radiobutton(root, text="Sunnyvale__2C-CA", variable=location_value, value="Sunnyvale__2C-CA")
michi_cb = Radiobutton(root, text="Michigan", variable=location_value, value="Michigan")
cali_cb = Radiobutton(root, text="Southern-California", variable=location_value, value="Southern-California")
silicon_cb = Radiobutton(root, text="Silicon-Valley", variable=location_value, value="Silicon-Valley")




#********************packing of the widgets**********************

choose_label.pack(pady=50)
software_cb.place(x=400, y=260)
sunny_cb.place(x=750, y=260)
python_cb.place(x=400, y=280)
cali_cb.place(x=750, y=280)
web_cb.place(x=400, y=300)
michi_cb.place(x=750, y=300)
android_cb.place(x=400, y=320)
silicon_cb.place(x=750, y=320)

search_button.place(x=405, y=350)




root.mainloop()
