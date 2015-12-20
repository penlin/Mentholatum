<html>
<head>
  <meta charset='utf-8'/>
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.css'/>
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.min.css' />
  <link rel='stylesheet' href='http://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.print.css' media='print'/>
  <link rel='stylesheet' href='/css/mentholatum.css' />
  <script type='text/javascript' src='https://cdn.rawgit.com/moment/moment/develop/min/moment.min.js'></script>
  <script type='text/javascript' src='https://code.jquery.com/jquery.min.js'></script>
  <script type='text/javascript' src='http://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.min.js'></script>
  <script type='text/javascript' src='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/lang-all.js'></script>
  <script>
    $(document).ready(function() {
      var events = {{ !schedule_json_arr }};
      // page is now ready, initialize the calendar...
      initFullCalendar(events);
    });
  </script>
</head>
<body>
  <div id="calendar" class="fc fc-ltr ui-widget"></div>	
  <script type='text/javascript' src='/js/mentholatum.js'></script>
</body>
</html>
