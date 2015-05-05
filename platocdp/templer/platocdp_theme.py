import copy

from platocdp.templer.platocdp_plone import PlatoCDPPlone
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class PlatoCDPTheme(PlatoCDPPlone):
    _template_dir = 'templates/platocdp_theme'
    summary = 'A comprehensive Plone package for PlatoCDP theme projects'
