from PIL import Image, ImageTk, ImageFilter  
import tkinter as tk
from tkinter import filedialog as fd

im = None
tk_img = None

# 파일 메뉴에서 “열기”를 선택하였을 때 호출되는 함수
def open():
    global im, tk_img, xsize, ysize
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    xsize, ysize = im.size
    window.update()

# 파일 메뉴에서 “종료”를 선택하였을 때 호출되는 함수
def quit():
    window.quit()

def image_reset():
    global im, tk_img  
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

# 영사처리 메뉴에서 “열기”를 선택하였을 때 호출되는 함수
def image_rotate():
    global im, tk_img
    out = im.rotate(45) 
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

# 영사처리 메뉴에서 “열기”를 선택하였을 때 호출되는 함수
def image_blur():
    global im, tk_img
    out = im.filter(ImageFilter.BLUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

# 영사처리 메뉴에서 “열기”를 선택하였을 때 호출되는 함수
def image_contour():
    global im, tk_img
    out = im.filter(ImageFilter.CONTOUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def image_gray():
    global im, tk_img
    out= im.convert("L")
    tk_img = ImageTk.PhotoImage(out)  
    canvas.create_image(250, 250, image=tk_img)
    window.update()  

def image_2():
    global im, tk_img  
    out= im.resize((xsize*2, ysize*2))
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def image_select():
    global im, tk_img, b1, b2, b3
    
    b1= canvas.bind("<B1-Motion>", paint)
    b2= canvas.bind("<ButtonPress-1>", press)
    b3= canvas.bind("<ButtonRelease-1>", release)

def press(event):
    global px, py, item
    px= event.x
    py= event.y
    item= canvas.create_rectangle(px, py, px+1, py+1, fill="")

def release(event):
    global im, tk_img, item, px, py, x, y
    x= event.x
    y= event.y

    canvas.delete(item)
    print(px, py, event.x, event.y)

    canvas.unbind("<B1-Motion>", b1)
    canvas.unbind("<ButtonPress-1>", b2)
    canvas.unbind("<ButtonRelease-1>", b3)
 
    out= im.crop((px, py, x, y))
    out= out.resize((xsize, ysize))
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()
    
def paint(event):
    global px, py, item
    canvas.delete(item)
    item= canvas.create_rectangle(px, py, event.x, event.y, fill="")
        
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
ipmenu.add_command(label="영상복구", command=image_reset)
ipmenu.add_command(label="영상회전", command=image_rotate)
ipmenu.add_command(label="영상흐리게", command=image_blur)
ipmenu.add_command(label="영상윤곽선", command=image_contour)
ipmenu.add_command(label="영상흑백", command=image_gray)
ipmenu.add_command(label="영상*2", command=image_2)
ipmenu.add_command(label="영상선택", command=image_select)
menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="영상처리", menu=ipmenu)

window.config(menu=menubar)
window.mainloop()
