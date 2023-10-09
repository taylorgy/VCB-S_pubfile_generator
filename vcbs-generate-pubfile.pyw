# python 3.10.6
# -*- coding: UTF-8 -*-

import tkinter as tk
from functools import partial
# from tkinter import font
from tkinter import ttk

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
    label_img_800 = tk.Label(root, text="发布图-竖")
    label_img_800.grid(row=0, column=0, sticky='ne')
    entry_img_800 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_img_800.insert(0, "https://img.2222.moe/images/2023/09/04/oregairu_800.webp")
    entry_img_800.grid(row=0, column=1, columnspan=4, sticky='nw')

    label_img_1400 = tk.Label(root, text="发布图-横")
    label_img_1400.grid(row=1, column=0, sticky='ne')
    entry_img_1400 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_img_1400.insert(0, "https://img.2222.moe/images/2023/09/04/oregairu_1400.webp")
    entry_img_1400.grid(row=1, column=1, columnspan=4, sticky='nw')

    label_sub = tk.Label(root, text="字幕组")
    label_sub.grid(row=2, column=0, sticky='ne')

    combs_sub = []
    subs = list(SUB.keys())
    
    def func_btn_sub():
        if len(combs_sub):
            subs.remove(combs_sub[-1].get())
        combs_sub.append(ttk.Combobox(root, values=subs, state="readonly", width=(EWIDTH-3)))
        combs_sub[-1].grid(row=2, column=1+len(combs_sub), sticky='nw')
        if len(combs_sub) == 3:
            btn_sub['state'] = 'disabled'
            btn_sub['text'] = '什么项目这么多字幕组？'
        return
    
    btn_sub = tk.Button(root, text="添加字幕组", width=EWIDTH, command=func_btn_sub)
    btn_sub.grid(row=2, column=1, sticky='nw')

    label_title_chn = tk.Label(root, text="标题-中文")
    label_title_chn.grid(row=3, column=0, sticky='ne')
    entry_title_chn = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_title_chn.insert(0, "测试：我的青春恋爱物语果然有问题")
    entry_title_chn.grid(row=3, column=1, columnspan=4, sticky='nw')

    label_title_eng = tk.Label(root, text="标题-英文")
    label_title_eng.grid(row=4, column=0, sticky='ne')
    entry_title_eng = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_title_eng.insert(0, "Yahari Ore no Seishun Lovecome wa Machigatte Iru.")
    entry_title_eng.grid(row=4, column=1, columnspan=4, sticky='nw')

    label_title_jpn = tk.Label(root, text="标题-日文")
    label_title_jpn.grid(row=5, column=0, sticky='ne')
    entry_title_jpn = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_title_jpn.insert(0, "やはり俺の青春ラブコメはまちがっている.")
    entry_title_jpn.grid(row=5, column=1, columnspan=4, sticky='nw')

    label_spec = tk.Label(root, text="规格")
    label_spec.grid(row=6, column=0, sticky='ne')
    entry_spec = tk.Entry(root, bd=2, width=EWIDTH)
    entry_spec.insert(0, "10-bit 1080p HEVC")
    entry_spec.grid(row=6, column=1, sticky='nw')
    entry_type = tk.Entry(root, bd=2, width=EWIDTH)
    entry_type.insert(0, "BDRip")
    entry_type.grid(row=6, column=2, sticky='nw')
    entry_range = tk.Entry(root, bd=2, width=EWIDTH)
    entry_range.insert(0, "S1-S2")
    entry_range.grid(row=6, column=3, sticky='nw')
    entry_mark = tk.Entry(root, bd=2, width=EWIDTH)
    entry_mark.grid(row=6, column=4, sticky='nw')

    var_rs = tk.IntVar(root)
    var_pgs = tk.IntVar(root)
    var_ct = tk.IntVar(root)
    var_ctc = tk.IntVar(root)
    var_mka = tk.IntVar(root)

    label_rs_chn = tk.Label(root, text="修正")
    btn_rs_chn = tk.Button(root, text="rs_chn.txt", width=EWIDTH2, command=partial(open_text_file, "./content/rs_chn.txt"))
    btn_rs_eng = tk.Button(root, text="rs_eng.txt", width=EWIDTH2, command=partial(open_text_file, "./content/rs_eng.txt"))

    # 定义函数-单选框-重发
    # 选中则添加按钮以编辑重发修正内容
    def func_check_rs():
        if(var_rs.get()):
            entry_mark.insert(0, "Reseed")

            label_rs_chn.grid(row=12, column=0, sticky='ne')
            btn_rs_chn.grid(row=12, column=1, columnspan=2, sticky='nw')
            btn_rs_eng.grid(row=12, column=3, columnspan=2, sticky='nw')
        else:
            entry_mark.delete(0, tk.END)

            label_rs_chn.grid_forget()
            btn_rs_chn.grid_forget()
            btn_rs_eng.grid_forget()
        return

    check_rs = tk.Checkbutton(root, text="重发", variable=var_rs, onvalue=1, offvalue=0, command=func_check_rs)
    check_rs.grid(row=7, column=0, sticky='ne')
    check_pgs = tk.Checkbutton(root, text="内封原盘字幕。", variable=var_pgs, onvalue=1, offvalue=0)
    check_pgs.grid(row=7, column=1, sticky='nw')
    check_ct = tk.Checkbutton(root, text="内封评论音轨。", variable=var_ct, onvalue=1, offvalue=0)
    check_ct.grid(row=7, column=2, sticky='nw')
    check_ctc = tk.Checkbutton(root, text="部分内封评论音轨。", variable=var_ctc, onvalue=1, offvalue=0)
    check_ctc.grid(row=7, column=3, sticky='nw')
    check_mka = tk.Checkbutton(root, text="外挂 FLAC 5.1",variable=var_mka, onvalue=1, offvalue=0)
    check_mka.grid(row=7, column=4, sticky='nw')

    label_process_chn = tk.Label(root, text="画质")
    label_process_chn.grid(row=8, column=0, sticky='ne')
    btn_process_chn = tk.Button(root, text="process_chn.txt", width=EWIDTH2, command=partial(open_text_file, "./content/process_chn.txt"))
    btn_process_chn.grid(row=8, column=1, columnspan=2, sticky='nw')

    btn_process_eng = tk.Button(root, text="process_eng.txt", width=EWIDTH2, command=partial(open_text_file, "./content/process_eng.txt"))
    btn_process_eng.grid(row=8, column=3, columnspan=2, sticky='nw')

    label_comment = tk.Label(root, text="吐槽")
    label_comment.grid(row=10, column=0, sticky='ne')
    entry_comment = tk.Text(root, width=EWIDTH4, height=5)
    entry_comment.insert(tk.INSERT, "好想看到会动的瑠衣酱")
    entry_comment.grid(row=10, column=1, columnspan=4, sticky='nw')

    label_provider = tk.Label(root, text="感谢")
    label_provider.grid(row=11, column=0, sticky='ne')
    entry_provider = tk.Text(root, width=EWIDTH4, height=3)
    entry_provider.insert(tk.INSERT, "BD: \nScans: \nCDs: ")
    entry_provider.grid(row=11, column=1, columnspan=4, sticky='nw')

    label_link1 = tk.Label(root, text="bangumi")
    label_link1.grid(row=14, column=0, sticky='ne')
    entry_link1 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_link1.insert(0, "https://bangumi.moe/torrent/xxxxxxxx")
    entry_link1.grid(row=14, column=1, columnspan=4, sticky='nw')

    label_link2 = tk.Label(root, text="s.acgnx")
    label_link2.grid(row=15, column=0, sticky='ne')
    entry_link2 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_link2.insert(0, "https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html")
    entry_link2.grid(row=15, column=1, columnspan=4, sticky='nw')

    label_link3 = tk.Label(root, text="acgnx")
    label_link3.grid(row=16, column=0, sticky='ne')
    entry_link3 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_link3.insert(0, "https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html")
    entry_link3.grid(row=16, column=1, columnspan=4, sticky='nw')

    label_link4 = tk.Label(root, text="acgrip")
    label_link4.grid(row=17, column=0, sticky='ne')
    entry_link4 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_link4.insert(0, "https://acg.rip/t/xxxxxx")
    entry_link4.grid(row=17, column=1, columnspan=4, sticky='nw')

    label_link5 = tk.Label(root, text="dmhy")
    label_link5.grid(row=18, column=0, sticky='ne')
    entry_link5 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_link5.insert(0, "https://share.dmhy.org/topics/view/xxxxxx.html")
    entry_link5.grid(row=18, column=1, columnspan=4, sticky='nw')

    label_link6 = tk.Label(root, text="nyaa")
    label_link6.grid(row=19, column=0, sticky='ne')
    entry_link6 = tk.Entry(root, bd=2, width=EWIDTH4)
    entry_link6.insert(0, "https://nyaa.si/view/xxxxxx")
    entry_link6.grid(row=19, column=1, columnspan=4, sticky='nw')

    btn_sc_html = tk.Button(root, text="screenshot.txt", width=EWIDTH2, command=partial(open_text_file, "./content/screenshot.txt"))
    btn_sc_html.grid(row=20, column=1, columnspan=2, sticky='nw')
    # btn_sc_md = tk.Button(root, text="screenshot_md.txt", width=EWIDTH-2, command=partial(open_text_file, "./content/screenshot_md.txt"))
    # btn_sc_md.grid(row=20, column=2, sticky='nw')
    btn_mediainfo = tk.Button(root, text="mediainfo.txt", width=EWIDTH2, command=partial(open_text_file, "./content/mediainfo.txt"))
    btn_mediainfo.grid(row=20, column=3, columnspan=2, sticky='nw')

    # 定义函数-输入框-获得焦点清除内容
    def entry_onfocus_clear(event):
        if isinstance(event.widget, tk.Entry):
            event.widget.delete(0, tk.END)
        if isinstance(event.widget, tk.Text):
            event.widget.delete(1.0, tk.END)

    for widget in root.winfo_children():
        if isinstance(widget, tk.Entry) or isinstance(widget, tk.Text):
            widget.bind('<FocusIn>', entry_onfocus_clear)

    # 定义函数-按钮-生成
    def func_btn_generate():
        doc=dict()
        # 获取输入信息
        doc['sub'] = [c.get() for c in combs_sub]
        doc['title_chn'] = entry_title_chn.get()
        doc['title_eng'] = entry_title_eng.get()
        doc['title_jpn'] = entry_title_jpn.get()
        doc['spec'] = entry_spec.get()
        doc['type'] = entry_type.get()
        doc['range'] = entry_range.get()
        doc['mark'] = entry_mark.get()
        doc['img_800'] = entry_img_800.get()
        doc['img_1400'] = entry_img_1400.get()
        doc['comment'] = entry_comment.get(1.0, tk.END)
        doc['provider'] = entry_provider.get(1.0, tk.END)
        doc['link1'] = entry_link1.get()
        doc['link2'] = entry_link2.get()
        doc['link3'] = entry_link3.get()
        doc['link4'] = entry_link4.get()
        doc['link5'] = entry_link5.get()
        doc['link6'] = entry_link6.get()
        doc['isRS'] = var_rs.get()
        doc['isPGS'] = var_pgs.get()
        doc['isCT'] = var_ct.get()
        doc['isCTC'] = var_ctc.get()
        doc['isMKA'] = var_mka.get()
        if(doc['range']):
            doc['range'] += " "
        if(doc['mark']):
            doc['mark'] += " "

        pubfile_bt(doc)
        pubfile_vcbs(doc)
        
        root.destroy()
        return

    # 创建按钮
    btn_generate = tk.Button(root, text="生成", width=EWIDTH4, command=func_btn_generate)
    btn_generate.grid(row=MAXROW, column=1, columnspan=4, sticky='nw')

    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    main()