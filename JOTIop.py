__module_name__ = "Scoutlink JOTI xchat op script" 
__module_version__ = "1.0" 
__module_description__ = "A script to assist JOTI ops in managing their channels on Scoutlink."

import xchat
import ConfigParser

is_live = False

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

'''
For every channel joined there is a channel class,
when enabled this will hold all od the users and 
ban information
'''
class Channel:
    def __init__(self, name):
        self.name = name                #stores chanel name.
        self.users = set()              #stores a User object for everyone in the channel.
        self.banned_users = set()       #a set of CURRENTLY BANNED users.
        #self.ops = Op[]
        #self.user_limit = user_limit

    '''
    Function is called when you choose to become an operator
    in said channel. This class is responsible for populating
    the users variable. Creating the log file etc.
    '''
    def enable_op(self):
        pass

    '''
    Function is called when you choose to stop being an operator
    in the channel. It is responsible for removing and bans set,
    and depopulating all of the fields that have been used in this
    session.
    '''
    def disable_op(self):
        pass

    def check_idle(self):
        pass

class User:
    def __init__(self, name, host):
        self.nickname = name
        self.hostmask = host
        self.warn_rude = 0
        self.warn_flood = 0
        self.warn_idle = False
        self.minutes_idle = 0
        self.kick_rude = 0
        self.kick_flood = 0

    def warn_notice(self, message):
        pass

    def warn_channel(self, message, channel):
        pass

def on_text(word, word_eol, userdata):
    print word, word_eol, userdata
    dest = xchat.get_context().get_info("channel")
    
def on_join(word, word_eol, userdata):
    print word, word_eol, userdata

def on_part(word, word_eol, userdata):
    print word, word_eol, userdata

xchat.hook_print('Channel Message', on_text)
xchat.hook_print('Join', on_join)
xchat.hook_print('Part', on_part)
#xchat.hook_print('Change Nick', on_change_nick)
