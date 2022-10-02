from tkinter import *
import requests
import json
root = Tk()
root.geometry("500x500")
root.title("Project 184")
root.configure(bg = "teal")

newsupdate = Label(root, text = "BBC News Update", font = ("Bahnshrift Light", 20, "bold"))
newsupdate.place(relx = 0.5, rely = 0.1, anchor = CENTER)
news1 = Label(root, text = "Title : ", font = ("Helvetica", 12, "bold"), fg ="red", wraplength = 500, justify = "left")
news1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
new_desc1 = Label(root, text = "Description : ", fg = "black", wraplength = 500, justify = "left")
new_desc1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
news2 = Label(root, text = "Title : ", font = ("Helvetica", 12, "bold"), wraplength = 500, justify = "left", fg = "red")
news2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
new_desc2 = Label(root, text = "Description : ", fg = "black", wraplength = 500, justify = "left")
new_desc2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
news3 = Label(root, text = "Title : ", font= ("Helvetica", 12, "bold"), fg = "red", wraplength = 500, justify = "left")
news3.place(relx = 0.5, rely = 0.6, anchor = CENTER)
news_desc3 = Label(root, text = "Description : ", fg = "black", wraplength = 500, justify = "left")
news_desc3.place(relx = 0.5, rely = 0.7, anchor = CENTER)
news4 = Label(root, text = "Title : ", fg = "red", wraplength = 500, font = ("Helvetica", 12, "bold"), justify = "left")
news4.place(relx = 0.5, rely = 0.8, anchor = CENTER)
news_desc4 = Label(root, text = "Description : ", fg = "black", wraplength = 500, justify = "left")
news_desc4.place(relx = 0.5, rely = 0.9, anchor = CENTER)

api_request = request.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=THE-API-KEY-WHICH-YOU-HAVE-GENERATED")
titl1 = open_bbc_page["articles"][0]["title"]
desc1 = open_bbc_page["articles"][0]["description"]
titl2 = open_bbc_page["articles"][1]["title"]
desc2 = open_bbc_page["articles"][1]["description"]
titl3 = open_bbc_page["articles"][2]["title"]
desc3 = open_bbc_page["articles"][2]["description"]
titl4 = open_bbc_page["articles"][3]["title"]
desc4 = open_bbc_page["articles"][3]["description"]

news1['text'] = "Title : " + titl1
news2['text'] = "Title : " + titl2
news3['text'] = "Title : " + titl3
news4['text'] = "Title : " + titl4
news_desc1['text'] = "Description : " + desc1
news_desc2['text'] = "Description : " + desc2
news_desc3['text'] = "Description : " + desc3
news_desc4['text'] = "Description : " + desc4
root.mainloop()