import os
from util.data import *

# 定义函数-打开文件，若不存在则创建
def open_text_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding='utf8') as f:
            pass
    
    os.system(f"notepad.exe {filepath}")
    return

# 输出发布内容-bt
def pubfile_bt(doc):
    isShort = (len(doc['title_eng']) < THTITLE)

    # 生成发布内容-bt
    if(doc['sub']):
        pubgroup = "["+ '&'.join(doc['sub']) +"&VCB-Studio] "
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

    with open(doc["title_chn"]+"-BANGUMI.html", 'w', encoding='utf8') as f:
        f.write(pubtitle_bt +"\n")
        f.write("<p>\n")
        f.write(pubimg_800 +"\n")
        f.write("<br />\n")
        f.write(pubtitle_content +"\n")
        f.write("<br />\n")
        if(doc['isPGS']):
            f.write("内封原盘 ENG + JPN 字幕。<br /> \nEmbedded official ENG + JPN PGS.<br />\n")
            f.write("<br />\n")
        if(doc['isCT']):
            f.write("内封评论音轨。<br />\nEmbedded commentary track.<br />\n")
            f.write("<br />\n")
        if(doc['isCTC']):
            f.write("部分剧集内封评论音轨。<br />\nCertain episodes contain commentary tracks.<br />\n")
            f.write("<br />\n")
        if(doc['isMKA']):
            f.write("外挂 FLAC 5.1 + Headphone X。<br />\nMKA contains FLAC 5.1 + Headphone X.<br />\n")
            f.write("<br />\n")
        if(doc['sub']):
            f.write("这个项目与 <strong>"+ ' & '.join(doc['sub']) +"</strong> 合作，感谢他们精心制作的字幕。<br />\n")
            f.write("This project is in collaboration with <strong>"+ ' & '.join([SUB[i] for i in doc['sub']]) +"</strong>. Thanks to them for elaborating Chinese subtitles.<br />\n")
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
        if not(doc['isRS']):
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
            with open("./content/screenshot.txt", 'r', encoding='utf8') as s:
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

    return

# 输出发布内容-vcbs
def pubfile_vcbs(doc):
    # 生成发布内容-vcbs
    pubtitle_vcbs = str(doc['title_eng'] +" / "+ doc['title_chn'] +" "+ doc['spec']+" "+ doc['type'] +" ["+ doc['range'] + doc['mark'] + "Fin]")
    
    pubimg_1400="<img src=\"" + doc["img_1400"] +"\" alt=\"" + doc["img_1400"].split('/')[-1] + "\" /><br />"

    # 输出发布内容到文件-vcbs
    with open(doc["title_chn"]+"-VCBS.html", 'w', encoding='utf8') as f:
        f.write(pubtitle_vcbs +"\n\n")
        f.write(pubimg_1400 +"\n\n")
        if(doc['sub']):
            f.write("这个项目与 <strong>" + ' & '.join(doc['sub']) + "</strong> 合作，感谢他们精心制作的字幕。\n")
        f.write("\n")
        with open("./content/process_chn.txt", 'r', encoding='utf8') as s:
                f.write(s.read())
        f.write("\n")

        if(doc['comment']!='\n'):
            f.write(doc['comment'])
            f.write("\n")
        if(doc['isPGS']):
            f.write("内封原盘 ENG + JPN 字幕。\n")
            f.write("\n")
        if(doc['isCT']):
            f.write("内封评论音轨。\n")
            f.write("\n")
        if(doc['isCTC']):
            f.write("部分剧集内封评论音轨。\n")
            f.write("\n")
        if(doc['isMKA']):
            f.write("外挂 FLAC 5.1 + Headphone X。\n")
            f.write("\n")

        f.write("<!--more-->\n\n")

        if(doc['isRS']):
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
    return


