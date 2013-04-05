## Installation

Clone this repo:

    $ git clone git@github.com:okfn/ckanext-edo.git

Activate your virtualenv, cd into the ckanext-edo dir, and install the plugin
into your virtualenv:

    ckanext-edo $ python setup.pt develop

Add the `edo` plugin to the `plugins` list in your `development.ini` file, for
example:

    ckan.plugins = stats json_preview recline_preview datastore edo

Now when you start CKAN (`paster serve development.ini`) the `edo` plugin
should be active.
