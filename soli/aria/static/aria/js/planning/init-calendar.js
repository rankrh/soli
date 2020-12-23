function initializeCalendar(events) {

    var calendarEl = document.getElementById('calendar');
    var today = new Date();

    var calendar = new FullCalendar.Calendar(calendarEl, {
    	headerToolbar: {
        	left: 'prev,next today',
        	center: 'title',
      	 	right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
      	},
      	initialDate: today,
      	navLinks: true,
      	editable: true,
      	selectable: true,
      	events: [
      		{
          title: 'First Frost',
          allDay: true,
          start: ,
        },
        {
          title: 'Meeting',
          start: '2020-09-13T11:00:00',
          constraint: 'availableForMeeting', // defined below
          color: '#257e4a'
        }
      	]
    });

	calendar.render();
}