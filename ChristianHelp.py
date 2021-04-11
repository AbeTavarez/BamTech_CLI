import os
from colored import fg, bg, attr
from random import randint
   


def christian_help():
  print("%s%s Hi! Christian here, how can I help? %s" % (fg(15), bg(28), attr(0)))
  user_input = int(input("%s%sPlease enter 1: to create breakout rooms, \nPlease enter 2: to spin the wheel:  %s" % (fg(15), bg(27), attr(0)) ))
  valid_entries = (1,2)
  while user_input not in valid_entries:
    print('-----------------------------\n')
    print("%s%sPlease read carefully you fool! %s" % (fg(15), bg(9), attr(0)))
    user_input = int(input("%s%sPlease enter 1: to create breakout rooms, \nPlease enter 2: to spin the wheel:  %s" % (fg(15), bg(27), attr(0)) ))
  
  
  if user_input == 1:
    breakout_room = [room for room in range(1,13)]  # Create 12 breakout rooms
    for room_num in breakout_room:
      print(f'Room {room_num} created.')
    print ("%s%s Done! Bye I need to go feed my cat... %s" % (fg(15), bg(27), attr(0)))

  if user_input == 2:
    for spin in range(3):
      print('Spinning the wheel...')
    print("%s%s\nGuess who it's Ermal !!! %s" % (fg(15), bg(61), attr(0)))
    


def download_more_ram():
  name = os.name()
  print(f"The Kernel name is: {name}")

