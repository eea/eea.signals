from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime



class SignalsView(BrowserView):
    """ View to use within signals_view template.
    """

    def get_old_reports(self):
        now = DateTime()
        catalog = getToolByName(self.context, 'portal_catalog')
        return catalog({
            'object_provides': 'eea.reports.interfaces.IReportContainerEnhanced',
            'review_state': 'published',
            'publication_groups': (u'environmental_assessment_report_2002_9',),
            'effectiveRange': now,
            'sort_on': 'effective',
            'sort_order' : 'reverse',
        })

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
        folder = self.context.restrictedTraverse('chapters')
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
        folder = self.context.restrictedTraverse('galleries')
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
        obj = self.context.restrictedTraverse('what-is-signals')
        return {
            'title': obj.Title(),
            'description': obj.Description(),
            'url': obj.absolute_url(),
        }

