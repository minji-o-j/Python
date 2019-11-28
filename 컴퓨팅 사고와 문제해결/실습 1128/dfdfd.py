from PIL import Image, ImageTk, ImageFilter  
import tkinter as tk
from tkinter import filedialog as fd

im = None
tk_img = None

# 파일 메뉴에서 “열기”를 선택하였을 때 호출되는 함수
def open():
    global im, tk_img,xsize,ysize
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    xsize, ysize=im.size
    window.update()

# 파일 메뉴에서 “종료”를 선택하였을 때 호출되는 함수
def quit():
    window.quit()
    
# 45도 회전
def image_rotate():
    global im, tk_img
    out = im.rotate(45) 
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

# 블러
def image_blur():
    global im, tk_img
    out = im.filter(ImageFilter.BLUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

#흑백
def black():
    global im, tk_img
    out = im.convert("L")
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

#2배축소
def half_size():
    global im, tk_img
    out = im.resize((xsize//2, ysize//2))
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

#2배확대
def double_size():
    global im, tk_img
    out = im.resize((xsize*2, ysize*2))
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()
    
    
#원본
def start():
    global im, tk_img

    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def image_contour():
    global im, tk_img
    out = im.filter(ImageFilter.CONTOUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

# 윈도우를 생성한다. 
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# 메뉴를 생성한다. 
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="종료", command=quit)
ipmenu.add_command(label="영상회전", command=image_rotate)
ipmenu.add_command(label="영상흐리게", command=image_blur)
ipmenu.add_command(label="영상흑백", command=black)
ipmenu.add_command(label="영상복구", command=start)
ipmenu.add_command(label="영상윤곽선", command=image_contour)
ipmenu.add_command(label="영상2배", command=double_size)
ipmenu.add_command(label="영상2배축소", command=half_size)
menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="영상처리", menu=ipmenu)

window.config(menu=menubar)
window.mainloop()
