__module_name__ = "Scoutlink JOTI xchat op script" 
__module_version__ = "1.0" 
__module_description__ = "A script to assist JOTI ops in managing their channels on Scoutlink."

import xchat

is_live = false

global_ops_list = Op[]

print "\0034",__module_name__, __module_version__,"has been loaded\003"

#when enabled
#find channels opped in (allow for enable on a channel by channel basis.)

#watch those channels for
#   idle people
#   swearing people
#   flooding people

#notify idle people they are idle automaticly
#record who is due to be idle kicked (nicks red?)
#(intelligent kick?)

#watch for swearing people
#warn people automatically about rudeness.
#record people who need a rude kick (nicks red?)
#warn if channel too busy..

#add the following options to the dropdown menu on nickname rightclick.
#   warn/kick idle
#   warn/kick rude
#   warn/kick flood
#   language warnings (english, spanish, french, german etc.)
#   language kicks
#   automatic half hour ban for all 4 reasons.


