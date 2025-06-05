from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Initialize the calendar
cal = Calendar()
cal.add('prodid', '-//AI Career Growth Roadmap//example.com//')
cal.add('version', '2.0')

# Define the start date (Tuesday, June 10, 2025)
start_date = datetime(2025, 6, 10, 9, 0, 0, tzinfo=pytz.timezone('Europe/Brussels'))

# Weekly roadmap entries
roadmap_entries = [
    "Week 1 – Scraping ID cards + Enroll in Courses + Draft CV",
    "Week 2 – Finish scraping + MLOps Intro + CV update",
    "Week 3 – OCR & text parsing + W&B Eval Intro + Portfolio planning",
    "Week 4 – Field parsing logic + MLOps CI/CD + GitHub cleanup",
    "Week 5 – LLM few-shot labeling + W&B eval logging",
    "Week 6 – Label accuracy checks + Finish MLOps + Target company list",
    "Week 7 – SLM fine-tuning start + LLM evaluation methods",
    "Week 8 – Fine-tuning eval + LinkedIn update",
    "Week 9 – Mobile deployment setup + W&B dashboards",
    "Week 10 – Deployment polish + Demo prep + Blog writing",
    "Week 11 – Final project cleanup + Course wrap-up + Job list",
    "Week 12 – Retrospective + Evaluate next steps",
]

# Create events for each week
for i, summary in enumerate(roadmap_entries):
    event = Event()
    event.add('summary', summary)
    event_start = start_date + timedelta(weeks=i)
    event_end = event_start + timedelta(hours=1)
    event.add('dtstart', event_start)
    event.add('dtend', event_end)
    event.add('dtstamp', datetime.now(pytz.utc))
    event['uid'] = f"{event_start.strftime('%Y%m%dT%H%M%S')}-ai-roadmap@example.com"
    cal.add_component(event)

# Write to disk
with open('AI_Career_Track_Roadmap.ics', 'wb') as f:
    f.write(cal.to_ical())
