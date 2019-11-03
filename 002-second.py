# CONTEXT PROCESSORS
    # Create a new file web/context_processors.py
        def main_context(request):

            return {
                "caption" : "Femme Caption"
            }
    # Add to settings.py (TEMPLATES/OPTIONS)

        'web.context_processors.main_context',

    <title>caption</title>  #this has to be Replaced with
    <title>{{caption}}</title>



# sample model
    class About(models.Model):
        title = models.CharField(max_length=128)
        content = models.TextField()
        image = models.ImageField(upload_to="web/about/")

        class Meta:
            db_table = 'web_about'
            verbose_name = "about"
            verbose_name_plural = "about"

        def __unicode__(self):
            return self.title

    #after every model creation/edit it should be migrated to database


# Import About model in admin.py to add data by admin
    from web.models import About


    class AboutAdmin(admin.ModelAdmin):
        list_display = ('title','content','image')

    admin.site.register(About,AboutAdmin)


#importand things to be imported in views.py
    from __future__ import unicode_literals
    from django.shortcuts import render
    from django.http.response import HttpResponse, HttpResponseRedirect
    from django.core.urlresolvers import reverse


# Define a new views.py entry
    def about(request):
        context = {
            "title" : "Femme",
            "caption" : "Femme Caption",
        }
        return render(request, 'web/about.html',context)
# Specify in url patterns (web/views.py)
    url(r'^about$', views.about,name="about"),

# update link in index 
    href = "{% url 'web:about' %}"
# Create a new page about.html and load http://localhost:8000/about


