# VCB-S-generate-pubfile
 creat bangumi.html, vcb-s.html, nyaa.md for VCB-S project publishing

## usage
将说明性内容写入同文件夹对应 txt 文件中，程序读取文件，生成并写入最终的发布文件。
- process_chn/eng.txt 画质吐槽 中 / 英
- rs_chn/eng.txt 重发修正 中 / 英
- screenshot_html/md.txt 截图链接 html / md
- mediainfo.txt

## changelog
- v0.3
  - 基本界面设计，功能验证
  - 生成发布文件-bt
  - 生成发布文件-主站
- v1.2
  - 改用外置 txt 文件编辑、存取相应文本信息
  - 整理文件结构，文本信息放入单独文件夹 info
- v2.1
  - 整理程序结构，在 util 文件夹中以 data.py 存储数据，func.py 存储函数
  - 调整界面设计