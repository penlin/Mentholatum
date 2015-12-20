<html>
<head>
  <meta charset='utf-8'/>
  <link rel='stylesheet' href='/css/mentholatum-tbl.css' />
  <script type='text/javascript' src='https://code.jquery.com/jquery.min.js'></script>
  <script>
    $(document).ready(function() {
      var result = {{ !result_json }};
      // page is now ready, initialize the calendar...
      console.log(result);
	  initMentholatumTbl(result);
    });
  </script>
</head>
<body>
  <h1 style="text-aign:center;">{{ !m_year }}-{{ !m_month }}</h1>
  <div id="Mentholatum-tbl"></div>	
  <script type='text/javascript' src='/js/mentholatum-tbl.js'></script>
</body>
</html>
