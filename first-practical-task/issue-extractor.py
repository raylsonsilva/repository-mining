from ghapi.all import GhApi
import sys
import csv

api = GhApi()
saida = sys.argv[3]
with open(saida, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['issue_id', 'creator',\
         'created_at', 'closed_at', 'labels',\
         'n_comments', 'n_reactions', 'is_locked'])
    repo = sys.argv[1].split('/')
    pages_issues = int(sys.argv[2])
    for page in range(1, pages_issues):
        issues = api.issues.list_for_repo(owner=repo[0], repo=repo[1], per_page=100, page=page, state='all')
        for issue in issues:
            # Ignorar pull requests e issues sem labels, que provavelmente foram criadas por engano
            if (issue.labels == [] or hasattr(issue, 'pull_request')): 
                continue
            labels = []
            for label in issue.labels:
                labels += [label.name]
            writer.writerow([issue.id, issue.user.login,\
                issue.created_at, issue.closed_at, labels,\
                issue.comments, issue.reactions.total_count, issue.locked])