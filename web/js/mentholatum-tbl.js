
var NOT_CONFIG_MONTH = '<p>This month has not been set yet!</p><p>Please click "Upload" button above to upload configuration file to schedule this month!</p>';

function initMentholatumTbl(result) {
  if (jQuery.isEmptyObject(result)) {
	$('#Mentholatum-tbl').html(NOT_CONFIG_MONTH);
	return
  }

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
        case '7-3\'':
          bodyHTML += ' day ';
          break;
        case '3-11\'':
          bodyHTML += ' night ';
          break;
        case '11-7\'':
          bodyHTML += ' dawn ';
          break;
        case 'OFF':
          bodyHTML += ' break ';
          break;
      }
      bodyHTML += '">' + s.replace('\'','') + '</td>';
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

function download(year, month, format) {
  var csv = ''
  $('#Mentholatum-tbl th').each(function(){
	csv = (csv + $(this).html() + ',')
  });

  csv += "\n"
  $('#Mentholatum-tbl tbody tr').each(function(){
    jQuery(this).find('td').each(function(){
		csv = (csv + $(this).html() + ',')
	})
	csv += "\n"
  });

  console.log('download ' + year.toString() + '-' + month.toString() + ' in csv format:' + csv)

  window.open("data:text/csv;charset=utf-8," + encodeURIComponent(csv))
}
