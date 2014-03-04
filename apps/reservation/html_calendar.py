import calendar
from datetime import date
from itertools import groupby

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext

class PriceHTMLCalendar(calendar.HTMLCalendar):
    """
    Price calendar is a basic calendar made with HTMLCalendar module.
    """
    def __init__(self, prices, settings, slug, *args, **kwargs):
        self.prices = self.group_by_day(prices)
        self.settings = settings
        self.slug = slug
        super(PriceHTMLCalendar, self).__init__(*args, **kwargs)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            today = date.today()
            curr_date = date(self.year, self.month, day)
            if today == curr_date:
                cssclass += ' today'
            
            day_html = '''
                <div class="day-container ui-corner-all%s">
                    <div class="header">
                        <div class="day">%s</div>
                        <div class="price">%s</div>
                        <br style='clear: both;'/>
                    </div>
                    <div class="state">%s</div>
                </div>
            '''
            
            item = None
            if day in self.prices:
                cssclass += ' filled'
                # set day price
                item = self.prices[day]
            elif self.settings and self.settings.show_default_price:
                # set default price from settings
                item = self.settings
            
            if curr_date < today or not item:
                cssclass += ' past'
                return self.day_cell(cssclass, day_html % ('', day, '', ''))
            else:
                html = day_html % (' state-%s' % item.state, day,
                                   '%s PLN' % item.formatted_price,
                                   item.get_state_display())
                return self.day_cell(cssclass, html)
        return self.day_cell('noday', '&nbsp;')
    
    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (self.cssclasses[day],
                                           ugettext(calendar.day_name[day]))
        
    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s = ''.join(self.formatweekday(i) for i in self.iterweekdays())
        return '<tr class="week-row">%s</tr>' % s
    
    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        self.year, self.month = theyear, themonth
        return super(PriceHTMLCalendar, self).formatmonth(theyear, themonth, withyear=True)
    
    def formatmonthname(self, theyear, themonth, withyear=True):
        month_name = ugettext(calendar.month_name[themonth])
        s = '%s %s' % (month_name, theyear) if withyear else '%s' % month_name
        
        month_a = '<a href="%s" class="calendar_month_switch">%s</a>'
        month_href = lambda y, m: reverse('reservation:month_calendar',
                                          args=(y, m, self.slug))
        
        prev_month = ''
        if self.month - 1 > 0:
            prev_month = month_a % (month_href(self.year, self.month-1), '<<')
        elif self.year - 1 > 0:
            prev_month = month_a % (month_href(self.year-1, 12), '<<')
        
        
        next_month = ''
        if self.month + 1 < 13:
            next_month = month_a % (month_href(self.year, self.month+1), '>>')
        else:
            next_month = month_a % (month_href(self.year+1, 1), '>>')
        
        return '''
            <tr class="month-row">
                <th colspan="7">
                    <div class="month-header ui-corner-all nav nav-pills">
                        <div class="row-fluid">
                            <div class="col-md-4 switch-left">%s</div>
                            <div class="col-md-4 month-name">%s</div>
                            <div class="col-md-4 switch-right">%s</div>
                        </div>
                    </div>
                </th>
            </tr>
        ''' % (prev_month, s, next_month)

    def group_by_day(self, prices):
        field = lambda price: price.date.day
        return dict(
            [(day, list(items)[0]) for day, items in groupby(prices, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
