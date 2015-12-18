<html>
<head>
  <meta charset='utf-8'/>
  <link rel='stylesheet' href='/css/mentholatum-tbl.css' />
  <script type='text/javascript' src='https://code.jquery.com/jquery.min.js'></script>
  <script>
    var gCurYear = parseInt({{ m_year }});
    var gCurMonth = parseInt({{ m_month }});
    $(document).ready(function() {
      var result = {{ !result_json }};
      // page is now ready, initialize the calendar...
      console.log(result);
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
  <script type='text/javascript' src='/js/mentholatum-tbl.js'></script>
</body>
</html>
