# Mentholatum

### Requirement
* Python 2.7
* Bottle package
* xlwt package

### Web URL
* Default page would be directed to the current month of the current year
* /[YEAR]-[MONTH], jump to the scedule of the specified month
* /export?year=[YEAR]&month=[MONTH]&fmt=['csv','excel'], download schedule in specified format

### Web Service API
* GET, /ws/calendar?month=[1-12] : Get total calendar of a certain month
* GET, /ws/calendar?month=[1-12]&user=xxx : Get xxx's personal calendar of a certain month
* POST, /ws/calendar: 參數未定, 目前是 人名, 職等, 包哪個班, 希望班次list, 排休日list....

