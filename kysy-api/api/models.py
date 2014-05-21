# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class QaAchievements(models.Model):
    user_id = models.IntegerField(unique=True)
    first_visit = models.DateTimeField(blank=True, null=True)
    oldest_consec_visit = models.DateTimeField(blank=True, null=True)
    longest_consec_visit = models.IntegerField(blank=True, null=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    total_days_visited = models.IntegerField(blank=True, null=True)
    questions_read = models.IntegerField(blank=True, null=True)
    posts_edited = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'qa_achievements'

class QaBlobs(models.Model):
    blobid = models.BigIntegerField(primary_key=True)
    format = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    filename = models.CharField(max_length=255, blank=True)
    userid = models.IntegerField(blank=True, null=True)
    cookieid = models.BigIntegerField(blank=True, null=True)
    createip = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'qa_blobs'

class QaBuilder(models.Model):
    name = models.CharField(unique=True, max_length=64)
    content = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'qa_builder'

class QaCache(models.Model):
    type = models.CharField(max_length=8)
    cacheid = models.BigIntegerField()
    content = models.TextField()
    created = models.DateTimeField()
    lastread = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'qa_cache'

class QaCategories(models.Model):
    categoryid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=80)
    tags = models.CharField(max_length=200)
    content = models.CharField(max_length=800)
    qcount = models.IntegerField()
    position = models.IntegerField()
    backpath = models.CharField(max_length=804)
    class Meta:
        managed = False
        db_table = 'qa_categories'

class QaCategorymetas(models.Model):
    categoryid = models.ForeignKey(QaCategories, db_column='categoryid')
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=8000)
    class Meta:
        managed = False
        db_table = 'qa_categorymetas'

class QaContentwords(models.Model):
    postid = models.ForeignKey('QaPosts', db_column='postid')
    wordid = models.ForeignKey('QaWords', db_column='wordid')
    count = models.IntegerField()
    type = models.CharField(max_length=4)
    questionid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_contentwords'

class QaCookies(models.Model):
    cookieid = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField()
    createip = models.IntegerField()
    written = models.DateTimeField(blank=True, null=True)
    writeip = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'qa_cookies'

class QaIplimits(models.Model):
    ip = models.IntegerField()
    action = models.CharField(max_length=1)
    period = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_iplimits'

class QaMessages(models.Model):
    messageid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=7)
    fromuserid = models.IntegerField()
    touserid = models.IntegerField()
    content = models.CharField(max_length=8000)
    format = models.CharField(max_length=20)
    created = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'qa_messages'

class QaOptions(models.Model):
    title = models.CharField(primary_key=True, max_length=40)
    content = models.CharField(max_length=8000)
    class Meta:
        managed = False
        db_table = 'qa_options'

class QaPages(models.Model):
    pageid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=80)
    nav = models.CharField(max_length=1)
    position = models.IntegerField(unique=True)
    flags = models.IntegerField()
    permit = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=200)
    heading = models.CharField(max_length=800, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'qa_pages'

class QaPostmetas(models.Model):
    postid = models.ForeignKey('QaPosts', db_column='postid')
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=8000)
    class Meta:
        managed = False
        db_table = 'qa_postmetas'

class QaPosts(models.Model):
    postid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=8)
    parentid = models.ForeignKey('self', db_column='parentid', blank=True, null=True, related_name='parent_post')
    categoryid = models.ForeignKey(QaCategories, db_column='categoryid', blank=True, null=True)
    catidpath1 = models.IntegerField(blank=True, null=True)
    catidpath2 = models.IntegerField(blank=True, null=True)
    catidpath3 = models.IntegerField(blank=True, null=True)
    acount = models.IntegerField()
    amaxvote = models.IntegerField()
    selchildid = models.IntegerField(blank=True, null=True)
    closedbyid = models.ForeignKey('self', db_column='closedbyid', blank=True, null=True, related_name='closed_post')
    userid = models.ForeignKey('QaUsers', db_column='userid', blank=True, null=True)
    cookieid = models.BigIntegerField(blank=True, null=True)
    createip = models.IntegerField(blank=True, null=True)
    lastuserid = models.IntegerField(blank=True, null=True)
    lastip = models.IntegerField(blank=True, null=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    netvotes = models.IntegerField()
    lastviewip = models.IntegerField(blank=True, null=True)
    views = models.IntegerField()
    hotness = models.FloatField(blank=True, null=True)
    flagcount = models.IntegerField()
    format = models.CharField(max_length=20)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    updatetype = models.CharField(max_length=1, blank=True)
    title = models.CharField(max_length=800, blank=True)
    content = models.CharField(max_length=8000, blank=True)
    tags = models.CharField(max_length=800, blank=True)
    name = models.CharField(max_length=40, blank=True)
    notify = models.CharField(max_length=80, blank=True)
    class Meta:
        managed = False
        db_table = 'qa_posts'

class QaPosttags(models.Model):
    postid = models.ForeignKey(QaPosts, db_column='postid')
    wordid = models.ForeignKey('QaWords', db_column='wordid')
    postcreated = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'qa_posttags'

class QaSharedevents(models.Model):
    entitytype = models.CharField(max_length=1)
    entityid = models.IntegerField()
    questionid = models.IntegerField()
    lastpostid = models.IntegerField()
    updatetype = models.CharField(max_length=1, blank=True)
    lastuserid = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'qa_sharedevents'

class QaTagmetas(models.Model):
    tag = models.CharField(max_length=80)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=8000)
    class Meta:
        managed = False
        db_table = 'qa_tagmetas'

