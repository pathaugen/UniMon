
import webapp2
from unimon.unimon import Unimon

application = webapp2.WSGIApplication([
    ('/.*', Unimon)
], debug=True)
