
import sys
import time
from hacker import hacker_text
from banners import * 
from colours import *
from configparser import ConfigParser
from clear import clear



# Reading the config.ini file
config_object=ConfigParser()
config_object.read("config.ini")
user_choice=config_object["USER_CHOICE"]


def typex(text,speed,colour):
    print(" "+colour)
    speed=float(speed)
    for character in text:
        
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    
    print(" "+reset)

def config():
    speed=0.001
    current_settings()
    typex(config_banner,speed,magenta)
    typex("Settings:",speed,white)
    typex(config_menu,speed,white)
    user_config = (input("(config)>>"))
    
    if user_config == "1":
        change_colour()
    elif user_config == "2":
        change_speed()
    elif user_config == "3":
        change_mode()


#main function
def type_writer():
    print_banners("t")
    colour=user_choice["colour"]
    typex(ask_for_input,0.01,yellow)
    typex("Type 'config:' to change the configuration settings;Type 'quit:' to quit",0.01,colour)
    while True:
        text=str(input(">>"))
        speed=user_choice["speed"]
        colour=user_choice["colour"]
        if text == "config:":
            config()
        elif text=="quit:":
            quit()
        else:
            typex(text,speed,colour)


def print_banners(x):
    speed=0.001
    if x == "t":
        typex(type_banner,speed,cyan)
        typex(by_mathenge,speed,green)
    elif x == "h":
        typex(hacker_banner,speed,cyan)
        typex(by_mathenge,speed,green)

#changing mode
def hacker_mode():
    print_banners("h")
    typex(hacker_text,0.001,green)
    change_mode_to_typewriter_mode()


def change_mode_to_hackermode():
    print("Changing to hackermode!!")
    user_choice["mode"]="hacker"
    with open("config.ini",'w') as conf:
        config_object.write(conf)
    hacker_mode()

def change_mode_to_typewriter_mode():
    print("Changing to TypeWriter!!")
    user_choice["mode"]="typewriter"
    with open("config.ini",'w') as conf:
        config_object.write(conf)
    type_writer()

    
def check_mode():
    mode = user_choice["mode"]
    if mode == "typewriter":
        type_writer()
    else:
        hacker_mode()
        
def change_colour():
    colour_menu = " \n Change Color To :\n 1.Cyan \n 2.Magenta \n 3.Green \n 4.Red \n 5.Blue \n 6.White \n ---------------- \n 7.Quit"
    typex(colour_menu,0.01,white)
    user_colour_input = str(input("(config) \ Color >>"))
    if user_colour_input == "1":
        change_colour_to_cyan()
    elif user_colour_input == "2":
        change_colour_to_magenta()
    elif user_colour_input == "3":
        change_colour_to_green()
    elif user_colour_input == "4":
        change_colour_to_red()
    elif user_colour_input == "5":
        change_colour_to_blue()
    elif user_colour_input == "6":
        change_colour_to_white()
    elif user_colour_input == "7":
        type_writer()

def change_speed():
    speed_menu = " \n Change Speed To :\n 1.Fast \n 2.Moderate \n 3.Slow \n ---------------- \n 4.Quit"
    typex(speed_menu,0.01,white)
    user_speed_input = str(input("(config) \ Speed >>"))
    if user_speed_input == "1":
        change_speed_to_fast()
    elif user_speed_input == "2":
        change_speed_to_moderate()
    elif user_speed_input == "3":
        change_speed_to_slow()
    elif user_speed_input == "4":
        type_writer()
        
def change_mode():
    if user_choice["mode"] == "typewriter":
        change_mode_to_hackermode()
    elif user_choice["mode"] == "hacker":
        print_banners()
        type_writer()
        
    

def update():
    with open("config.ini",'w') as conf:
        config_object.write(conf)

#changing colour
def change_colour_to_cyan():
    user_choice["colour"]=cyan
    print(" \n Color changed to Cyan!")
    update()
        
def change_colour_to_magenta():
    user_choice["colour"]=magenta
    update()
    print(" \n Color changed to Magenta!")
    type_writer()
        
def change_colour_to_green():
    user_choice["colour"]=green
    update()
    print(" \n Color changed to Green!")
    type_writer()
    
def change_colour_to_red():
    user_choice["colour"]= red
    update()
    print(" \n Color changed to Red!")
    type_writer()
    
def change_colour_to_blue():
    user_choice["colour"]=blue
    update()
    print(" \n Color changed to Blue!")
    type_writer()
    
def change_colour_to_white():
    user_choice["colour"]=white
    update()
    print(" \n Color changed to White!")
    type_writer()


#changing speed
def change_speed_to_fast():
    user_choice["speed"]="0.01"
    update()
    print(" \n Speed changed to fast!")
    type_writer()
def change_speed_to_moderate():
    user_choice["speed"]="0.05"
    update()
    print(" \n Speed changed to moderate!")
    type_writer()
def change_speed_to_slow():
    user_choice["speed"]="0.1"
    update()
    print(" \n Speed changed to slow!")
    type_writer()
    
def current_settings():
    speed=str(user_choice["speed"])
    colour=user_choice["colour"]
    mode=user_choice["mode"]
    print("Current mode:",mode)
    print(""+colour)
    print("Current Color"+reset)
    current_speed=''
    if speed=="0.05":
        current_speed="Moderate"
    elif speed=="0.01":
        current_speed="Fast"
    elif speed=="0.1":
        current_speed="Slow"
        
    print(current_speed)
    
        
clear()   
check_mode()
