# python 3.10.6
# -*- coding: UTF-8 -*-

from util.func import *

import tkinter as tk
from functools import partial
# from tkinter import font
from tkinter import ttk

def main():
    if not os.path.exists("./content"):
        os.makedirs("./content")
    
    if os.path.exists("./content/doc.xml"):
        DOC.update(load_xml_to_dict("./content/doc.xml"))

    # 创建主窗口
    root = tk.Tk()
    root.title("VCB-S 发布文档生成程序")
    root.geometry(WINDOW)
    
    # 创建垂直滚动条
    scrollbar = tk.Scrollbar(root, orient='vertical')

    # 创建 canvas 部件，并与滚动条关联
    canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
    scrollbar.config(command=canvas.yview)

    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # 在 canvas 上添加内容，
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    def on_mousewheel(event):
        if event.delta:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # 配置 Canvas 的滚动区域
    canvas.bind('<Configure>', on_configure)

    # 绑定鼠标滚轮事件
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # 设置行和列的权重，使其在调整窗口大小时可以自动扩展
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # 创建一个自定义字体
    # custom_font = font.Font(family="Arial", size=12)
    # # 将自定义字体设置为窗口的默认字体
    # root.option_add("*Font", custom_font)
    
    currRow = 0

    # 创建标签和输入栏
    label_img_800 = tk.Label(frame, text="发布图")
    label_img_800.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))

    entry_img_800 = tk.Entry(frame, bd=2, width=EWIDTH4)
    entry_img_800.grid(row=currRow, column=1, columnspan=4, sticky='nw')
    DOC['img_800'] and entry_img_800.insert(0, DOC['img_800'])

    currRow+=1

    label_sub = tk.Label(frame, text="字幕组")
    label_sub.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))

    combs_sub = []
    subs = list(SUB.keys())
    
    def func_btn_sub():
        if len(combs_sub):
            subs.remove(combs_sub[-1].get())
        combs_sub.append(ttk.Combobox(frame, values=subs, state="readonly", width=(EWIDTH-3)))
        combs_sub[-1].grid(row=currRow, column=1+len(combs_sub), sticky='nw')
        if len(combs_sub) == 3:
            btn_sub['state'] = 'disabled'
            btn_sub['text'] = '什么项目这么多字幕组？'
        return
    
    btn_sub = tk.Button(frame, text="添加字幕组", width=EWIDTH, command=func_btn_sub)
    btn_sub.grid(row=currRow, column=1, sticky='nw')

    currRow+=1

    label_title_chn = tk.Label(frame, text="标题-中文")
    label_title_chn.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    entry_title_chn = tk.Entry(frame, bd=2, width=EWIDTH4)
    entry_title_chn.grid(row=currRow, column=1, columnspan=4, sticky='nw')
    DOC['title_chn'] and entry_title_chn.insert(0, DOC['title_chn'])

    currRow+=1

    label_title_eng = tk.Label(frame, text="标题-英文")
    label_title_eng.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    entry_title_eng = tk.Entry(frame, bd=2, width=EWIDTH4)
    entry_title_eng.grid(row=currRow, column=1, columnspan=4, sticky='nw')
    DOC['title_eng'] and entry_title_eng.insert(0, DOC['title_eng'])

    currRow+=1

    label_title_jpn = tk.Label(frame, text="标题-日文")
    label_title_jpn.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    entry_title_jpn = tk.Entry(frame, bd=2, width=EWIDTH4)
    entry_title_jpn.grid(row=currRow, column=1, columnspan=4, sticky='nw')
    DOC['title_jpn'] and entry_title_jpn.insert(0, DOC['title_jpn'])

    currRow+=1

    label_spec = tk.Label(frame, text="规格")
    label_spec.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    entry_spec = tk.Entry(frame, bd=2, width=EWIDTH)
    entry_spec.grid(row=currRow, column=1, sticky='nw')
    if DOC['spec']:
        entry_spec.insert(0, DOC['spec'])
    else:
        entry_spec.insert(0, "10-bit 1080p HEVC")
    entry_type = tk.Entry(frame, bd=2, width=EWIDTH)
    if DOC['type']:
        entry_type.insert(0, DOC['type'])
    else:
        entry_type.insert(0, "BDRip")
    entry_type.grid(row=currRow, column=2, sticky='nw')
    entry_range = tk.Entry(frame, bd=2, width=EWIDTH)
    DOC['range'] and entry_range.insert(0, DOC['range'])
    # entry_range.insert(0, "S1-S2")
    entry_range.grid(row=currRow, column=3, sticky='nw')
    entry_mark = tk.Entry(frame, bd=2, width=EWIDTH)
    entry_mark.grid(row=currRow, column=4, sticky='nw')

    currRow+=1

    var_rs = tk.IntVar(frame)
    var_pgs = tk.IntVar(frame)
    var_ct = tk.IntVar(frame)
    var_ctc = tk.IntVar(frame)
    var_mka = tk.IntVar(frame)

    label_rs_chn = tk.Label(frame, text="修正")
    btn_rs_chn = tk.Button(frame, text="rs_chn.txt", width=EWIDTH2, command=partial(open_text_file, "./content/rs_chn.txt"))
    btn_rs_eng = tk.Button(frame, text="rs_eng.txt", width=EWIDTH2, command=partial(open_text_file, "./content/rs_eng.txt"))

    # 定义函数-单选框-重发
    # 选中则添加按钮以编辑重发修正内容
    def func_check_rs():
        if(var_rs.get()):
            entry_mark.insert(0, "Reseed")

            label_rs_chn.grid(row=rsRow, column=0, sticky='ne', padx=(10, 10))
            btn_rs_chn.grid(row=rsRow, column=1, columnspan=2, sticky='nw')
            btn_rs_eng.grid(row=rsRow, column=3, columnspan=2, sticky='nw')
        else:
            entry_mark.delete(0, tk.END)

            label_rs_chn.grid_forget()
            btn_rs_chn.grid_forget()
            btn_rs_eng.grid_forget()
        return
    check_rs = tk.Checkbutton(frame, text="重发", variable=var_rs, onvalue=1, offvalue=0, command=func_check_rs)
    check_rs.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    DOC['isRS'] and var_rs.set(DOC['isRS'])
    rsRow = currRow+1
    func_check_rs()
    check_pgs = tk.Checkbutton(frame, text="内封原盘字幕。", variable=var_pgs, onvalue=1, offvalue=0)
    check_pgs.grid(row=currRow, column=1, sticky='nw')
    DOC['isPGS'] and var_pgs.set(DOC['isPGS'])
    check_ct = tk.Checkbutton(frame, text="内封评论音轨。", variable=var_ct, onvalue=1, offvalue=0)
    check_ct.grid(row=currRow, column=2, sticky='nw')
    DOC['isCT'] and var_ct.set(DOC['isCT'])
    check_ctc = tk.Checkbutton(frame, text="部分内封评论音轨。", variable=var_ctc, onvalue=1, offvalue=0)
    check_ctc.grid(row=currRow, column=3, sticky='nw')
    DOC['isCTC'] and var_ctc.set(DOC['isCTC'])
    check_mka = tk.Checkbutton(frame, text="外挂 FLAC 5.1",variable=var_mka, onvalue=1, offvalue=0)
    check_mka.grid(row=currRow, column=4, sticky='nw')
    DOC['isMKA'] and var_mka.set(DOC['isMKA'])
    
    currRow+=2

    label_process_chn = tk.Label(frame, text="画质")
    label_process_chn.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    btn_process_chn = tk.Button(frame, text="process_chn.txt", width=EWIDTH2, command=partial(open_text_file, "./content/process_chn.txt"))
    btn_process_chn.grid(row=currRow, column=1, columnspan=2, sticky='nw')

    btn_process_eng = tk.Button(frame, text="process_eng.txt", width=EWIDTH2, command=partial(open_text_file, "./content/process_eng.txt"))
    btn_process_eng.grid(row=currRow, column=3, columnspan=2, sticky='nw')

    currRow+=1

    label_provider = tk.Label(frame, text="感谢")
    label_provider.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    entry_provider = tk.Text(frame, width=EWIDTH4, height=3)
    DOC['provider'] and entry_provider.insert(1.0, DOC['provider'].rstrip('\n'))
    entry_provider.grid(row=currRow, column=1, columnspan=4, sticky='nw')

    currRow+=1

    label_comment = tk.Label(frame, text="吐槽")
    label_comment.grid(row=currRow, column=0, sticky='ne', padx=(10, 10))
    entry_comment = tk.Text(frame, width=EWIDTH4, height=5)
    DOC['comment'] and entry_comment.insert(1.0, DOC['comment'].rstrip('\n'))
    entry_comment.grid(row=currRow, column=1, columnspan=4, sticky='nw')

    currRow+=1

    btn_sc_html = tk.Button(frame, text="screenshot.txt", width=EWIDTH2, command=partial(open_text_file, "./content/screenshot.txt"))
    btn_sc_html.grid(row=currRow, column=1, columnspan=2, sticky='nw')
    btn_mediainfo = tk.Button(frame, text="mediainfo.txt", width=EWIDTH2, command=partial(open_text_file, "./content/mediainfo.txt"))
    btn_mediainfo.grid(row=currRow, column=3, columnspan=2, sticky='nw')

    currRow+=1

    entry_links = []
    sites = list(LINK.keys())
    for i in range(LENLINK):
        label_link = tk.Label(frame, text=sites[i])
        label_link.grid(row=i+currRow, column=0, sticky='ne', padx=(10, 10))
        entry_link = tk.Entry(frame, bd=2, width=EWIDTH4)
        entry_link.insert(0, LINK[sites[i]])
        entry_link.grid(row=i+currRow, column=1, columnspan=4, sticky='nw')
        entry_links.append(entry_link)

    currRow+=LENLINK

    # 定义函数-按钮-链接更新
    # 根据固定格式
    def func_btn_link_update():
        links = []
        with open("./content/link.txt", 'r') as f:
            links = f.readlines()
        links = links[:LENLINK]
        for i in range(LENLINK):
            # if i in range(1, LENLINK-1):
            if ': ' in links[i]:
                links[i] = links[i].split(': ')[1]
            entry_links[i].delete(0, tk.END)
            entry_links[i].insert(0, links[i].rstrip('\n'))
        with open("./content/link.txt", 'w') as f:
            f.writelines(links)
            f.write("\n")
            f.write("\n")
            for i in range(LENLINK):
                link = links[i].rstrip('\n')
                f.write(f"<a href=\"{link}\" rel=\"noopener\" target=\"_blank\">{link}</a>\n")
                if (i < LENLINK-1):
                    f.write("\n")
        return

    btn_link_edit = tk.Button(frame, text="link.txt", width=EWIDTH2, command=partial(open_text_file, "./content/link.txt"))
    btn_link_edit.grid(row=currRow, column=1, columnspan=2, sticky='nw')
    btn_link_update = tk.Button(frame, text="link update", width=EWIDTH2, command=func_btn_link_update)
    btn_link_update.grid(row=currRow, column=3, columnspan=2, sticky='nw')

    currRow+=1

    # 定义函数-右键双击事件-若是文本框则清除内容
    def func_root_doubleclick_entryclear(event):
        # event.widget.focus_set()
        if isinstance(event.widget, tk.Entry):
            event.widget.delete(0, tk.END)
        if isinstance(event.widget, tk.Text):
            event.widget.delete(1.0, tk.END)
        return

    root.bind("<Double-3>", func_root_doubleclick_entryclear)

    # 定义函数-按钮-生成
    def func_btn_generate():
        # 获取输入信息
        DOC['sub'] = [c.get() for c in combs_sub]
        DOC['title_chn'] = entry_title_chn.get()
        DOC['title_eng'] = entry_title_eng.get()
        DOC['title_jpn'] = entry_title_jpn.get()
        DOC['spec'] = entry_spec.get()
        DOC['type'] = entry_type.get()
        DOC['range'] = entry_range.get()
        DOC['mark'] = entry_mark.get()
        DOC['img_800'] = entry_img_800.get()
        # DOC['img_1400'] = entry_img_1400.get()
        DOC['comment'] = entry_comment.get(1.0, tk.END)
        DOC['provider'] = entry_provider.get(1.0, tk.END)
        links = []
        for i in range(LENLINK):
            links.append(entry_links[i].get())
        DOC['links'] = links
        DOC['isRS'] = var_rs.get()
        DOC['isPGS'] = var_pgs.get()
        DOC['isCT'] = var_ct.get()
        DOC['isCTC'] = var_ctc.get()
        DOC['isMKA'] = var_mka.get()

        save_dict_to_xml(DOC, "./content/doc.xml")

        if(DOC['range']):
            DOC['range'] += " "
        if(DOC['mark']):
            DOC['mark'] += " "
        pubfile_bt(DOC)
        pubfile_vcbs(DOC)

        root.destroy()
        return

    # 创建按钮
    btn_generate = tk.Button(frame, text="生成", width=EWIDTH4, command=func_btn_generate)
    btn_generate.grid(row=currRow, column=1, columnspan=4, sticky='nw')
    
    currRow+=1

    # 设置元素间距
    for i in range(currRow):
        frame.grid_rowconfigure(i, pad=10)

    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    main()