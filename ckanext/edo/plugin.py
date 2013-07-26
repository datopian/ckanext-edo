import routes.mapper
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
import ckan.lib.base as base


class EdoPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_public_directory(config, 'public')

        # Add this plugin's fanstatic dir.
        tk.add_resource('fanstatic', 'ckanext-edo')

    def before_map(self, route_map):
        with routes.mapper.SubMapper(route_map,
                controller='ckanext.edo.plugin:EdoController') as m:
            m.connect('privacy', '/privacy', action='privacy')
            m.connect('accessibility', '/accessibility', action='accessibility')
            m.connect('tou', '/terms-of-use', action='tou')
            m.connect('faq', '/faq', action='faq')
            m.connect('remarks-and-speeches', '/remarks-and-speeches', action='remarks_and_speeches')
            m.connect('contact', '/contact', action='contact')
        return route_map

    def after_map(self, route_map):
        return route_map


class EdoController(base.BaseController):

    def privacy(self):
        return base.render('content/privacy.html')

    def accessibility(self):
        return base.render('content/accessibility.html')

    def tou(self):
        return base.render('content/tou.html')

    def faq(self):
        return base.render('content/faq.html')

    def remarks_and_speeches(self):
        return base.render('content/remarks_and_speeches.html')

    def contact(self):
        return base.render('content/contact.html')
