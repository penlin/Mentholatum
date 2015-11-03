<html>
<head>
  <meta charset='utf-8'/>
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.css'/>
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.min.css' />
  <link rel='stylesheet' href='http://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.print.css' media='print'/>
  <script type='text/javascript' src='https://cdn.rawgit.com/moment/moment/develop/min/moment.min.js'></script>
  <script type='text/javascript' src='https://code.jquery.com/jquery.min.js'></script>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.min.js'></script>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/lang-all.js'></script>
  <script type='text/javascript'>
    $(document).ready(function() {
      var events = {{ !schedule_json_arr }};
  	  // page is now ready, initialize the calendar...
      $('#calendar').fullCalendar({
        // put your options and callbacks here
        theme: true,
        header: {
          left: 'prev,next today',
          center: 'title',
          right: 'month,agendaWeek,agendaDay'
        },
        lang: 'zh-tw', 
        //themebuttonIcons: false, // show the prev/ next text instead of arrow icon
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        dayClick: function(date, jsEvent, view){
          $('#calendar').fullCalendar('gotoDate', date);
          $('#calendar').fullCalendar('changeView', "agendaDay");
        },
		    contentHeight: 850,
        eventClick: function(calEvent, jsEvent, view){alert('Clicked on: ' + calEvent.title);},
		    eventMouseover: function(calEvent, jsEvent, view) {
          savBg = $(this).css("background-color");
          savClr = $(this).css("color");
          $(this).css( { color:'#000', backgroundColor:"#AAF" } );
          $(this).fadeTo('slow',.8); // opacity
        },
        eventMouseout: function(calEvent, jsEvent, view) {
          $(this).css( { color:savClr, backgroundColor:savBg } );
          $(this).fadeTo('normal',1); // opacity
			  },
        events: events
      });
    });
  </script>
  <style>
  body {
    margin: 40px 10px;
    padding: 0;
    font-family: "Lucida Grande",Helvetica,Arial,Verdana,sans-serif;
    font-size: 14px;
  }

  #calendar {
    max-width: 900px;
    margin: 0 auto;
  }

  .fc-content {
    height: 30px;
  }
  
  span.fc-title {
    display: block;
  }
  
  span.fc-time {
    display: none;
  }
  
  td.fc-day:hover{
    background: lightgreen;
  }
  
  /*Allow pointer-events through*/
  .fc-slats, /*horizontals*/
  .fc-content-skeleton, /*day numbers*/
  .fc-bgevent-skeleton /*events container*/{
    pointer-events:none
  }

  /*Turn pointer events back on*/
  .fc-bgevent,
  .fc-event-container{
    pointer-events:auto; /*events*/
  }
  </style>
</head>
<body>
  <div id="calendar" class="fc fc-ltr ui-widget"></div>	
</body>
</html>
