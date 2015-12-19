
function initMentholatumTbl(result) {
  var headHTML = '<thead><tr><th scope="col" class="Name">名字</th>';
  var bodyHTML = '<tbody>';
  var day = 1;
  $.each(result, function(name, schedule){
    bodyHTML += '<tr class="row"><td class="name-header">' + name + '</td>';
	schedule.forEach( function(s){
      if (day <= 31) {
        headHTML += '<th scope="col" class="Date">' + day + '</th>'
        day ++;
      }
      bodyHTML += '<td class="normal ';
      switch(s){
        case '7-3':
          bodyHTML += 'day ';
          break;
        case '3-11':
          bodyHTML += 'night ';
          break;
        case '11-7':
          bodyHTML += 'dawn ';
          break;
        case 'OFF':
          bodyHTML += 'break ';
          break;
      }
      bodyHTML += '">' + s + '</td>';
    });
    bodyHTML += '</tr>';
  });
  headHTML += '</tr></thead>';
  bodyHTML += '</tbody>';
  var innerHTML =  '<table class="schedule-tbl">' + headHTML + bodyHTML + '</table>';
  $('#Mentholatum-tbl').html(innerHTML);
}
