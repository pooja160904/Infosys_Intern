def issue_escal(text):
    imp = ['Urgent','Disruption','Outage','Crash','Critical','Breach','Virus','Incident','Failure','immediate','crucial','exchange']
    for element in imp:
        if element.lower() in text.lower():
            return 'high'
    return 'low'

def req_issue_escal(text):
    if text=="high":
        return True
    else:
        return False