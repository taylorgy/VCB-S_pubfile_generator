# python 3.10.6
# -*- coding: UTF-8 -*-

import tkinter as tk
import os
from functools import partial

SUB= {
    '千夏字幕组': 'Airota',
    '喵萌奶茶屋': 'Nekomoe kissaten',
    '喵萌Production': 'Nekomoe kissaten',
    '悠哈璃羽字幕社': 'UHA-WINGS',
    '诸神字幕组': 'Kamigami',
    '天香字幕社': 'T.H.X',
    '动漫国字幕组': 'DMG',
    '星空字幕组': 'XKsub',
    '茉语星梦': 'MakariHoshiyume',
    '风之圣殿': 'FZSD',
    '白恋字幕组': 'Shirokoi',
    'SweetSub': 'SweetSub'
}

pubrest_bt_new = '''
VCB-Studio 已不再保证收集作品相关 CD 和扫图资源，详情请参见 <a href="https://vcb-s.com/archives/14331">https://vcb-s.com/archives/14331</a>。<br />
Please refer to <a href="https://vcb-s.com/archives/14331">https://vcb-s.com/archives/14331</a> for more information about that VCB-Studio will no longer guarantee to include relevant CDs and scans.<br />
<br />
本组（不）定期招募新成员。详情请参见 <a href="https://vcb-s.com/archives/16986">https://vcb-s.com/archives/16986</a>。<br />
Please refer to <a href="https://vcb-s.com/archives/16986">https://vcb-s.com/archives/16986</a> about information of our (un)scheduled recruitment.<br />
<br />
有关 TSDM 合购区的详情请参见 <a href="https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923">https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923</a>。<br />
Please refer to <a href="https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923">https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923</a> for more information about jointly purchased music.<br />
<br />
播放器教程索引： <a href="https://vcb-s.com/archives/16639" target="_blank">VCB-Studio 播放器推荐</a><br />
中文字幕分享区： <a href="https://bbs.acgrip.com/" target="_blank">Anime 分享论坛</a><br />
项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a><br />
特殊格式与说明： <a href="https://vcb-s.com/archives/7949" target="_blank">WebP 扫图说明</a><br />
<br />
</p>
<hr />
'''

pubrest_bt_rs = '''
<br />
</p>
<hr />
<p>
本次发布来自 VCB-Studio 旧作重发计划。我们会不定期重发过去发布过的合集，或为补充做种，或为修正制作错漏，或为整合系列合集。<br />
<br />
</p>
<hr />
<p>
播放器教程索引： <a href="https://vcb-s.com/archives/16639" target="_blank">VCB-Studio 播放器推荐</a><br />
中文字幕分享区： <a href="https://bbs.acgrip.com/" target="_blank">Anime 分享论坛</a><br />
项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a><br />
特殊格式与说明： <a href="https://vcb-s.com/archives/7949" target="_blank">WebP 扫图说明</a><br />
<br />
</p>
'''

doc=dict()

if not os.path.exists("./content"):
    os.makedirs("./content")

# 创建主窗口
root = tk.Tk()
root.title("VCB-S 发布文档生成程序")

root.geometry('820x1000')
EWIDTH = 100
THTITLE = 25
MAXROW = 30
for i in range(MAXROW):
    root.grid_rowconfigure(i, pad=15)
# root.grid_columnconfigure(1, pad=100)

# 创建标签和输入栏
l_img_800 = tk.Label(root, text="发布图-800")
l_img_800.grid(row=0, column=0, sticky='ne')
e_img_800 = tk.Entry(root, width=EWIDTH)
e_img_800.insert(0, "https://img.2222.moe/images/2023/09/04/oregairu_800.webp")
e_img_800.grid(row=0, column=1, columnspan=4, sticky='nw')

l_img_1400 = tk.Label(root, text="发布图-1400")
l_img_1400.grid(row=1, column=0, sticky='ne')
e_img_1400 = tk.Entry(root, width=EWIDTH)
e_img_1400.insert(0, "https://img.2222.moe/images/2023/09/04/oregairu_1400.webp")
e_img_1400.grid(row=1, column=1, columnspan=4, sticky='nw')

l_sub = tk.Label(root, text="字幕组")
l_sub.grid(row=2, column=0, sticky='ne')
e_sub = tk.Entry(root, width=EWIDTH)
# e_sub.insert(0, "动漫国字幕组")
e_sub.grid(row=2, column=1, columnspan=4, sticky='nw')

