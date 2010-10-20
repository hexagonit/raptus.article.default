from Products.CMFCore.utils import getToolByName

DEPENDENCIES = (
    'raptus.article.lightbox',
    'raptus.article.additionalwysiwyg',
    'raptus.article.lightboxgallery',
    'raptus.article.fader',
    'raptus.article.contentfader',
    'raptus.article.randomimage',
    'raptus.article.randomcontent',
    'raptus.article.media',
    'raptus.article.maps',
    'raptus.article.flash',
    'raptus.article.form',
    'raptus.article.hidecolumns',
    'raptus.article.header',
    'raptus.article.contentflow',
    'raptus.article.upload',
    'raptus.article.multilanguagefields',
    'raptus.article.table',
    'raptus.backlink',
)

def installDependencies(context):
    """ Installs optional dependencies
    """
    if context.readDataFile('raptus.article.default_install.txt') is None:
        return
    portal = context.getSite()
    
    inst = getToolByName(portal, 'portal_quickinstaller')
    for prod in DEPENDENCIES:
        try:
            if not inst.isProductInstalled(prod):
                inst.installProduct(prod)
            else:
                inst.reinstallProducts(prod)
        except:
            pass
