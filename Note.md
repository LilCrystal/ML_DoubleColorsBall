## Notes


### python mysqldb

```Html
<div class="ygkj_wqkjgg dn">
<style>
  table {
    width: 1200px;
    border-right: 1px solid #e4dbdb;
    box-sizing: border-box;
    border-collapse: unset;
  }

  .ygkj-wjkjgg .table-hea {
    border: none;
    border-bottom: 1px solid #e4dbdb;
   }

  .ygkj-wjkjgg .table-hea .select {
    border: none;
  }

  .ygkj-wjkjgg .table tbody tr:nth-child(2n) td {
    background-color: #ffffff;
  }

  .ygkj-wjkjgg .table thead,
  .ssq_table tr,
  .kl8_table tr,
  .qlc_table tr,
  .fc3d_table tr {
    background-color: #ffffff;
  }

  .ygkj-wjkjgg .table tbody td {
    border-left: 1px solid #e4dbdb;
    border-bottom: 1px solid #e4dbdb;
  }

  .ygkj-wjkjgg .table tr th {
    font-weight: 500;
    text-align: center;
    border-left: 1px solid #e4dbdb;
    border-bottom: 1px solid #e4dbdb;
  }

  .kl8_table thead tr th,
  .fc3d_table thead tr th {
    padding: 13px 0;
  }

  .ygkj-wjkjgg .table-hea .select .select-type {
    width: 130px;
  }

  .ygkj-wjkjgg .table tbody .qiu .qiu-item {
    width: 25px;
    height: 29px;
    line-height: 29px;
    border-radius: none;
    margin-bottom: 0;
  }

  .play-fun {
    margin-left: 10px;
    padding-top: 5px;
    line-height: 32px;
  }

  .qiu-item-wqgg-zjhm-red {
    background: url(/img/ball/redCircle.png) no-repeat;
    background-size: 25px auto;
  }

  .qiu-item-wqgg-zjhm-blue {
    background: url(/img/ball/blueCircle.png) no-repeat;
    background-size: 25px auto;
  }

  .kl8-item-wqgg-zjhm-red {
    background: url(/img/kl8/kl8.png) no-repeat;
    background-size: 25px auto;
  }

  .wqgg-item-3D-zjhm-blue {
    background: url(/img/fc3d/fc3d.png) no-repeat;
    background-size: 25px auto;
  }

  .qlc-item-wqgg-zjhm-red {
    background: url(/img/qlc/orange.png) no-repeat;
    background-size: 25px auto;
   }

  .qlc-item-wqgg-zjhm-blue {
    background: url(/img/qlc/orange_dark.png) no-repeat;
    background-size: 25px auto;
  }
</style>
<div class="body-content ygkj-wjkjgg">
<div class="body-content-item">
<div class="table-hea">
<div class="select">
<div class="fl">
<select autocomplete="off" class="select-type gg-type" onchange="handleChangeType()" style="height: 35px">
<option value="ssq">åè²ç</option>
<option value="kl8">å¿«ä¹8</option>
<option value="3d">ç¦å½©3D</option>
<option value="qlc">ä¸ä¹å½©</option>
</select>
</div>
<div class="fl time">[ æ¯å¨äºãåãæ¥21:15å¼å¥ ]</div>
<div class="radio-btn" style="display: inline-block; vertical-align:top;padding: 0;">
<select autocomplete="off" class="select-type gg-date-type" onchange="handleChangeDate()" style="margin-left:20px;height: 35px;">
<option value="all">å¨é¨</option>
<option value="è¿30æ">è¿30æ</option>
<option value="è¿50æ">è¿50æ</option>
<option value="è¿100æ">è¿100æ</option>
</select>
<select autocomplete="off" class="select-type gg-week-type" onchange="handleChangeWeekDate()" style="margin-left:20px; height: 35px">
<option value="all">å¨é¨å¼å¥æ¥æ</option>
<option value="2">å¨äº</option>
<option value="4">å¨å</option>
<option value="0">å¨æ¥</option>
</select>
</div>
<div class="fl">
</div>
<div class="custom-search">
<div class="custom" onclick="handleShowCustom()">
            èªå®ä¹æ¥è¯¢<span class="fr glyphicon glyphicon-menu-down"></span>
</div>
<div class="custom-list">
<div class="border-hr"></div>
<div class="item-wrap">
<div class="item-name">æææ°</div>
<div class="hr"></div>
<div class="item-name active">ææå·</div>
<div class="hr"></div>
<div class="item-name">æå¤©æ°</div>
</div>
<div class="item-content">
<div>
<div>
<div>
                    æè¦æ¥è¯¢æè¿<input autocomplete="off" class="issue-count" min="1" oninput="if(!/^[0-9]+$/.test(value))   value=value.replace(/\D/g,''); 
                      if(value == 0) value=''
                      " type="number"/>æ
                  </div>
</div>
</div>
<div class="show">
<div>
                  ç¬¬<input autocomplete="off" class="issue-start" min="1" oninput="if(!/^[0-9]+$/.test(value)) value=value.replace(/\D/g,'');if(value == 0) value=''" type="number"/>è³<input autocomplete="off" class="issue-end" min="1" oninput="if(!/^[0-9]+$/.test(value)) value=value.replace(/\D/g,'');if(value == 0) value=''" type="number"/>
</div>
<div class="tip">æ³¨ï¼æå·æ ¼å¼ä¸º 2017041</div>
</div>
<div>
<div>
                  ç¬¬<input autocomplete="off" class="day-start day" maxlength="12" onfocus="WdatePicker({skin:'whyGreen',maxDate:'%y-%M-%d'})" type="text" value="2017-10-24"/>è³<input autocomplete="off" class="day-end day" maxlength="12" onfocus="WdatePicker({skin:'whyGreen',maxDate:'%y-%M-%d'})" type="text" value="2017-10-24"/>
</div>
</div>
</div>
<div class="item-btn">
<div class="fl custom-query" onclick="handleCustom()">
                å¼å§æ¥è¯¢
              </div>
<div class="fr custom-reset" onclick="handleReset()">éç½®</div>
</div>
</div>
</div>
<span class="play-fun yxgz-wrap">
<a href="/c/2018/10/12/417937.shtml" target="_blank">æ¸¸æè§å</a>
</span>
<div class="clearfix"></div>
</div>
</div>
<div class="table ssq dnone">
<table class="ssq_table">
<thead>
<tr>
<th rowspan="2">æå·</th>
<th rowspan="2">å¼å¥æ¥æ</th>
<th rowspan="2">å¼å¥å·ç </th>
<th colspan="2">ä¸ç­å¥</th>
<th colspan="2">äºç­å¥</th>
<th rowspan="2">éå®é¢ï¼åï¼</th>
<th rowspan="2">å¥æ± éé¢ï¼åï¼</th>
<th rowspan="2">å¼å¥å¬å</th>
</tr>
<tr>
<th>æ³¨æ°</th>
<th>éé¢</th>
<th>æ³¨æ°</th>
<th>éé¢</th>
</tr>
</thead>
<tbody></tbody>
</table>
<div style="margin-top:10px">æ³¨ï¼ä»¥ä¸è¡¨æ ¼ä¸­ä»æ¾ç¤ºå½æä¸ç­å¥ãäºç­å¥ä¸­å¥æåµï¼å¶ä»ä¸­å¥æåµè¯·æ¥éå¼å¥å¬åè¯¦æã</div>
</div>
<div class="table kl8 dnone">
<table class="kl8_table">
<thead>
<tr>
<th>æå·</th>
<th>å¼å¥æ¥æ</th>
<th>å¼å¥å·ç </th>
<th>éå®é¢ï¼åï¼</th>
<th>å¼å¥å¬å</th>
</tr>
</thead>
<tbody></tbody>
</table>
</div>
<div class="table 3d dnone">
<table class="fc3d_table">
<thead>
<tr>
<th>æå·</th>
<th>å¼å¥æ¥æ</th>
<th>å¼å¥å·ç </th>
<th>éå®é¢ï¼åï¼</th>
<th>å¼å¥å¬å</th>
</tr>
</thead>
<tbody></tbody>
</table>
</div>
<div class="table qlc dnone">
<table class="qlc_table">
<thead>
<tr>
<th rowspan="2">æå·</th>
<th rowspan="2">å¼å¥æ¥æ</th>
<th rowspan="2">å¼å¥å·ç </th>
<th colspan="2">ä¸ç­å¥</th>
<th colspan="2">äºç­å¥</th>
<th rowspan="2">éå®é¢ï¼åï¼</th>
<th rowspan="2">å¥æ± éé¢ï¼åï¼</th>
<th rowspan="2">å¼å¥å¬å</th>
</tr>
<tr>
<th>æ³¨æ°</th>
<th>éé¢</th>
<th>æ³¨æ°</th>
<th>éé¢</th>
</tr>
</thead>
<tbody></tbody>
</table>
<div style="margin-top:10px">æ³¨ï¼ä»¥ä¸è¡¨æ ¼ä¸­ä»æ¾ç¤ºå½æä¸ç­å¥ãäºç­å¥ä¸­å¥æåµï¼å¶ä»ä¸­å¥æåµè¯·æ¥éå¼å¥å¬åè¯¦æã</div>
</div>
</div>
<div class="pagebar">
<div id="paging" onclick="handleClickPaging()"></div>
</div>
</div>
<script>
  $('.day-start').val(today())
  $('.day-end').val(today())
  function wqkjgg() {
    var aliasList = currentAlias
    var queryType = aliasList.split('_')
    if (queryType[2]) {
      type = queryType[2]
      $('.gg-type').val(type)
      handleChangeType()
    } else {
      getDrawNoticeData(type)
    }
  }
  var type = 'ssq'
  var issueCount
  var issueStart
  var issueEnd
  var dayStart
  var dayEnd
  var dataList
  var pageNo = 1
  var pageSize = 30
  var totalSize;
  var operate;
  var weekValue;
  var systemType = "PC";
  // è·åæ°æ®
  function getDrawNoticeData(type, operation) {
    operate = operation;
    if (operate != 'changePage') {
      pageNo = 1
    }
    var sendData = wqcx(
      type,
      issueCount,
      issueStart,
      issueEnd,
      dayStart,
      dayEnd,
      pageNo,
      pageSize,
      weekValue,
      systemType
    )
    if (sendData.message == 'æ¥è¯¢æå') {
      if (!operate) {
        getSize()
      }
      totalSize = sendData.total;
      $('.pagebar').show();
      this.handleData(sendData)
      dataList = sendData;
    } else {
      if (!operate) {
        getSize()
      }
      totalSize = 0;
      $('.' + type + ' tbody').html('');
      $('.pagebar').hide();
    }
  }
  // è¿æ»¤æ°æ®
  function handleData(sendData, week) {
    $('.' + type + ' tbody').html('')
    for (var i = 0; i < sendData.result.length; i++) {
      $('.' + type).removeClass('dnone')
      handleDomData(sendData.result[i], week)
    }
  }
  // è¿æ»¤çæ°æ®æ¾ç¤ºå°é¡µé¢
  function handleDomData(item, dataWeek) {
    var qiuHtml = []
    var redHtml = ''
    var blueHtml = ''
    var redQiu = item.red.split(',')
    var blueQiu = item.blue.split(',')
    if (type == '3d') {
      blueQiu = redQiu
      redQiu = []
    } else if (type == 'kl8') {
      blueQiu = []
    }
    // åè²ç
    if (redQiu.length != 0 && type == 'ssq') {
      for (var j = 0; j < redQiu.length; j++) {
        redHtml =
          '<div class="qiu-item qiu-item-small qiu-item-wqgg-zjhm-red">' +
          parseInt(redQiu[j]) +
          '</div>'
        qiuHtml.push(redHtml)
      }
    }
    if (blueQiu.length != 0 && type == 'ssq') {
      for (var j = 0; j < blueQiu.length; j++) {
        blueHtml =
          '<div class="qiu-item qiu-item-small qiu-item-wqgg-zjhm-blue">' +
          parseInt(blueQiu[j]) +
          '</div>'
        qiuHtml.push(blueHtml)
      }
    }
    // å¿«ä¹8
    if (redQiu.length != 0 && type == 'kl8') {
      for (var j = 0; j < redQiu.length; j++) {
        redHtml =
          '<div class="qiu-item qiu-item-small kl8-item-wqgg-zjhm-red">' +
          parseInt(redQiu[j]) +
          '</div>'
        qiuHtml.push(redHtml)
      }
    }
    //3D 
    if (blueQiu.length != 0 && type == '3d') {
      for (var j = 0; j < blueQiu.length; j++) {
        blueHtml =
          '<div class="qiu-item qiu-item-small wqgg-item-3D-zjhm-blue">' +
          parseInt(blueQiu[j]) +
          '</div>'
        qiuHtml.push(blueHtml)
      }
    }
    //ä¸ä¹å½©
    if (redQiu.length != 0 && type == 'qlc') {
      for (var j = 0; j < redQiu.length; j++) {
        redHtml =
          '<div class="qiu-item qiu-item-small qlc-item-wqgg-zjhm-red">' +
          parseInt(redQiu[j]) +
          '</div>'
        qiuHtml.push(redHtml)
      }
    }
    if (blueQiu.length != 0 && type == 'qlc') {
      for (var j = 0; j < blueQiu.length; j++) {
        blueHtml =
          '<div class="qiu-item qiu-item-small qlc-item-wqgg-zjhm-blue">' +
          parseInt(blueQiu[j]) +
          '</div>'
        qiuHtml.push(blueHtml)
      }
    }



    if (type == 'kl8') {
      $('.' + type + ' tbody').append(
        '<tr data-alias="' +
        dataWeek +
        '""><td>' +
        item.code +
        '</td><td>' +
        item.date +
        '</td><td><div class="qiu">' +
        qiuHtml.join('') +
        '</div></td><td>' +
        numFormat(item.sales) +
        '</td><td><a href="' +
        item.detailsLink +
        '" target = "blank">è¯¦æ</a></td></tr>'
      )
    } else {
      if (type == '3d') {
        if (item.code > 2021334) {
          $('.' + type + ' tbody').append(
            '<tr data-alias="' +
            dataWeek +
            '""><td>' +
            item.code +
            '</td><td>' +
            item.date +
            '</td><td><div class="qiu">' +
            qiuHtml.join('') +
            '</div></td><td>' +
            numFormat(item.sales) +
            '</td><td><a href="' +
            item.detailsLink +
            '" target = "blank">è¯¦æ</a></td></tr>'
          )
        } else {
          $('.' + type + ' tbody').append(
            '<tr data-alias="' +
            dataWeek +
            '""><td>' +
            item.code +
            '</td><td>' +
            item.date +
            '</td><td><div class="qiu">' +
            qiuHtml.join('') +
            '</div></td><td>' +
            numFormat(item.sales) +
            '</td><td><a href="' +
            item.detailsLink +
            '" target = "blank">è¯¦æ</a></td></tr>'
          )
        }
      } else {
        // åè²ç
        $('.' + type + ' tbody').append(
          '<tr data-alias="' +
          dataWeek +
          '""><td>' +
          item.code +
          '</td><td>' +
          item.date +
          '</td><td><div class="qiu">' +
          qiuHtml.join('') +
          '</div></td><td>' +
          item.prizegrades[0].typenum +
          '</td><td>' +
          item.prizegrades[0].typemoney +
          '</td><td>' +
          item.prizegrades[1].typenum +
          '</td><td>' +
          item.prizegrades[1].typemoney +
          '</td><td>' +
          numFormat(item.sales) +
          '</td><td>' +
          numFormat(item.poolmoney) +
          '</td><td><a href="' +
          item.detailsLink +
          '" target = "blank">è¯¦æ</a></td></tr>'
        )
      }
    }
  }

  //åæ¢æ¸¸æ
  function handleChangeType() {
    resetData()
    resetShowData();
    issueCount = '';
    issueStart = '';
    issueEnd = '';
    dayStart = '';
    dayEnd = '';
    dataList = '';
    totalSize = '';
    operate = undefined;
    weekValue = '';
    pageNo = 1;
    pageSize = 30;

    type = $('.gg-type').val()
    $('.table').addClass('dnone')
    getDrawNoticeData(type)
    $('.period-list  div')
      .eq(0)
      .addClass('active')
      .siblings()
      .removeClass('active')
    if (type == 'ssq') {
      $('.table-hea .time').text('[ æ¯å¨äºãåãæ¥21:15å¼å¥ ]')
      $('.radio-btn .day-search').removeClass('dnone')
      $('.radio-btn .gg-date-type').html(
        '<option value="all">å¨é¨</option><option value="è¿30æ">è¿30æ</option><option value="è¿50æ">è¿50æ</option><option value="è¿100æ">è¿100æ</option>'
      )
      $('.radio-btn .gg-week-type').show();
      $('.radio-btn .gg-week-type').html(
        '<option value="all">å¨é¨å¼å¥æ¥æ</option><option value="2">å¨äº</option><option value="4">å¨å</option><option value="0">å¨æ¥</option>'
      )
      $('.play-fun').html(
        '<span><a href="/c/2018/10/12/417937.shtml" target="_blank">æ¸¸æè§å</a></span>'
      )
    } else if (type == 'kl8') {
      $('.table-hea .time').text('[ æ¯æ¥ 21:30å¼å¥  ]')
      $('.radio-btn .day-search').addClass('dnone')
      $('.radio-btn .gg-date-type').html(
        '<option value="all">å¨é¨</option><option value="è¿30æ">è¿30æ</option><option value="è¿50æ">è¿50æ</option><option value="è¿100æ">è¿100æ</option>'
      )
      $('.radio-btn .gg-week-type').hide();
      $('.play-fun').html(
        '<span><a href="/c/2020/08/19/472721.shtml" target="_blank">æ¸¸æè§å</a></span>'
      )
    } else if (type == 'qlc') {
      $('.table-hea .time').text('[ æ¯å¨ä¸ãä¸ãäº 21:15å¼å¥  ]')
      $('.radio-btn .day-search').removeClass('dnone')
      $('.radio-btn .gg-date-type').html(
        '<option value="all">å¨é¨</option><option value="è¿30æ">è¿30æ</option><option value="è¿50æ">è¿50æ</option><option value="è¿100æ">è¿100æ</option>'
      )
      $('.radio-btn .gg-week-type').show();
      $('.radio-btn .gg-week-type').html(
        '<option value="all">å¨é¨å¼å¥æ¥æ</option><option value="1">å¨ä¸</option><option value="3">å¨ä¸</option><option value="5">å¨äº</option>'
      )
      $('.play-fun').html(
        '<span><a href="/c/2017/11/15/418902.shtml" target="_blank">æ¸¸æè§å</a></span>'
      )
    } else if (type == '3d') {
      $('.table-hea .time').text('[ æ¯æ¥ 21:15å¼å¥  ]')
      $('.radio-btn .day-search').addClass('dnone')
      $('.radio-btn .gg-date-type').html(
        '<option value="all">å¨é¨</option><option value="è¿30æ">è¿30æ</option><option value="è¿50æ">è¿50æ</option><option value="è¿100æ">è¿100æ</option>'
      )
      $('.radio-btn .gg-week-type').hide();
      $('.play-fun').html(
        '<span><a href="/c/2017/11/15/418903.shtml" target="_blank">æ¸¸æè§å</a></span>'
      )
    }
  }

  //æ¥çè¿xxæï¼ä¿®æ¹åï¼
  function handleChangeDate() {
    //éç½®ç»åç«¯ä¼ éçæ°æ®
    resetData();
    //éç½®æ¾ç¤ºæ°æ®
    resetShowData();
    if ($('.gg-date-type').val() == 'è¿30æ') {
      issueCount = 30
    } else if ($('.gg-date-type').val() == 'è¿50æ') {
      issueCount = 50
    } else if ($('.gg-date-type').val() == 'è¿100æ') {
      issueCount = 100
    } else if ($('.gg-date-type').val() == 'è¿30æ') {
      issueCount = null
    }
    getDrawNoticeData(type)
  }

  //éç½®èªå®ä¹æ¥è¯¢éé¢çæ°æ®
  function resetShowData() {
    $('.issue-start').val('');
    $('.issue-end').val('');
    $('.issue-count').val('');
    $('.day-start').val(today());
    $('.day-end').val(today());
  }


  // æ¥çè¿xxæ
  $('.period-list  div').click(function () {
    resetData()
    $(this).addClass('active').siblings().removeClass('active')
    if ($(this).text() == 'è¿30æ') {
      issueCount = 30
    } else if ($(this).text() == 'è¿50æ') {
      issueCount = 50
    } else if ($(this).text() == 'è¿100æ') {
      issueCount = 100
    }
    $('.day-list > div')
      .eq(3)
      .addClass('active')
      .siblings()
      .removeClass('active')
    getDrawNoticeData(type)
  })

  //å¼å¥æ¥æ¥è¯¢ï¼æ°ï¼
  function handleChangeWeekDate() {
    var valueWeek = $('.gg-week-type').val();
    // console.log(valueWeek);
    if (valueWeek == 'all') {
      weekValue = '';
      // handleData(dataList)
      getDrawNoticeData(type)
    } else {
      weekValue = valueWeek;
      // handleData(dataList, valueWeek)
      getDrawNoticeData(type)
    }
  }


  // èªå®ä¹æ¡æ¾ç¤º
  function handleShowCustom(e) {
    window.event ? (window.event.cancelBubble = true) : e.stopPropagation()
    if ($('.custom').hasClass('active')) {
      handleHideCustom()
    } else {
      $('.custom').addClass('active')
      $('.custom-list').addClass('show')
    }
  }
  // èªå®ä¹æ¡éè
  function handleHideCustom() {
    $('.custom').removeClass('active')
    $('.custom-list').removeClass('show')
  }
  $(window).click(function () {
    handleHideCustom()
  })
  $('.custom-list').click(function () {
    window.event ? (window.event.cancelBubble = true) : e.stopPropagation()
  })
  var customIndex = 1
  // èªå®ä¹æ¥è¯¢ æå·/ææ°/å¤©æ° ç±»ååæ¢
  $('.custom-list .item-wrap .item-name').click(function () {
    resetShowData();
    customIndex = $(this).index() / 2
    $(this).addClass('active').siblings().removeClass('active')
    $('.custom-list .item-content>div')
      .eq(customIndex)
      .addClass('show')
      .siblings()
      .removeClass('show')
  })
  // èªå®ä¹æ¥è¯¢
  function handleCustom() {
    var obj = $('.gg-date-type option:first');
    obj.text('å¨é¨');
    $('.radio-btn .gg-date-type').html(
      '<option value="all">å¨é¨</option><option value="è¿30æ">è¿30æ</option><option value="è¿50æ">è¿50æ</option><option value="è¿100æ">è¿100æ</option>'
    )
    if (customIndex == 0) {
      resetData()
      issueCount = $('.issue-count').val()
    } else if (customIndex == 1) {
      resetData()
      issueCount = ''
      issueStart = $('.issue-start').val()
      issueEnd = $('.issue-end').val()
    } else if (customIndex == 2) {
      resetData()
      issueCount = ''
      dayStart = $('.day-start').val()
      dayEnd = $('.day-end').val()
    }
    getDrawNoticeData(type)
    handleHideCustom()
  }

  function handleReset() {
    if (customIndex == 0) {
      $('.issue-count').val('')
    } else if (customIndex == 1) {
      $('.issue-start').val('')
      $('.issue-end').val('')
    } else if (customIndex == 2) {
      $('.day-start').val('')
      $('.day-end').val('')
    }
  }
  // éç½®æ°æ®
  function resetData() {
    issueStart = ''
    issueEnd = ''
    issueCount = ''
    dayStart = ''
    dayEnd = ''
    var qhDom = $('.period-list .active')
    if (qhDom.text() == 'è¿30æ') {
      issueCount = 30
    } else if (qhDom.text() == 'è¿50æ') {
      issueCount = 50
    } else if (qhDom.text() == 'è¿100æ') {
      issueCount = 100
    }
  }

  function getSize() {
    layui.use('laypage', function () {
      var laypage = layui.laypage;
      //æ§è¡ä¸ä¸ªlaypageå®ä¾
      laypage.render({
        elem: 'paging' //æ³¨æï¼è¿éç test1 æ¯ IDï¼ä¸ç¨å  # å·
        , count: totalSize //æ°æ®æ»æ°ï¼ä»æå¡ç«¯å¾å°
        , prev: '<em>Â«</em>'
        , next: '<em>Â»</em>'
        , limit: 30
        , theme: '#e81f18'
        , jump: function (obj) {
          pageNo = obj.curr;
        }
      });
    });

  }


  //ç¹å»åé¡µæ¶åççäºæ
  function handleClickPaging() {
    getDrawNoticeData(type, 'changePage');
  }


</script>
</div>
```


