Introduction
============

The new and easy way to create a site with the necessary features in a good style.
With this add-on you install default configuration of the raptus.article package.
All you need for a smart page in one step. But that's not all. If you need more
just have a look at the list of extensions and add the desired ones to your buildout.cfg. 
The rest is handled by the raptus.article.default package. 

For developers
--------------
Have a look at our developer documentation
 `http://pypi.python.org/pypi/raptus.article.core <http://pypi.python.org/pypi/raptus.article.core>`_.

The following features for raptus.article are provided by this package:

Packages
--------
    * `raptus.article.listings <http://pypi.python.org/pypi/raptus.article.listings>`_
    * `raptus.article.gallery <http://pypi.python.org/pypi/raptus.article.gallery>`_
    * `raptus.article.links <http://pypi.python.org/pypi/raptus.article.links>`_
    * `raptus.article.files <http://pypi.python.org/pypi/raptus.article.files>`_
    * `raptus.article.teaser <http://pypi.python.org/pypi/raptus.article.teaser>`_
    * `raptus.article.reference <http://pypi.python.org/pypi/raptus.article.reference>`_

Dependencies
------------
    * raptus.article.listings
    * raptus.article.gallery
    * raptus.article.links
    * raptus.article.files
    * raptus.article.teaser
    * raptus.article.reference

Installation
============

To install raptus.article.default into your Plone instance, locate the file
buildout.cfg in the root of your Plone instance directory on the file system,
and open it in a text editor.

Add the actual raptus.article.default add-on to the "eggs" section of
buildout.cfg. Look for the section that looks like this::

    eggs =
        Plone

This section might have additional lines if you have other add-ons already
installed. Just add the raptus.article.default on a separate line, like this::

    eggs =
        Plone
        raptus.article.core

Next step is to add the zcml files to the "zcml" section of
buildout.cfg. Look for the section that looks like this::

    eggs =
        Plone

This section might have additional lines if you have other zmcl's already
installed. Just add the raptus.article.default* on separate lines, like this::

    eggs =
        Plone
        raptus.article.default
        raptus.article.default-overrides
  
Note that there are two zcml files you have to register. This because
any of these register to different times, which is necassary for the product. 

Once you have added these lines to your configuration file it is time to run
buildout so the system can add and set up raptus.article.default for you. Go to the
command line, and from the root of your Plone instance (same directory as
buildout.cfg is located in), run buildout like this::

    $ bin/buildout

If everything went according to plan you now have raptus.article.default installed
in your Zope instance.

Next, start up Zope, e.g with::

    $ bin/instance fg
    
Next go to the "Add-ons" control panel in Plone as an administrator and
install the "raptus.article.default" product. You should then be able to add
a new content type called Article.

Usage
=====

1.) Add a new Article from the "Add new" menu.

- Provide a title for the new article.
- Provide a description for the article.
- Provide body text for the article.

In this page one can now add the following page elements:

- Article
- File
- Image

To change the presentation of your Article select the Tab "Components". There you
will get a list of installed layout parts (components).

Note that you have to select a component otherwise it's possible you won't see your
(for example) file in your view.

Additional components
=====================
raptus.article.default depends on the following packages and will install them accordingly:

- `raptus.article.files <http://pypi.python.org/pypi/raptus.article.files>`_
- `raptus.article.gallery <http://pypi.python.org/pypi/raptus.article.gallery>`_
- `raptus.article.images <http://pypi.python.org/pypi/raptus.article.images>`_
- `raptus.article.links <http://pypi.python.org/pypi/raptus.article.links>`_
- `raptus.article.listings <http://pypi.python.org/pypi/raptus.article.listings>`_
- `raptus.article.reference <http://pypi.python.org/pypi/raptus.article.reference>`_
- `raptus.article.teaser <http://pypi.python.org/pypi/raptus.article.teaser>`_

The following additional packages are currently available for raptus.article and their zcml will be included
by raptus.article.default and they will be installed if present.

- `raptus.article.additionalwysiwyg <http://pypi.python.org/pypi/raptus.article.additionalwysiwyg/>`_
- `raptus.article.contentfader <http://pypi.python.org/pypi/raptus.article.contentfader>`_
- `raptus.article.contentflow <http://pypi.python.org/pypi/raptus.article.contentflow>`_
- `raptus.article.fader <http://pypi.python.org/pypi/raptus.article.fader>`_
- `raptus.article.flash <http://pypi.python.org/pypi/raptus.article.flash>`_
- `raptus.article.form <http://pypi.python.org/pypi/raptus.article.form>`_
- `raptus.article.header <http://pypi.python.org/pypi/raptus.article.header>`_
- `raptus.article.hidecolumns <http://pypi.python.org/pypi/raptus.article.hidecolumns>`_
- `raptus.article.lightbox <http://pypi.python.org/pypi/raptus.article.lightbox>`_
- `raptus.article.lightboxgallery <http://pypi.python.org/pypi/raptus.article.lightboxgallery>`_
- `raptus.article.maps <http://pypi.python.org/pypi/raptus.article.maps>`_
- `raptus.article.media <http://pypi.python.org/pypi/raptus.article.media>`_
- `raptus.article.multilanguagefields <http://pypi.python.org/pypi/raptus.article.multilanguagefields>`_
- `raptus.article.nesting <http://pypi.python.org/pypi/raptus.article.nesting>`_
- `raptus.article.randomcontent <http://pypi.python.org/pypi/raptus.article.randomcontent>`_
- `raptus.article.randomimage <http://pypi.python.org/pypi/raptus.article.randomimage>`_
- `raptus.article.table <http://pypi.python.org/pypi/raptus.article.table>`_
- `raptus.article.upload <http://pypi.python.org/pypi/raptus.article.upload>`_

Extend your article
-------------------
The raptus.article is so easy to extend. Just add the desired raptus.article packages to the "eggs" list 
in your buildout.cfg. The whole rest is handled by raptus.article.default.

Note that it's not necessary to add the zcml files for raptus.article extensions in your buildout.cfg
if you are using raptus.article.default.

Copyright and credits
=====================

raptus.article is copyrighted by `Raptus AG <http://raptus.com>`_ and licensed under the GPL. 
See LICENSE.txt for details.
