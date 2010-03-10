from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime



class SignalsView(BrowserView):
    """ View to use within signals_view template.

    This view expects a few folders and smartfolders to be set up:
    1. a folder w/ id 'chapters'
    2. a folder w/ id 'galleries'
    3. a smartfolder w/ id 'old-reports'
    4. a smartfolder w/ id 'old-articles'
    5. a document/page/item w/ id 'what-is-signals'
    """

    def _get_translated_item(self, name):
        try:
            return self.context.getCanonical().restrictedTraverse(name).getTranslations()[self.request['LANGUAGE']][0]
        except:
            return None

    def get_old_reports(self):
        folder = self._get_translated_item('old-reports')
        if folder == None:
            return None
        return {
            'folder_title': folder.Title(),
            'folder_description': folder.Description(),
            'folder_url': folder.absolute_url(),
            'contents': folder.queryCatalog(),
        }

    def get_old_articles(self):
        folder = self._get_translated_item('old-articles')
        if folder == None:
            return None
        return {
            'folder_title': folder.Title(),
            'folder_description': folder.Description(),
            'folder_url': folder.absolute_url(),
            'contents': folder.queryCatalog(),
        }

    def get_chapters(self):
        folder = self._get_translated_item('chapters')
        if folder == None:
            return None
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
        folder = self._get_translated_item('galleries')
        if folder == None:
            return None
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
        doc = self._get_translated_item('what-is-signals')
        if doc == None:
            return None
        return {
            'title': doc.Title(),
            'description': doc.Description(),
            'url': doc.absolute_url(),
        }

