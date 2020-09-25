from subprocess import Popen

# With urls
with open('list_urls.txt', 'r') as f:
    urls = f.readlines()

processes = []

for url in urls:
    processes.append(Popen('python crawler.py --href=%s' % url, shell=True))

# Run all process parallel
for process in processes:
    process.wait()
