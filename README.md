# VCB-S-generate-pubfile
 生成 VCB-S 发布文件 bangumi.html, vcb-s.html

## 功能
将说明性内容写入同文件夹对应 txt 文件中，程序读取文件，生成并写入最终的发布文件。
- process_chn/eng.txt 画质吐槽 中 / 英
- rs_chn/eng.txt 重发修正 中 / 英
- screenshot_html/md.txt 截图链接 html / md
- mediainfo.txt

## 更新
- v3.4
  - 引入 xml 保存上次编辑
  - 输入框焦点清空功能，改为右键双击触发
  - 修正中文名含有特殊字符时无法作为文件名的问题
  - 取消 img_1400 相关功能
- v2.6
  - 整理程序结构，在 util 文件夹中以 data.py 存储数据，func.py 存储函数
  - 调整界面设计，修改变量名称
  - 将字幕组输入改为选项模式
  - 更改文件类型为 pyw，并打包 exe 发布
  - 更新发布链接编辑与生成方式
  - 修正并优化输入框焦点清空问题，txt 末行空格问题
- v1.2
  - 改用外置 txt 文件编辑、存取相应文本信息
  - 整理文件结构，文本信息放入单独文件夹 info
- v0.3
  - 基本界面设计，功能验证
  - 生成发布文件-bt
  - 生成发布文件-主站
