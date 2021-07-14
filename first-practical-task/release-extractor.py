from ghapi.all import GhApi
import sys
import csv

api = GhApi()
saida = sys.argv[3]
with open(saida, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['release_id', 'release_name', 'created_at', 'published_at', 'author'])
    repo = sys.argv[1].split('/')
    n_pages = int(sys.argv[2])
    for i in range(1, n_pages+1):
        releases = api.repos.list_releases(owner=repo[0], repo=repo[1], per_page=100, page=i)
        for release in releases:
            writer.writerow([release.id, release.tag_name, release.created_at, release.published_at, release.author.login])
