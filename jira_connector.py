# Python code to connect to JIRA and execute query to get results

from jira import JIRA
import csv

Class Config:
    server = "https://JIRA_SERVER"
    username = "USERNAME"
    password = "PASSWORD"

options = {'server': Config.server}
jira = JIRA(options, basic_auth=(Config.username, Config.password))

search_assignee = ["assignee1", "assignee2"]
start_date = "2017/08/08" # Format: yyyy/mm/dd
search_query = "(" +
            " OR ".join(map(lambda x: "assignee='{0}'".format(x), search_assignee)) + 
            ") AND created>='{0}' ORDER BY assignee".format(start_date)

block_size = 1000
block_num = 0

with open("D:\\output.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Key', 'Summary', 'Assignee', 'Status'])

    while True:
        start_idx = block_num * block_size
        issues = jira.search_issues(search_query, start_idx, block_size)

        if len(issues) == 0:
            break

        block_num += 1

        for issue in issues:
            writer.writerow([
                    issue.key,
                    issue.fields.summary,
                    issue.fields.assignee.displayName,
                    issue.fields.status.name
                ])