l_title_chn = tk.Label(root, text="标题-中文")
l_title_chn.grid(row=3, column=0, sticky='ne')
e_title_chn = tk.Entry(root, width=EWIDTH)
e_title_chn.insert(0, "测试：我的青春恋爱物语果然有问题")
e_title_chn.grid(row=3, column=1, columnspan=4, sticky='nw')

l_title_eng = tk.Label(root, text="标题-英文")
l_title_eng.grid(row=4, column=0, sticky='ne')
e_title_eng = tk.Entry(root, width=EWIDTH)
e_title_eng.insert(0, "Yahari Ore no Seishun Lovecome wa Machigatte Iru.")
e_title_eng.grid(row=4, column=1, columnspan=4, sticky='nw')

l_title_jpn = tk.Label(root, text="标题-日文")
l_title_jpn.grid(row=5, column=0, sticky='ne')
e_title_jpn = tk.Entry(root, width=EWIDTH)
e_title_jpn.insert(0, "やはり俺の青春ラブコメはまちがっている.")
e_title_jpn.grid(row=5, column=1, columnspan=4, sticky='nw')

l_spec = tk.Label(root, text="规格")
l_spec.grid(row=6, column=0, sticky='ne')
e_spec = tk.Entry(root, width=int(EWIDTH/4)-2)
e_spec.insert(0, "10-bit 1080p HEVC")
e_spec.grid(row=6, column=1)
e_type = tk.Entry(root, width=int(EWIDTH/4)-2)
e_type.insert(0, "BDRip")
e_type.grid(row=6, column=2)
e_range = tk.Entry(root, width=int(EWIDTH/4)-2)
# e_range.insert(0, "S1-S2")
e_range.grid(row=6, column=3)
e_mark = tk.Entry(root, width=int(EWIDTH/4)-2)
e_mark.grid(row=6, column=4)

check_rs = tk.IntVar()
check_pgs = tk.IntVar()
check_ct = tk.IntVar()
check_ctc = tk.IntVar()
check_mka = tk.IntVar()

# 定义重发单选框事件
def func_rs():
    if(check_rs.get()):
        e_mark.insert(0, "Reseed")

        l_rs_chn.grid(row=12, column=0, sticky='ne')
        b_rs_chn.grid(row=12, column=1, columnspan=4, sticky='nw')
        l_rs_eng.grid(row=13, column=0, sticky='ne')
        b_rs_eng.grid(row=13, column=1, columnspan=4, sticky='nw')
    else:
        e_mark.delete(0, tk.END)

        l_rs_chn.grid_forget()
        b_rs_chn.grid_forget()
        l_rs_eng.grid_forget()
        b_rs_eng.grid_forget()

c0 = tk.Checkbutton(root, text="重发", variable=check_rs, onvalue=1, offvalue=0, command=func_rs)
c0.grid(row=7, column=0)
c1 = tk.Checkbutton(root, text="内封原盘 ENG + JPN 字幕。", variable=check_pgs, onvalue=1, offvalue=0)
c1.grid(row=7, column=1)
c2 = tk.Checkbutton(root, text="内封评论音轨。", variable=check_ct, onvalue=1, offvalue=0)
c2.grid(row=7, column=2)
c3 = tk.Checkbutton(root, text="部分剧集内封评论音轨。", variable=check_ctc, onvalue=1, offvalue=0)
c3.grid(row=7, column=3)
c4 = tk.Checkbutton(root, text="外挂 FLAC 5.1 + Headphone X。",variable=check_mka, onvalue=1, offvalue=0)
c4.grid(row=7, column=4)

# 定义按钮打开文件函数
def open_text_file(filename):
    file_path = os.path.join("./content", filename)
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf8') as f:
            pass
    
    os.system(f"notepad.exe {file_path}")

l_process_chn = tk.Label(root, text="画质")
l_process_chn.grid(row=8, column=0, sticky='ne')
b_process_chn = tk.Button(root, text="process_chn.txt", width=EWIDTH, command=partial(open_text_file, "process_chn.txt"))
b_process_chn.grid(row=8, column=1, columnspan=4, sticky='nw')

l_process_eng = tk.Label(root, text="翻译")
l_process_eng.grid(row=9, column=0, sticky='ne')
b_process_eng = tk.Button(root, text="process_eng.txt", width=EWIDTH, command=partial(open_text_file, "process_eng.txt"))
b_process_eng.grid(row=9, column=1, columnspan=4, sticky='nw')

