from Products.Five import BrowserView


class SubFolderView(BrowserView):
    """ View that shows the contents of all subfolders in the context folder
    """

    @property
    def subfolders(self):
        """Get the folderish items in cachable list/dict format"""
        res = []
        for folder in self.context.getFolderContents():
            if folder.portal_type == 'Folder':
                brains = folder.getObject().getFolderContents()
            elif folder.portal_type in ['Topic', 'RichTopic']:
                brains = folder.getObject().queryCatalog()
            else:
                continue
            contents = []
            for brain in brains:
                contents.append({
                    'title': brain.Title,
                    'description': brain.Title,
                    'url': brain.getURL(),
                    'portal_type': brain.portal_type,
                })
            res.append({
                'title': folder.Title,
                'description': folder.Description,
                'url': folder.getURL(),
                'contents': contents,
            })
        return res

    @property
    def nonfolders(self):
        """Get the non-folderish items in cachable list/dict format"""
        res = []
        for brain in self.context.getFolderContents():
            if brain.portal_type not in ['Folder', 'Topic', 'RichTopic']:
                res.append({
                    'title': brain.Title,
                    'description': brain.Description,
                    'url': brain.absolute_url,
                    'portal_type': brain.portal_type,
                })
        return res
