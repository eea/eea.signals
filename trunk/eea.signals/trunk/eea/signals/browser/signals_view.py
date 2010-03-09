from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime



class SignalsView(BrowserView):
    """ View to use within signals_view template.

    This view expects a few folders and smartfolders to be set up:
    1. a folder w/ id 'chapters'
    2. a folder w/ id 'galleries'
    3. a smartfolder w/ id 'old-reports'
    4. a document/page/item w/ id 'what-is-signals'
    """

    def get_old_reports(self):
        try:
            smartfolder = self.context.restrictedTraverse('old-reports').getTranslations()[self.request['LANGUAGE']][0]
        except:
            return None
        return {
            'folder_title': smartfolder.Title(),
            'folder_description': smartfolder.Description(),
            'folder_url': smartfolder.absolute_url(),
            'contents': smartfolder.queryCatalog(),
        }

    def get_old_articles(self):
        portal_url = getToolByName(self.context, 'portal_url')
        portal = portal_url.getPortalObject()
        try:
            article = portal.restrictedTraverse('/SITE/publications/signals-2009')
        except:
            return None
        ret = {}
        for obj in article.getRelatedItems():
            ret.append({
                'title': obj.Title(),
                'description': obj.Description(),
                'url': obj.absolute_url(),
            })
        return ret

    def get_chapters(self):
        folder = self.context.restrictedTraverse('chapters').getTranslations()[self.request['LANGUAGE']][0]
        contents = []
        for brain in folder.getFolderContents({'portal_type': ['Article']}):
            contents.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': brain.getURL(),
            })
        return {
            'folder_title': folder.Title(),
            'folder_description': folder.Description(),
            'folder_url': folder.absolute_url(),
            'contents': contents,
        }

    def get_eyewitness_stories(self):
        folder = self.context.restrictedTraverse('galleries').getTranslations()[self.request['LANGUAGE']][0]
        contents = []
        for brain in folder.getFolderContents({'portal_type': ['EyewitnessStory']}):
            contents.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': brain.getURL(),
            })
        return {
            'folder_title': folder.Title(),
            'folder_description': folder.Description(),
            'folder_url': folder.absolute_url(),
            'contents': contents,
        }

    def get_more_info_document(self):
        try:
            obj = self.context.restrictedTraverse('what-is-signals').getTranslations()[self.request['LANGUAGE']][0]
        except:
            return None
        return {
            'title': obj.Title(),
            'description': obj.Description(),
            'url': obj.absolute_url(),
        }

