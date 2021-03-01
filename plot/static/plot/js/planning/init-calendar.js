function initializeCalendar(events) {

    var calendarEl = document.getElementById('calendar');
    var today = new Date();

    var calendar = new FullCalendar.Calendar(calendarEl, {
    	headerToolbar: {
        	left: 'prev,next today',
        	center: 'title',
      	 	right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
      	},
      	initialDate: today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate(),
      	navLinks: true,
      	editable: true,
      	selectable: true,
      	events: [
      		{
          title: 'Business Lunch',
          start: '2020-09-03T13:00:00',
          constraint: 'businessHours'
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