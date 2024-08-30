# python 3.10.6
# -*- coding: UTF-8 -*-

from util.data import *

import os
import re
import json
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import platform

def open_text_file(filepath: str) -> None:
    """ 打开文本文件，若不存在则创建。

    Args:
        filepath: 打开文件的路径，形如 "{filepath}/{filename}.txt"。
    """
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf8') as f:
            pass

    # 系统判断 windows / macos
    # curr_platform = platform.platform().lower()
    # if 'windows' in curr_platform:
    #     os.system(f"notepad.exe {filepath}")
    # elif 'macos' in curr_platform:
    #     os.system(f"open {filepath}")
    # else:
    #     print("其它系统暂不支持")

    curr_system = platform.system()
    if 'Windows' == curr_system:
        os.system(f"notepad.exe {filepath}")
    elif 'Darwin' == curr_system:
        os.system(f"open {filepath}")
    else:
        print("其它系统暂不支持")

    with open(filepath, 'r+', encoding='utf8') as f:
        lines = f.read()
        # 文本末行若不为空行则添加
        if lines and lines[-1] != '\n':
            f.write("\n")
            # 文本预处理
            # mediainfo.txt 文件路径替换为 "D:\SAYA IS ∞ LOLICON!"
            if filepath == "./content/mediainfo.txt":
                pattern = re.compile(r"(?<=(Complete name\s{28}:\s)).*(?=(\\\[))")
                repl = r"D:\\SAYA IS ∞ LOLICON!"
                f.seek(0)
                f.truncate()
                f.write(re.sub(pattern, repl, lines, count=1))
                return
            # process_chn.txt | rs_chn.txt 中英文之间添加空格
            if filepath == "./content/process_chn.txt" or "./content/rs_chn.txt":
                pattern_zh_en = re.compile(r'([\u4e00-\u9fa5]+)([a-zA-Z0-9]+)')
                pattern_en_zh = re.compile(r'([a-zA-Z0-9]+)([\u4e00-\u9fa5]+)')
                f.seek(0)
                f.truncate()
                lines = re.sub(pattern_zh_en, r'\1 \2', lines)
                lines = re.sub(pattern_en_zh, r'\1 \2', lines)
                f.write(lines)
                return



def save_dict_to_json(dictionary: dict, filename: str) -> None:
    """ 将字典变量保存为 json 文件。
    
    Args:
        dictionary: 字典变量。
        filename: 保存的 xml 文件路径，形如 "{filepath}/{filename}.xml"。
    """
    with open(filename, 'w', encoding='utf8') as file:
        file.write(json.dumps(dictionary))

def load_json_to_dict(filename: str) -> dict:
    """ 读取 json 文件并转换为字典变量。
    Args: 
        filename: 保存的 xml 文件路径，形如 "{filepath}/{filename}.xml"。

    Returns:
        转换后的字典变量。
    """
    with open(filename, 'r', encoding='utf8') as file:
        return json.load(file)
    
def member_str_to_dict(member_str: str) -> dict:
    """ 将文本框输入的成员字符串转换为字典。
    Args: 
        member_str: 成员字符串，来自 DOC['member']，形如 "- 总监: aaa\n- 压制: bbb\n- 整理: ccc\n- 发布: ddd"。

    Returns:
        转换后的成员字典，形如 {'总监':'aaa', '压制':'bbb', '整理':'ccc', '发布':'ddd'}
    """
    # return {member.split(r'[:：]')[0].strip():member.split(r'[:：]')[1].strip() for member in member_str.splitlines()}
    return {re.split(r'[:：]', member)[0].strip()[2:]:re.split(r'[:：]', member)[1].strip() for member in member_str.splitlines()}

    # member_dict = dict()
    # for member in member_str.splitlines():
    #     title, name = member.split(': ')
    #     member_dict.update({title: name})
    # return member_dict

