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

    * Install a default configuration:
    * `raptus.article.listings <http://pypi.python.org/pypi/raptus.article.listings>`_
    * `raptus.article.gallery <http://pypi.python.org/pypi/raptus.article.gallery>`_
    * `raptus.article.links <http://pypi.python.org/pypi/raptus.article.links>`_
    * `raptus.article.files <http://pypi.python.org/pypi/raptus.article.files>`_
    * `raptus.article.teaser <http://pypi.python.org/pypi/raptus.article.teaser>`_
    * `raptus.article.reference <http://pypi.python.org/pypi/raptus.article.reference>`_

Dependencies:

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
This short documentation provide only the range of standard default installation.
For more information and how to use the other extensions please have a look on the
`end-user documentations <http://...>`_ on plone.org. 

1.) Add a new Article (Page) from the "Add new" menu.

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
  (Integrate your files easy to article)

- `raptus.article.gallery <http://pypi.python.org/pypi/raptus.article.gallery>`_
  (The easy way to create a gallery in your article)
  
- `raptus.article.images <http://pypi.python.org/pypi/raptus.article.images>`_
  (Give you the possibility to add links in your article)

- `raptus.article.links <http://pypi.python.org/pypi/raptus.article.links>`_
  (The easy way to create tables in your article)

- `raptus.article.listings <http://pypi.python.org/pypi/raptus.article.listings>`_
  (The easy way to list your subarticles)

- `raptus.article.reference <http://pypi.python.org/pypi/raptus.article.reference>`_
  (Give you the possibility to add internal and external references to article)

- `raptus.article.teaser <http://pypi.python.org/pypi/raptus.article.teaser>`_
  (Give you the possibility to display several components like article, image as teaser)

The following additional packages are currently available for raptus.article and their zcml will be included
by raptus.article.default and they will be installed if present.

- `raptus.article.additionalwysiwyg <http://pypi.python.org/pypi/raptus.article.additionalwysiwyg/>`_
  (Gives you the possibility to separate your text in e second WYSIWYG editor. So you can for example 
  write text above and bellow an image.)
  
- `raptus.article.contentfader <http://pypi.python.org/pypi/raptus.article.contentfader>`_
  (Give you the possibility to fade through your subcontents)
  
- `raptus.article.contentflow <http://pypi.python.org/pypi/raptus.article.contentflow>`_
  (Browse throgh your subarticles as you know from iTunes)
  
- `raptus.article.fader <http://pypi.python.org/pypi/raptus.article.fader>`_
  (Give you the possibility to fade through your images)
  
- `raptus.article.flash <http://pypi.python.org/pypi/raptus.article.flash>`_
  (Integrate your flash files easy to article)
  
- `raptus.article.form <http://pypi.python.org/pypi/raptus.article.form>`_
  (Integrate PloneFormGen for forms. Create your own forms in your article)
  
- `raptus.article.header <http://pypi.python.org/pypi/raptus.article.header>`_
  (Define your own banner image for every article)
  
- `raptus.article.hidecolumns <http://pypi.python.org/pypi/raptus.article.hidecolumns>`_
  (Give you the possibility to hide some rows in the table component of an article)
  
- `raptus.article.lightbox <http://pypi.python.org/pypi/raptus.article.lightbox>`_
  (Give you the possibility to display your images in a lightbox)
  
- `raptus.article.lightboxgallery <http://pypi.python.org/pypi/raptus.article.lightboxgallery>`_
  (Give you the possibility to display your galleries in a lightbox with a carousel bellow the images)
  
- `raptus.article.maps <http://pypi.python.org/pypi/raptus.article.maps>`_
  (Integrate Plone Google Maps in your article)
  
- `raptus.article.media <http://pypi.python.org/pypi/raptus.article.media>`_
  (Give you the possibility to add your own videos and audio files or to embedded one from 
  video portals like youtube)
  
- `raptus.article.multilanguagefields <http://pypi.python.org/pypi/raptus.article.multilanguagefields>`_
  (Give you the possibility to translate your article in several languages)
  
- `raptus.article.nesting <http://pypi.python.org/pypi/raptus.article.nesting>`_
  (Give you the possibility to configure if your subarticle should be listed in a cowerflow, fader, etc.)
  
- `raptus.article.randomcontent <http://pypi.python.org/pypi/raptus.article.randomcontent>`_
  (Give you the possibility to display your subarticles by random)
  
- `raptus.article.randomimage <http://pypi.python.org/pypi/raptus.article.randomimage>`_
  (Give you the possibility to display your images by random)
  
- `raptus.article.table <http://pypi.python.org/pypi/raptus.article.table>`_
  (The easy way to create tables in your article)
  
- `raptus.article.upload <http://pypi.python.org/pypi/raptus.article.upload>`_
  (Create an upload tab for raptus.article. Use the product collective.uploadify and give you the
  possibility to upload several files at the same time)

Extend your article
-------------------
The raptus.article is so easy to extend. Just add the desired raptus.article packages to the "eggs" list 
in your buildout.cfg. The whole rest is handled by raptus.article.default.

Note that it's not necessary to add the zcml files for raptus.article extensions in your buildout.cfg
if you are using raptus.article.default.

Copyright and credits
=====================

raptus.article is copyrighted by raptus_, and licensed under the GPL. 
See LICENSE.txt for details.

.. _raptus: http://raptus.com/ 