# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kai = Character("Kai")
define sage = Character("sage")
define jax = Character("Jax")
define tal = Character("Tal")
define raven = Character("Raven")
define mommy = Character("sage's Mom")
define boss = Character("Kai's Employer")
define engineer = Character("Nikolai")
define scientist = Character("Ms. Frermi")
define hosptial = Character("Hospital Receptionist")
define n1 = Character("Nurse 1")
define n2 = Character("Nurse 2")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

#scene 1 - 15 Years Before, Kai's House
    scene kai treehouse
    # [All black. sage.]
    # 1A ALL BLACK SAGE
    
    sage "When I was younger, I had three best friends."

    sage "We were tight. Really tight."

    sage "Our mothers were all best friends, so we got their permission to hang out as much as we wanted to.
"
    sage "Only God knows how many playdates we had. We hung out every single day after school."

    sage "Our favorite spot was Kai’s house, because he had a treehouse and his moms were incredibly kind."

    sage "It got harder to stay connected when we got into our high school years, because a lot of us moved away."

    sage "But in those younger years? It was golden."

    sage "And it turned out that we had more in common than we thought."

    sage "But I’ll let you see what happened for yourself."


#scene 2 - sage's Car
    scene sage car
#scene 3 - Tal's House
    scene tal house
#scene 4 - Jax's House
    scene jax house
#scene 5 - Kai's Treehouse
    scene outside treehouse
#scene 6 - Outside Treehouse
    scene city
#scene 7 - In the City
    scene hospital
#scene 8 - Hospital
    scene college
#scene 9 - College
    scene witch house
#scene 10 - Witch
    scene witch exp room
#scene 11 - Witch's House
#scene 12 - Witch's Experimentation Room
#scene 13 - Forest
#scene 14 - Witch's House
#scene 15 - Witch's Experimentation Room
#Ending 1
#Ending 2
#Ending 3


    # This ends the game.

    return
