from subprocess import check_output

touchscreen_state = "xinput --list-props 12 | grep Enabled | awk {'print $4'}"
touchscreen_enable = 'xinput --enable 12'
touchscreen_disable = 'xinput --disable 12 && xinput --enable 14 && xinput --enable 15 '


keyboard_state = "xinput --list-props 15 | grep Enabled | awk {'print $4'}"
keyboard_enable = 'xinput --enable 14 && xinput --enable 15 '
keyboard_disable = 'xinput --disable 14 && xinput --disable 15 && xinput --enable 12 '


screen_state = "xrandr -q --verbose | grep connected | grep primary | awk {'print $6'}"
screen_normal = 'xrandr --output eDP-1 --rotate normal && xinput --enable 14 && xinput --enable 15 ' \
                '&& xinput --disable 12'
screen_inverted = 'xrandr --output eDP-1 --rotate inverted && xinput --enable 12 && xinput --disable 14 ' \
                '&& xinput --disable 15'

def cmd_exec(cmd_str):
    output = check_output(cmd_str, shell=True)
    return str(output.rstrip())
