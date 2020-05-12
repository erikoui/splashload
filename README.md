## splashload
Lightweight splash art viewer while another program is loading on linux

# Requirements: 
OpenCV2

# How to use:
1. Change the name of the process you want to add your splash art in splashload.py
2. Add your picture as image.jpg in the same folder as splashload.py
3. Run the splashed program by `python3 path/to/splashload/splashload.py & splashed_program`

# Example using as an i3 keybind and polo file manager:
`~/.config/i3/config`:
``` bash
bindsym $mod+m exec python3 ~/Documents/splashload/src/splashload.py & polo-gtk ~
```
