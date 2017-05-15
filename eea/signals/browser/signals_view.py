""" Signals View module
"""
from Products.Five import BrowserView


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
        """ Returns translated item if available
        """
        context = self.context
        try:
            return context.getCanonical().restrictedTraverse(name) \
                        .getTranslations()[context.Language()][0]
        except Exception:
            return None

    def get_old_reports(self):
        """ Returns folder named old-reports if available
        """
        folder = self._get_translated_item('old-reports')
        if folder is None:
            return None
        return {
            'folder_title': folder.Title(),
            'folder_description': folder.Description(),
            'folder_url': folder.absolute_url(),
            'contents': folder.queryCatalog(),
        }

    def get_old_articles(self):
        """ Returns folder named old-articles if available
        """
        folder = self._get_translated_item('old-articles')
        if folder is None:
            return None
        return {
            'folder_title': folder.Title(),
            'folder_description': folder.Description(),
            'folder_url': folder.absolute_url(),
            'contents': folder.queryCatalog(),
        }

    def get_chapters(self):
        """ Returns articles inside folder named chapters if available
        """
        folder = self._get_translated_item('chapters')
        if folder is None:
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
        """ Returns eyewitnesstory's inside folder named galleries if available
        """
        folder = self._get_translated_item('galleries')
        if folder is None:
            return None
        contents = []
        for brain in folder.getFolderContents(
                                    {'portal_type': ['EyewitnessStory']}):
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
        """ Returns what-is-signals document if available
        """
        doc = self._get_translated_item('what-is-signals')
        if doc is None:
            return None
        return {
            'title': doc.Title(),
            'description': doc.Description(),
            'url': doc.absolute_url(),
        }
