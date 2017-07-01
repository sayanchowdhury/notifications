from django.db import models

# Create your models here.
class GHUser(models.Model):
    """ Comment goes here """
    username = models.CharField(max_length=20, unique=True)


class GHProject(models.Model):
    """ Comment goes here """
    title =
    project_id = 
    project_owner = 


class GHIssues(models.Model):
    """ Comment goes here """
    title = 
    issue_repository =
    issue_repo_owner =
    issue_id =
    issue_body =
    issue_body_html =
    issue_comments_count =
    issue_created_at =
    issue_last_modified =
    issue_updated_at =


class GHPullRequest(models.Model):
    """ Comment goes here """
    title =
    pr_repository = # CharField
    pr_repo_owner = # User
    pr_id = #Integer
    pr_body = #TextField
    pr_body_html = #TextField
    pr_review_comments_count = #Inger
    pr_mergeable = #Boolean
    pr_merged = #Boolean
    pr_merged_at = #DateTime
    pr_merged_by = # User
    pr_created_at = # DateTime
    pr_last_modified = # DateTime
    pr_updated_at = # DateTime
