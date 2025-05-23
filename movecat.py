from tkinter import Tk, Entry, Button, Label, Text, StringVar, PhotoImage, ttk # 标注python环境，Tkinter 已默认包含，无需额外安装；
from PIL import Image, ImageTk
from pynput import mouse
import time
import threading

# 初始化全局变量
going = False


def thread_it(func, *args):
    myThread = threading.Thread(target=func, args=args)
    myThread.setDaemon(True)
    myThread.start()

"""
def move():
    control = mouse.Controller()
    global going
    going = True
    while going == True:
        control.move(-20, 0)
        time.sleep(2)
        control.move(20, 0)
        time.sleep(58) 
"""
def move():
    control = mouse.Controller()
    global going
    going = True
    try:
        while going:
            # print("Moving mouse left...")
            control.move(-20, 0)  # 向左移动 20 像素
            time.sleep(2)         # 等待 2 秒

            # print("Moving mouse right...")
            control.move(20, 0)   # 向右移动 20 像素
            time.sleep(58)        # 等待 58 秒
    except Exception as e:
        print(f"Error in move function: {e}")

def end():
    global going
    going = False


def GUI():
    fm_main = Tk()
    fm_main.resizable(False, False)
    fm_main.geometry("250x300+500+200")
    fm_main.title("move cat")
    fm_main.iconbitmap(r'e:\xuexi\vscode\move_cat\image\程序图标.ico') # 使用绝对路径，相对路径可能会报错
    
    btn1 = Button(fm_main, text='开始运行', command=lambda: thread_it(move), font=("华文行楷", 12))
    btn2 = Button(fm_main, text='结束运行', command=lambda: end(), font=("华文行楷", 12))
    btn1.grid(row=1, column=0, columnspan=1, sticky="w", padx=40, pady=9)
    btn2.grid(row=1, column=0, columnspan=1, sticky="e", padx=40, pady=9)
    
    # 插入图片
    global photo # 定义全局变量photo
    image = Image.open(r'e:\xuexi\vscode\move_cat\image\猫咪.png')
    image = image.resize((240, 200), Image.Resampling.LANCZOS) # 从 PIL 8.3.0 开始，Image.ANTIALIAS 已被弃用，建议改为 Image.Resampling.LANCZOS
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.grid(row=2, column=0, padx=2, pady=0)
    
    # 插入进度条
    # label = Label(fm_main,text = "进度条：",font=("华文行楷",12))
    # label.grid(row=3,column=0,sticky="w")
    #
    # pbar = ttk.Progressbar(fm_main)
    # pbar.grid(row=3,column=0,sticky="e",padx=80)
    # pbar['maximum'] = 60
    # pbar['value'] = 0

    fm_main.mainloop()


# def jindutiao():
#     for i in range(60):
#         time.sleep(1)
#         pbar['value'] += 1
#         fm_main.update()


GUI()
# pyinstaller -F movecat.py --noconsole --icon="./image/程序图标.ico"
