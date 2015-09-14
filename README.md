For my text entry device I chose to make an predictive text entry pair of gloves, since I've had the idea for a similar device for quite a while. It has switches at the ends of the finger and the mbed code detects when the switch is closed and prints to serial which finger was just used. A python script running on the host machine then stores the sequence of fingers used until spacebar is reached, which is left or right thumb. When spacebar is reached, the python script looks at the recent finger sequence and picks from a dictionary of finger sequences to word mappings and outputs using system commands the correct keystrokes to the system. It also echos which fingers are pressed and which word it picks to the terminal.

The circuit is simply 10 switches hooked up to the D3-12 pins on my mbed board. I used copper thread for maximum flexibility and each glove has a strip of copper tape used for common ground, so each glove has 6 wires (5 for signals for each finger and 1 for ground). I used tape to insulate my connections and for ergonomic purposes.

This assignment was pretty awesome and it's especially cool to use it to actually output characters to my computer screen. In the future I want to have time to make a less cumbersome prototype of this device so I can use it in the real world.

https://youtu.be/80229PhfTDo
