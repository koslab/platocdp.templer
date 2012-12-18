from templer.core.vars import var
from inigo.templer.localcommands import SubTemplate

class BasicPortlet(SubTemplate):
    
    _template_dir = 'templates/portlet/basic'
    summary = 'Adds a basic portlet skeleton'

    vars = [
        var('portlet_name', 'Portlet name', default='Example Portlet'),
        var('portlet_description', 'Portlet description')
    ]

    def pre(self, command, output_dir, vars):
        vars['portlet_classname'] = vars['portlet_name'].replace(" ", "")
        vars['portlet_interfacename'] = 'I' + vars['portlet_classname']
        vars['portlet_filename'] = vars['portlet_classname'].lower()
