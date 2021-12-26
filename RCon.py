import ui
from mcrcon import MCRcon
import config

def send_cmd(sender):
	command = v["command"].text
	
	resp = mcr.command(command)
	
	v["console"].text += f"\n⇥ {command}\n{resp}"
	v["command"].text = ""

def clear(sender):
	v["console"].text = ""
	
def close(sender):
	mcr.disconnect()
	sender.superview.close()

mcr = MCRcon(config.IP, config.PASSWORD, config.PORT)
mcr.connect()

v = ui.load_view()
v.present('sheet')
