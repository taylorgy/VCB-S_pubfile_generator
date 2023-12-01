from util.data import *

import os
import re
import xml.etree.ElementTree as ET

# 定义函数-打开文件，若不存在则创建
def open_text_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf8') as f:
            pass
    os.system(f"notepad.exe {filepath}")
    with open(filepath, 'a+', encoding='utf8') as f:
        f.seek(0)
        lines = f.readlines()
        if lines and lines[-1][-1] != '\n':
            f.write("\n")
    return

# 将字典转换为 XML 元素
def dict_to_xml(dictionary, parent=None):
    if parent is None:
        parent = ET.Element('root')

    for key, value in dictionary.items():
        if isinstance(value, dict):
            dict_to_xml(value, ET.SubElement(parent, key))
        else:
            ET.SubElement(parent, key).text = str(value)

    return parent

# 将字典保存为 XML 文件
def save_dict_to_xml(dictionary, filename):
    root = dict_to_xml(dictionary)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

# 将 XML元素转换为字典
def xml_to_dict(element):
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result

# 将 XML 文件内容转换为字典
def load_xml_to_dict(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return xml_to_dict(root)

# 输出发布内容-bt
def pubfile_bt(doc):
    isShort = (len(doc['title_eng']) < THTITLE)

    # 生成发布内容-bt
    pubimg_800 = f"<img src=\"{doc['img_800']}\" alt=\"{doc['img_800'].split('/')[-1]}\" /><br />"

    if(doc['sub']):
        pubgroup = f"[{'&'.join(doc['sub'])}&VCB-Studio] "
    else:
        pubgroup = "[VCB-Studio] "

    if(isShort):
        pubtitle_bt = f"{pubgroup}{doc['title_chn']} / {doc['title_eng']} / {doc['title_jpn']} {doc['spec']} {doc['type']} [{doc['range']}{doc['mark']}Fin]"
        pubtitle_content = f"{doc['title_chn']} / {doc['title_eng']} / {doc['title_jpn']} {doc['range']}{doc['type']} {doc['mark']}<br />"
    else:
        pubtitle_bt = f"{pubgroup}{doc['title_chn']} / {doc['title_eng']} {doc['spec']} {doc['type']} [{doc['range']}{doc['mark']}Fin]"
        pubtitle_content = \
            f"{doc['title_chn']} {doc['range']}{doc['type']} {doc['mark']}<br />\n" +\
            f"{doc['title_eng']} {doc['range']}{doc['type']} {doc['mark']}<br />\n" +\
            f"{doc['title_jpn']} {doc['range']}{doc['type']} {doc['mark']}<br />"
        
    filename = re.search(r'([\u4e00-\u9fa5]+)', doc["title_chn"]).group(1)
    with open(filename+"-bangumi.html", 'w', encoding='utf8') as f:
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
            f.write(f"这个项目与 <strong>{' & '.join(doc['sub'])}</strong> 合作，感谢他们精心制作的字幕。<br />\n")
            f.write(f"This project is in collaboration with <strong>{' & '.join([SUB[i] for i in doc['sub']])}</strong>. Thanks to them for elaborating Chinese subtitles.<br />\n")
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
    # pubimg_1400="<img src=\"" + doc["img_1400"] +"\" alt=\"" + doc["img_1400"].split('/')[-1] + "\" /><br />"

    pubtitle_vcbs = f"{doc['title_eng']} / {doc['title_chn']} {doc['spec']} {doc['type']} [{doc['range']}{doc['mark']}Fin]"

    # 输出发布内容到文件-vcbs
    filename = re.search(r'([\u4e00-\u9fa5]+)', doc["title_chn"]).group(1)
    with open(filename+"-vcbs.html", 'w', encoding='utf8') as f:
        f.write(pubtitle_vcbs +"\n\n")
        # f.write(pubimg_1400 +"\n\n")
        if(doc['sub']):
            f.write(f"这个项目与 <strong>{' & '.join(doc['sub'])}</strong> 合作，感谢他们精心制作的字幕。\n")
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
        if doc['range'] or doc['mark']:
            f.write(f" ({doc['range']}{doc['mark']}"[:-1] +")")
        f.write("\n")
        f.write("\n")
        for i in range(LENLINK):
            link = doc['links'][i].rstrip('\n')
            f.write(f"<a href=\"{link}\" rel=\"noopener\" target=\"_blank\">{link}</a>\n")
            if (i < LENLINK-1):
                f.write("\n")
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


