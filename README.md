## Installation

Clone this repo:

    $ git clone git@github.com:okfn/ckanext-edo.git

Activate your virtualenv, cd into the ckanext-edo dir, and install the plugin
into your virtualenv:

    ckanext-edo $ python setup.py develop

Add the `edo` plugin to the `plugins` list in your configuration file, as well as the
following options needed:

    ckan.plugins = stats datastore disqus edo recline_view googleanalytics text_view pdf_view resource_proxy datapusher
    ckan.views.default_views = pdf_view text_view recline_view

    googleanalytics.id = UA-XXXX

    disqus.name = dataedostate

    ckan.featured_groups=  education agriculture environment finance health projects

    ckan.i18n_directory = /usr/lib/ckan/edo/src/ckanext-edo/
    ckan.locale_default = en_GB


