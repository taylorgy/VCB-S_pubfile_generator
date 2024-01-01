WINDOW = '700x800'
THTITLE = 25
EWIDTH = 20
EWIDTH2 = int(2*EWIDTH)
EWIDTH4 = int(4*EWIDTH+2)

LINK = {
    "bangumi": "https://bangumi.moe/torrent/xxxxxxxx",
    "s.acgnx": "https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html",
    "acgnx": "https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html",
    "acgrip": "https://acg.rip/t/xxxxxx",
    "dmhy": "https://share.dmhy.org/topics/view/xxxxxx.html",
    "nyaa": "https://nyaa.si/view/xxxxxx"
    }
LENLINK = len(LINK)

DOC = dict()
DOC['sub'] = []
DOC['title_chn'] = "测试中文标题"
DOC['title_eng'] = ""
DOC['title_jpn'] = ""
DOC['spec'] = "10-bit 1080p HEVC"
DOC['type'] = "BDRip"
DOC['range'] = ""
DOC['mark'] = ""
DOC['img_800'] = "_800.webp"
# DOC['img_1400'] = "_1400.webp"
DOC['comment'] = ""
DOC['provider'] = "BD: \nScans: \nCDs: "
DOC['links'] = list(LINK.values())
DOC['isRS'] = 0
DOC['isPGS'] = 0
DOC['isCT'] = 0
DOC['isCTC'] = 0
DOC['isMKA'] = 0

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