import io
import webbrowser
import requests
from tkinter import *

from urllib.request import urlopen
from PIL import ImageTk, Image


class NewsApp:

    def __init__(self):
        # fetch data
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=us&apiKey=07ce6431517e45c5b04b589c36e5bed6').json()
        # initial GUI load
        self.load_gui()
        # load the 1st news item
        self.load_news_item(1)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.title('News App')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        # clear the screen for the new news item


        self.clear()
        label1 = Label(self.root, text='headlines',font=('verdana', 16, 'bold'), bg='black', fg='white')
        label1.pack(pady=10)
        img_url = self.data['articles'][index]['urlToImage']
        binary_data = urlopen(img_url).read()
        rs = Image.open(io.BytesIO(binary_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(rs)
        label = Label(self.root, image=photo)
        label.pack()

        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)
        prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_item(index - 1), fg='white',
                      bg='blue', )
        prev.pack(side=LEFT)

        read = Button(frame, text='Read more', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['description']), fg='white',
                      bg='blue', )

        read.pack(side=LEFT)

        next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_item(index + 1),
                      fg='white', bg='blue')
        next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


obj = NewsApp()
