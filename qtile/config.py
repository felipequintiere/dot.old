from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, KeyChord, Match, Screen
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy
from libqtile import hook
from libqtile import extension
import os
import subprocess

mod = "mod4"
terminal = guess_terminal()
home = os.path.expanduser("~")

settings = os.path.expanduser("~/.config/settings")
alacritty = os.path.expanduser("~/.config/alacritty")
fish= os.path.expanduser("~/.config/settings/fish.sh")


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)

@hook.subscribe.startup
def after_autostart():
    home = os.path.expanduser('~/.config/qtile/after_autostart.sh')
    subprocess.call(home)

def get_volume():
    try:
        output = subprocess.check_output(
            "pactl get-sink-volume @DEFAULT_SINK@",
            shell=True,
            text=True
        )
        for part in output.split():
            if part.endswith('%'):
                return f"vol: {part}"
        return "vol: N/A"
    except Exception:
        return "vol: Err"


keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    #Key([mod], "space", lazy.layout.next()),

    Key(["mod1","shift"], "h", lazy.window.move_floating(-100, 0)),
    Key(["mod1", "shift"], "j", lazy.window.move_floating(0, 100)),
    Key(["mod1", "shift"], "k", lazy.window.move_floating(0, -100)),
    Key(["mod1", "shift"], "l", lazy.window.move_floating(100, 0)),

    Key(["mod1", "control"], "h", lazy.window.resize_floating(-100, 0)),
    Key(["mod1", "control"], "j", lazy.window.resize_floating(0, 100)),
    Key(["mod1", "control"], "k", lazy.window.resize_floating(0, -100)),
    Key(["mod1", "control"], "l", lazy.window.resize_floating(100, 0)),

    
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key(["mod1", "shift"], "h", lazy.layout.swap_column_left()),
    Key(["mod1", "shift"], "l", lazy.layout.swap_column_right()),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod], "n", lazy.layout.normalize()),

    Key([mod], "Tab", lazy.group.next_window()),
    Key([mod, "shift"], "Tab", lazy.group.prev_window()),
    Key([mod], "space", lazy.group.next_window()),
    Key([mod, "shift"], "space", lazy.group.prev_window()),

    Key([mod], "c", lazy.window.kill()),
    Key([mod], "r", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.next_layout()),
    Key([mod, "shift"], "q", lazy.prev_layout()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    #Key([mod], "t", lazy.window.move_to_top()),
    Key([mod], "t", lazy.window.keep_above()),
    Key([mod, "shift"], "t", lazy.window.move_to_top()),

    Key([mod], "Return", lazy.spawn(fish)),
    Key([mod], "d", lazy.spawn(settings + "/dmenu_run.sh")),
    Key([mod], "p", lazy.spawn(settings + "/dmenu_scripts.sh")),
    Key([mod], "o", lazy.spawn(settings + "/dmenu_books.sh")),

    Key([mod], "x", lazy.spawn(settings + "/b_up.sh")),
    Key([mod], "z", lazy.spawn(settings + "/b_down.sh")),
    Key([mod, "shift"], "x", lazy.spawn(settings + "/inc_vol.sh")),
    Key([mod, "shift"], "z", lazy.spawn(settings + "/dec_vol.sh")),

    Key([mod, "shift"], "f", lazy.spawn("flameshot gui")),
    Key(["mod1", "shift"], "s", lazy.spawn("flameshot gui")),

    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),

    KeyChord([mod], "e", [
        #Key([mod], "a", lazy.group["0"].dropdown_toggle("term")),
        #Key([], "a", lazy.group["0"].dropdown_toggle("term")),
        #Key([mod], 'r', lazy.group['0'].dropdown_toggle('ranger manager')),
        #Key([], 'r', lazy.group['0'].dropdown_toggle('ranger manager')),
        #Key([mod], 'q', lazy.group['0'].dropdown_toggle('qtile shell')),
        #Key([], 'q', lazy.group['0'].dropdown_toggle('qtile shell')),

        Key([mod], "r", lazy.spawn(settings + "/color_inversion.sh")),
        Key([], "r", lazy.spawn(settings + "/color_inversion.sh")),

        Key([mod], "e", lazy.ungrab_chord()),
        Key([], "e", lazy.ungrab_chord()),
        Key([mod], "c", lazy.ungrab_chord()),
        ],
        name="evoker",
        #mode=True,
    ),

    KeyChord([mod], "m", [
        Key([mod], "p", lazy.spawn(alacritty + "/theme_down.sh")),
        Key([mod], "n", lazy.spawn(alacritty + "/theme_up.sh")),
        Key([], "p", lazy.spawn(alacritty + "/theme_down.sh")),
        Key([], "n", lazy.spawn(alacritty + "/theme_up.sh")),

        Key([mod], "m", lazy.ungrab_chord()),
        Key([], "m", lazy.ungrab_chord()),
        Key([mod], "c", lazy.ungrab_chord()),
        ],
        name="misc",
        #mode=True,
    ),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [
        Group("1", label="α"), 
        Group("2", label="β"),
        Group("3", label="γ"),
        Group("4", label="δ"),
        Group("5", label="ε"),
        Group("6", label="ζ"),
        Group("7", label="η"),
        Group("8", label="θ"),
        Group("9", label="ι"),

        ScratchPad('0', [
            DropDown(
                "term",
                "alacritty",
                height = 0.4,
                width = 0.8,
                on_focus_lost_hide = False,
                #opacity = 0.8,
                ),

            DropDown(
                "ranger manager",
                "alacritty -e ranger",
                x = 0.0,
                y = 0.5,
                width=0.5,
                height=0.5,
                on_focus_lost_hide = False,
                #opacity = 0.8,
                ),
            # define another terminal exclusively for ``qtile shell` at different position
            DropDown("qtile shell", "kitty -e qtile shell",
                     x=0.05, y=0.4, width=0.9, height=0.6, opacity=0.9,
                     on_focus_lost_hide=True), 
        ]),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc=f"move focused window to group {i.name}",
            ),
        ],
    ),

