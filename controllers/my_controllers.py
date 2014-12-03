import openerp.http as http
from openerp.http import request

class MyController(http.Controller):

    @http.route('/google0de4eeccbb910ddf.html', type="http", auth='none')
    def google0de4eeccbb910ddf(self):
        return "google-site-verification: google0de4eeccbb910ddf.html"
