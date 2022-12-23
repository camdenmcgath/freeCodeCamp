def add_time(start, duration, day=None):
  # Split data into hour, minute, and AM/PM
  # for easier calculations
  start = start.split()
  ampm = start[1]
  start = start[0].split(":")
  dur = duration.split(":")
  starthr = int(start[0])
  startmin = int(start[1])
  durhr = int(dur[0])
  durmin = int(dur[1])

  # Check if summing minutes changes the hour
  if ((startmin + durmin) // 60) > 0:
      starthr += 1
  # Calculate days passed
  dayslater = ""
  days = (starthr + 12 + durhr) // 24
  if ampm == "PM":
      if days == 1:
          dayslater = "(next day)"
      elif days > 1:
          dayslater = f"({days} days later)"
  else:
      days = (starthr + durhr) // 24
      if days == 1:
          dayslater = "(next day)"
      elif days > 1:
          dayslater = f"({days} days later)"

  # Fucntion to Calculate day of week
  def current_day(pday, pdays):
      weekdays = [
          "Sunday",
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday",
      ]
      # Convert str pday to list to ensure
      # correct case for searching weekdays list
      dlist = list(pday)
      pday = dlist[0].upper()
      for i in dlist[1:]:
          i = i.lower()
          pday += i
      current_day = weekdays[(weekdays.index(pday) + days) % 7]
      return current_day

  # Set AM/PM
  halfdays = (starthr + durhr) // 12
  if halfdays > 0:
      if (halfdays % 2) != 0:
          if ampm == "AM":
              ampm = "PM"
          else:
              ampm = "AM"

  # Calculate new values for new time
  hrrollover = (starthr + durhr) % 12
  if hrrollover == 0:
      newhr = "12"
  else:
      newhr = str(hrrollover)
  newmin = str((startmin + durmin) % 60)

  # Assign the return variable add_time to correct time and output format
  if day == None and dayslater == "":
      new_time = newhr + ":" + newmin.zfill(2) + " " + ampm
  elif day == None and dayslater != "":
      new_time = newhr + ":" + newmin.zfill(2) + " " + ampm + " " + dayslater
  elif day != None and dayslater == "":
      new_time = newhr + ":" + newmin.zfill(
          2) + " " + ampm + ", " + current_day(day, days)
  elif day != None and dayslater != "":
      new_time = (newhr + ":" + newmin.zfill(2) + " " + ampm + ", " +
                  current_day(day, days) + " " + dayslater)

  return new_time