columns_layout = {
    "align": 1,
    "border_focus": "DE1D95",
    "border_normal": "A662DF",
    "border_focus_stack": "#47F9D5",
    "border_normal_stack": "#58A58B",
    "border_width": 2,
    "fair": False,
    "grow_amount":10,
    "initial_ratio": 1,
    "insert_position": 1,
    "margin": 4,
    "margin_on_single": None,
    "num_columns": 2,
    "single_border_width": None,
    "split": True,
    "wrap_focus_columns": True,
    "wrap_focus_rows": True,
    "wrap_focus_stacks": True,
}


layouts = [
    layout.Columns(**columns_layout),
    layout.Max(),
    #layout.MonadTall(),
    #layout.MonadWide(),
    #layout.Bsp(),
]

GroupBox_theme0 = {
    "this_current_screen_border": "DE1D95",
    "this_screen_border": "#47F9D5", 
    "active": "A662DF",
    "inactive":'ffffff80',

    "background":'000000cc',
    "block_highlight_text_color":None,
    "borderwidth":0,
    "center_aligned":True,
    "disable_drag":True,
    "fmt":'{}',
    "font":'sans',
    "fontshadow":None,
    "fontsize":16,
    "foreground":'ffffff',
    "hide_crash":False,
    "hide_unused":False,
    "highlight_method":'text',
    "invert_mouse_wheel":False,
    #"margin":3,
    "margin_x":10,
    "margin_y":3,
    "markup":False,
    "max_chars":0,
    "mouse_callbacks":{},
    "other_current_screen_border":'F2211D',
    "other_screen_border":'1DE4F2',
    #padding:10,
    #padding_x:None,
    #padding_y:None,
    "rotate":True,
    "rounded":True,
    #spacing:-10,
    "toggle":True,
}

widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=0,
)
extension_defaults = widget_defaults.copy()

bar_background = "#000000cc"
screens = [
    Screen(
        bottom=bar.Gap(5),
        left=bar.Gap(5),
        right=bar.Gap(5),

        top=bar.Bar(
            [
                #widget.TextBox(text=':|:',font='DejaVu Sans Mono',fontsize=16,padding=5,foreground='#ffffff',background=bar_background,), 
                #widget.Sep(linewidth=0, padding=10, background=bar_background),

                #widget.CurrentLayout(),
                widget.GroupBox(**GroupBox_theme0),

                widget.TaskList(
                    background=bar_background,
                    border="#de1d95cc",
                    borderwidth=0,
                    #font='',
                    fontsize=16,
                    highlight_method='block',

                    margin=0,
                    margin_y=0,
                    padding=10,
                    padding_y=5,
                    icon_size=20,
                    rounded=True,

                    #max_title_width=200,
                    #title_width_method='uniform',
                    ),

                #widget.WidgetBox(
                #    widgets=[
                #        widget.Memory(format='RAM: {MemUsed:.0f}{mm}', measure_mem='M'),
                #        widget.Sep(linewidth=0, padding=5, background=bar_background),
                #        widget.CPU(format='CPU: {load_percent}%'),
                #    ],
                #    text_closed='[+]',
                #    text_open='  [-]',
                #    close_button_location='right',
                #),

                widget.Systray(
                    background=bar_background,
                    padding=3,
                    ),

                widget.Chord(
                    background="#de1d95cc",
                    fmt= " {} ",
                    ),

                widget.TextBox(text=':|:',font='DejaVu Sans Mono',fontsize=16,padding=5,foreground='#ffffff',background=bar_background,), 

                widget.Clipboard(timeout=0),

                widget.TextBox(text=':|:',font='DejaVu Sans Mono',fontsize=16,padding=5,foreground='#ffffff',background=bar_background,), 

                widget.GenPollText(
                    func=lambda: get_volume(),
                    fontsize=16,
                    padding=0,
                    foreground='#ffffff',
                    background=bar_background,
                    update_interval=10,
                ),

                widget.TextBox(text=' ',font='DejaVu Sans Mono',fontsize=16,padding=0,foreground='#ffffff',background=bar_background,), 

                widget.GenPollCommand(
                    cmd="/bin/sh -c \"sed 's/^\\.//' ~/.config/settings/.b_log\"",
                    #direction = ,
                    fmt = "bri: {}%",
                    shell = True,
                    update_interval=10,
                    ),

                widget.TextBox(text=':|:',font='DejaVu Sans Mono',fontsize=16,padding=5,foreground='#ffffff',background=bar_background,), 

                widget.Clock(
                    format="%a %d/%m %I:%M",
                    background=bar_background,
                    ),

                widget.TextBox(text=':|:',font='DejaVu Sans Mono',fontsize=16,padding=5,foreground='#ffffff',background=bar_background,), 

                widget.QuickExit(
                    background=bar_background,
                ),
            ],
            background=bar_background,
            size=28,
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry

        Match(wm_class="PacketTracer"),
        Match(wm_class="discord"),
        Match(wm_class="steam"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
