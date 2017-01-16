
UniMon
======

UniMon is a solution for unifying agent and agent-less servers together under a unified dashboard.

* Code publicly hosted on GitHub: <https://github.com/pathaugen/unimon>
* Utilizing Travis CI for builds: <https://travis-ci.org/pathaugen/unimon>
* Running on Google App Engine (GAE): <https://pmd-unimon.appspot.com/>

---------- ---------- ---------- ---------- ----------

External Backend Libraries and Resources Utilized in Application
----------------------------------------------------------------

* AWS CloudWatch <https://aws.amazon.com/cloudwatch/>
* AWS Boto 3 Python SDK <https://github.com/boto/boto3>
* GAE Stackdriver <https://cloud.google.com/monitoring/> (API <https://cloud.google.com/monitoring/api/v3/>)

---------- ---------- ---------- ---------- ----------

External Frontend Libraries and Resources Utilized in Application
----------------------------------------------------------------

* Font Awesome 4.7.0: <http://fontawesome.io/>
* jQuery 3.1.1: <http://jquery.com/>
* jQuery UI 1.12.1: <http://jqueryui.com/>
* Chart.js <http://www.chartjs.org/> (e.g. <http://www.chartjs.org/docs/#line-chart-introduction>)
* (future if budgeted) Highcharts <http://www.highcharts.com/> (e.g. <http://www.highcharts.com/demo/line-time-series/dark-unica>)

---------- ---------- ---------- ---------- ----------

Feature List
------------

* Backend:
  * Custom backend in Python hosted on Google App Engine
  * Utilization of pure HTML/CSS/JS to keep frontend updates to app simple
  * Login via Google credentials to internal dashboard
  * Dashboard for viewing monitoring data
  * Continuous Integration via Travis CI autodeploys on GitHub master branch checkin

* Frontend:
  * Responsive design
  * Chart.js library for visualization of data

---------- ---------- ---------- ---------- ----------

Resources
---------

* Google App Engine: <https://cloud.google.com/appengine/>
* Google Hosted Libraries: <https://developers.google.com/speed/libraries/>
* Markdown Syntax: <http://daringfireball.net/projects/markdown/syntax>
