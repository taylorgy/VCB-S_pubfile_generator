$(document).ready(function () {
  $('#member').val("- 总监: \n- 压制: \n- 整理: \n- 发布: ");
  $('#link-sync').attr('placeholder', "AcgnX: https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html\nAcgnX INT: https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html\nACG.RIP: https://acg.rip/t/xxxxxx\nDMHY: http://share.dmhy.org/topics/view/xxxxxx.html");

  var subs_json;
  var subs;
  var added_subs = [];

  $.getJSON("./static/data/subs.json", function (data) {
    subs_json = data;
    // subs_chn = Object.keys(subs).join('');
    // subs_eng = Object.values(subs).join('');
    subs = Object.keys(subs_json);
  });

  // 按钮方法-添加字幕组
  $('#btn-sub-add').on('click', function () {
    const sub_selector = $('<select>', {
      class: 'sub-selector',
      // id: `sub${num_sub}`
    });

    // sub_selector.append($('<option>', { value: '', text: '--请选择--' }));
    subs.forEach(sub => {
      sub_selector.append($('<option>', { value: sub, text: sub }));
    });
    sub_selector.append($('<option>', { value: 'remove', text: '--删除此项--' }));

    $('.input-subs').append(sub_selector);

    update_sub_selectors();

    // 字幕组选项更新
    sub_selector.on('change', function () {
      if ($(this).val() === 'remove') {
        $(this).remove();
      }
      update_sub_selectors();
    });

  });

  function update_sub_selectors() {
    // 判断字幕组数量以禁用添加按钮
    if ($('.sub-selector').length < subs.length) {
      $('#btn-sub-add').prop('disabled', false);
    } else {
      $('#btn-sub-add').prop('disabled', true);
    }

    // 统计所有已添加的字幕组
    added_subs = [];
    $('.sub-selector').each(function () {
      let value = $(this).val();
      if (value && value !== 'remove') {
        // 自动调整重复的字幕组
        if (added_subs.includes(value)) {
          value = subs.find(sub => !added_subs.includes(sub));
          $(this).val(value);
        }
        added_subs.push(value);
      }
    });

    // 在选项中隐藏已添加的字幕组
    $('.sub-selector').each(function () {
      const selected_sub = $(this).val();
      // 遍历当前选择框中的每一个选项
      $(this).find('option').each(function () {
        const value = $(this).val();
        if (value && value !== selected_sub && value !== 'remove') {
          if (added_subs.includes(value)) {
            $(this).hide();
          } else {
            $(this).show();
          }
        }
      });
    });
  }

  // 按钮方法-编辑
  var input_url = {
    "process-chn": "",
    "process-eng": "",
    "screenshot": "",
    "mediainfo": "",
    "rs-chn": "",
    "rs-eng": ""
  };

  let text_id = null;

  function save_input(id) {
    if (id != null) {
      let text = $('#input-textarea').val() + '\n';

      // 自动修改 mediainfo 的路径
      if (id == 'mediainfo') {
        const pattern = /(?<=(Complete name\s*:\s)).*(?=(\\\[))/g;
        const repl = "D:\\SAYA IS ∞ LOLICON!";
        text = text.replace(pattern, repl);
      }
      input_url[id] = text;
      id = null;
    }

  }

  $('.btn-edit').on('click', function () {
    $('.btn-edit').removeClass('active');
    $(this).addClass('active');
    $('.wrapper-input-textarea').removeClass('hidden');
    if ($(this).attr('id') != text_id) {
      save_input(text_id);
      text_id = $(this).attr('id');
      $('#input-textarea').val(input_url[text_id]);
    }
  });

  // 按钮方法-保存
  $('#btn-save').on('click', function () {
    save_input(text_id);
    $('.btn-edit').removeClass('active');
    $('.wrapper-input-textarea').addClass('hidden');
  });

  // 生成发布文档
  var template_bt = new Array;
  var template_vcbs = new Array;
  var pubfile_bt = new Array;
  var pubfile_vcbs = new Array;

  // 载入模板-bt
  $.ajax({
    url: "./static/data/template_bt.html",
    dataType: 'text',
    success: function (data) {
      // 按行拆分为数组
      template_bt = data.split('\n');
      // 为每行添加换行符
      template_bt = template_bt.map(line => line + '\n');
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert('加载JSON文件时出错：' + errorThrown);
    }
  });

  // 载入模板-vcbs
  $.ajax({
    url: "./static/data/template_vcbs.html",
    dataType: 'text',
    success: function (data) {
      // 按行拆分为数组
      template_vcbs = data.split('\n');
      // 为每行添加换行符
      template_vcbs = template_vcbs.map(line => line + '\n');
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert('加载JSON文件时出错：' + errorThrown);
    }
  });

  // 当输入变化时，更新发布文件并预览
  $('.area-input, #btn-save').on('input change click', function () {
    generate_pubfiles();
    preview_pubfile();
  });

  // 更新预览
  function preview_pubfile() {
    let preview_content;
    if ($('#btn-file').is(':checked')) {
      preview_content = pubfile_vcbs.join('');
    } else {
      preview_content = pubfile_bt.join('');
    }
    $('#preview-edit').val(preview_content);
    $('#preview-show').html($('#preview-edit').val());
  }

  // 英文标题过长时自动判断为长标题
  $('#title-eng').on('input', function () {
    if ($('#title-eng').val().length > 30) {
      $('#check-longtitle').prop('checked', true);
    } else {
      $('#check-longtitle').prop('checked', false);
    }
  });

  // 重发选项
  $('#check-rs').on('change', function () {
    if ($('#check-rs').is(':checked')) {
      $('#mark').val("Reseed");
      $('.input-rs').removeClass('hidden');
    } else {
      $('#mark').val("");
      $('.input-rs').addClass('hidden');
    }
  });

  // 生成发布文件-bt
  var pubname = "";

  function generate_pubfiles() {
    // 初始化
    pubfile_bt = template_bt.slice(0, 6);
    pubfile_vcbs = template_vcbs.slice(0);
    // pubfile_vcbs = template_vcbs;
    // 以上写法会直接赋值指针（地址），修改 pubfile_vcb 时相当于修改 template_vcbs

    // 获取输入
    const check_longtitle = $('#check-longtitle').is(':checked'); // 长标题标志
    const check_rs = $('#check-rs').is(':checked'); // 长标题标志

    const title_chn = $('#title-chn').val();
    const title_eng = $('#title-eng').val();
    const title_jpn = $('#title-jpn').val();
    const spec = $('#spec').val();
    const type = $('#type').val();
    const range = $('#range').val() && $('#range').val() + ' ';
    const mark = $('#mark').val() && $('#mark').val() + ' ';
    const comment = $('#comment').val() && $('#comment').val() + '\n';
    const member = member_str_to_dict($('#member').val());
    const provider = $('#provider').val() && $('#provider').val() + '\n';

    // 字幕组
    let pubgroup;
    if (added_subs.length) {
      pubgroup = `[${added_subs.join('&')}&VCB-Studio]`;
    }
    else {
      pubgroup = "[VCB-Studio]"
    }

    // 发布标题
    pubname = title_chn && title_chn.match(/^[^\s\\/:*?"<>|]+/);

    let pubtitle_bt;
    let pubtitle_content;

    if (!check_longtitle) {
      pubtitle_bt = `${pubgroup} ${title_chn} / ${title_eng} / ${title_jpn} ${spec} ${type} [${range}${mark}Fin]`;
      pubtitle_content = `${title_chn} / ${title_eng} / ${title_jpn} ${range}${type} ${mark}<br />`;
    } else {
      pubtitle_bt = `${pubgroup} ${title_chn} / ${title_eng} ${spec} ${type} [${range}${mark}Fin]`;
      pubtitle_content = `${title_chn} ${range}${type} ${mark}<br />\n` +
        `${title_eng} ${range}${type} ${mark}<br />\n` +
        `${title_jpn} ${range}${type} ${mark}<br />`;
    }

    pubfile_bt[0] = pubtitle_bt + '\n';
    pubfile_bt[2] = template_bt[2].replace(/{img_800}/g, $('#img-800').val());
    pubfile_bt[4] = pubtitle_content + '\n';

    pubfile_vcbs[0] = `${title_eng} / ${title_chn} ${spec} ${type} [${range}${mark}Fin]\n`;

    let index = 6;
    let flag_br = false;

    // 标注字幕 音轨
    pubfile_bt[index] = "";
    if ($('#check-pgs').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(6, 8).join('');
      flag_br = true;
      console.log(template_vcbs[7]);
    } else {
      pubfile_vcbs[8] = "";
    }
    if ($('#check-ctc').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(8, 10).join('');
      flag_br = true;
    } else {
      pubfile_vcbs[9] = "";
    }
    if ($('#check-ct').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(10, 12).join('');
      flag_br = true;
    } else {
      pubfile_vcbs[10] = "";
    }
    if ($('#check-mka').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(12, 14).join('');
      flag_br = true;
    } else {
      pubfile_vcbs[11] = "";
    }
    if (flag_br) {
      pubfile_bt[index] += "<br />\n";
      index++;
      flag_br = false;
    } else {
      pubfile_vcbs[12] = "";
    }

    // 合作字幕组
    if (added_subs.length) {
      const sub_chn = added_subs.join(' & ');
      const content_sub_chn = template_bt[15].replace(/{sub_chn}/, sub_chn);
      const sub_eng = added_subs.map(sub => subs_json[sub]).join(' & ');
      const content_sub_eng = template_bt[16].replace(/{sub_eng}/, sub_eng);

      pubfile_bt[index] = content_sub_chn + content_sub_eng;
      pubfile_bt[index] += "<br />\n";
      index++;

      pubfile_vcbs[2] = template_vcbs[2].replace(/{sub_chn}/, sub_chn);;
    } else {
      pubfile_vcbs[2] = "";
      pubfile_vcbs[3] = "";
    }

    // 小作文
    pubfile_bt[index] = input_url['process-chn'].replace(/\n/g, '<br />\n');
    pubfile_bt[index] += input_url['process-eng'].replace(/\n/g, '<br />\n');
    pubfile_bt[index] += "<br />\n";
    index++;

    pubfile_vcbs[4] = input_url['process-chn'];

    // 吐槽
    if (comment) {
      pubfile_bt[index] = comment.replace(/\n/g, '<br />\n');
      pubfile_bt[index] += "<br />\n";
      index++;

      pubfile_vcbs[6] = comment;
    } else {
      pubfile_vcbs[6] = "";
      pubfile_vcbs[7] = "";
    }

    // 分段
    pubfile_bt[index] = template_bt.slice(22, 25).join('');
    index++;

    // 重发
    if (check_rs) {
      pubfile_bt[index] = template_bt[25];
      pubfile_bt[index] += input_url['rs-chn'].replace(/\n/g, '<br />\n');
      pubfile_bt[index] += template_bt.slice(27, 29).join('');
      pubfile_bt[index] += input_url['rs-eng'].replace(/\n/g, '<br />\n');
      pubfile_bt[index] += template_bt.slice(30, 32).join('');
      index++;

      pubfile_vcbs[18] = input_url['rs-chn'];
    } else {
      pubfile_vcbs.fill("", 15, 21);
    }
    // 感谢-成员
    pubfile_bt[index] = template_bt[33];
    pubfile_bt[index] += template_bt[34].replace(/{member_script}/, member['总监']);
    pubfile_bt[index] += template_bt[35].replace(/{member_encode}/, member['压制']);
    pubfile_bt[index] += template_bt[36].replace(/{member_collate}/, member['整理']);
    pubfile_bt[index] += template_bt[37].replace(/{member_upload}/, member['发布']);
    pubfile_bt[index] += template_bt.slice(38, 40).join('');
    index++;

    // 感谢-资源提供
    if (provider) {
      pubfile_bt[index] = template_bt[40];
      pubfile_bt[index] += provider.replace(/\n/g, '<br />\n');
      pubfile_bt[index] += "<br />\n";
      index++;
    }

    // 分段
    pubfile_bt[index] = template_bt.slice(43, 46).join('');
    index++;

    // 声明-长标题
    if (check_longtitle) {
      pubfile_bt[index] = template_bt.slice(46, 49).join('');
      index++;
    }

    if (!check_rs) {
      // 声明-新番
      pubfile_bt[index] = template_bt.slice(49, 64).join('');
      index++;
      // 对比截图
      pubfile_bt[index] = input_url['screenshot'];
    } else {
      // 声明-重发
      pubfile_bt[index] = template_bt.slice(67, 79).join('');
    }

    // pubfile-vcbs 发布链接
    pubfile_vcbs[22] = `${spec}`;
    if (range || mark) {
      pubfile_vcbs[22] += ` (${range}${mark}`.trimEnd() + ')';
    }
    pubfile_vcbs[22] += '\n';

    var links = ["https://bangumi.moe/torrent/xxxxxxxx",
      "https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html",
      "https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html",
      "https://acg.rip/t/xxxxxx",
      "https://share.dmhy.org/topics/view/xxxxxx.html",
      "https://nyaa.si/view/xxxxxx"]

    links[0] = $('#link-bangumi').val() || links[0];
    links[5] = $('#link-nyaa').val() || links[5];

    let link_sync = $('#link-sync').val().split('\n');
    if (link_sync.length > 1) {
      for (let i = 0; i < link_sync.length; i++) {
        links[1 + i] = link_sync[i].split(': ')[1];
      }
    }

    pubfile_vcbs[24] = template_vcbs[24].replace(/{link_bangumi}/g, links[0]);
    pubfile_vcbs[26] = template_vcbs[26].replace(/{link_sacgnx}/g, links[1]);
    pubfile_vcbs[28] = template_vcbs[28].replace(/{link_acgnx}/g, links[2]);
    pubfile_vcbs[30] = template_vcbs[30].replace(/{link_acgrip}/g, links[3]);
    pubfile_vcbs[32] = template_vcbs[32].replace(/{link_dmhy}/g, links[4]);
    pubfile_vcbs[34] = template_vcbs[34].replace(/{link_nyaa}/g, links[5]);

    // pubfile-vcbs mediainfo
    pubfile_vcbs[39] = template_vcbs[39].replace(/{mediainfo}/, input_url['mediainfo']);

  } // end of function generate_pubfiles();


  // 将输入的字符串转为字典形式
  // 这里主要针对成员感谢，可无视输入的前后顺序，增加程序健壮性。
  function member_str_to_dict(str) {
    let dict = {};
    str.split('\n').forEach(line => {
      if (/^-\s/.test(line)) {
        line = line.replace(/^-\s/, '');
      }
      let [key, value] = line.split(/[:：]/).map(item => item.trim()); // 分割每一行并去除首尾空格
      dict[key] = value; // 将键值对添加到字典对象中
    });
    return dict;
  }

  // 调整左右界面宽度
  let resizing_middle = false;
  $('.divider-middle').mousedown(function (e) {
    resizing_middle = true;
    $(document).mousemove(resize_middle);
    $(document).mouseup(resize_stop_middle);
  });

  function resize_middle(e) {
    if (resizing_middle) {
      const containerRect = $('.wrapper-content').get(0).getBoundingClientRect();
      const leftWidth = e.clientX - containerRect.left;
      const rightWidth = containerRect.width - leftWidth;
      $('.wrapper-input').width(leftWidth);
      $('.wrapper-preview').width(rightWidth);
    }
  }
  function resize_stop_middle() {
    resizing_middle = false;
    $(document).off('mousemove', resize_middle);
    $(document).off('mouseup', resize_stop_middle);
  }
  
  // 调整上下界面高度
  let resizing_bottom = false;
  $('.divider-bottom').mousedown(function (e) {
    resizing_bottom = true;
    $(document).mousemove(resize_bottom);
    $(document).mouseup(resize_stop_bottom);
  });

  function resize_bottom(e) {
    if (resizing_bottom) {
      $('.wrapper-content').height(e.clientY);
    }
  }
  
  function resize_stop_bottom() {
    resizing_bottom = false;
    $(document).off('mousemove', resize_bottom);
    $(document).off('mouseup', resize_stop_bottom);
  }

  // 按钮方法-预览
  $('#btn-preview').on('change', function () {
    if ($(this).is(':checked')) {
      // $('#preview-show').html($('#preview-edit').val());
      $('#preview-edit').addClass('hidden');
      $('#preview-show').removeClass('hidden');
    } else {
      $('#preview-edit').removeClass('hidden');
      $('#preview-show').addClass('hidden');
    }
  });

  // 按钮方法-文件
  $('#btn-file').on('change', function () {
    preview_pubfile();
  });

  // 按钮方法-生成
  $('#btn-download').click(function () {
    // 生成文件内容
    // pubfile_bt.push("测试生成按钮");
    var file_content = $('#preview-edit').val();

    // 创建一个 Blob 对象，并将文件内容放入其中
    var blob = new Blob([file_content], { type: "text/plain" });

    // 创建一个临时的 URL
    var url = window.URL.createObjectURL(blob);

    // 创建一个 <a> 元素，并设置其属性
    var a = $('<a>');
    a.attr('href', url);

    let filename = "default.html";
    if ($('#btn-file').is(':checked')) {
      filename = `${pubname}-vcbs.html`;
    } else {
      filename = `${pubname}-bangumi.html`
    }
    a.attr('download', filename);

    // 模拟点击 <a> 元素来下载文件
    $('body').append(a);
    a[0].click();

    // 删除临时的 URL 和 <a> 元素
    window.URL.revokeObjectURL(url);
    a.remove();
  });

});