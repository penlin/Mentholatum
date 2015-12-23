<html>
<head>
  <meta charset='utf-8'/>
  <script type='text/javascript' src='https://code.jquery.com/jquery.min.js'></script>
  <link rel='stylesheet' href='/css/mentholatum-tbl.css' />
  <link rel='stylesheet' href='/css/modal.css' />
  <script>
    var gCurYear = parseInt({{ m_year }});
    var gCurMonth = parseInt({{ m_month }});
    $(document).ready(function() {
      var result = {{ !result_json }};
      // page is now ready, initialize the calendar...
	  initMentholatumTbl(result);
      
      var lastmonth = (gCurMonth === 1)?((gCurYear-1).toString()+'-12'):(gCurYear.toString()+'-'+(gCurMonth-1).toString());
      $('button.last-month').html(lastmonth);
      $('a#last-month').attr('href','/'+lastmonth)
      var nextmonth = (gCurMonth === 12)?((gCurYear+1).toString()+'-1'):(gCurYear.toString()+'-'+(gCurMonth+1).toString());
      $('button.next-month').html(nextmonth);
      $('a#next-month').attr('href','/'+nextmonth)
    });
  </script>
</head>
<body>
  <div class="navigation">
    <ul class="horizontal blue">
      <li><a href="javascript:void(0)" class="active">Home</a></li>
      <li><a href="javascript:void(0)">Style</a></li>
      <li><a href="#modal-upload">Upload</a></li>
      <li><a href="javascript:void(0);">Download</a></li>
    </ul>
  </div>
  <div class="container">
    <div class="header-bar">
      <div class="bar-item">
        <a id="last-month"><button  type="button" class="last-month"></button></a>
      </div>
      <div class="bar-item center">
        <h1 class="cur-month">{{ m_year }}-{{ m_month }}</h1>
      </div>
      <div class="bar-item">
        <a id="next-month"><button  type="button" class="next-month"></button></a>
      </div>
    </div>
    <div id="Mentholatum-tbl"></div>	
  </div>

  <!-- popup upload dialog -->
  <div id="modal-upload" class="modalDialog">
    <div>
      <a href="#" title="Close" class="close">X</a>
      <div class="modal-header">
        <h2>上傳設定檔</h2>
      </div>
      <div class="modal-body">
        <form action="/do_upload" method="post" enctype="multipart/form-data" style="vertical-align:middle;">
          <p style="float:top;font-size:14px;margin-bottom:5px;">csv format with .csv or .txt filename extension.</p>
		  <br/>
          <input type="month" name="upload_month" id="modal-upload-year" required="required" style="float:left;margin-bottom:10px;"/>
          <br/>
          <input type="file" name="upload" style="float:left;" required="required"/> 
          <input type="submit" value="Upload" style="float:right;"/> 
        </form>
      </div>
    </div>
  </div>
</body>
<script type='text/javascript' src='/js/mentholatum-tbl.js'></script>
</html>
