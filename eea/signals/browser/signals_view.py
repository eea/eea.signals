from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime



class SignalsView(BrowserView):
    """ View to use within signals_view template.
    """

    @property
    def old_reports(self):
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

    @property
    def more_info_document(self):
        obj = self.context.restrictedTraverse('more')
        return {
            'title': obj.getTitle(),
            'description': obj.getDescription(),
            'url': obj.absolute_url(),
        }

