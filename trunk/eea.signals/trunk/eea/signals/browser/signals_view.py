from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class SignalsView(BrowserView):
    """ View to use within signals_view template.
    """

    @property
    def old_reports(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        return catalog({
            'object_provides': 'eea.reports.interfaces.IReportContainerEnhanced',
            'review_state': 'published',
            'publication_groups': (u'environmental_assessment_report_2002_9',),
        })