```Json
{'state': 0, 'message': '查询成功', 'total': 1624, 'pageNum': 55, 'pageNo': 1, 'pageSize': 30, 'Tflag': 0, 'result': [{'name': '双色球', 'code': '2023119', 'detailsLink': '/c/2023/10/17/556491.shtml', 'videoLink': '/c/2023/10/17/556489.shtml', 'date': '2023-10-17(二)', 'week': '二', 'red': '01,02,03,19,21,28', 'blue': '15', 'blue2': '', 'sales': '379869478', 'poolmoney': '2404112623', 'content': '北京1注,福建1注,广东2注,共4注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '4', 'typemoney': '10000000'}, {'type': 2, 'typenum': '76', 'typemoney': '392351'}, {'type': 3, 'typenum': '797', 'typemoney': '3000'}, {'type': 4, 'typenum': '48851', 'typemoney': '200'}, {'type': 5, 'typenum': '990336', 'typemoney': '10'}, {'type': 6, 'typenum': '8959355', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023118', 'detailsLink': '/c/2023/10/15/556272.shtml', 'videoLink': '/c/2023/10/15/556270.shtml', 'date': '2023-10-15(日)', 'week': '日', 'red': '01,02,11,19,25,29', 'blue': '04', 'blue2': '', 'sales': '416077564', 'poolmoney': '2354656592', 'content': '河北1注,辽宁1注,江苏1注,福建1注,山东1注,湖北1注,湖南1注,广东1注,云南1注,共9注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '9', 'typemoney': '7221722'}, {'type': 2, 'typenum': '400', 'typemoney': '62485'}, {'type': 3, 'typenum': '2281', 'typemoney': '3000'}, {'type': 4, 'typenum': '108685', 'typemoney': '200'}, {'type': 5, 'typenum': '1734179', 'typemoney': '10'}, {'type': 6, 'typenum': '11595741', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023117', 'detailsLink': '/c/2023/10/12/556145.shtml', 'videoLink': '/c/2023/10/12/556143.shtml', 'date': '2023-10-12(四)', 'week': '四', 'red': '02,11,14,17,18,28', 'blue': '08', 'blue2': '', 'sales': '382441836', 'poolmoney': '2344668961', 'content': '河北2注,内蒙古2注,湖北1注,广东1注,广西2注,共8注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '8', 'typemoney': '6198467'}, {'type': 2, 'typenum': '114', 'typemoney': '105128'}, {'type': 3, 'typenum': '2638', 'typemoney': '3000'}, {'type': 4, 'typenum': '115945', 'typemoney': '200'}, {'type': 5, 'typenum': '1946691', 'typemoney': '10'}, {'type': 6, 'typenum': '17777580', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023116', 'detailsLink': '/c/2023/10/10/555925.shtml', 'videoLink': '/c/2023/10/10/555923.shtml', 'date': '2023-10-10(二)', 'week': '二', 'red': '02,08,09,13,24,27', 'blue': '12', 'blue2': '', 'sales': '373229184', 'poolmoney': '2358302682', 'content': '北京1注,安徽3注,福建2注,河南1注,广西1注,云南1注,宁夏1注,共10注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '10', 'typemoney': '6501260'}, {'type': 2, 'typenum': '238', 'typemoney': '78847'}, {'type': 3, 'typenum': '2608', 'typemoney': '3000'}, {'type': 4, 'typenum': '112589', 'typemoney': '200'}, {'type': 5, 'typenum': '1784492', 'typemoney': '10'}, {'type': 6, 'typenum': '11926507', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023115', 'detailsLink': '/c/2023/10/08/555704.shtml', 'videoLink': '/c/2023/10/08/555703.shtml', 'date': '2023-10-08(日)', 'week': '日', 'red': '02,07,16,21,26,27', 'blue': '16', 'blue2': '', 'sales': '399381218', 'poolmoney': '2367018008', 'content': '浙江1注,福建1注,重庆5注,新疆6注,共13注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '13', 'typemoney': '6684992'}, {'type': 2, 'typenum': '123', 'typemoney': '222610'}, {'type': 3, 'typenum': '1561', 'typemoney': '3000'}, {'type': 4, 'typenum': '76820', 'typemoney': '200'}, {'type': 5, 'typenum': '1432085', 'typemoney': '10'}, {'type': 6, 'typenum': '10360882', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023114', 'detailsLink': '/c/2023/10/05/555478.shtml', 'videoLink': '/c/2023/10/05/555476.shtml', 'date': '2023-10-05(四)', 'week': '四', 'red': '07,09,15,16,17,26', 'blue': '09', 'blue2': '', 'sales': '370562742', 'poolmoney': '2371779513', 'content': '河北1注,山西1注,辽宁1注,黑龙江1注,安徽1注,山东1注,河南1注,湖北1注,云南1注,共9注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '9', 'typemoney': '6717188'}, {'type': 2, 'typenum': '157', 'typemoney': '123046'}, {'type': 3, 'typenum': '2523', 'typemoney': '3000'}, {'type': 4, 'typenum': '107090', 'typemoney': '200'}, {'type': 5, 'typenum': '1828640', 'typemoney': '10'}, {'type': 6, 'typenum': '11405771', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023113', 'detailsLink': '/c/2023/09/28/555353.shtml', 'videoLink': '/c/2023/09/28/555350.shtml', 'date': '2023-09-28(四)', 'week': '四', 'red': '01,02,13,18,25,27', 'blue': '03', 'blue2': '', 'sales': '373161172', 'poolmoney': '2374279095', 'content': '北京1注,辽宁1注,浙江1注,广东1注,宁夏5注,共9注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '9', 'typemoney': '7108275'}, {'type': 2, 'typenum': '101', 'typemoney': '234832'}, {'type': 3, 'typenum': '1190', 'typemoney': '3000'}, {'type': 4, 'typenum': '66454', 'typemoney': '200'}, {'type': 5, 'typenum': '1322883', 'typemoney': '10'}, {'type': 6, 'typenum': '11577391', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023112', 'detailsLink': '/c/2023/09/26/554833.shtml', 'videoLink': '/c/2023/09/26/554831.shtml', 'date': '2023-09-26(二)', 'week': '二', 'red': '09,12,13,22,24,31', 'blue': '04', 'blue2': '', 'sales': '369828352', 'poolmoney': '2367099281', 'content': '北京1注,天津1注,山西1注,浙江5注,陕西1注,甘肃4注,共13注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '13', 'typemoney': '6599921'}, {'type': 2, 'typenum': '176', 'typemoney': '147720'}, {'type': 3, 'typenum': '1276', 'typemoney': '3000'}, {'type': 4, 'typenum': '73069', 'typemoney': '200'}, {'type': 5, 'typenum': '1349884', 'typemoney': '10'}, {'type': 6, 'typenum': '9056067', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023111', 'detailsLink': '/c/2023/09/24/554512.shtml', 'videoLink': '/c/2023/09/24/554511.shtml', 'date': '2023-09-24(日)', 'week': '日', 'red': '05,06,12,17,20,33', 'blue': '09', 'blue2': '', 'sales': '404303630', 'poolmoney': '2374902077', 'content': '山西1注,内蒙古1注,湖南1注,四川1注,共4注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '4', 'typemoney': '10000000'}, {'type': 2, 'typenum': '121', 'typemoney': '208017'}, {'type': 3, 'typenum': '1640', 'typemoney': '3000'}, {'type': 4, 'typenum': '75068', 'typemoney': '200'}, {'type': 5, 'typenum': '1394133', 'typemoney': '10'}, {'type': 6, 'typenum': '12710665', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023110', 'detailsLink': '/c/2023/09/21/554284.shtml', 'videoLink': '/c/2023/09/21/554283.shtml', 'date': '2023-09-21(四)', 'week': '四', 'red': '02,06,20,25,29,33', 'blue': '16', 'blue2': '', 'sales': '375580258', 'poolmoney': '2339391685', 'content': '浙江1注,山东1注,四川4注,共6注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '6', 'typemoney': '8972251'}, {'type': 2, 'typenum': '70', 'typemoney': '425598'}, {'type': 3, 'typenum': '719', 'typemoney': '3000'}, {'type': 4, 'typenum': '46046', 'typemoney': '200'}, {'type': 5, 'typenum': '987121', 'typemoney': '10'}, {'type': 6, 'typenum': '8725876', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023109', 'detailsLink': '/c/2023/09/19/554066.shtml', 'videoLink': '/c/2023/09/19/554064.shtml', 'date': '2023-09-19(二)', 'week': '二', 'red': '06,08,10,13,16,28', 'blue': '13', 'blue2': '', 'sales': '372318810', 'poolmoney': '2303849540', 'content': '河南1注,四川1注,陕西1注,共3注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '3', 'typemoney': '10000000'}, {'type': 2, 'typenum': '221', 'typemoney': '115585'}, {'type': 3, 'typenum': '1348', 'typemoney': '3000'}, {'type': 4, 'typenum': '71622', 'typemoney': '200'}, {'type': 5, 'typenum': '1405642', 'typemoney': '10'}, {'type': 6, 'typenum': '9566800', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023108', 'detailsLink': '/c/2023/09/17/553746.shtml', 'videoLink': '/c/2023/09/17/553744.shtml', 'date': '2023-09-17(日)', 'week': '日', 'red': '01,03,06,08,18,24', 'blue': '09', 'blue2': '', 'sales': '414140392', 'poolmoney': '2257216493', 'content': '河北1注,安徽2注,福建1注,江西1注,山东1注,重庆1注,河南1注,湖南1注,广东2注,广西1注,共12注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '12', 'typemoney': '6002668'}, {'type': 2, 'typenum': '109', 'typemoney': '137981'}, {'type': 3, 'typenum': '2589', 'typemoney': '3000'}, {'type': 4, 'typenum': '109256', 'typemoney': '200'}, {'type': 5, 'typenum': '1826668', 'typemoney': '10'}, {'type': 6, 'typenum': '18976757', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023107', 'detailsLink': '/c/2023/09/14/553516.shtml', 'videoLink': '/c/2023/09/14/553515.shtml', 'date': '2023-09-14(四)', 'week': '四', 'red': '03,07,18,25,29,33', 'blue': '14', 'blue2': '', 'sales': '377747376', 'poolmoney': '2284128424', 'content': '山东1注,河南1注,四川3注,贵州1注,共6注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '6', 'typemoney': '7890900'}, {'type': 2, 'typenum': '194', 'typemoney': '111761'}, {'type': 3, 'typenum': '1685', 'typemoney': '3000'}, {'type': 4, 'typenum': '84502', 'typemoney': '200'}, {'type': 5, 'typenum': '1479496', 'typemoney': '10'}, {'type': 6, 'typenum': '12323767', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023106', 'detailsLink': '/c/2023/09/12/553296.shtml', 'videoLink': '/c/2023/09/12/553294.shtml', 'date': '2023-09-12(二)', 'week': '二', 'red': '07,09,10,20,22,24', 'blue': '07', 'blue2': '', 'sales': '375981944', 'poolmoney': '2266428564', 'content': '上海1注,江苏1注,四川1注,深圳1注,共4注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '4', 'typemoney': '8594088'}, {'type': 2, 'typenum': '140', 'typemoney': '128360'}, {'type': 3, 'typenum': '2311', 'typemoney': '3000'}, {'type': 4, 'typenum': '98329', 'typemoney': '200'}, {'type': 5, 'typenum': '1674053', 'typemoney': '10'}, {'type': 6, 'typenum': '13802009', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023105', 'detailsLink': '/c/2023/09/10/553076.shtml', 'videoLink': '/c/2023/09/10/553074.shtml', 'date': '2023-09-10(日)', 'week': '日', 'red': '01,03,05,26,30,32', 'blue': '16', 'blue2': '', 'sales': '405852212', 'poolmoney': '2246893587', 'content': '北京1注,广东2注,共3注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '3', 'typemoney': '10000000'}, {'type': 2, 'typenum': '77', 'typemoney': '404257'}, {'type': 3, 'typenum': '964', 'typemoney': '3000'}, {'type': 4, 'typenum': '55080', 'typemoney': '200'}, {'type': 5, 'typenum': '1163315', 'typemoney': '10'}, {'type': 6, 'typenum': '9763015', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023104', 'detailsLink': '/c/2023/09/07/552848.shtml', 'videoLink': '/c/2023/09/07/552846.shtml', 'date': '2023-09-07(四)', 'week': '四', 'red': '10,19,23,25,30,31', 'blue': '12', 'blue2': '', 'sales': '371735912', 'poolmoney': '2183510069', 'content': '北京1注,浙江1注,共2注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '2', 'typemoney': '10000000'}, {'type': 2, 'typenum': '76', 'typemoney': '311447'}, {'type': 3, 'typenum': '1616', 'typemoney': '3000'}, {'type': 4, 'typenum': '73618', 'typemoney': '200'}, {'type': 5, 'typenum': '1401010', 'typemoney': '10'}, {'type': 6, 'typenum': '10777766', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023103', 'detailsLink': '/c/2023/09/05/552628.shtml', 'videoLink': '/c/2023/09/05/552631.shtml', 'date': '2023-09-05(二)', 'week': '二', 'red': '05,06,13,24,25,29', 'blue': '15', 'blue2': '', 'sales': '370559376', 'poolmoney': '2132500020', 'content': '浙江3注,共3注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '3', 'typemoney': '10000000'}, {'type': 2, 'typenum': '103', 'typemoney': '281418'}, {'type': 3, 'typenum': '917', 'typemoney': '3000'}, {'type': 4, 'typenum': '57934', 'typemoney': '200'}, {'type': 5, 'typenum': '1212034', 'typemoney': '10'}, {'type': 6, 'typenum': '7834347', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023102', 'detailsLink': '/c/2023/09/03/552310.shtml', 'videoLink': '/c/2023/09/03/552308.shtml', 'date': '2023-09-03(日)', 'week': '日', 'red': '01,09,10,13,21,28', 'blue': '10', 'blue2': '', 'sales': '408618502', 'poolmoney': '2075541857', 'content': '山西2注,江苏2注,浙江3注,湖北1注,贵州1注,宁夏1注,共10注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '10', 'typemoney': '6615741'}, {'type': 2, 'typenum': '98', 'typemoney': '206089'}, {'type': 3, 'typenum': '3131', 'typemoney': '3000'}, {'type': 4, 'typenum': '89259', 'typemoney': '200'}, {'type': 5, 'typenum': '1634397', 'typemoney': '10'}, {'type': 6, 'typenum': '15169449', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023101', 'detailsLink': '/c/2023/08/31/552080.shtml', 'videoLink': '/c/2023/08/31/552079.shtml', 'date': '2023-08-31(四)', 'week': '四', 'red': '01,05,09,15,18,26', 'blue': '04', 'blue2': '', 'sales': '370629284', 'poolmoney': '2081108979', 'content': '安徽1注,重庆1注,云南2注,共4注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '4', 'typemoney': '10000000'}, {'type': 2, 'typenum': '164', 'typemoney': '182582'}, {'type': 3, 'typenum': '962', 'typemoney': '3000'}, {'type': 4, 'typenum': '60139', 'typemoney': '200'}, {'type': 5, 'typenum': '1237291', 'typemoney': '10'}, {'type': 6, 'typenum': '6909501', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023100', 'detailsLink': '/c/2023/08/29/551763.shtml', 'videoLink': '/c/2023/08/29/551761.shtml', 'date': '2023-08-29(二)', 'week': '二', 'red': '05,06,12,15,23,25', 'blue': '04', 'blue2': '', 'sales': '359711540', 'poolmoney': '2031278380', 'content': '北京3注,河北2注,黑龙江1注,上海1注,浙江2注,福建3注,湖北2注,湖南1注,广东4注,共19注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '19', 'typemoney': '5762908'}, {'type': 2, 'typenum': '243', 'typemoney': '74564'}, {'type': 3, 'typenum': '2824', 'typemoney': '3000'}, {'type': 4, 'typenum': '117607', 'typemoney': '200'}, {'type': 5, 'typenum': '1788007', 'typemoney': '10'}, {'type': 6, 'typenum': '10781773', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023099', 'detailsLink': '/c/2023/08/27/551543.shtml', 'videoLink': '/c/2023/08/27/551541.shtml', 'date': '2023-08-27(日)', 'week': '日', 'red': '09,11,14,19,27,33', 'blue': '05', 'blue2': '', 'sales': '390452378', 'poolmoney': '2086416405', 'content': '河北11注,吉林6注,安徽1注,共18注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '18', 'typemoney': '6174885'}, {'type': 2, 'typenum': '82', 'typemoney': '322377'}, {'type': 3, 'typenum': '1572', 'typemoney': '3000'}, {'type': 4, 'typenum': '68358', 'typemoney': '200'}, {'type': 5, 'typenum': '1319933', 'typemoney': '10'}, {'type': 6, 'typenum': '10799007', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023098', 'detailsLink': '/c/2023/08/24/551414.shtml', 'videoLink': '/c/2023/08/24/551413.shtml', 'date': '2023-08-24(四)', 'week': '四', 'red': '02,10,11,14,21,27', 'blue': '11', 'blue2': '', 'sales': '362199042', 'poolmoney': '2118259570', 'content': '辽宁1注,浙江2注,江西2注,山东1注,重庆1注,河南1注,四川2注,贵州1注,陕西1注,深圳1注,共13注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '13', 'typemoney': '6522117'}, {'type': 2, 'typenum': '266', 'typemoney': '92986'}, {'type': 3, 'typenum': '1634', 'typemoney': '3000'}, {'type': 4, 'typenum': '79485', 'typemoney': '200'}, {'type': 5, 'typenum': '1454255', 'typemoney': '10'}, {'type': 6, 'typenum': '8639674', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023097', 'detailsLink': '/c/2023/08/22/551196.shtml', 'videoLink': '/c/2023/08/22/551194.shtml', 'date': '2023-08-22(二)', 'week': '二', 'red': '01,09,14,19,29,30', 'blue': '15', 'blue2': '', 'sales': '357725994', 'poolmoney': '2128843885', 'content': '北京1注,河北1注,吉林1注,江西1注,海南1注,四川3注,云南5注,共13注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '13', 'typemoney': '6311615'}, {'type': 2, 'typenum': '225', 'typemoney': '94727'}, {'type': 3, 'typenum': '2256', 'typemoney': '3000'}, {'type': 4, 'typenum': '108823', 'typemoney': '200'}, {'type': 5, 'typenum': '1767679', 'typemoney': '10'}, {'type': 6, 'typenum': '8764273', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023096', 'detailsLink': '/c/2023/08/20/550976.shtml', 'videoLink': '/c/2023/08/20/550974.shtml', 'date': '2023-08-20(日)', 'week': '日', 'red': '08,11,18,26,31,32', 'blue': '15', 'blue2': '', 'sales': '387715200', 'poolmoney': '2146953645', 'content': '河北2注,山西1注,辽宁2注,安徽1注,四川1注,云南1注,共8注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '8', 'typemoney': '7789981'}, {'type': 2, 'typenum': '125', 'typemoney': '223198'}, {'type': 3, 'typenum': '1156', 'typemoney': '3000'}, {'type': 4, 'typenum': '67955', 'typemoney': '200'}, {'type': 5, 'typenum': '1302927', 'typemoney': '10'}, {'type': 6, 'typenum': '9658580', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023095', 'detailsLink': '/c/2023/08/17/550848.shtml', 'videoLink': '/c/2023/08/17/550846.shtml', 'date': '2023-08-17(四)', 'week': '四', 'red': '03,08,16,17,22,26', 'blue': '11', 'blue2': '', 'sales': '357870744', 'poolmoney': '2125574043', 'content': '河北7注,山西1注,浙江1注,福建1注,江西2注,山东3注,重庆1注,河南1注,广东1注,广西1注,四川1注,陕西1注,宁夏1注,共22注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '22', 'typemoney': '5751004'}, {'type': 2, 'typenum': '342', 'typemoney': '60387'}, {'type': 3, 'typenum': '2162', 'typemoney': '3000'}, {'type': 4, 'typenum': '109563', 'typemoney': '200'}, {'type': 5, 'typenum': '1818621', 'typemoney': '10'}, {'type': 6, 'typenum': '9232272', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023094', 'detailsLink': '/c/2023/08/15/550628.shtml', 'videoLink': '/c/2023/08/15/550626.shtml', 'date': '2023-08-15(二)', 'week': '二', 'red': '06,10,12,14,30,31', 'blue': '12', 'blue2': '', 'sales': '353863692', 'poolmoney': '2190138271', 'content': '浙江1注,福建2注,山东8注,四川1注,陕西1注,共13注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '13', 'typemoney': '6482678'}, {'type': 2, 'typenum': '62', 'typemoney': '388605'}, {'type': 3, 'typenum': '1054', 'typemoney': '3000'}, {'type': 4, 'typenum': '57805', 'typemoney': '200'}, {'type': 5, 'typenum': '1154774', 'typemoney': '10'}, {'type': 6, 'typenum': '10149675', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023093', 'detailsLink': '/c/2023/08/13/550308.shtml', 'videoLink': '/c/2023/08/13/550307.shtml', 'date': '2023-08-13(日)', 'week': '日', 'red': '10,21,24,25,27,32', 'blue': '07', 'blue2': '', 'sales': '382160878', 'poolmoney': '2202132520', 'content': '河北1注,陕西1注,共2注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '2', 'typemoney': '10000000'}, {'type': 2, 'typenum': '55', 'typemoney': '500947'}, {'type': 3, 'typenum': '838', 'typemoney': '3000'}, {'type': 4, 'typenum': '47779', 'typemoney': '200'}, {'type': 5, 'typenum': '1029761', 'typemoney': '10'}, {'type': 6, 'typenum': '10936581', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023092', 'detailsLink': '/c/2023/08/10/550181.shtml', 'videoLink': '/c/2023/08/10/550180.shtml', 'date': '2023-08-10(四)', 'week': '四', 'red': '03,12,24,25,32,33', 'blue': '13', 'blue2': '', 'sales': '357345052', 'poolmoney': '2139476134', 'content': '浙江3注,山东1注,陕西2注,共6注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '6', 'typemoney': '8563809'}, {'type': 2, 'typenum': '98', 'typemoney': '272740'}, {'type': 3, 'typenum': '1075', 'typemoney': '3000'}, {'type': 4, 'typenum': '63928', 'typemoney': '200'}, {'type': 5, 'typenum': '1253157', 'typemoney': '10'}, {'type': 6, 'typenum': '7928526', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023091', 'detailsLink': '/c/2023/08/08/549962.shtml', 'videoLink': '/c/2023/08/08/549961.shtml', 'date': '2023-08-08(二)', 'week': '二', 'red': '16,20,22,26,30,32', 'blue': '16', 'blue2': '', 'sales': '358375594', 'poolmoney': '2110673283', 'content': '天津1注,浙江4注,广东1注,新疆1注,深圳1注,共8注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '8', 'typemoney': '7716754'}, {'type': 2, 'typenum': '69', 'typemoney': '393732'}, {'type': 3, 'typenum': '1010', 'typemoney': '3000'}, {'type': 4, 'typenum': '50480', 'typemoney': '200'}, {'type': 5, 'typenum': '1012117', 'typemoney': '10'}, {'type': 6, 'typenum': '8737338', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}, {'name': '双色球', 'code': '2023090', 'detailsLink': '/c/2023/08/06/549744.shtml', 'videoLink': '/c/2023/08/06/549742.shtml', 'date': '2023-08-06(日)', 'week': '日', 'red': '01,02,09,26,30,31', 'blue': '07', 'blue2': '', 'sales': '384947064', 'poolmoney': '2090904684', 'content': '北京1注,湖北1注,广东2注,共4注。', 'addmoney': '', 'addmoney2': '', 'msg': '', 'z2add': '', 'm2add': '', 'prizegrades': [{'type': 1, 'typenum': '4', 'typemoney': '9305795'}, {'type': 2, 'typenum': '97', 'typemoney': '221948'}, {'type': 3, 'typenum': '1268', 'typemoney': '3000'}, {'type': 4, 'typenum': '75044', 'typemoney': '200'}, {'type': 5, 'typenum': '1492374', 'typemoney': '10'}, {'type': 6, 'typenum': '13754324', 'typemoney': '5'}, {'type': 7, 'typenum': '', 'typemoney': ''}]}]}

```