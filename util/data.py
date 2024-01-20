MYFOLDER = "E:\\[media]\\anime" # 实际文件路径

# 界面布局相关参数
WINDOW = '700x800'          # 窗口大小
EWIDTH = 20                 # 单位宽度
EWIDTH2 = int(2*EWIDTH)     # 2 单位宽度
EWIDTH4 = int(4*EWIDTH+2)   # 4 单位宽度，+2 是为了布局对齐

# bt站：默认发布链接，此处修改可以直接影响界面
LINK = {
    "bangumi": "https://bangumi.moe/torrent/xxxxxxxx",
    "s.acgnx": "https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html",
    "acgnx": "https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html",
    "acgrip": "https://acg.rip/t/xxxxxx",
    "dmhy": "https://share.dmhy.org/topics/view/xxxxxx.html",
    "nyaa": "https://nyaa.si/view/xxxxxx"
    }
LENLINK = len(LINK) # bt站数量

THTITLE = 30 # 长标题阈值，英文标题长度大于此数值则判定为长标题

# 发布内容字典，连通界面、后端、xml 的媒介
DOC = dict()
DOC['sub'] = []                             # 字幕组列表
DOC['title_chn'] = "测试中文标题"            # 标题-中文
DOC['title_eng'] = ""                       # 标题-英文
DOC['title_jpn'] = ""                       # 标题-日文
DOC['spec'] = "10-bit 1080p HEVC"           # 规格
DOC['type'] = "BDRip"                       # 类型 DVDRip / WebRip / TVRip (格式自由)
DOC['range'] = ""                           # 内容 TV S1 / Movie / TV S2 + OVA (格式自由)
DOC['mark'] = ""                            # 标记 Reseed / Rev
DOC['img_800'] = "_800.webp"                # 发布图-bt
DOC['img_1400'] = ""                        # 发布图-vcbs 输入 pixiv 链接自动获取作者生成 image credit
DOC['comment'] = ""                         # 吐槽
DOC['provider'] = "BD: \nScans: \nCDs: "    # 感谢
DOC['links'] = list(LINK.values())          # 发布链接
DOC['isRS'] = 0                             # 是否 重发
DOC['isPGS'] = 0                            # 是否 内封原盘 ENG + JPN 字幕
DOC['isCT'] = 0                             # 是否 内封评论音轨
DOC['isCTC'] = 0                            # 是否 部分剧集内封评论音轨
DOC['isMKA'] = 0                            # 是否 外挂 FLAC 5.1 + Headphone X

# 字幕组中文名：英文名
SUB = {
    '千夏字幕组': 'Airota',
    '喵萌奶茶屋': 'Nekomoe kissaten',
    '悠哈璃羽字幕社': 'UHA-WINGS',
    '诸神字幕组': 'Kamigami',
    '天香字幕社': 'T.H.X',
    '动漫国字幕组': 'DMG',
    '星空字幕组': 'XKsub',
    '茉语星梦': 'MakariHoshiyume',
    '风之圣殿': 'FZSD',
    '白恋字幕组': 'Shirokoi',
    'SweetSub': 'SweetSub',
    '喵萌Production': 'Nekomoe kissaten',
    '豌豆字幕组': 'BeanSub'
    }

# 发布默认内容-bt站-新番
pubrest_bt_new = '''
VCB-Studio 已不再保证收集作品相关 CD 和扫图资源，详情请参见 <a href="https://vcb-s.com/archives/14331">https://vcb-s.com/archives/14331</a>。<br />
Please refer to <a href="https://vcb-s.com/archives/14331">https://vcb-s.com/archives/14331</a> for more information about that VCB-Studio will no longer guarantee to include relevant CDs and scans.<br />
<br />
本组（不）定期招募新成员。详情请参见 <a href="https://vcb-s.com/archives/16986">https://vcb-s.com/archives/16986</a>。<br />
Please refer to <a href="https://vcb-s.com/archives/16986">https://vcb-s.com/archives/16986</a> about information of our (un)scheduled recruitment.<br />
<br />
播放器教程索引： <a href="https://vcb-s.com/archives/16639" target="_blank">VCB-Studio 播放器推荐</a><br />
中文字幕分享区： <a href="https://bbs.acgrip.com/" target="_blank">Anime 分享论坛</a><br />
项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a><br />
特殊格式与说明： <a href="https://vcb-s.com/archives/7949" target="_blank">WebP 扫图说明</a><br />
<br />
</p>
<hr />
'''

# 发布默认内容-bt站-重发
pubrest_bt_rs = '''
<br />
</p>
<hr />
<p>
本次发布来自 VCB-Studio 旧作重发计划。我们会不定期重发过去发布过的合集，或为补充做种，或为修正制作错漏，或为整合系列合集。<br />
This is a release of VCB-Studio Reseed Project. We would re-upload pervious torrents from time to time, to resurrect old torrents with few seeders, to correct errors/omissions, or to batch separate releases that belong to a same series. <br />
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