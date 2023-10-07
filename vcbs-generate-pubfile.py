# python 3.10.6
# -*- coding: UTF-8 -*-

import tkinter as tk
from functools import partial
# from tkinter import font

from util.func import *

def main():
    if not os.path.exists("./content"):
        os.makedirs("./content")

    # 创建主窗口
    root = tk.Tk()
    root.title("VCB-S 发布文档生成程序")
    root.geometry(WINDOW)

    # # 创建一个自定义字体
    # custom_font = font.Font(family="Arial", size=12)
    # # 将自定义字体设置为窗口的默认字体
    # root.option_add("*Font", custom_font)

    for i in range(MAXROW):
        root.grid_rowconfigure(i, pad=15)
    # root.grid_columnconfigure(1, pad=100)

    # 创建标签和输入栏
    l_img_800 = tk.Label(root, text="发布图-竖")
    l_img_800.grid(row=0, column=0, sticky='ne')
    e_img_800 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_img_800.insert(0, "https://img.2222.moe/images/2023/09/04/oregairu_800.webp")
    e_img_800.grid(row=0, column=1, columnspan=4, sticky='nw')

    l_img_1400 = tk.Label(root, text="发布图-横")
    l_img_1400.grid(row=1, column=0, sticky='ne')
    e_img_1400 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_img_1400.insert(0, "https://img.2222.moe/images/2023/09/04/oregairu_1400.webp")
    e_img_1400.grid(row=1, column=1, columnspan=4, sticky='nw')

    l_sub = tk.Label(root, text="字幕组")
    l_sub.grid(row=2, column=0, sticky='ne')
    e_sub = tk.Entry(root, bd=2, width=EWIDTH4)
    e_sub.insert(0, "动漫国字幕组")
    e_sub.grid(row=2, column=1, columnspan=4, sticky='nw')

    l_title_chn = tk.Label(root, text="标题-中文")
    l_title_chn.grid(row=3, column=0, sticky='ne')
    e_title_chn = tk.Entry(root, bd=2, width=EWIDTH4)
    e_title_chn.insert(0, "测试：我的青春恋爱物语果然有问题")
    e_title_chn.grid(row=3, column=1, columnspan=4, sticky='nw')

    l_title_eng = tk.Label(root, text="标题-英文")
    l_title_eng.grid(row=4, column=0, sticky='ne')
    e_title_eng = tk.Entry(root, bd=2, width=EWIDTH4)
    e_title_eng.insert(0, "Yahari Ore no Seishun Lovecome wa Machigatte Iru.")
    e_title_eng.grid(row=4, column=1, columnspan=4, sticky='nw')

    l_title_jpn = tk.Label(root, text="标题-日文")
    l_title_jpn.grid(row=5, column=0, sticky='ne')
    e_title_jpn = tk.Entry(root, bd=2, width=EWIDTH4)
    e_title_jpn.insert(0, "やはり俺の青春ラブコメはまちがっている.")
    e_title_jpn.grid(row=5, column=1, columnspan=4, sticky='nw')

    l_spec = tk.Label(root, text="规格")
    l_spec.grid(row=6, column=0, sticky='ne')
    e_spec = tk.Entry(root, bd=2, width=EWIDTH)
    e_spec.insert(0, "10-bit 1080p HEVC")
    e_spec.grid(row=6, column=1, sticky='nw')
    e_type = tk.Entry(root, bd=2, width=EWIDTH)
    e_type.insert(0, "BDRip")
    e_type.grid(row=6, column=2, sticky='nw')
    e_range = tk.Entry(root, bd=2, width=EWIDTH)
    e_range.insert(0, "S1-S2")
    e_range.grid(row=6, column=3, sticky='nw')
    e_mark = tk.Entry(root, bd=2, width=EWIDTH)
    e_mark.grid(row=6, column=4, sticky='nw')

    check_rs = tk.IntVar()
    check_pgs = tk.IntVar()
    check_ct = tk.IntVar()
    check_ctc = tk.IntVar()
    check_mka = tk.IntVar()

    # 定义函数-单选框-重发
    def func_rs():
        if(check_rs.get()):
            e_mark.insert(0, "Reseed")

            l_rs_chn.grid(row=12, column=0, sticky='ne')
            b_rs_chn.grid(row=12, column=1, columnspan=2, sticky='nw')
            b_rs_eng.grid(row=12, column=3, columnspan=2, sticky='nw')
        else:
            e_mark.delete(0, tk.END)

            l_rs_chn.grid_forget()
            b_rs_chn.grid_forget()
            b_rs_eng.grid_forget()

    c0 = tk.Checkbutton(root, text="重发", variable=check_rs, onvalue=1, offvalue=0, command=func_rs)
    c0.grid(row=7, column=0, sticky='ne')
    c1 = tk.Checkbutton(root, text="内封原盘字幕。", variable=check_pgs, onvalue=1, offvalue=0)
    c1.grid(row=7, column=1, sticky='nw')
    c2 = tk.Checkbutton(root, text="内封评论音轨。", variable=check_ct, onvalue=1, offvalue=0)
    c2.grid(row=7, column=2, sticky='nw')
    c3 = tk.Checkbutton(root, text="部分内封评论音轨。", variable=check_ctc, onvalue=1, offvalue=0)
    c3.grid(row=7, column=3, sticky='nw')
    c4 = tk.Checkbutton(root, text="外挂 FLAC 5.1",variable=check_mka, onvalue=1, offvalue=0)
    c4.grid(row=7, column=4, sticky='nw')

    l_process_chn = tk.Label(root, text="画质")
    l_process_chn.grid(row=8, column=0, sticky='ne')
    b_process_chn = tk.Button(root, text="process_chn.txt", width=EWIDTH2, command=partial(open_text_file, "./content/process_chn.txt"))
    b_process_chn.grid(row=8, column=1, columnspan=2, sticky='nw')

    b_process_eng = tk.Button(root, text="process_eng.txt", width=EWIDTH2, command=partial(open_text_file, "./content/process_eng.txt"))
    b_process_eng.grid(row=8, column=3, columnspan=2, sticky='nw')

    l_comment = tk.Label(root, text="吐槽")
    l_comment.grid(row=10, column=0, sticky='ne')
    e_comment = tk.Text(root, width=EWIDTH4, height=5)
    e_comment.insert(tk.INSERT, "好想看到会动的瑠衣酱")
    e_comment.grid(row=10, column=1, columnspan=4, sticky='nw')

    l_provider = tk.Label(root, text="感谢")
    l_provider.grid(row=11, column=0, sticky='ne')
    e_provider = tk.Text(root, width=EWIDTH4, height=3)
    e_provider.insert(tk.INSERT, "BD: \nScans: \nCDs: ")
    e_provider.grid(row=11, column=1, columnspan=4, sticky='nw')

    l_rs_chn = tk.Label(root, text="修正")
    b_rs_chn = tk.Button(root, text="rs_chn.txt", width=EWIDTH2, command=partial(open_text_file, "./content/rs_chn.txt"))

    b_rs_eng = tk.Button(root, text="rs_eng.txt", width=EWIDTH2, command=partial(open_text_file, "./content/rs_eng.txt"))

    l_link1 = tk.Label(root, text="bangumi")
    l_link1.grid(row=14, column=0, sticky='ne')
    e_link1 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_link1.insert(0, "https://bangumi.moe/torrent/xxxxxxxx")
    e_link1.grid(row=14, column=1, columnspan=4, sticky='nw')

    l_link2 = tk.Label(root, text="s.acgnx")
    l_link2.grid(row=15, column=0, sticky='ne')
    e_link2 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_link2.insert(0, "https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html")
    e_link2.grid(row=15, column=1, columnspan=4, sticky='nw')

    l_link3 = tk.Label(root, text="acgnx")
    l_link3.grid(row=16, column=0, sticky='ne')
    e_link3 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_link3.insert(0, "https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html")
    e_link3.grid(row=16, column=1, columnspan=4, sticky='nw')

    l_link4 = tk.Label(root, text="acgrip")
    l_link4.grid(row=17, column=0, sticky='ne')
    e_link4 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_link4.insert(0, "https://acg.rip/t/xxxxxx")
    e_link4.grid(row=17, column=1, columnspan=4, sticky='nw')

    l_link5 = tk.Label(root, text="dmhy")
    l_link5.grid(row=18, column=0, sticky='ne')
    e_link5 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_link5.insert(0, "https://share.dmhy.org/topics/view/xxxxxx.html")
    e_link5.grid(row=18, column=1, columnspan=4, sticky='nw')

    l_link6 = tk.Label(root, text="nyaa")
    l_link6.grid(row=19, column=0, sticky='ne')
    e_link6 = tk.Entry(root, bd=2, width=EWIDTH4)
    e_link6.insert(0, "https://nyaa.si/view/xxxxxx")
    e_link6.grid(row=19, column=1, columnspan=4, sticky='nw')

    b_sc_html = tk.Button(root, text="screenshot_html.txt", width=EWIDTH2, command=partial(open_text_file, "./content/screenshot_html.txt"))
    b_sc_html.grid(row=20, column=1, columnspan=2, sticky='nw')
    # b_sc_md = tk.Button(root, text="screenshot_md.txt", width=EWIDTH-2, command=partial(open_text_file, "./content/screenshot_md.txt"))
    # b_sc_md.grid(row=20, column=2, sticky='nw')
    b_mediainfo = tk.Button(root, text="mediainfo.txt", width=EWIDTH2, command=partial(open_text_file, "./content/mediainfo.txt"))
    b_mediainfo.grid(row=20, column=3, columnspan=2, sticky='nw')

    # 定义函数-输入框-获得焦点事件，清除内容
    def e_onfocus_clear(event):
        if isinstance(event.widget, tk.Entry) or isinstance(event.widget, tk.Text):
            event.widget.delete(0, tk.END)

    for widget in root.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.bind('<FocusIn>', e_onfocus_clear)
        if isinstance(widget, tk.Text):
            widget.bind('<FocusIn>', e_onfocus_clear)

    # 定义函数-按钮-生成
    def btn_click_generate():
        doc=dict()
        # 获取输入信息
        doc['sub'] = e_sub.get()
        doc['title_chn'] = e_title_chn.get()
        doc['title_eng'] = e_title_eng.get()
        doc['title_jpn'] = e_title_jpn.get()
        doc['spec'] = e_spec.get()
        doc['type'] = e_type.get()
        doc['range'] = e_range.get()
        doc['mark'] = e_mark.get()
        doc['img_800'] = e_img_800.get()
        doc['img_1400'] = e_img_1400.get()
        doc['comment'] = e_comment.get(1.0, tk.END)
        doc['provider'] = e_provider.get(1.0, tk.END)
        doc['link1'] = e_link1.get()
        doc['link2'] = e_link2.get()
        doc['link3'] = e_link3.get()
        doc['link4'] = e_link4.get()
        doc['link5'] = e_link5.get()
        doc['link6'] = e_link6.get()
        doc['isRS'] = check_rs.get()
        doc['isPGS'] = check_pgs.get()
        doc['isCT'] = check_ct.get()
        doc['isCTC'] = check_ctc.get()
        doc['isMKA'] = check_mka.get()
        if(doc['range']):
            doc['range'] += " "
        if(doc['mark']):
            doc['mark'] += " "

        pubfile_bt(doc)
        pubfile_vcbs(doc)

        root.destroy()

    # 创建按钮
    b_generate = tk.Button(root, text="生成", width=EWIDTH4, command=btn_click_generate)
    b_generate.grid(row=MAXROW, column=1, columnspan=4, sticky='nw')

    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    main()