from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.core.models import Base, Slugged


class Provider(Base):
    """
    Comment goes here
    """
    name = models.CharField(
        _("Provider Name"), max_length=255, db_index=True,
        help_text=_("Name of the Provider"))

    def __str__(self):
        return self.name


class Project(Base, Slugged):
    """
    Comment goes here.
    """
    name = models.CharField(
        _("Project Name"), max_length=255, db_index=True,
        help_text=_("Name of the Project"))

    description = models.CharField(
        _("Project Description"), max_length=255, null=True, blank=True,
        help_text=_("Description of the Project"))

    provider_id = models.IntegerField(
        _("Provider ID"), help_text=_("ID of the Provider"))

    def __str__(self):
        return "%s: %s" % (self.provider_id, self.name)


class GithubProject(Project):
    """
    Comment goes here.
    """
    project_id = models.IntegerField(
        _('Project ID'), help_text=_("ID of the Project in Github"))

    full_name = models.CharField(
        _('Full Length'), max_length=255,
        help_text=_("Full Name of the Project in Github,"
                    "<username>/<projectname>"))

    is_fork = models.BooleanField(
        _("Forked?"), default=False, help_text=_("Is the project forked?"))

    open_issues_count = models.IntegerField(
        _("Open Issues Count"), help_text=_("Number of open issues?"))

    created_at = models.DateTimeField(
        _("Created at"), help_text=_("Timestamp the project was created in "
                                     "Github"))

    updated_at = models.DateTimeField(
        _("Updated at"), help_text=_("Timestamp the project was last updated "
                                     "in Github"))

    pushed_at = models.DateTimeField(
        _("Pushed at"), help_text=_("Timestamp of the last push activity"))

    private = models.BooleanField(
        _("Private?"), help_text=_("Is project private?"))

    has_issues = models.BooleanField(
        _("Has Issues?"), help_text=_("Does the project have issues"))

    def __str__(self):
        return "%s: %s" % (self.provider_id, self.name)
