import tkinter
from tkinter import messagebox
import customtkinter
from customtkinter import *
from pytube import Playlist, YouTube
from moviepy.editor import *
import glob

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x780")
app.title("ADE🍹")

# def slider_callback(value):
#     progressbar_1.set(value)

def lowVideo():
    par = list(entry_1.get().split())
    messagebox.showinfo("ADE", "Please wait")
    for i in par :
        yt = YouTube(i)
        print("제목 : ", yt.title)
        print("길이 : ", yt.length)
        print("게시자 : ", yt.author)
        print("게시날짜 : ", yt.publish_date)
        print("조회수 : ", yt.views)
        print("키워드 : ", yt.keywords)
        print("설명 : ", yt.description)
        print("썸네일 : ", yt.thumbnail_url)
        print('success')
        yt.streams.get_highest_resolution().download()
    messagebox.showinfo("ADE", "Download Success")
    
def highvideo() :
    #url = "https://www.youtube.com/watch?v=X8jjlicVUyY"
    #audio file
    audiofile = "C:\\Users\\sanghoon\\ade\\audio"
    videofile = "C:\\Users\\sanghoon\\ade\\video"

    def ydown():
        yt = YouTube(entry_2.get())

        vpath = (
            yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True)
            .order_by("resolution")
            .desc()
            .first()
            .download(videofile)
        )

        apath = (
            yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True)
            .order_by("abr")
            .desc()
            .first()
            .download(audiofile)
        )


        v = VideoFileClip(vpath)
        a = AudioFileClip(apath)

        v.audio = a
        v.write_videofile((yt.title + ".mp4"))
        [os.remove(f) for f in glob.glob('C:\\Users\\sanghoon\\udl\\audio\\*.mp4')]
        [os.remove(f) for f in glob.glob('C:\\Users\\sanghoon\\udl\\video\\*.mp4')]

    def playlistdown(url):
        pl = Playlist(url)

        for v in pl.video_urls:
            try:
                ydown(v)
            except:
                continue

    ydown()

tabview_1 = customtkinter.CTkTabview(master=app, width=400, height=780)
tabview_1.pack(pady=10, padx=10)
tabview_1.add("low quality video")
tabview_1.add("high quality video")

frame_1 = customtkinter.CTkFrame(tabview_1.tab("low quality video"))
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT , text="ADE🍹")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Input link" )
entry_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=lowVideo , text = "Download")
button_1.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "Fill the youtube link and click \nthe download button")

options_1 = customtkinter.CTkFrame(master=frame_1)
options_1.pack(pady=15, padx=30, fill="both")
optionlabel = customtkinter.CTkLabel(master= options_1 ,justify=tkinter.RIGHT ,text = "options")
optionlabel.pack(pady=10, padx=10)
convertmp3 = customtkinter.CTkCheckBox(master = options_1 , text= "convert mp3")
convertmp3.pack(pady=(20, 10), padx=20)

#second tap view
frame_2 = customtkinter.CTkFrame(tabview_1.tab("high quality video"))
frame_2.pack(pady=20, padx=60, fill="both", expand=True)

label_2 = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT , text="ADE🍹")
label_2.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_2, placeholder_text="Input link" )
entry_2.pack(pady=10, padx=10)

# title = customtkinter.CTkEntry(master=frame_2, placeholder_text="Input the title")

button_2 = customtkinter.CTkButton(master=frame_2, command=highvideo , text = "Download")
button_2.pack(pady=10, padx=10)

text_2 = customtkinter.CTkTextbox(master=frame_2, width=200, height=70)
text_2.pack(pady=10, padx=10)
text_2.insert("0.0", "Fill the youtube link and title. \n It takes a long time")

app.mainloop()
# progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
# progressbar_1.pack(pady=10, padx=10)
# slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
# slider_1.pack(pady=10, padx=10)
# slider_1.set(0.5)



# optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# optionmenu_1.pack(pady=10, padx=10)
# optionmenu_1.set("CTkOptionMenu")

# combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# combobox_1.pack(pady=10, padx=10)
# combobox_1.set("CTkComboBox")

# checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
# checkbox_1.pack(pady=10, padx=10)

# radiobutton_var = tkinter.IntVar(value=1)

# radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
# radiobutton_1.pack(pady=10, padx=10)

# radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
# radiobutton_2.pack(pady=10, padx=10)

# switch_1 = customtkinter.CTkSwitch(master=frame_1)
# switch_1.pack(pady=10, padx=10)
# segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
# segmented_button_1.pack(pady=10, padx=10)