def pubfile_bt(doc: dict) -> None:
    """ 生成并保存发布内容-bt
    
    Args:
        doc: 保存发布内容的字典变量
    """
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
        
    filename = re.search(r'^[^\s\\/:*?"<>|]+', doc["title_chn"]).group(0)

    member = member_str_to_dict(doc['member'])

    with open(filename+"-bangumi.html", 'w', encoding='utf8') as f:
        f.write(pubtitle_bt +"\n\n")
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
            f.write("感谢所有参与制作者 / Thanks to our participating members: <br />\n")
            f.write(f"总监 / Script: {member['总监']}<br />\n")
            f.write(f"压制 / Encode: {member['压制']}<br />\n")
            f.write(f"整理 / Collate: {member['整理']}<br />\n")
            f.write(f"发布 / Upload: {member['发布']}<br />\n")
            f.write("分流 / Seed: VCB-Studio CDN 分流成员<br />\n")
            f.write("<br />\n")
            if(doc['provider'] != "\n"):
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
            f.write("感谢所有参与制作者 / Thanks to our participating members: <br />\n")
            f.write(f"总监 / Script: {member['总监']}<br />\n")
            f.write(f"压制 / Encode: {member['压制']}<br />\n")
            f.write(f"整理 / Collate: {member['整理']}<br />\n")
            f.write(f"发布 / Upload: {member['发布']}<br />\n")
            f.write("分流 / Seed: VCB-Studio CDN 分流成员<br />\n")
            f.write("<br />\n")
            if(doc['provider'] != "\n"):
                f.write("感谢所有资源提供者 / Thanks to all resource providers: <br />\n")
                f.write(str(doc['provider']).replace('\n', '<br />\n'))
                f.write("<br />\n")
            f.write(pubrest_bt_rs)

    return

def get_img_author(url: str) -> str:
    """ 解析图片网址，获取图片作者。
        支持的网站：pixiv，zerochan。

    Args:
        url: 图片网址，形如 "https://www.pixiv.net/artworks/xxxxxxxxx"
                           "https://www.zerochan.net/xxxxxxx"

    Returns:
        img_author: 图片作者。
    """
    # 支持的网站
    SUPPORTED = ['pixiv', 'zerochan']
    # User-Agent 请求头，告诉服务器，请求来自一个运行在 Windows 10 64 位版本的 Chrome 104 浏览器。
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    img_author = 'Unknown Author'
    # 判断输入的网站
    website = urlparse(url).netloc.split('.')[1]
    if website in SUPPORTED:
        # 发送HTTP请求并获取页面内容
        response = requests.get(url=url, headers=headers)
        # 检查请求是否成功
        if response.status_code == 200:
            # 使用 BeautifulSoup 解析 HTML 内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # pixiv 参考 /ref/soup-pixiv.html，lang="ja"
            if website == SUPPORTED[0]:
                # <title> 中含有作者信息，特征为 - {img_author}のイラスト
                img_author = re.search(r'- (.*?)の', str(soup.head.title)).group(1)
            # zerochan 参考 /ref/soup-zerochan.html
            elif website == SUPPORTED[1]:
                # 
                # <title> 中含有作者信息，特征为 by {img_author} #xxxx
                img_author = re.search(r'by (.*?) #', str(soup.head.title)).group(1)

        # 请求失败
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    else:
        print("该网址暂时无法解析，请等待后续版本更新。")

    return img_author

def pubfile_vcbs(doc: dict) -> None:
    """ 生成并保存发布内容-vcbs
    
    Args:
        doc: 保存发布内容的字典变量
    """
    # 生成发布内容-vcbs
    # pubimg_1400="<img src=\"" + doc["img_1400"] +"\" alt=\"" + doc["img_1400"].split('/')[-1] + "\" /><br />"

    pubtitle_vcbs = f"{doc['title_eng']} / {doc['title_chn']} {doc['spec']} {doc['type']} [{doc['range']}{doc['mark']}Fin]"

    member = member_str_to_dict(doc['member'])

    # 输出发布内容到文件-vcbs
    # filename = re.search(r'([\u4e00-\u9fa5]+)', doc["title_chn"]).group(1)
    filename = re.search(r'^[^\s\\/:*?"<>|]+', doc["title_chn"]).group(0)
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

        f.write("感谢所有参与制作者：\n")
        f.write(f"总监：{member['总监']}\n")
        f.write(f"压制：{member['压制']}\n")
        f.write(f"整理：{member['整理']}\n")
        f.write(f"发布：{member['发布']}\n")
        f.write("分流：VCB-Studio CDN 分流成员\n")
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

        if doc['img_1400']:
            # img_author = 'author'
            f.write(f"Image Credit: <a href=\"{doc['img_1400']}\" rel=\"noopener\" target=\"_blank\">{get_img_author(doc['img_1400'])}</a>\n")
            f.write("\n")
        f.write("<label for=\"medie-info-switch\" class=\"btn btn-inverse-primary\" title=\"展开MediaInfo\">MediaInfo</label>\n")
        f.write("\n")
        f.write("<pre class=\"js-medie-info-detail medie-info-detail\" style=\"display: none;\">")
        with open("./content/mediainfo.txt", 'r', encoding='utf8') as s:
            # pattern = re.compile(r"(?<=(Complete name\s{28}:\s)).*(?=(\\\[))")
            # repl = r"D:\\SAYA IS ∞ LOLICON!"
            # f.write(re.sub(pattern, repl, s.read(), count=1))
            f.write(s.read())
        f.write("</pre>\n")
    return
