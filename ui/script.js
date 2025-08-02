async function loadSchedule() {
  const response = await fetch('../data/schedule_output.json');
  const data = await response.json();
  const select = document.getElementById('therapist-select');
  const scheduleDiv = document.getElementById('schedule');

  for (const id in data) {
    const option = document.createElement('option');
    option.value = id;
    option.textContent = data[id].name;
    select.appendChild(option);
  }

  function render() {
    const therapistId = select.value;
    scheduleDiv.innerHTML = '';
    const therapist = data[therapistId];
    if (!therapist) return;
    for (const day in therapist.schedule) {
      const dayDiv = document.createElement('div');
      dayDiv.className = 'day';
      const heading = document.createElement('h2');
      heading.textContent = day;
      dayDiv.appendChild(heading);
      therapist.schedule[day].forEach(slot => {
        const slotDiv = document.createElement('div');
        slotDiv.className = 'time-slot';
        slotDiv.textContent = `${slot.time} - ${slot.patient_name}`;
        dayDiv.appendChild(slotDiv);
      });
      scheduleDiv.appendChild(dayDiv);
    }
  }

  select.addEventListener('change', render);
  render();
}

loadSchedule();
