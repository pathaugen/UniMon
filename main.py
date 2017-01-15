
import webapp2
#import time # Used for delaying a few seconds for testing
#import json
import os
import re

from google.appengine.api import users

import constants as c

# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
class MainPage(webapp2.RequestHandler):
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    def post(self): # Run when a page POST happens
        self.response.write(fh5_post_ajax(self.request))
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    def get(self): # Run when a page is requested (not POST)
        
        # https://developers.google.com/appengine/docs/python/users/userclass#User_email
        if not users.get_current_user():
            c.EMAIL = ''
            #c.REDIRECT = users.create_login_url('/xxx/xxx') # TODO: Should be the current page
            c.REDIRECT = None
        else:
            c.EMAIL = users.get_current_user().email()
            c.REDIRECT = None
        
        if c.REDIRECT:
            #c.WARNINGS_DOMAIN = []
            #c.WARNINGS_PAGE = []
            #c.WARNINGS_ADMIN = []
            #c.WARNINGS_DEV = []
            self.redirect(c.REDIRECT)
        else:
            self.response.headers['Content-Type'] = 'text/html'
            
            
            # ---------- ---------- ---------- ---------- ---------- #
            # Warnings
            #warnings = []
            #warnings.append('This is a test 111')
            #warnings.append('This is another test 222')
            # ---------- ---------- ---------- ---------- ---------- #
            
            
            # ---------- ---------- ---------- ---------- ---------- #
            # Build which admin pages will be loaded
            #admin = []
            #admin_title_content = ( 'Testing Title', '<div>This is a test</div>' )
            #admin.append( admin_title_content )
            # ---------- ---------- ---------- ---------- ---------- #
            
            
            # ---------- ---------- ---------- ---------- ---------- #
            # Experiments
            
            # website.com/this-page/that-page/final-page
            # page name: final-page
            # page parent: that-page
            #    Creating new: checks parent and children for existing name
            # sitemap: all pages and the UID of each
            
            servername = os.environ['SERVER_NAME']
            
            currentpath = os.environ['PATH_INFO']
            p = re.compile('(/|\\\| |\'|")')
            currentpath = p.sub('', currentpath)
            if currentpath == '': currentpath = 'index'
            
            content = ''
            content += '''
                <div style="width:50%;padding:2%;background-color:lightblue;color:black;">
                    <div>currentdomain = {SERVERNAME}</div>
                    <div>currentpath = {CURRENTPATH}</div>
                </div>
            '''
            content = content.replace('{SERVERNAME}', servername)
            content = content.replace('{CURRENTPATH}', currentpath)
            # ---------- ---------- ---------- ---------- ---------- #
            
            #html = get_framework( content ) # Send content, warnings, admin
            
            self.response.write( content )
    # ---------- ---------- ---------- ---------- ---------- #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
application = webapp2.WSGIApplication([
    # ---------- ---------- ---------- ---------- ---------- #
    # MainPage that is the default for all URLs sans the ones listed above. All URLs go to MainPage: /index, /contact, etc.
    ('/.*', MainPage)
    # ---------- ---------- ---------- ---------- ---------- #
], debug=True)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