class QaTagwords(models.Model):
    postid = models.ForeignKey(QaPosts, db_column='postid')
    wordid = models.ForeignKey('QaWords', db_column='wordid')
    class Meta:
        managed = False
        db_table = 'qa_tagwords'

class QaTitlewords(models.Model):
    postid = models.ForeignKey(QaPosts, db_column='postid')
    wordid = models.ForeignKey('QaWords', db_column='wordid')
    class Meta:
        managed = False
        db_table = 'qa_titlewords'

class QaUserbadges(models.Model):
    awarded_at = models.DateTimeField()
    user_id = models.IntegerField()
    notify = models.IntegerField()
    object_id = models.IntegerField(blank=True, null=True)
    badge_slug = models.CharField(max_length=64, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'qa_userbadges'

class QaUserevents(models.Model):
    userid = models.ForeignKey('QaUsers', db_column='userid')
    entitytype = models.CharField(max_length=1)
    entityid = models.IntegerField()
    questionid = models.IntegerField()
    lastpostid = models.IntegerField()
    updatetype = models.CharField(max_length=1, blank=True)
    lastuserid = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'qa_userevents'

class QaUserfavorites(models.Model):
    userid = models.ForeignKey('QaUsers', db_column='userid')
    entitytype = models.CharField(max_length=1)
    entityid = models.IntegerField()
    nouserevents = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_userfavorites'

class QaUserfields(models.Model):
    fieldid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=40, blank=True)
    position = models.IntegerField()
    flags = models.IntegerField()
    permit = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'qa_userfields'

class QaUserlevels(models.Model):
    userid = models.ForeignKey('QaUsers', db_column='userid')
    entitytype = models.CharField(max_length=1)
    entityid = models.IntegerField()
    level = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'qa_userlevels'

class QaUserlimits(models.Model):
    userid = models.ForeignKey('QaUsers', db_column='userid')
    action = models.CharField(max_length=1)
    period = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_userlimits'

class QaUserlogins(models.Model):
    userid = models.ForeignKey('QaUsers', db_column='userid')
    source = models.CharField(max_length=16)
    identifier = models.CharField(max_length=1024)
    identifiermd5 = models.CharField(max_length=16)
    class Meta:
        managed = False
        db_table = 'qa_userlogins'

class QaUsermetas(models.Model):
    userid = models.ForeignKey('QaUsers', db_column='userid')
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=8000)
    class Meta:
        managed = False
        db_table = 'qa_usermetas'

class QaUsernotices(models.Model):
    noticeid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey('QaUsers', db_column='userid')
    content = models.CharField(max_length=8000)
    format = models.CharField(max_length=20)
    tags = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'qa_usernotices'

class QaUserpoints(models.Model):
    userid = models.IntegerField(primary_key=True)
    points = models.IntegerField()
    qposts = models.IntegerField()
    aposts = models.IntegerField()
    cposts = models.IntegerField()
    aselects = models.IntegerField()
    aselecteds = models.IntegerField()
    qupvotes = models.IntegerField()
    qdownvotes = models.IntegerField()
    aupvotes = models.IntegerField()
    adownvotes = models.IntegerField()
    qvoteds = models.IntegerField()
    avoteds = models.IntegerField()
    upvoteds = models.IntegerField()
    downvoteds = models.IntegerField()
    bonus = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_userpoints'

class QaUserprofile(models.Model):
    userid = models.ForeignKey('QaUsers', db_column='userid')
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=8000)
    class Meta:
        managed = False
        db_table = 'qa_userprofile'

class QaUsers(models.Model):
    userid = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    createip = models.IntegerField()
    email = models.CharField(max_length=80)
    handle = models.CharField(max_length=20)
    avatarblobid = models.BigIntegerField(blank=True, null=True)
    avatarwidth = models.IntegerField(blank=True, null=True)
    avatarheight = models.IntegerField(blank=True, null=True)
    passsalt = models.CharField(max_length=16, blank=True)
    passcheck = models.CharField(max_length=20, blank=True)
    level = models.IntegerField()
    loggedin = models.DateTimeField()
    loginip = models.IntegerField()
    written = models.DateTimeField(blank=True, null=True)
    writeip = models.IntegerField(blank=True, null=True)
    emailcode = models.CharField(max_length=8)
    sessioncode = models.CharField(max_length=8)
    sessionsource = models.CharField(max_length=16, blank=True)
    flags = models.IntegerField()
    wallposts = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_users'

class QaUservotes(models.Model):
    postid = models.ForeignKey(QaPosts, db_column='postid')
    userid = models.ForeignKey(QaUsers, db_column='userid')
    vote = models.IntegerField()
    flag = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_uservotes'

class QaWidgets(models.Model):
    widgetid = models.IntegerField(primary_key=True)
    place = models.CharField(max_length=2)
    position = models.IntegerField(unique=True)
    tags = models.CharField(max_length=800)
    title = models.CharField(max_length=80)
    class Meta:
        managed = False
        db_table = 'qa_widgets'

class QaWords(models.Model):
    wordid = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=80)
    titlecount = models.IntegerField()
    contentcount = models.IntegerField()
    tagwordcount = models.IntegerField()
    tagcount = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'qa_words'