l_comment = tk.Label(root, text="吐槽")
l_comment.grid(row=10, column=0, sticky='ne')
e_comment = tk.Text(root, width=EWIDTH, height=5)
# e_comment.insert(tk.INSERT, "好想看到会动的瑠衣酱")
e_comment.grid(row=10, column=1, columnspan=4, sticky='nw')

l_provider = tk.Label(root, text="感谢")
l_provider.grid(row=11, column=0, sticky='ne')
e_provider = tk.Text(root, width=EWIDTH, height=3)
e_provider.insert(tk.INSERT, "BD: \nScans: \nCDs: ")
e_provider.grid(row=11, column=1, columnspan=4, sticky='nw')

l_rs_chn = tk.Label(root, text="重发")
# l_rs_chn.grid(row=12, column=0, sticky='ne')
b_rs_chn = tk.Button(root, text="rs_chn.txt", width=EWIDTH, command=partial(open_text_file, "rs_chn.txt"))
# b_rs_chn.grid(row=12, column=1, columnspan=4, sticky='nw')

l_rs_eng = tk.Label(root, text="翻译")
# l_rs_eng.grid(row=13, column=0, sticky='ne')
b_rs_eng = tk.Button(root, text="rs_eng.txt", width=EWIDTH, command=partial(open_text_file, "rs_eng.txt"))
# b_rs_eng.grid(row=13, column=1, columnspan=4, sticky='nw')

l_link1 = tk.Label(root, text="bangumi")
l_link1.grid(row=14, column=0, sticky='ne')
e_link1 = tk.Entry(root, width=EWIDTH)
e_link1.insert(0, "https://bangumi.moe/torrent/xxxxxxxx")
e_link1.grid(row=14, column=1, columnspan=4, sticky='nw')

l_link2 = tk.Label(root, text="s.acgnx")
l_link2.grid(row=15, column=0, sticky='ne')
e_link2 = tk.Entry(root, width=EWIDTH)
e_link2.insert(0, "https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html")
e_link2.grid(row=15, column=1, columnspan=4, sticky='nw')

l_link3 = tk.Label(root, text="acgnx")
l_link3.grid(row=16, column=0, sticky='ne')
e_link3 = tk.Entry(root, width=EWIDTH)
e_link3.insert(0, "https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html")
e_link3.grid(row=16, column=1, columnspan=4, sticky='nw')

l_link4 = tk.Label(root, text="acgrip")
l_link4.grid(row=17, column=0, sticky='ne')
e_link4 = tk.Entry(root, width=EWIDTH)
e_link4.insert(0, "https://acg.rip/t/xxxxxx")
e_link4.grid(row=17, column=1, columnspan=4, sticky='nw')

l_link5 = tk.Label(root, text="dmhy")
l_link5.grid(row=18, column=0, sticky='ne')
e_link5 = tk.Entry(root, width=EWIDTH)
e_link5.insert(0, "https://share.dmhy.org/topics/view/xxxxxx.html")
e_link5.grid(row=18, column=1, columnspan=4, sticky='nw')

l_link6 = tk.Label(root, text="nyaa")
l_link6.grid(row=19, column=0, sticky='ne')
e_link6 = tk.Entry(root, width=EWIDTH)
e_link6.insert(0, "https://nyaa.si/view/xxxxxx")
e_link6.grid(row=19, column=1, columnspan=4, sticky='nw')

b_sc_html = tk.Button(root, text="screenshot_html.txt", width=int(EWIDTH/4)-2, command=partial(open_text_file, "screenshot_html.txt"))
b_sc_html.grid(row=20, column=1, sticky='nw')
b_sc_md = tk.Button(root, text="screenshot_md.txt", width=int(EWIDTH/4)-2, command=partial(open_text_file, "screenshot_md.txt"))
b_sc_md.grid(row=20, column=2, sticky='nw')
b_mediainfo = tk.Button(root, text="mediainfo.txt", width=int(EWIDTH/4)-2, command=partial(open_text_file, "mediainfo.txt"))
b_mediainfo.grid(row=20, column=3, sticky='nw')

# 输入框获得焦点事件，清除内容函数
def e_onfocus_clear(event):
    if isinstance(event.widget, tk.Entry) or isinstance(event.widget, tk.Text):
        event.widget.delete(0, tk.END)

for widget in root.winfo_children():
    if isinstance(widget, tk.Entry):
        widget.bind('<FocusIn>', e_onfocus_clear)
    if isinstance(widget, tk.Text):
        widget.bind('<FocusIn>', e_onfocus_clear)

