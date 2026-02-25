from django.db import models

# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=100,null=False)
    email = models.EmailField(unique=True, max_length=150,null=False)
    password = models.CharField(max_length=255, null=False)
    roles = (("admin", "admin"), ("reader", "reader"),("jounralist","jounralist"),('advertiser','advertiser'))
    role = models.CharField(max_length=20, choices=roles, null=False)
    phone = models.CharField(max_length=15, null=True)
    profile_image = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta: 
        db_table = "users"

    def __str__(self):
        return self.email
    

class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.category_name
    
class State(models.Model):
    state_name = models.CharField(max_length=100, null=False, unique=True)

    class Meta:
        db_table = "state"

    def __str__(self):
        return self.state_name
    
class City(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = "city"

    def __str__(self):
        return self.city_name

class News_article(models.Model):
    title = models.CharField(max_length=255, null=False)
    slug = models.CharField(max_length=255, unique=True)
    content = models.TextField(null=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    choice = (("pending", "pending"), ("approved", "approved"), ("rejected", "rejected"))
    status = models.CharField(max_length=20, choices=choice, null=False)
    is_breaking = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "news_article"

    def __str__(self):
        return self.title

class Comment(models.Model):
    article_id = models.ForeignKey(News_article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment_text = models.TextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
    
    def __str__(self):
        return self.comment_text[:20]  # Return the first 20 characters of the comment for display purposes

class ArticleTranslation(models.Model):
    article_id = models.ForeignKey(News_article, on_delete=models.CASCADE)
    language_code = models.CharField(max_length=10, null=False)
    translated_title = models.CharField(max_length=255, null=False)
    translated_content = models.TextField(null=False)

    class Meta:
        db_table = "article_translation"
    
    def __str__(self):
        return f"{self.article_id.title} - {self.language_code}"


class ArticleMedia(models.Model):
    article_id = models.ForeignKey(News_article, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=50, null=False)  # e.g., 'image', 'video'
    file_url = models.TextField(max_length=255, null=False)
    file_size = models.IntegerField(null=True)  # Size in bytes
    duration = models.IntegerField(null=True)  # Duration in seconds (for videos)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "article_media"
    
    def __str__(self):
        return f"{self.article_id.title} - {self.media_type}"
    

class CitizenReport(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    status = (("pending", "pending"), ("reviewed", "reviewed"), ("dismissed", "dismissed"))
    report_status = models.CharField(max_length=20, choices=status, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "citizen_report"
    
    def __str__(self):
        return f"{self.user_id.email} - {self.article_id.title}"


class Subscription(models.Model):

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    subscription_type = (("free", "free"), ("premium", "premium"))
    subscription_plan = models.CharField(max_length=20, choices=subscription_type, null=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "subscription"
    
    def __str__(self):
        return f"{self.user_id.email} - {self.subscription_plan}"


class Advertisement(models.Model):
    advertiser_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    placement = (("homepage", "homepage"), ("sidebar", "sidebar"))
    ad_placement = models.CharField(max_length=20, choices=placement, null=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    payment_status_choice = (("pending", "pending"), ("completed", "completed"))
    payment_status = models.CharField(max_length=20, choices=payment_status_choice, null=False)
    created_at = models.DateTimeField(auto_now_add=True)    

    class Meta:
        db_table = "advertisement"
    
    def __str__(self):
        return f"{self.advertiser_id.email} - {self.title}"
    
class AdMedia(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    file_url = models.TextField(max_length=255, null=False)
    media_type = models.CharField(max_length=50, null=False)  # e.g., 'image', 'video'

    class Meta:
        db_table = "ad_media"
    
    def __str__(self):
        return f"{self.ad_id.title} - {self.media_type}"