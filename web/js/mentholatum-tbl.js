
function initMentholatumTbl(result) {
  var headHTML = '<thead><tr><th scope="col" class="Name">名字</th>';
  var bodyHTML = '<tbody>';
  var headerRenderDone = false;
  $.each(result, function(name, schedule){
    bodyHTML += '<tr class="row"><td class="name-header">' + name + '</td>';
    var day = 1;
	schedule.forEach( function(s){
      if (!headerRenderDone) {
        headHTML += '<th scope="col" class="Date d' + day + '">' + day + '</th>'
      }
      bodyHTML += '<td class="normal d' + day;
      switch(s){
        case '7-3':
          bodyHTML += ' day ';
          break;
        case '3-11':
          bodyHTML += ' night ';
          break;
        case '11-7':
          bodyHTML += ' dawn ';
          break;
        case 'OFF':
          bodyHTML += ' break ';
          break;
      }
      bodyHTML += '">' + s + '</td>';
      day++;
    });
    bodyHTML += '</tr>';
    headerRenderDone = true;
  });
  headHTML += '</tr></thead>';
  bodyHTML += '</tbody>';
  var innerHTML =  '<table class="schedule-tbl">' + headHTML + bodyHTML + '</table>';
  $('#Mentholatum-tbl').html(innerHTML);

  d = new Date();
  if (d.getFullYear() === gCurYear && d.getMonth() === (gCurMonth-1)){
    $('.d' + d.getDate()).addClass('current-date');
  }
}
