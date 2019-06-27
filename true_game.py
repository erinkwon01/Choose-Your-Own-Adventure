start = '''
  You wake up and you can't see anything because it's night.
  You're panicking because your friend John has left you behind
  only a granola bar to eat for the rest of the journey.
  Well, lucky for you, there is a voice to offer you choices
  throughout your journey through the dark.
  '''
  print(start)
  print("You feel a cool breeze on your left and hear the sound of metal clanging on your right.")
  print("Type 'left' to go left or 'right' to go right.")
  user_input = input()
  if user_input == "left":
      print("You decide to go left and fall straight into the ocean.") # Update to match your story.
      print("You seriously are running out of energy and feel your body cramping up.")
      print("To use the last bit of energy your body has, type 'swim' or type 'sink.'")
      user_input = input()
      if user_input == "swim":
          print("You manage to use the tiny bit of energy you have left to swim to a deserted island.")
          print("You begin to feel your eyelids closing and you slowly give in to the urge to sleep.")
          print("Or... maybe the urge isn't to sleep...")
          print("Maybe the urge is to die...")
          print("Quick! Type 'eat granola bar' to eat or 'sleep' to just give in.")
          user_input = input()
          if user_input == 'eat granola bar':
              print("You eat the granola bar and save yourself for another 5 hours until you'll feel like you need to eat again.")
              print("Good job I guess.")
              print("But now you need to find a way to find civilization again. Sigh.")
          if user_input == 'sleep':
              print("You decide to catch up on some beauty sleep at the worst time ever.")
              print("Some starving wolf finds you and eats you during your sleep.")
              print("Maybe next time, don't sleep on an island where the only source of food for other animals is you.")

      if user_input == "sink":
          print("You die.")
          print("Honestly what did you expect? You're not a mermaid.")
  user_input = input()
  if user_input == "right":
      print("You decide to follow the sound of metal clanging and feel something fuzzy.")
      print("Your face changes to confusion when the lights turn on and you see a ball of yarn in a room filled with old people knitting.")
      print("A grandma approaches you and asks if you would like a cookie.")
      print("Type 'yes' if you want to accept the offer or 'no' to reject.")
      user_input = input()
      if user_input == "yes":
          print("Knowing that you only have one more cookie, you gladly accept the offer.")
          print("The grandma gives you a cookie and you bite in.")
          print("You close your eyes as the ooey gooey cookie filled with chocolate chips instantly makes you feel better.")
          print("You look back up and see the grandma, whose warm smile slowly but surely turns into a demonic smile.")
          print("She says, 'Goodbye, child,' and you black out.")

      if user_input == "no":
          print("Despite knowing that you only have one more cookie, you refuse the offer because... stranger danger?")
          print("The expression on the grandma's face slowly changes to a demonic face of disapproval.")
          print("She says, 'Well, that's too bad. Eating the cookie might have been a less painful way to go.'")
          print("Your confused expression changes to one of pure panic when the grandma takes her large knitting needles and prepares to stab you with them.")
          print("The metal clanging that led you to this knitting club was that of these huge knitting needles.")
          print("Needless to say, you die.")

  if user_input == "left":
      print("You decide to go left and fall straight into the ocean.") # Update to match your story.
      print("You seriously are running out of energy and feel your body cramping up.")
      print("To use the last bit of energy your body has, type 'swim' or type 'sink.'")
      user_input = input()
      if user_input == "swim":
          print("You manage to use the tiny bit of energy you have left to swim to a deserted island.")
          print("You begin to feel your eyelids closing and you slowly give in to the urge to sleep.")
          print("Or... maybe the urge isn't to sleep...")
          print("Maybe the urge is to die...")
          print("Quick! Type 'eat granola bar' to eat or 'sleep' to just give in.")
          user_input = input()
          if user_input == 'eat granola bar':
              print("You eat the granola bar and save yourself for another 5 hours until you'll feel like you need to eat again.")
              print("Good job I guess.")
              print("But now you need to find a way to find civilization again. Sigh.")
          if user_input == 'sleep':
              print("You decide to catch up on some beauty sleep at the worst time ever.")
              print("Some starving wolf finds you and eats you during your sleep.")
              print("Maybe next time, don't sleep on an island where the only source of food for other animals is you.")

      if user_input == "sink":
          print("You die.")
          print("Honestly what did you expect? You're not a mermaid.")

  if user_input == "right":
      print("You decide to follow the sound of metal clanging and feel something fuzzy.")
      print("Your face changes to confusion when the lights turn on and you see yourself in a room filed with old people knitting.")
      print("A grandma approaches you and asks if you would like a cookie.")
      print("Type 'yes' if you want to accept the offer or 'no' to reject.")
      user_input = input()
      if user_input == "yes":
          print("Knowing that you only have one more granola bar, you gladly accept the offer.")
          print("The grandma gives you a cookie and you bite in.")
          print("You close your eyes as the ooey gooey cookie filled with chocolate chips instantly makes you feel better.")
          print("You look back up and see the grandma, whose warm smile slowly but surely turns into a demonic smile.")
          print("She says, 'Goodbye, child,' and you black out.")

      if user_input == "no":
          print("Despite knowing that you only have one more granola bar, you refuse the offer because... stranger danger?")
          print("The expression on the grandma's face slowly changes to a demonic face of disapproval.")
          print("She says, 'Well, that's too bad. Eating the cookie might have been a less painful way to go.'")
          print("Your confused expression changes to one of pure panic when the grandma takes her large knitting needles and prepares to stab you with them.")
          print("The metal clanging that led you to this knitting club was that of these huge knitting needles.")
          print("NEEDLEss to say, you die.")
