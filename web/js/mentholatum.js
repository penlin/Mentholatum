/* calendar javascript */
function initFullCalendar(events) {
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
}