# 定义按钮点击事件
def btn_click_generate():
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

    isShort = (len(doc['title_eng']) < THTITLE)
    isRS = check_rs.get()
    if(doc['range']):
        doc['range'] += " "
    if(doc['mark']):
        doc['mark'] += " "

    # 生成发布内容-bt
    if(doc['sub']):
        pubgroup = "["+ doc['sub'] +"&VCB-Studio] "
    else:
        pubgroup = "[VCB-Studio] "
    if(isShort):
        pubtitle_bt = (pubgroup + doc['title_chn'] +" / "+ doc['title_eng'] +" / "+ doc['title_jpn'] +" "+ doc['spec'] +" "+ doc['type'] +" ["+ doc['range'] + doc['mark'] + "Fin]")
    else:
        pubtitle_bt = (pubgroup + doc['title_chn'] +" / "+ doc['title_eng'] +" "+ doc['spec'] +" "+ doc['type'] +" ["+ doc['range'] + doc['mark'] + "Fin]")
     
    pubimg_800="<img src=\"" + doc["img_800"] +"\" alt=\"" + doc["img_800"].split('/')[-1] + "\" /><br />"
    
    if(isShort):
        pubtitle_content = (doc['title_chn'] +" / "+ doc['title_eng'] +" / "+ doc['title_jpn'] +" "+ doc['range'] + doc['type'] +" "+ doc['mark'] + "<br />")
    else:
        pubtitle_content = (\
        doc['title_chn'] +" "+ doc['range'] + doc['type'] +" "+ doc['mark'] + "<br />\n" + \
        doc['title_eng'] +" "+ doc['range'] + doc['type'] +" "+ doc['mark'] + "<br />\n" +\
        doc['title_jpn'] +" "+ doc['range'] + doc['type'] +" "+ doc['mark'] + "<br />")

    # 输出发布内容到文件-bt
    with open(doc["title_chn"]+"-BANGUMI.html", 'w', encoding='utf8') as f:
        f.write(pubtitle_bt +"\n")
        f.write("<p>\n")
        f.write(pubimg_800 +"\n")
        f.write("<br />\n")
        f.write(pubtitle_content +"\n")
        f.write("<br />\n")
        if(check_pgs.get()):
            f.write("内封原盘 ENG + JPN 字幕。<br /> \nEmbedded official ENG + JPN PGS.<br />\n")
            f.write("<br />\n")
        if(check_ct.get()):
            f.write("内封评论音轨。<br />\nEmbedded commentary track.<br />\n")
            f.write("<br />\n")
        if(check_ctc.get()):
            f.write("部分剧集内封评论音轨。<br />\nCertain episodes contain commentary tracks.<br />\n")
            f.write("<br />\n")
        if(check_mka.get()):
            f.write("外挂 FLAC 5.1 + Headphone X。<br />\nMKA contains FLAC 5.1 + Headphone X.<br />\n")
            f.write("<br />\n")
        if(doc['sub']):
            f.write("这个项目与 <strong>" + doc['sub'] + "</strong> 合作，感谢他们精心制作的字幕。<br />\n")
            f.write("This project is in collaboration with <strong>" +SUB[doc['sub']]+ "</strong>. Thanks to them for elaborating Chinese subtitles.<br />\n")
            f.write("<br />\n")
        
        with open("./content/process_chn.txt", 'r', encoding='utf8') as s:
                f.write(s.read().replace('\n', '<br />\n'))
        with open("./content/process_eng.txt", 'r', encoding='utf8') as s:
                f.write(s.read().replace('\n', '<br />\n'))
        f.write("<br />\n")
        
        if(doc['comment']!='\n'):
            f.write(str(doc['comment']).replace('\n', '<br />\n'))
            f.write("<br />\n")
        f.write("</p>\n")
        f.write("<hr />\n")

        # 新番
        if not(isRS):
            f.write("<p>\n")
            f.write("感谢所有资源提供者 / Thanks to all resource providers: <br />\n")
            f.write(str(doc['provider']).replace('\n', '<br />\n'))
            f.write("<br />\n")
            f.write("</p>\n")
            f.write("<hr />\n")
            f.write("<p>\n")
            if not(isShort):
                f.write("本项目文件名较长，下载时请注意存放路径，以免发生无法下载的情况。<br />\nPlease be mindful of long paths in this torrent to avoid download error. <br />\n")
                f.write("<br />\n")
            f.write(pubrest_bt_new)
            with open("./content/screenshot_html.txt", 'r', encoding='utf8') as s:
                f.write(s.read())
        # 重发
        else:
            f.write("<p>\n")
            f.write("重发修正：<br />\n")
            with open("./content/rs_chn.txt", 'r', encoding='utf8') as s:
                f.write(s.read().replace('\n', '<br />\n'))
            f.write("<br />\n")
            f.write("Reseed comment:<br />\n")
            with open("./content/rs_eng.txt", 'r', encoding='utf8') as s:
                f.write(s.read().replace('\n', '<br />\n'))
            f.write("<br />\n")
            f.write("</p>\n")
            f.write("<hr />\n")
            f.write("<p>\n")
            f.write("感谢所有资源提供者 / Thanks to all resource providers: <br />\n")
            f.write(str(doc['provider']).replace('\n', '<br />\n'))
            f.write(pubrest_bt_rs)

    # 生成发布内容-vcbs
    pubtitle_vcbs = str(doc['title_eng'] +" / "+ doc['title_chn'] +" "+ doc['spec']+" "+ doc['type'] +" ["+ doc['range'] + doc['mark'] + "Fin]")
    
    pubimg_1400="<img src=\"" + doc["img_1400"] +"\" alt=\"" + doc["img_1400"].split('/')[-1] + "\" /><br />"

    # 输出发布内容到文件-vcbs
    with open(doc["title_chn"]+"-VCBS.html", 'w', encoding='utf8') as f:
        f.write(pubtitle_vcbs +"\n\n")
        f.write(pubimg_1400 +"\n\n")
        if(doc['sub']):
            f.write("这个项目与 <strong>" + doc['sub'] + "</strong> 合作，感谢他们精心制作的字幕。\n")
        f.write("\n")
        with open("./content/process_chn.txt", 'r', encoding='utf8') as s:
                f.write(s.read())
        f.write("\n")

        if(doc['comment']!='\n'):
            f.write(doc['comment'])
            f.write("\n")
        if(check_pgs.get()):
            f.write("内封原盘 ENG + JPN 字幕。\n")
            f.write("\n")
        if(check_ct.get()):
            f.write("内封评论音轨。\n")
            f.write("\n")
        if(check_ctc.get()):
            f.write("部分剧集内封评论音轨。\n")
            f.write("\n")
        if(check_mka.get()):
            f.write("外挂 FLAC 5.1 + Headphone X。\n")
            f.write("\n")

        f.write("<!--more-->\n\n")

        if(isRS):
            f.write("[box style=\"info\"]\n重发修正：\n")
            f.write("\n")
            with open("./content/rs_chn.txt", 'r', encoding='utf8') as s:
                f.write(s.read())
            f.write("[/box]\n")
            f.write("\n")

        f.write("[box style=\"download\"]\n")
        f.write(doc['spec'])
        if(doc['mark']):
            f.write(" ("+doc['mark']+")")
        f.write("\n")
        f.write("\n")
        f.write("<a href=\""+ doc['link1'] +"\" rel=\"noopener\" target=\"_blank\">"+ doc['link1'] +"</a>\n")
        f.write("\n")
        f.write("<a href=\""+ doc['link2'] +"\" rel=\"noopener\" target=\"_blank\">"+ doc['link2'] +"</a>\n")
        f.write("\n")
        f.write("<a href=\""+ doc['link3'] +"\" rel=\"noopener\" target=\"_blank\">"+ doc['link3'] +"</a>\n")
        f.write("\n")
        f.write("<a href=\""+ doc['link4'] +"\" rel=\"noopener\" target=\"_blank\">"+ doc['link4'] +"</a>\n")
        f.write("\n")
        f.write("<a href=\""+ doc['link5'] +"\" rel=\"noopener\" target=\"_blank\">"+ doc['link5'] +"</a>\n")
        f.write("\n")
        f.write("<a href=\""+ doc['link6'] +"\" rel=\"noopener\" target=\"_blank\">"+ doc['link6'] +"</a>\n")
        f.write("[/box]\n")
        f.write("\n")
        # f.write("<hr />\n")

        f.write("<label for=\"medie-info-switch\" class=\"btn btn-inverse-primary\" title=\"展开MediaInfo\">MediaInfo</label>\n")
        f.write("\n")
        f.write("<pre class=\"js-medie-info-detail medie-info-detail\" style=\"display: none;\">")
        with open("./content/mediainfo.txt", 'r', encoding='utf8') as s:
            f.write(s.read())
        f.write("</pre>\n")
    root.destroy()

# 创建按钮
b_generate = tk.Button(root, text="生成", width=EWIDTH, command=btn_click_generate)
b_generate.grid(row=MAXROW, column=1, columnspan=4, sticky='nw')

# 启动主循环
root.mainloop()
