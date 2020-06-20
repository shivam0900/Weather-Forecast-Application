from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
import requests


def printing_response(weather):

    try:   
        name=weather['name']
        descrip=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str= 'City: %s \nConditions: %s \nTemperature(*F): %s' %(name,descrip,temp)
    except :
        final_str='There is aproblem retrieving that infromation'

    return final_str

def get_weather(city):
    weather_key='86a261758b72c7ad83b83849e55718bb'
    url='https://api.openweathermap.org/data/2.5/weather?'
    parameters={'APPID': weather_key,'q':city,'units':'Imperial'}
    response=requests.get(url,params=parameters)
    weather=response.json()
    weather_label['text']=printing_response(weather)


root=Tk()
root.title('Weather Report')
root.iconbitmap('Papirus-Team-Papirus-Apps-Weather.ico')

canvas=Canvas(root,height=480,width=640).pack()

background_img=ImageTk.PhotoImage(Image.open('photo-1506744038136-46273834b3fb.jpg'))
background_img_label=Label(root,image=background_img)
background_img_label.place(relwidth=1,relheight=1)



upper_frame=Frame(root,bg='#80c1ff',bd=5)
upper_frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=Entry(upper_frame,font=('Courier',14))
entry.place(relx=0.005,rely=0.01,relwidth=0.65,relheight=0.98)

button=Button(upper_frame,bg='gray',text='Search',font=('Helvika',14),command=lambda:get_weather(entry.get()))
button.place(relx=0.67,rely=0.01,relwidth=0.34,relheight=0.98)


lower_frame=Frame(root,bg='#80c1ff',bd=5)
lower_frame.place(relx=0.5,rely=0.3,relwidth=0.75,relheight=0.6,anchor='n')

weather_label=Label(lower_frame,font=('Helvika',18))
weather_label.place(relheight=1,relwidth=1)

mainloop()