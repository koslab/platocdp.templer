import copy

from platocdp.templer.platocdp_plone import PlatoCDPPlone
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class PlatoCDPI18NOverride(PlatoCDPPlone):
    _template_dir = 'templates/platocdp_i18noverride'
    summary = 'A package for overriding translation'
