$(document).ready(function () {
  $('#member').val("- 总监: \n- 压制: \n- 整理: \n- 发布: ");

  var subs_json;
  var subs;
  var added_subs;

  $.getJSON("./static/data/subs.json", function (data) {
    subs_json = data;
    // subs_chn = Object.keys(subs).join('\n');
    // subs_eng = Object.values(subs).join('\n');
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

  $('.btn-edit').on('click', function () {
    $('.btn-edit').removeClass('active');
    $(this).addClass('active');
    $('.wrapper-input-textarea').removeClass('hidden');
    if ($(this).attr('id') != text_id) {
      if (text_id != null) {
        input_url[text_id] = $('#input-textarea').val();
      }
      text_id = $(this).attr('id');
      $('#input-textarea').val(input_url[text_id]);
    }
  });

  // 按钮方法-保存
  $('#btn-save').on('click', function () {
    if (text_id != null) {
      input_url[text_id] = $('#input-textarea').val();
      text_id = null;
    }
    $('.btn-edit').removeClass('active');
    $('.wrapper-input-textarea').addClass('hidden');
  });

  // 生成发布文档
  var template_bt = new Array;
  var pubfile_bt = new Array;
  var pubfile_vcbs = new Array;

  // 载入模板-bt
  $.ajax({
    url: "./static/data/template_bt.html",
    dataType: 'text',
    success: function (data) {
      template_bt = data.split('\n');
      // template_bt[0] = "{pubtitle_bt}";
      // $('#preview-edit').val(pubfile_bt.join('\n'));
      // $('#preview-show').html($('#preview-edit').val());
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert('加载JSON文件时出错：' + errorThrown);
    }
  });

  // 当输入变化时，更新预览
  $('.area-input, #btn-save').on('input change click', function () {
    generate_pubfiles();
    $('#preview-edit').val(pubfile_bt.join('\n'));
    $('#preview-show').html($('#preview-edit').val());
  });

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
  var filename = "";

  function generate_pubfiles() {
    // 初始化
    pubfile_bt = template_bt.slice(0, 6);

    // 长标题标志
    const check_longtitle = $('#check-longtitle').is(':checked');

    // 字幕组
    let pubgroup;
    if (added_subs) {
      pubgroup = `[${added_subs.join('&')}&VCB-Studio]`;
    }
    else {
      pubgroup = "[VCB-Studio]"
    }

    // 获取输入
    const title_chn = $('#title-chn').val();
    const title_eng = $('#title-eng').val();
    const title_jpn = $('#title-jpn').val();
    const spec = $('#spec').val();
    const type = $('#type').val();
    const range = $('#range').val() && $('#range').val() + ' ';
    const mark = $('#mark').val() && $('#mark').val() + ' ';
    const comment = $('#comment').val();
    const member = member_str_to_dict($('#member').val());
    const provider = $('#provider').val();


    // 发布标题-bt
    filename = title_chn && title_chn.match(/^[^\s\\/:*?"<>|]+/);

    let pubtitle_bt;
    let pubtitle_content;

    if (!check_longtitle) {
      pubtitle_bt = `${pubgroup} ${title_chn} / ${title_eng} / ${title_jpn} ${spec} ${type} [${range}${mark}Fin]\n`
      pubtitle_content = `${title_chn} / ${title_eng} / ${title_jpn} ${range}${type} ${mark}<br />`;
    } else {
      pubtitle_bt = `${pubgroup} ${title_chn} / ${title_eng} ${spec} ${type} [${range}${mark}Fin]\n`
      pubtitle_content = `${title_chn} ${range}${type} ${mark}<br />\n` +
        `${title_eng} ${range}${type} ${mark}<br />\n` +
        `${title_jpn} ${range}${type} ${mark}<br />`
    }

    pubfile_bt[0] = pubtitle_bt;
    pubfile_bt[2] = template_bt[2].replace(/{img_800}/g, $('#img-800').val());
    pubfile_bt[4] = pubtitle_content;

    let index = 6;
    let flag_br = false;

    // 额外字幕 音轨
    pubfile_bt[index] = "";
    if ($('#check-pgs').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(6, 8).join('\n');
      flag_br = true;
    }
    if ($('#check-ctc').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(8, 10).join('\n');
      flag_br = true;
    }
    if ($('#check-ct').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(10, 12).join('\n');
      flag_br = true;
    }
    if ($('#check-mka').is(':checked')) {
      pubfile_bt[index] += template_bt.slice(12, 14).join('\n');
      flag_br = true;
    }
    if (flag_br) {
      pubfile_bt[index] += "<br />";
      index++;
      flag_br = false;
    }

    // 合作字幕组
    if (added_subs) {
      const sub_chn = added_subs.join(' & ');
      const content_sub_chn = template_bt[15].replace("{sub_chn}", sub_chn);
      const sub_eng = added_subs.map(sub => subs_json[sub]).join(' & ');
      const content_sub_eng = template_bt[16].replace("{sub_eng}", sub_eng);

      pubfile_bt[index] = content_sub_chn + content_sub_eng;
      pubfile_bt[index] += "<br />";
      index++;
    }

    // 小作文
    pubfile_bt[index] = input_url['process-chn'].replace('\n', '<br />\n') + '<br />\n';
    pubfile_bt[index] += input_url['process-eng'].replace('\n', '<br />\n') + '<br />\n';
    pubfile_bt[index] += "<br />";
    index++;

    // 吐槽
    if (comment) {
      pubfile_bt[index] = comment.replace('\n', '<br />\n') + '<br />\n';
      pubfile_bt[index] += "<br />";
      index++;
    }

    // 分段
    pubfile_bt[index] = template_bt.slice(22, 25).join('\n')
    index++;
    
    // 新番
    if (!$('#check-rs').is(':checked')) {
      // 感谢-成员
      pubfile_bt[index] = template_bt[25];
      pubfile_bt[index] += template_bt[26].replace("{member_script}", member['总监']);
      pubfile_bt[index] += template_bt[27].replace("{member_encode}", member['压制']);
      pubfile_bt[index] += template_bt[28].replace("{member_collate}", member['整理']);
      pubfile_bt[index] += template_bt[29].replace("{member_upload}", member['发布']);
      pubfile_bt[index] += template_bt.slice(30, 32).join('\n');
      index++;

      // 感谢-资源提供
      if(provider) {
        pubfile_bt[index] = template_bt[32];
        pubfile_bt[index] += provider.replace('\n', '<br />\n') + '<br />\n';
        pubfile_bt[index] += "<br />";
        index++;
      }

    // 分段
    pubfile_bt[index] = template_bt.slice(35, 38).join('\n')
    index++;
    if(check_longtitle) {
      pubfile_bt[index] = template_bt.slice(38, 41).join('\n')
      index++;
    }
    pubfile_bt[index] = template_bt.slice(41, 56).join('\n')
    index++;

    // 对比截图
    pubfile_bt[index] = input_url['screenshot'];
    } // 新番

  }

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
  let isResizing = false;
  $('.divider-middle').mousedown(function (e) {
    isResizing = true;
    $(document).mousemove(resize);
    $(document).mouseup(stopResize);
  });

  function resize(e) {
    if (isResizing) {
      const containerRect = $('.wrapper-content').get(0).getBoundingClientRect();
      const leftWidth = e.clientX - containerRect.left;
      const rightWidth = containerRect.width - leftWidth;
      $('.wrapper-input').width(leftWidth);
      $('.wrapper-preview').width(rightWidth);
    }
  }

  function stopResize() {
    isResizing = false;
    $(document).off('mousemove', resize);
    $(document).off('mouseup', stopResize);
  }

  // 按钮方法-预览
  $("#btn-preview").on('change', function () {
    if ($(this).is(':checked')) {
      $('#preview-show').html($('#preview-edit').val());
      $('#preview-edit').addClass('hidden');
      $('#preview-show').removeClass('hidden');
    } else {
      $('#preview-edit').removeClass('hidden');
      $('#preview-show').addClass('hidden');
    }
  });

  // 按钮方法-生成
  $("#btn-download").click(function () {
    // 获取输入框的内容

    // 生成文件内容
    // pubfile_bt.push("测试生成按钮");
    var file_content = $('#preview-edit').val();

    // 创建一个 Blob 对象，并将文件内容放入其中
    var blob = new Blob([file_content], { type: "text/plain" });

    // 创建一个临时的 URL
    var url = window.URL.createObjectURL(blob);

    // 创建一个 <a> 元素，并设置其属性
    var a = $("<a>");
    a.attr("href", url);
    a.attr("download", `${filename}-bangumi.html`);

    // 模拟点击 <a> 元素来下载文件
    $("body").append(a);
    a[0].click();

    // 删除临时的 URL 和 <a> 元素
    window.URL.revokeObjectURL(url);
    a.remove();
  });

});